from playsound import playsound
import speech_recognition as sr
from commands import George


running = True
r = sr.Recognizer()
george = George()


def play_audio(file):
	playsound(file)


def init_speech():
	print("Listening...")
	playsound('audio/start.mp3')

	with sr.Microphone() as source:
		print("Say something")
		audio = r.listen(source)

	play_audio('audio/end.mp3')

	command = ""

	try:
		command = r.recognize_google(audio)
	except:
		print("Couldn't understand. Please repeat!")

	print("Your command:")
	print(command)

	if command in ["quit", "that's it", "thank you", "thank you George", "bye", "goodbye", "exit"]:
		global running
		running = False
	else:
		george.discover(command)


while running:
	init_speech()
