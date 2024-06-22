from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from tika import parser as tika_parser
import requests  # Add for making HTTP requests
from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
final_result_set = []

# Function to extract text using Tika
def extract_text_using_tika(file_path):
    parsed = tika_parser.from_file(file_path)
    return parsed.get('content', '')

# Function to chunk text into 400 words
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

# Function to call ML Model 1 and get JSON output
def call_pretrained_model(text_chunks):

    URL = 'http://localhost:5000/pii'
    payload = {'text': text_chunks}
    result = requests.post(URL, json=payload, verify=False)
    modelResponse = result.json()
    return modelResponse


# Function to call ML Model 2 and get JSON output
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


# Function to compare outputs of two models
def concatenate_model_outputs(output1, output2):

    for entity1 in output1["response"]:
        final_result_set.append(entity1)

    for entity2 in output2["response"]:
        final_result_set.append(entity2)

    # print(final_result_set)


# Route for uploading file and processing
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # # Extract text using Tika
    # file_path = "C:\\Users\\smate\\Desktop\\story.txt"
    text = extract_text_using_tika(file_path)

    os.remove(file_path)  # Remove the uploaded file to clean up

    # Chunk text into 400-word segments
    chunks = chunk_text_into_400_words(text)

    for chunk in chunks:
        # Call ML Model 1 and ML Model 2
        model1_output = call_pretrained_model(chunk)
        model2_output = call_precedio_model(chunk)
        # print(model2_output)
        concatenate_model_outputs(model1_output, model2_output)

    print(final_result_set)
    return {"response" : "new response"}

# Route for homepage
@app.route('/')
def index():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(port=5111, debug=True)
