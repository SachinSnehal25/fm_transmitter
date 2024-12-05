import subprocess
import sys

def convert_audio_to_wav(input_file, output_file):
    """
    Convert the input audio file to a WAV format supported by PiFM.
    """
    print(f"Converting {input_file} to WAV format...")
    try:
        subprocess.run(
            ['ffmpeg', '-i', input_file, '-ar', '44100', '-ac', '1', '-sample_fmt', 's16', output_file],
            check=True
        )
        print(f"Converted to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting file: {e}")
        sys.exit(1)

