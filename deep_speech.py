import deepspeech
import wave
import numpy as np

def func(audio_file, transcript):
    model_file_path = 'deepspeech-0.6.0-models/output_graph.pbmm'
    beam_width = 500
    model = deepspeech.Model(model_file_path, beam_width)

    lm_file_path = 'deepspeech-0.6.0-models/lm.binary'
    trie_file_path = 'deepspeech-0.6.0-models/trie'
    lm_alpha = 0.75
    lm_beta = 1.85
    model.enableDecoderWithLM(lm_file_path, trie_file_path, lm_alpha, lm_beta)

    filename = audio_file
    w = wave.open(filename, 'r')
    rate = w.getframerate()
    frames = w.getnframes()
    buffer = w.readframes(frames)

    data16 = np.frombuffer(buffer, dtype=np.int16)
    #print(str(type(data16)))

    text = model.stt(data16)
    
    with open("D:/Users/Monami/Video_to_text/Files/Transcript/output.txt", "w+") as f:
        f.write(text)
    
    return(text)