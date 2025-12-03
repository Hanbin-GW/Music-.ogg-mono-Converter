from pydub import AudioSegment
import os
import sys

class Color:
    BOLD = "\033[1m"
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"
    RESET = "\033[0m"

try:
    input_file = input("Insert a filename (including path if not in the current directory): ")

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The file '{input_file}' does not exist.")

    try:
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        raise RuntimeError(f"Failed to read audio file: {e}")

    mono_audio = audio.set_channels(1)

    resampled_audio = mono_audio.set_frame_rate(48000)

    output_dir = "output"
    if not os.path.exists(output_dir):
        print(Color.MAGENTA + "The Directory does not exist. Creating one..." + Color.RESET)
        os.makedirs(output_dir)

    base_name = os.path.basename(input_file)
    new_name = os.path.splitext(base_name)[0] + ".ogg"
    resampled_output_file = os.path.join(output_dir, new_name)

    try:
        resampled_audio.export(resampled_output_file, format="ogg")
    except Exception as e:
        raise RuntimeError(f"Failed to export the audio file: {e}")

    print(Color.GREEN+ f"Successfully exported '{input_file}' → '{resampled_output_file}'" + Color.RESET)

except Exception as e:
    print("\nError occurred:")
    print(Color.RED + str(e) + Color.RESET)

finally:
    input(Color.GREEN + "\nPress Enter to exit..." + Color.RESET)
