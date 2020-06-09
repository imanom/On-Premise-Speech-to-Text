import os, io, json
from pydub.utils import mediainfo
import datetime
import subprocess
import srt


def video_info(video_filepath):
    """ This function returns number of channels, bit rate, and sample rate of the video"""

    video_data = mediainfo(video_filepath)
    channels = video_data["channels"]
    bit_rate = video_data["bit_rate"]
    sample_rate = video_data["sample_rate"]

    return channels, bit_rate, sample_rate


def convert_to_audio(path, video, audio_name, channels, bit_rate, sample_rate):
    """ This function converts the video file to audio (.wav) with sample_rate 16kHz.
        We are also trimming the audio to 50 seconds """
    
    audio_path = '"' + audio_name + '"'
    video_path = '"' + video + '"'
    
    #command = f"ffmpeg -y -i { video_path } -b:a {bit_rate} -ac {channels} -ar {sample_rate} -t 00:00:50.0 -vn { audio_path }"
    command = f"ffmpeg -y -i { video_path } -acodec pcm_s16le -ac 1 -ar 16000 -t 00:00:50.0 -vn { audio_path }"
    return (subprocess.call(command, shell=True))



def home(path, video):
    channels, bit_rate, sample_rate = video_info(video)
    [input_name, input_type] = os.path.splitext(video)
    output_name = input_name.split('/')[-1]
    audio_name = path + "Audio/" + output_name + ".wav"
    transcript_name = path + "Transcript/" + output_name + ".txt"
    
    v = convert_to_audio(path, video, audio_name,channels, bit_rate, sample_rate)
    return(audio_name, transcript_name)
