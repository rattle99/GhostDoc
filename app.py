import importlib
import os
import re

import requests
from flask import Flask, jsonify, render_template, request, send_file
from presidio_analyzer import AnalyzerEngine
from tika import parser as tika_parser
from werkzeug.utils import secure_filename

import CustomFaker
import numericRegex
from docx_utils import export_to_docx, extractText, get_html_from_docx

app = Flask(__name__)
analyzer = AnalyzerEngine()


mapDict = {}
UPLOAD_FOLDER = "./uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

PRESIDIO_ENTITIES = ["PERSON", "PHONE_NUMBER"]
MODEL_EXCLUSION_LIST = {
    "FIRSTNAME",
    "LASTNAME",
    "MIDDLENAME",
    "ACCOUNTNAME",
    "USERNAME",
    "PHONENUMBER",
    "COMPANYNAME",
    "PREFIX",
    "NEARBYGPSCOORDINATE",
}


def extract_text_using_tika(file_path):
    """

    :param file_path: 

    """
    parsed_file = tika_parser.from_file(file_path)
    return parsed_file.get("content", "")


def split_text_into_chunks(text):
    """

    :param text: 

    """
    sentences = text.split(".")

    chunk_list = []
    current_chunk = ""
    word_count = 0

    for sentence in sentences:
        current_chunk += sentence + "."
        word_count += len(sentence.split(" "))
        if word_count >= 350:
            chunk_list.append(current_chunk)
            current_chunk = ""
            word_count = 0

    if len(current_chunk) != 0:
        chunk_list.append(current_chunk)

    return chunk_list


def pretrained_model(current_chunk):
    """

    :param current_chunk: 

    """
    URL = "http://localhost:5000/pii"
    payload = {"text": current_chunk}
    result = requests.post(URL, json=payload, verify=False)
    pretrained_model_response = result.json()

    entities = pretrained_model_response["response"]
    filtered_entities = list()
    for entity in entities:
        if entity["entity_group"] not in MODEL_EXCLUSION_LIST:
            filtered_entities.append(entity)

    pretrained_model_response = {"response": filtered_entities}
    return pretrained_model_response


def presidio_model(current_chunk):
    """

    :param current_chunk: 

    """
    analyzer_results = analyzer.analyze(
        text=current_chunk, entities=PRESIDIO_ENTITIES, language="en"
    )
    chunk_result = []

    for result in analyzer_results:
        result = result.to_dict()
        required_result = {
            "end": result["end"],
            "entity_group": result["entity_type"],
            "score": result["score"],
            "start": result["start"],
        }
        chunk_result.append(required_result)

    presidio_model_response = {"response": chunk_result}
    return presidio_model_response


def combine_model_results(pretrained_result, presidio_result):
    """

    :param pretrained_result: 
    :param presidio_result: 

    """
    result_set = []

    for entity in pretrained_result["response"]:
        result_set.append(entity)

    for entity in presidio_result["response"]:
        result_set.append(entity)

    result_set = sorted(result_set, key=lambda x: x["start"])

    return result_set


def transform_chunk(model_results, chunk):
    """

    :param model_results: 
    :param chunk: 

    """
    module_name = "CustomFaker"
    module = importlib.import_module(module_name)
    modified_chunk = ""

    isFirstRun = True
    prev_index = None

    for json_object in model_results:
        start_index = json_object["start"]
        end_index = json_object["end"]
        method_name = json_object["entity_group"]
        replaced_text = chunk[start_index:end_index]
        res = ""

        if any(char.isdigit() for char in replaced_text) and numericRegex.regexCheck(
            replaced_text
        ):
            res = CustomFaker.alter_random_digits(replaced_text)

        else:
            if replaced_text in mapDict:
                res = mapDict[replaced_text]
            else:
                method = getattr(module, method_name)
                res = method()
                mapDict[str(replaced_text)] = str(res)

        if isFirstRun:
            modified_chunk = chunk[:start_index] + str(res)
            isFirstRun = False
        else:
            space = ""
            if prev_index == start_index:
                space = " "
            modified_chunk = (
                modified_chunk + space + chunk[prev_index:start_index] + str(res)
            )
        prev_index = end_index

    modified_chunk = modified_chunk + chunk[prev_index:] + " "

    return modified_chunk


def export_to_original(modified_text, original_file_path):
    """

    :param modified_text: 
    :param original_file_path: 

    """
    original_ext = original_file_path.rsplit(".", 1)[-1].lower()
    temp_file = secure_filename("modified_" + os.path.basename(original_file_path))
    temp_file_path = os.path.join(app.config["UPLOAD_FOLDER"], temp_file)

    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write(modified_text)
    if original_ext == "pdf":
        mime_type = "application/pdf"
    elif original_ext == "doc" or original_ext == "docx":
        mime_type = "application/msword"
    else:
        mime_type = "text/plain"
    return temp_file_path, mime_type


def get_file():
    """ """
    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)
    return filepath


def preprocess_file(file_path):
    """

    :param file_path: 

    """
    if file_path.endswith(".docx"):
        html_content = get_html_from_docx(file_path)
        text = extractText(html_content)
        chunks = split_text_into_chunks(text)
        return chunks
    else:
        text = extract_text_using_tika(file_path)
        chunks = split_text_into_chunks(text)
        return chunks


@app.route("/upload", methods=["POST", "GET"])
def upload_file():
    """ """
    if request.method == "GET":
        return render_template("upload.html")
    else:
        filepath = get_file()
        chunks = preprocess_file(filepath)
        modified_chunks_list = []

        for chunk in chunks:
            pretrained_model_output = pretrained_model(chunk)
            presidio_model_output = presidio_model(chunk)
            result_set = combine_model_results(
                pretrained_model_output, presidio_model_output
            )
            modified_chunk = transform_chunk(result_set, chunk)
            modified_chunks_list.append(modified_chunk)

        modified_content = " ".join(modified_chunks_list)

        for key in mapDict:
            matchSequence = f'"(?<=[^a-zA-Z])({key})(?=[^a-zA-Z])"gm'
            modified_content = re.sub(matchSequence, mapDict[key], modified_content)

        if filepath.endswith(".docx") or filepath.endswith(".doc"):
            temp_file_path, mime_type = export_to_docx(filepath, mapDict, UPLOAD_FOLDER)
        else:
            temp_file_path, mime_type = export_to_original(modified_content, filepath)

        return send_file(temp_file_path, mimetype=mime_type, as_attachment=True)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
