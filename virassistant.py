import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()  # calling instance

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[18].id)  # 1 for female voices; 0 for male 

recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noise... Please wait.')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything..')
        recorded_audio = recognizer.listen(source)

    command = ""  # Initialize command to avoid UnboundLocalError

    try:
        command = recognizer.recognize_google(recorded_audio, language='en_US')  # converting speech to text
        command = command.lower()
        print('Your message:', format(command))
    except Exception as ex:
        print("Error:", ex)
        return  # If an error occurs, exit the function to avoid further processing with an undefined command

    # Assigning task to the program
    if 'chrome' in command:
        engine.say('Opening Chrome..')
        engine.runAndWait()
        program = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        subprocess.Popen([program])

    if 'chess' in command:
        engine.say('Opening chess')
        engine.runAndWait()
        program = "/System/Applications/Chess.app/Contents/MacOS/Chess"
        subprocess.Popen([program])

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()

    if 'play' in command:
        engine.say('playing..')
        engine.runAndWait()
        pywhatkit.playonyt(command)  # on YouTube

    if 'youtube' in command:
        engine.say('Opening YouTube')
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com')

    if 'irctc' in command:
        engine.say('Opening')
        engine.runAndWait()
        webbrowser.open('https://www.irctc.co.in/nget/train-search')

    if 'exit' in command:
        engine.say('Closing all programs..')
        engine.runAndWait()
        exit()

    
while True:
    cmd()
