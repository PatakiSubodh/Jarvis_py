# play wav file
import pyaudio
import wave

# Set up the WAV file
wav_file = wave.open('audio.wav', 'rb')

# Set up the PyAudio stream
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                channels=wav_file.getnchannels(),
                rate=wav_file.getframerate(),
                output=True)

# Play the WAV file
data = wav_file.readframes(1024)
while data:
    stream.write(data)
    data = wav_file.readframes(1024)

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()

# Close the WAV file
wav_file.close()

# *****************************************************************************************

#play mp3 file
from pydub import AudioSegment         #pip install pydub
from pydub.playback import play

# Open the MP3 file
mp3_file = AudioSegment.from_mp3("audio.mp3")

# Play the MP3 file
play(mp3_file)

# Close the MP3 file
mp3_file.close()


