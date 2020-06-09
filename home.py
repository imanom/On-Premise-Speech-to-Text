import flask
import os
from flask import request, abort
from flask import send_file, send_from_directory
import video_structuring as vy
import deep_speech as deep_speech
import cmu_sphinx as cmu_sphinx
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)
CORS(app)

app.config["DEBUG"] = True


def combine(method, name):
    path = "D:/Video_to_text/Files/"
    video =  name
    audio, transcript = vy.home(path, video)
    res = ""
    if method=='deepspeech':
        res = deep_speech.func(audio, transcript)
    elif method=='cmu':
        res = cmu_sphinx.func(audio, transcript)
    return(res)
    

# API to generate the transcript and store it in the local path
@app.route('/generate_transcript', methods=['POST'])
def home():
    #print(request.get_data())
    print('form',request.form)
    
    if 'file' not in request.files:
        print('file',request.files)
        
        abort(400)
        
    elif 'method' not in request.form:
        print('method',request.form)
        abort(400)
        
    file_request = request.files['file']
    content_type_file = file_request.content_type
    
    print(file_request)
    print(request.form['method'])
    
    if "video" in content_type_file:
        print("video")
    elif "audio" in content_type_file:
        print("audio")
    else:
        abort(400)
        
    filename = secure_filename(file_request.filename)
    file_request.save(os.path.join('D:/Video_to_text/Files/Video', filename))
    print("saved file successfully")
    video_name = 'D:/Video_to_text/Files/Video/'+filename
    print(video_name)

    return(combine(request.form['method'], video_name))


# API to download the trancript from the local file system where it was stored
@app.route('/download_transcript', methods=['GET'])   
def download():

    return send_file(os.path.join('D:/Video_to_text/Files/Transcript/output.txt'), attachment_filename="output.txt", as_attachment=True)

	
	
if __name__ == '__main__':

    app.run(host='0.0.0.0', port='5002')
    