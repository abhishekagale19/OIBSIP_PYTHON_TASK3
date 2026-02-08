import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Sorry, I didn't understand.")
        return ""

def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "your name" in command:
        speak("I am your simple Python voice bot.")
    elif "bye" in command:
        speak("Goodbye! Have a nice day.")
        return False
    else:
        speak("Sorry, I don't know that yet.")
    return True

# Main loop
speak("Voice bot started. Say something!")

running = True
while running:
    command = listen()
    if command:
        running = respond(command)
