from pydub import AudioSegment
import os

input_file = input("Insert a filename")

audio = AudioSegment.from_file(input_file)

mono_audio = audio.set_channels(1)


resampled_audio = mono_audio.set_frame_rate(48000)

output_dir = "output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

resampled_output_file = f"output/{input_file}.ogg"
resampled_audio.export(resampled_output_file, format="ogg")

resampled_output_file

