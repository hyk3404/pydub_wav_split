from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys
from os import walk
from os.path import join
import os

def data_path():
    path = "./"
    path_list = []
    name_list = []

    for root, dirs, files in walk(path):
        for f in files:
            fullpath = join(root, f)
            # print(fullpath)

            if fullpath.endswith(".wav"):
                path_list.append(fullpath)
                name_list.append(os.path.splitext(f)[0])
                # print(f)
    # print(path_list)
    # print(name_list)

    return path_list, name_list

def pydub_wavs_split():
    
    wavs_path, wavs_name = data_path()
    wavs_folder = "./wavs"
    if not os.path.isdir(wavs_folder):
        os.mkdir(wavs_folder)

    for wav_path_element, wav_name_element in zip(wavs_path, wavs_name):
        wav = AudioSegment.from_wav(wav_path_element)
        wavs_split = split_on_silence(wav,min_silence_len=500,silence_thresh=-40)

        for count, wav_element in enumerate(wavs_split):
            wav_list = AudioSegment.empty()
            wav_list += wav_element

            wav_element.export('./wavs/{}{}.wav'.format(wav_name_element, count), format='wav')

if __name__ == "__main__":
    pydub_wavs_split()
    # data_path()