🚀 Features

🎤 Voice input using microphone

📝 Speech-to-text conversion

🔊 Text-to-speech response

🧠 Simple keyword-based responses

🔁 Continuous listening loop until exit

🛠️ Technologies Used

Python 3.x

speechrecognition

pyttsx3

pyaudio

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/voice-bot.git
cd voice-bot

2️⃣ Install Dependencies
pip install SpeechRecognition pyttsx3 pyaudio

⚠️ If PyAudio fails on Windows:
pip install pipwin
pipwin install pyaudio

▶️ How to Run
python voice_bot.py


Make sure your microphone is connected and working properly.

🧠 Supported Commands
Command	Response
"hello"	Greets the user
"your name"	Tells bot name
"bye"	Exits the program

You can modify the respond() function to add more commands.

📁 Project Structure
voice-bot/
│
├── voice_bot.py
└── README.md

🔄 How It Works

Microphone captures voice input

Google Speech Recognition converts speech to text

Program checks for keywords

pyttsx3 converts response text to speech

🌐 Internet Requirement

Speech recognition uses Google's API.

Internet connection is required for speech-to-text conversion.

🔮 Future Improvements

Integrate ChatGPT API

Add GUI using Tkinter

Add wake word detection

Make fully offline assistant

Add system commands (open apps, search web)

🧑‍💻 Author

Abhishek Agale
