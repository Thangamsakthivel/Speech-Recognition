import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
browserPath="C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s"
def speak(text):
	print(text)
	engine.say(text)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)

	if hour >= 0 and hour < 12:
		speak("Good Morning...")
	elif hour >= 12 and hour < 16:
		speak("Good  Afternoon")
	else:
		speak("Good Evening")
	speak("i am friday.... how may i help you?")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		speak("tell me what to do...")
		audio = r.listen(source)
	try:
		print("Reognizing...")
		query = r.recognize_google(audio, language = 'en-in')
		print(f"you said:{query}\n")

	except Exception as e:
		speak(e)
		query = None
		takeCommand()
	return query

speak(" initializing  system....")
wishMe()
# query = takeCommand()
query ='play music'# query.lower()
if 'wikipedia' in query:
	speak("searching wikipedia...")
	quer = query.replace("wikipedia","")
	results = wikipedia.summary(quer,sentences = 2)
	speak(results)
elif 'youtube' in query:
	speak("opening youtube...")
	webbrowser.get(browserPath).open("youtube.com")#open browser with provided url
elif 'search' in query:
	quer = query.replace("search","")
	speak("searching..."+quer)
	webbrowser.get(browserPath).open(query)
elif 'music' in query:
	speak("opening music...")
	songs_dir = "E:/song"
	songs = os.listdir(songs_dir)
	print(songs)
	os.startfile(os.path.join(songs_dir, songs[0]))
elif 'the time' in query:
	Time = datetime.datetime.now().strftime("%H :%M")
	speak("the time is "+Time)
elif 'sublime' in query:
	speak("opening sublime...")
	sublime = "C:\\Program Files (x86)\\Sublime Text 3\\sublime_text.exe"
	os.startfile(sublime)