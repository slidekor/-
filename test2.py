import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import keyboard
# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ru-RU")
        return text.lower()
    except sr.UnknownValueError:
        return "Извините, я не понял."
    except sr.RequestError:
        return "Извините, я не могу подключиться к интернету."

# Define activation command
ACTIVATION_COMMAND = "джарвис"


# Main loop
speak("Скажите команду.")

    # Listen for activation command

while True:
    command = recognize_speech()
    if ACTIVATION_COMMAND in command:
        # Listen for voice command
        speak("Чем я могу вам помочь?")
        command = recognize_speech()
        # Process command
        if "открой" in command:
            app = command.replace("открой", "").strip()
            os.system(f"start {app}")
            speak(f"Открываю {app}.")
        elif "найди" in command:
            query = command.replace("найди", "").strip()
            url = f"https://ya.ru?q={query}"
            webbrowser.open(url)
            speak(f"Ищу {query}.")
        elif "включи" in command:
            song = command.replace("включи", "").strip()
            url = f"https://www.youtube.com/results?search_query={song}"
            webbrowser.open(url)
            speak(f"Воспроизвожу {song}.")
        elif "выход" in command or "закрыть" in command:
            speak("До свидания!")
        elif "начать" in command:
            keyboard.press("win + r")
            speak("выполняю")
        else:    
            speak("Извините, я не понял.")