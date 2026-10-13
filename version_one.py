import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import datetime
import random
from urllib.parse import quote


# =========================================================
# SETTINGS
# =========================================================

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

VSCODE_PATH = r"C:\Users\pc\AppData\Local\Programs\Microsoft VS Code\Code.exe"


# =========================================================
# VOICE ENGINE
# =========================================================


def speak(text):
    print("JARVIS:", text)

    engine = pyttsx3.init("sapi5")

    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()


# =========================================================
# LISTENING
# =========================================================

def take_command():

    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 0.8

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        audio = recognizer.listen(source)

    try:

        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-in"
        )

        print("YOU:", query)

        return query.lower()

    except sr.UnknownValueError:

        speak("Sorry sir, I didn't catch that.")

        return ""

    except sr.RequestError:

        speak("Sir, the speech service seems to be unavailable.")

        return ""


# =========================================================
# BASIC ACTIONS
# =========================================================

def open_chrome():

    speak("Opening Chrome, sir.")

    subprocess.Popen(CHROME_PATH)


def open_vscode():

    speak("Opening Visual Studio Code, sir.")

    subprocess.Popen(VSCODE_PATH)


def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"Sir, the time is {current_time}")


def tell_date():

    today = datetime.datetime.now().strftime("%d %B %Y")

    speak(f"Today is {today}, sir.")


def tell_day():

    today = datetime.datetime.now().strftime("%A")

    speak(f"Today is {today}, sir.")


def search_google(query):

    search_query = query.strip()

    if not search_query:

        speak("What should I search for, sir?")

        return

    speak(f"Searching for {search_query}")

    url = "https://www.google.com/search?q=" + quote(search_query)

    webbrowser.open(url)


def search_youtube(query):

    search_query = query.strip()

    if not search_query:

        speak("What should I search for on YouTube?")

        return

    speak(f"Searching YouTube for {search_query}")

    url = "https://www.youtube.com/results?search_query=" + quote(search_query)

    webbrowser.open(url)


# =========================================================
# PERSONALITY
# =========================================================

def tell_joke():

    jokes = [

        "Why do programmers prefer dark mode? Because light attracts bugs.",

        "I told my computer I needed a break. Now it keeps sending me KitKat advertisements.",

        "There are only ten kinds of people in the world. Those who understand binary and those who don't.",

        "Sir, I would tell you a UDP joke, but you might not get it."

    ]

    speak(random.choice(jokes))


def respond_how_are_you():

    responses = [

        "I'm doing great, sir. My circuits are feeling fantastic.",

        "All systems operational, sir.",

        "I'm good, sir. Just waiting for your next command.",

        "Doing excellent, sir. How about you?"

    ]

    speak(random.choice(responses))


def morning_response():

    responses = [

        "Good morning, sir. Let's make today count.",

        "Good morning, sir. Systems are online.",

        "Good morning, sir. Ready when you are."

    ]

    speak(random.choice(responses))


def night_response():

    responses = [

        "Good night, sir. Don't stay up too late.",

        "Good night, sir. Systems standing by.",

        "Good night, sir. Rest well."

    ]

    speak(random.choice(responses))


def thank_you_response():

    responses = [

        "You're welcome, sir.",

        "Anytime, sir.",

        "Always happy to help.",

        "My pleasure, sir."

    ]

    speak(random.choice(responses))


def bored_response():

    responses = [

        "Boredom detected, sir. Perhaps some coding would help.",

        "You could build something, sir.",

        "How about working on JARVIS instead of being bored?",

        "Sir, boredom is simply an opportunity for a new project."

    ]

    speak(random.choice(responses))


def who_am_i():

    speak(
        "You are my creator, sir. "
        "At least according to my current programming."
    )


def who_are_you():

    speak(
        "I am JARVIS, your personal voice assistant. "
        "Currently running on Python and a questionable amount of ambition."
    )


def what_can_you_do():

    speak(
        "I can open applications, tell you the time and date, "
        "search Google and YouTube, tell jokes, answer basic questions, "
        "and execute multiple commands."
    )


# =========================================================
# CALCULATOR
# =========================================================

def calculate(command):

    expression = command

    expression = expression.replace("calculate", "")
    expression = expression.replace("what is", "")
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("times", "*")
    expression = expression.replace("multiplied by", "*")
    expression = expression.replace("divided by", "/")

    expression = expression.strip()

    try:

        result = eval(expression)

        speak(f"The answer is {result}")

    except:

        speak("Sorry sir, I couldn't calculate that.")


# =========================================================
# UNDERSTANDING COMMANDS
# =========================================================

def understand(command):

    command = command.lower().strip()


    # -----------------------------------------------------
    # EXIT
    # -----------------------------------------------------

    if any(word in command for word in [
        "exit",
        "quit",
        "shutdown",
        "goodbye",
        "stop"
    ]):

        return "exit"


    # -----------------------------------------------------
    # GREETING
    # -----------------------------------------------------

    if any(word in command for word in [
        "hello",
        "hi jarvis",
        "hey jarvis",
        "hey",
        "hi"
    ]):

        return "greeting"


    # -----------------------------------------------------
    # MORNING
    # -----------------------------------------------------

    if "good morning" in command:

        return "morning"


    # -----------------------------------------------------
    # NIGHT
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "good night",
        "goodnight"
    ]):

        return "night"


    # -----------------------------------------------------
    # HOW ARE YOU
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "how are you",
        "how are you doing",
        "you good"
    ]):

        return "how_are_you"


    # -----------------------------------------------------
    # THANK YOU
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "thank you",
        "thanks",
        "thanks jarvis"
    ]):

        return "thanks"


    # -----------------------------------------------------
    # WHO ARE YOU
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "who are you",
        "what are you",
        "tell me about yourself"
    ]):

        return "who_are_you"


    # -----------------------------------------------------
    # WHO AM I
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "who am i",
        "do you know me"
    ]):

        return "who_am_i"


    # -----------------------------------------------------
    # WHAT CAN YOU DO
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "what can you do",
        "your capabilities",
        "what are your capabilities",
        "help me"
    ]):

        return "capabilities"


    # -----------------------------------------------------
    # TIME
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "what time",
        "tell me the time",
        "current time",
        "time"
    ]):

        return "time"


    # -----------------------------------------------------
    # DATE
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "what date",
        "today's date",
        "todays date",
        "date"
    ]):

        return "date"


    # -----------------------------------------------------
    # DAY
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "what day",
        "which day",
        "day today"
    ]):

        return "day"


    # -----------------------------------------------------
    # JOKE
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "tell me a joke",
        "tell a joke",
        "make me laugh",
        "joke"
    ]):

        return "joke"


    # -----------------------------------------------------
    # BORED
    # -----------------------------------------------------

    if any(phrase in command for phrase in [
        "i am bored",
        "i'm bored",
        "bored"
    ]):

        return "bored"


    # -----------------------------------------------------
    # OPEN CHROME
    # -----------------------------------------------------

    if (
        "chrome" in command
        and any(word in command for word in [
            "open",
            "launch",
            "start",
            "run",
            "show"
        ])
    ):

        return "chrome"


    # -----------------------------------------------------
    # OPEN VS CODE
    # -----------------------------------------------------

    if (
        ("vs code" in command or "visual studio code" in command)
        and any(word in command for word in [
            "open",
            "launch",
            "start",
            "run"
        ])
    ):

        return "vscode"


    # -----------------------------------------------------
    # YOUTUBE
    # -----------------------------------------------------

    if any(word in command for word in [
        "youtube",
        "play on youtube",
        "search youtube"
    ]):

        return "youtube"


    # -----------------------------------------------------
    # GOOGLE SEARCH
    # -----------------------------------------------------

    if any(word in command for word in [
        "search",
        "google",
        "look up"
    ]):

        return "google"


    # -----------------------------------------------------
    # CALCULATOR
    # -----------------------------------------------------

    if any(word in command for word in [
        "calculate",
        "plus",
        "minus",
        "multiplied",
        "divided"
    ]):

        return "calculate"


    return "unknown"


# =========================================================
# EXECUTION
# =========================================================

def execute(intent, command):

    if intent == "greeting":

        speak("Hello sir. How can I help you?")


    elif intent == "morning":

        morning_response()


    elif intent == "night":

        night_response()


    elif intent == "how_are_you":

        respond_how_are_you()


    elif intent == "thanks":

        thank_you_response()


    elif intent == "who_are_you":

        who_are_you()


    elif intent == "who_am_i":

        who_am_i()


    elif intent == "capabilities":

        what_can_you_do()


    elif intent == "time":

        tell_time()


    elif intent == "date":

        tell_date()


    elif intent == "day":

        tell_day()


    elif intent == "joke":

        tell_joke()


    elif intent == "bored":

        bored_response()


    elif intent == "chrome":

        open_chrome()


    elif intent == "vscode":

        open_vscode()


    elif intent == "google":

        query = command

        for trigger in [
            "search for",
            "search",
            "google",
            "look up"
        ]:

            if trigger in query:

                query = query.replace(trigger, "", 1)

                break

        search_google(query)


    elif intent == "youtube":

        query = command

        for trigger in [
            "search youtube for",
            "youtube",
            "play"
        ]:

            if trigger in query:

                query = query.replace(trigger, "", 1)

                break

        search_youtube(query)


    elif intent == "calculate":

        calculate(command)


    elif intent == "exit":

        speak("Goodbye sir. JARVIS shutting down.")

        return False


    else:

        speak(
            "I'm not sure what you mean yet, sir. "
            "I'm still learning."
        )


    return True


# =========================================================
# COMMAND STACKING
# =========================================================

def process_command(command):

    """
    Allows commands like:

    "open chrome and search Python"

    to be split into multiple commands.
    """

    commands = command.split(" and ")

    for single_command in commands:

        intent = understand(single_command)

        running = execute(intent, single_command)

        if running is False:

            return False

    return True


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    speak(
        "JARVIS online, sir. "
        "All systems are ready."
    )

    running = True

    while running:

        command = take_command()

        if command:

            running = process_command(command)