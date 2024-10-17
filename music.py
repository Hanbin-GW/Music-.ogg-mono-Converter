from pydub import AudioSegment
import os
import sys

input_file = input("Insert a filename (including path if not in the current directory): ")

# 입력 파일이 존재하는지 확인
if not os.path.isfile(input_file):
    print(f"Error: The file {input_file} does not exist.")
    sys.exit(1)

audio = AudioSegment.from_file(input_file)

mono_audio = audio.set_channels(1)


resampled_audio = mono_audio.set_frame_rate(48000)

output_dir = "output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

resampled_output_file = f"output/{input_file}.ogg"
resampled_audio.export(resampled_output_file, format="ogg")

resampled_output_file

