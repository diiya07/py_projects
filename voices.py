import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get a list of all voices available
voices = engine.getProperty('voices')

# Iterate through each voice and print its details
for index, voice in enumerate(voices):
    print(f"Voice {index}: ID: {voice.id}, Name: {voice.name}")

    # Set the voice to the current one and say something to test it
    engine.setProperty('voice', voice.id)
    engine.say(f"Hello, this is voice number {index}")
    engine.runAndWait()