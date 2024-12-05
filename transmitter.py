import os
import subprocess
import sys

def check_pifm_installed():
    """
    Check if PiFM executable is present in the current directory.
    """
    if not os.path.isfile('./pifm'):
        print("PiFM executable not found. Ensure it is in the current directory.")
        sys.exit(1)

def transmit_fm(file_path, frequency):
    """
    Start FM transmission using PiFM.
    """
    print(f"Starting FM transmission on {frequency} MHz...")
    try:
        subprocess.run(['sudo', './pifm', file_path, str(frequency)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting FM transmission: {e}")
        sys.exit(1)
