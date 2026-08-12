import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import asyncio
import edge_tts
import pygame
import os
import pyautogui
import time
import webbrowser


listener = sr.Recognizer()

pygame.mixer.init()


async def speak(text):
    filename = "voice.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    if os.path.exists(filename):
        os.remove(filename)


def talk(text):
    print("Olly :", text)
    asyncio.run(speak(text))


def input_instruction():
    instruction = ""

    try:
        with sr.Microphone() as source:
            print("Listening...")

            listener.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = listener.listen(source)

            instruction = listener.recognize_google(audio)
            instruction = instruction.lower()

            print("You said:", instruction)

            instruction = instruction.replace("olly", "")
            instruction = instruction.replace("olivia", "")

            instruction = instruction.strip()

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")

    except sr.RequestError:
        print("Speech recognition service unavailable.")

    except Exception as e:
        print("Error:", e)

    return instruction


def play_olly():

    instruction = input_instruction()

    if instruction == "":
        return True

    # Play YouTube
    if "play" in instruction and "music" not in instruction:

        song = instruction.replace("play", "").strip()

        if song:
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)
        else:
            talk("Please tell me what you want to play.")

    # Current time
    elif "time" in instruction:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        talk(f"The current time is {current_time}")

    # Date
    elif "date" in instruction:

        today = datetime.datetime.now().strftime("%d %B %Y")

        print(today)

        talk(f"Today is {today}")

    # Open YouTube
    elif ("open youtube" in instruction 
          or "start youtube" in instruction):

        talk("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    # Open Google
    elif ("open google" in instruction 
        or "start youtube" in instruction):

        talk("Opening Google")

        webbrowser.open("https://www.google.com")

    # Open GitHub
    elif "open github" in instruction:

        talk("Opening GitHub")

        webbrowser.open("https://github.com")

    # Play Music
    elif "play music" in instruction:

        talk("Playing music")

        music_url = (
            "https://music.youtube.com/playlist?"
            "list=PLIL965-SXjbVEiWwe1l6RApWYDnbhc_Oz"
        )

        webbrowser.open(music_url)

        time.sleep(5)

        pyautogui.press("space")
        

    # Search Google
    elif "search google for" in instruction:

        search_query = instruction.replace(
            "search google for",
            ""
        ).strip()

        if search_query:
            talk(f"Searching Google for {search_query}")

            webbrowser.open(
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )
        else:
            talk("Please tell me what you want to search.")

    # Search YouTube
    elif "search youtube for" in instruction:

        search_query = instruction.replace(
            "search youtube for",
            ""
        ).strip()

        if search_query:
            talk(f"Searching YouTube for {search_query}")

            webbrowser.open(
                "https://www.youtube.com/results?search_query="
                + search_query.replace(" ", "+")
            )
        else:
            talk("Please tell me what you want to search.")

    # Open Notepad
    elif "open notepad" in instruction:

        talk("Opening Notepad")

        os.system("start notepad.exe")

    # Open Calculator
    elif "open calculator" in instruction:

        talk("Opening Calculator")

        os.system("start calc.exe")

    # Open Command Prompt
    elif "open command prompt" in instruction:

        talk("Opening Command Prompt")

        os.system("start cmd.exe")

    # Shutdown
    elif "shutdown" in instruction:

        talk("Shutting down the computer")

        os.system("shutdown /s /t 1")

        return False

    # Restart
    elif "restart" in instruction:

        talk("Restarting the computer")

        os.system("shutdown /r /t 1")

        return False

    # How are you
    elif "how are you" in instruction:

        talk("I am fine. Thank you for asking.")

    # Assistant name
    elif "what is your name" in instruction:

        talk(
            "My name is olly. "
            "I am your personal voice assistant."
        )

    # Wikipedia
    elif ("who is" in instruction
        or "what is" in instruction
        or "tell me about" in instruction
        or "search wikipedia for" in instruction
        or "check wikipedia" in instruction):

        person = instruction.replace("who is", "").strip()
        person = instruction.replace("what is", "").strip()
        person = instruction.replace("tell me about", "").strip()
        person = instruction.replace("search wikipedia for", "").strip()
        person = instruction.replace("check wikipedia", "").strip()
        person = instruction.replace("give me", "").strip()

        try:
            info = wikipedia.summary(person, sentences=2)
            print(info)
            talk(info)
        except Exception:
            talk("Sorry, I couldn't find information about that person.")


    # Stop / Exit
    elif (
        "stop" in instruction
        or "exit" in instruction
        or "goodbye" in instruction
    ):

        talk("Goodbye. Have a nice day.")

        return False

    # Unknown command
    else:

        talk("Please repeat again.")

    return True


talk("Hello. I am olly. How can I help you today?")


while True:

    if play_olly() is False:
        break