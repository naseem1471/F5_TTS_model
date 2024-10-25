import wave
import numpy as np

def check_wav_file(filename):
    with wave.open(filename, 'rb') as wav:
        # Get basic info
        print(f"Number of channels: {wav.getnchannels()}")
        print(f"Sample width: {wav.getsampwidth()}")
        print(f"Frame rate: {wav.getframerate()}")
        print(f"Number of frames: {wav.getnframes()}")
        
        # Read the frames
        frames = wav.readframes(wav.getnframes())
        audio_data = np.frombuffer(frames, dtype=np.int16)
        
        # Check if there's any sound
        print(f"Max amplitude: {np.max(np.abs(audio_data))}")
        print(f"Mean amplitude: {np.mean(np.abs(audio_data))}")
        print(f"Contains all zeros: {np.all(audio_data == 0)}")

# Use one of these formats:
check_wav_file(r"C:\Users\nasee\Desktop\Random\audio1empty.wav")  # using raw string (r prefix)
# OR
# check_wav_file("C:\\Users\\nasee\\Desktop\\Random\\audio1empty.wav")  # using double backslashes
# OR
# check_wav_file("C:/Users/nasee/Desktop/Random/audio1empty.wav")  # using forward slashes
