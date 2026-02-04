import speech_recognition as sr
import pyttsx3
import logging
import os
import webbrowser
import datetime
import wikipedia
#import google.generativeai as genai
from dotenv import load_dotenv
import platform
import pygetwindow as gw
import pyautogui
#from transformers import pipeline
import requests
from pytube import Search
import re
from youtubesearchpython import Search
import pywhatkit
import keyboard
import shutil
#import smtplib
import g4f
import screen_brightness_control as sbc
'''
from func.Chat import Chat
from func.SpeakOnline import Speak
from func.ListenJs import Listen
from func.DataOnline import Online_Scraper
from llm.ChatGpt import ChatGpt
from func.Ocr import Ocr
'''


# Logging setup
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to male voice
def speak(text):
    """
    Converts text to speech.
    """
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    """
    Listens to the user's voice input and converts it to text.
    Returns:
        str: The recognized speech as text, or None if not understood.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-US")
            print(f"You said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that. Please try again.")
            speak("Sorry, I didn't understand that. Please try again.")
            logging.info("Speech not understood.")
        except sr.RequestError as e:
            print("Could not request results. Check your internet connection.")
            speak("Could not request results. Check your internet connection.")
            logging.error(f"API error: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            speak("An error occurred. Please try again.")
        return None
def wish_me():
    """
    Greets the user based on the time of day.
    """
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Taamim!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Taamim!")
    else:
        speak("Good Evening Taamim!")
    speak("I am Jarvis. Please tell me how I can help you.")
    """
    Locks the device based on the operating system.
    """
    operating_system = platform.system()








messages = [{"role": "user", "content": "Hello"}]


def ChatGpt(input_message: str, provider_name: str):
    """
    Function to interact with GPT model using the g4f library.


    Parameters:
    - input_message (str): The user's input message.
    - provider_name (str): The name of the provider to use.
   
    Returns:
    - response_content (str): The assistant's response content.
    """
    # Update the conversation history with the user's input
    import g4f


# Initialize the messages list with a default user message
import g4f


# Initialize the messages list with a default user message
messages = [{"role": "user", "content": "Hello"}]


def ChatGpt(input_message: str, provider_name: str = "OpenaiChat"):
    """
    Function to interact with GPT model using the g4f library.


    Parameters:
    - input_message (str): The user's input message.
    - provider_name (str): The name of the provider to use (default is 'OpenaiChat').


    Returns:
    - response_content (str): The assistant's response content.
    """
    global messages


    # Append the user's input to the conversation history
    messages.append({"role": "user", "content": input_message})


    try:
        # Dynamically retrieve the provider
        provider = getattr(g4f.Provider, provider_name, None)
        if not provider:
            raise ValueError(f"Invalid provider: {provider_name}")


        # Generate a response using g4f
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=provider,
            messages=messages,
            stream=True,
        )


        # Collect the streamed response
        response_content = ""
        for chunk in response:
            print(chunk, end="", flush=True)  # Streamed output
            response_content += chunk


        print()  # Add a newline for formatting


        # Append the assistant's response to the conversation history
        messages.append({"role": "assistant", "content": response_content})


        return response_content


    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


# Example usage
response = ChatGpt("What is AI?")
print("\nAssistant Response:", response)








def lock_device():
    """
    Locks the device based on the operating system.
    """
    os_name = platform.system()
    if os_name == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif os_name == "Darwin":  # macOS
        os.system("/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend")
    elif os_name == "Linux":
        os.system("gnome-screensaver-command -l")
    else:
        speak("Unsupported operating system.")
#  API key for today's latest news
API_KEY = "15fd8378b1904f969ab670730e8886f8"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
def main():
    """
    The main function to run the assistant.
    """
    wish_me()
    while True:
        query = takeCommand()
        if query:
            query = query.lower()
            if "time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif "date" in query:
                today_date = datetime.datetime.now().date()
                speak(f"Todays date is {today_date}")
            elif "open google" in query:
                speak("Opening Google...")
                webbrowser.open("http://www.google.com")
            elif "open facebook" in query:
                speak("Opening Facebook...")
                webbrowser.open("http://www.facebook.com")
            elif "open youtube" in query:
                speak("Opening YouTube...")
                webbrowser.open("http://www.youtube.com")
            elif "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Sorry, I couldn't find any results on Wikipedia.")
            elif "play music" in query:
                musicPath = r"C:\Users\LENOVO\Downloads\dark-netflix-theme-song.mp3"
                speak("Playing music...")
                os.startfile(musicPath)
            elif "open meet" in query:
                speak("Opening Google Meet...")
                webbrowser.open("https://meet.google.com/landing")
            elif "open ugv portal" in query:
                speak("Opening UGV portal...")
                webbrowser.open("https://webportal.ugv.edu.bd/LoginPage.aspx")
            elif "open ms word" in query:
                speak("Opening Microsoft Word...")
                word_location = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
                os.startfile(word_location)


            elif "open PowerPoint" in query:
                speak("Opening Microsoft Powerpoint...")
                powerpoint_location  = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
                os.startfile(powerpoint_location)


            elif "open ms excel" in query:
                speak("Opening Microsoft Excel...")
                excel_location = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
                os.startfile(excel_location)


            elif "search" in query and "on youtube" in query:
                def search_youtube(query):
                    search_query = query.replace("search", "").replace("on youtube", "").strip()
                    speak(f"Searching for {search_query} on YouTube...")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
                search_youtube(query)


            elif "play" in query and "" in query:
                def play():
                        if 'play' in query:
                            song = query.replace('play', '').strip()
                            speak(f"Playing {song}")
                            pywhatkit.playonyt(song)
                play()


            elif "pause the video" in query:
                def pause():
                    speak("Pausing the video")
                    keyboard.press_and_release('space')
                pause()


            elif "start the video" in query:
                def start():
                    speak("starting the video")
                    keyboard.press_and_release('space')
                start()    




            elif "search" in query and "on google" in query:
                def search_google(query):
                    search_query = query.replace("search", "").replace("on google", "").strip()
                    speak(f"Searching for {search_query} on Google...")
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")
                search_google(query)
            elif "today's latest news" in query:
                speak("Fetching today's latest news...")
   
                # Define the function to fetch and speak news
                def get_latest_news():
                    try:
                        response = requests.get(NEWS_URL)
                        if response.status_code == 200:
                            news_data = response.json()
                            articles = news_data.get('articles', [])
                            if not articles:
                                return "No news found!"
                            news_summary = []
                            for idx, article in enumerate(articles[:5], start=1):  # Display top 5 news
                                title = article['title']
                                source = article['source']['name']
                                url = article['url']
                                news_summary.append(f"{idx}. {title} (Source: {source}).")
                            return "\n".join(news_summary)
                        else:
                            return f"Error fetching news. HTTP Status Code: {response.status_code}"
                    except Exception as e:
                        return f"An error occurred: {e}"
                # Fetch and speak the news
                latest_news = get_latest_news()
                print(latest_news)  # Also print the news to the console for reference
                speak(latest_news)  # Use the assistant's speech function to read the news
            elif "exit" in query or "quit" in query:
                speak("Thank you for using Jarvis. Goodbye!")
                break
            elif "lock the device" in query:
                speak("Locking the device...")
                lock_device()
            elif "close the window" in query:
                speak("Closing the window...")
                pyautogui.hotkey('alt', 'f4')
            elif "open file explorer" in query:
                speak("Opening File Explorer...")
                pyautogui.hotkey('win', 'e')
            elif "open settings" in query:
                speak("Opening Settings...")
                pyautogui.hotkey('win', 'i')
            elif "switch tab" in query:
                speak("Switching tab...")
                pyautogui.hotkey('ctrl', 'tab')
            elif "new tab" in query:
                speak("Opening new tab...")
                pyautogui.hotkey('ctrl', 't')
            elif "close tab" in query:
                speak("Closing tab...")
                pyautogui.hotkey('ctrl', 'w')
            elif "open task manager" in query:
                speak("Opening Task Manager...")
                pyautogui.hotkey('ctrl', 'shift', 'esc')
            elif "open command prompt" in query:
                speak("Opening Command Prompt...")
                os.system("start cmd")
            elif "minimize all" in query:
                speak("Minimizing all windows...")
                pyautogui.hotkey('win', 'd')
            elif "maximize window" in query:
                speak("Maximizing window...")
                pyautogui.hotkey('win', 'up')
            elif "open notepad" in query:
                speak("Opening Notepad...")
                os.system("notepad")
            elif "open calculator" in query:
                speak("Opening Calculator...")
                os.system("calc")
            elif "shutdown" in query:
                speak("Shutting down system...")
                os.system("shutdown /s /t 1")  
            elif "restart" in query:
                speak("Restarting system...")
                os.system("shutdown /r /t 1")    


            elif "increase volume" in query:
                speak("Increasing volume...")
                pyautogui.press("volumeup")
            elif "decrease volume" in query:
                speak("Decreasing volume...")
                pyautogui.press("volumedown")
            elif "mute" in query:
                speak("Muting audio...")
                pyautogui.press("volumemute")    


            elif "increase brightness" in query:
                speak("Increasing brightness...")
                current = sbc.get_brightness(display=0)[0]
                sbc.set_brightness(min(current + 10, 100))


            elif "lower brightness" in query:
                speak("Decreasing brightness...")
                current = sbc.get_brightness(display=0)[0]
                sbc.set_brightness(max(current - 10, 0))




            elif "create new folder" in query:
                speak("Please say the names of the folders you want to create, separated by commas.")
   
    # Get folder names from the user
                folder_input = input("Enter folder names (comma separated): ")  # Or use speech recognition if you're using voice
                folder_names = [name.strip() for name in folder_input.split(",")]


                for folder_name in folder_names:
                    try:
                        os.makedirs(folder_name, exist_ok=True)
                        speak(f"Folder '{folder_name}' created successfully.")
                    except Exception as e:
                        speak(f"Failed to create folder '{folder_name}': {e}")




            elif "delete folder" in query:
                speak("Please say the names of the folders you want to delete, separated by commas.")
   
    # Take folder names from the user
                folder_input = input("Enter folder names to delete (comma separated): ")  # Replace with takeCommand() if using voice
                folder_names = [name.strip() for name in folder_input.split(",")]


                for folder_name in folder_names:
                    if os.path.exists(folder_name):
                        try:
                            shutil.rmtree(folder_name)  # Deletes folders even if they have files inside
                            os.rmdir(folder_name) #delete folder if the folder is empty
                            speak(f"Folder '{folder_name}' has been deleted successfully.")
                        except Exception as e:
                            speak(f"Failed to delete folder '{folder_name}': {e}")
                    else:
                        speak(f"Folder '{folder_name}' does not exist.")




            elif "create new file" in query:
                speak("Please say the name of the file you want to create, including the extension.")
   
                # Get the file name from the user
                file_name = input("Enter the file name (e.g., myfile.txt): ")  # Replace with takeCommand() if using voice


                try:
                    with open(file_name, 'x') as file:
                        file.write("")  # Creates an empty file
                    speak(f"File '{file_name}' created successfully.")
                except Exception as e:
                    speak(f"Failed to create file '{file_name}': {e}")






            elif "delete file" in query:
                speak("Please say the names of the files you want to delete, separated by commas.")


    # Get file names from user
                file_input = input("Enter file names to delete (comma separated): ")  # Or use takeCommand()
                file_names = [name.strip() for name in file_input.split(",")]


                for file_name in file_names:
                    if os.path.exists(file_name):
                        try:
                            os.remove(file_name)
                            speak(f"File '{file_name}' has been deleted successfully.")
                        except Exception as e:
                            speak(f"Failed to delete file '{file_name}': {e}")
                    else:
                        speak(f"File '{file_name}' does not exist.")








if __name__ == "__main__":
    main()







