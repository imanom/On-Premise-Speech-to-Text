import speech_recognition as sr


def func(audio_file, transcript):
    r = sr.Recognizer()

    audioFile = sr.AudioFile(audio_file)

    with audioFile as source:
        audio = r.record(source)
            
    text = r.recognize_sphinx(audio)
    with open("D:/Users/Monami/Video_to_text/Files/Transcript/output.txt", "w+") as f:
        f.write(text)
    return(text)