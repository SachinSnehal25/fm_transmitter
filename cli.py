from fm_transmitter.audio_utils import convert_audio_to_wav
from fm_transmitter.transmitter import check_pifm_installed, transmit_fm

def main():
    """
    Command-line interface for FM Transmitter.
    """
    check_pifm_installed()

    # Get user inputs
    input_audio = input("Enter the path to your audio file: ").strip()
    output_wav = "converted_audio.wav"
    frequency = 107.9  # Default frequency

    # Convert and transmit
    convert_audio_to_wav(input_audio, output_wav)
    transmit_fm(output_wav, frequency)

if __name__ == "__main__":
    main()
