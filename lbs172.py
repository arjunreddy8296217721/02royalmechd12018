import speech_recognition as sr 

AUDIO_FILE = ("my.wav")

#use the audio file as the audio source

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	#reads the audio file. Here we use record insteadof
	#listen
	audio = r.record(source)

try:
	print("The audio file contains:" + r.recognize_google(audio))

except sr.UnknownValueError:
	print("Google Speech Recognition service; {0}.format"(e))
