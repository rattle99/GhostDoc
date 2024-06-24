from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from tika import parser as tika_parser
import requests  # Add for making HTTP requests
from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()
import importlib
import CustomFaker
from flask import send_file
app = Flask(__name__)

mapDict = {}
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
final_result_set = []

def extract_text_using_tika(file_path):
    parsed = tika_parser.from_file(file_path)
    return parsed.get('content', '')


def chunk_text_into_400_words(text):
    words = text.split()
    chunks = []
    current_chunk = []
    word_count = 0

    for word in words:
        current_chunk.append(word)
        word_count += 1
        if word_count >= 50:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            word_count = 0
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks


def call_pretrained_model(text_chunks):

    URL = 'http://localhost:5000/pii'
    payload = {'text': text_chunks}
    result = requests.post(URL, json=payload, verify=False)
    modelResponse = result.json()
    return modelResponse


def call_precedio_model(text_chunks):
    analyzer_results = analyzer.analyze(text=text_chunks, language='en')
    results = list()
    for result in analyzer_results:
        result = result.to_dict()
        required_result = {'end' : result['end'], 'entity_group' : result['entity_type'],
                            'score' : result['score'], 'start' : result['start']}
        results.append(required_result)

    presidioResponse = {"response" : results}
    return presidioResponse

def model_outputs(output1,output2):
    result_set=[]
    for entity1 in output1["response"]:
        if entity1['entity_group']!='FIRSTNAME' and entity1['entity_group']!='LASTNAME' and entity1['entity_group']!='COMPANYNAME':
            result_set.append(entity1)

    for entity2 in output2["response"]:
        result_set.append(entity2)

    return result_set

def transform_chunks(result,chunk):
    module_name = "CustomFaker"
    module = importlib.import_module(module_name)
    
    for json_object in result:
        start_index= json_object['start']
        end_index=json_object['end']
        method_name = json_object['entity_group']
        replaced_text = chunk[start_index:end_index+1]
        res=''
        if replaced_text in mapDict:
            res = mapDict[replaced_text]
        else:
            method = getattr(module, method_name)
            res =method()
            mapDict[replaced_text]=  res

        chunk = chunk[:start_index] + str(res) + chunk[end_index+1:]

        
    return chunk

def export_to_original(modified_text, original_file_path):
    
    
    original_ext = original_file_path.rsplit('.', 1)[-1].lower()
    temp_file = secure_filename('modified_' + os.path.basename(original_file_path))
    temp_file_path = os.path.join(app.config['UPLOAD_FOLDER'], temp_file)
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        f.write(modified_text)
    if original_ext == 'pdf':
        mime_type = 'application/pdf'
    elif original_ext == 'doc' or original_ext == 'docx':
        mime_type = 'application/msword'  
    else:
        mime_type = 'text/plain'
    return temp_file_path,mime_type
    

@app.route('/upload', methods=['POST','GET'])
def upload_file():

    if request.method=='GET':
        return render_template('upload.html')
    else:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        text = extract_text_using_tika(filepath)
        chunks = chunk_text_into_400_words(text)
        final_result_set=[]
        modified_chunks_list=[]
        
        for chunk in chunks:
        
            model1_output = call_pretrained_model(chunk)
            model2_output = call_precedio_model(chunk)
            result_set=model_outputs(model1_output,model2_output)
            modified_chunks_list.append(transform_chunks(result_set,chunk))
        modified_content = ' '.join(modified_chunks_list)
        temp_file_path,mime_type=export_to_original(modified_content,filepath)
        print(mapDict)
        return send_file(temp_file_path,mimetype=mime_type,as_attachment=True)

if __name__ == '__main__':
    app.run(port=5111, debug=True)
