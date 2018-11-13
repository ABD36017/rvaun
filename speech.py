import speech_recognition as sr
AUDIO_FILE=("example2.wav")
#use the audio file as the audio source
r=sr.recognizer()
with sr.Audiofile(AUDIO_FILE)as source:
#reads the audio file.here we use record instead of
#listen
audio = r.record(source)
try:
	print("The audio file contains:"+r.recognize_Google(audio))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition.service; {0}".forma)