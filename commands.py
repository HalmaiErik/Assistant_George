from win32com.client import Dispatch
from get_answer import Fetcher


def respond(response):
	print(response)
	speak = Dispatch("SAPI.SpVoice")
	speak.Speak(response)


class George:
	def __init__(self):
		self.confirm = {"yes", "affirmative", "correct", "sure", "do it", "yeah", "confirm"}
		self.cancel = {"no", "negative", "incorrect", "wait", "don't", "do not", "cancel"}

	def discover(self, text):
		if "what" in text and "your name" in text:
			respond("My name is George.")
		else:
			if "define" in text:
				text = text.replace(" ", "+")
				f = Fetcher("https://www.google.com/search?q=" + text, "def")
				answers = f.look_up()
				i = 0
				for answer in answers:
					i += 1
					respond(str(i) + ". " + answer.getText())
			elif "weather in" in text:
				text = text.replace(" ", "+")
				f = Fetcher("https://www.google.com/search?q=" + text, "weather")
				answers = f.look_up()
				respond(answers[0].getText() + " degrees celsius")
			else:
				text = text.replace(" ", "+")
				f = Fetcher("https://www.google.com/search?q=" + text, "other")
				answers = f.look_up()
				respond(answers[0].getText())
