# On-Premise-Speech-to-Text
A Flask API to convert speech to text using Offline Transcription methods - CMU Sphinx and DeepSpeech.

## File Descriptions:

1. DeepSpeech.ipynb - Run this file to generate the DeepSpeech model and store the model files in a folder called 'deepspeech-0.6.0-models'. This step has to be completed before running anything else.

2. home.py - Main python file containing the flask APIs. 

3. video_structuring.py - This python script converts the video/audio file into a .wav file (16kHz, 16 bit rate and 1 channel) of duration 50 seconds and saves it to the 'Files/Audio' folder.

4. cmu_sphinx.py - Python code to convert the wav file to text using CMU Sphinx.

5. deep_speech.py - Python code to convert the wav file to text using DeepSpeech.

## Output:

Output will be stored in 'Files/Transcript/output.txt' file.

## APIs:

Home.py contains two flask APIs - 

### 1. /generate_transcript (POST) 
```
Request body: (form-data format)
'method': 'cmu' (for cmu sphinx) or 'deepspeech' (for deepspeech),
'file': <The uploaded audio/video file>
```
### 2. /download_transcript (GET)
Sends the 'output.txt' file containing the transcript of the uploaded audio to the client.

## Libraries:

Few of the libraries that have to be imported - 
```
ffmpeg
pydub
flask-cors
srt
SpeechRecognition
download swigwin (and add to path)
download Visual studio C++ Build tools and add to path. https://visualstudio.microsoft.com/visual-cpp-build-tools/ 

```




