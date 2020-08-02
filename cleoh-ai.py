from time import ctime
from gtts import gTTS
import speech_recognition as sr
import re
import wikipedia
import webbrowser
import requests
import os
from pygame import mixer
import sys
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import urllib.request
from xml.dom import minidom

i = 0


def speak(audio_string):
    global i
    i = i + 1
    print(audio_string)
    tts = gTTS(text=audio_string, lang='en', slow=False)
    tts.save("audio" + str(i) + ".mp3")
    mixer.init()
    mixer.music.load("audio" + str(i) + ".mp3")
    mixer.music.play()


def my_command():
    """listens for commands"""

    r = sr.Recognizer()

    with sr.Microphone(device_index=0, chunk_size=2048, sample_rate=48000) as source:
        print('Please speak some commands')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = my_command()

    return command


def assistant(command):
    """if statements for executing commands"""

    if 'github' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://github.com/mkdirlove'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        os.system('clear && clear')
        print(banner)
        print('Done!')
        speak("How can i help you more, sir?")
    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            os.system('clear && clear')
            print(banner)
            print('Done!')
            speak("Done,,How can i help you more, sir?")
        else:
            pass

    elif 'what are you doing' in command:
        speak('Just chillin here')

    elif 'search' in command:
        reg_ex = re.search('search (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.google.com/maps/place/' + domain
            webbrowser.open(url)
            os.system('clear && clear')
            print(banner)
            print('Done!')
            speak("Done,,How can i help you more, sir?")
        else:
            pass

    elif 'find' in command:
        reg_ex = re.search('find (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.google.co.in/search?q=' + domain
            webbrowser.open(url)
            os.system('clear && clear')
            print(banner)
            print('Done!')
            speak("Done,,How can i help you more sir?")
        else:
            pass

    elif 'tell weather at' in command:
        reg_ex = re.search('tell weather at(.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'http://www.intellicast.com/Local/Default.aspx?query=' + domain
            webbrowser.open(url)
            os.system('clear && clear')
            print(banner)
            print('Done!')
            speak("Done,,How can i help you more sir?")
        else:
            pass

    elif 'what is your name' in command:
        os.system('clear && clear')
        print(banner)
        speak('My name is Cleoh, how can i help you sir?')
    
    elif 'meaning' in command:
        reg_ex = re.search('meaning (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://translate.google.com/#en/hi/' + domain
            webbrowser.open(url)
            os.system('clear && clear')
            print(banner)
            print('Done!')
            speak("Done,,How can i help you more sir?")
        else:
            pass

    elif 'reboot system' in command:
        os.system('clear && clear')
        print(banner)
        speak("System, rebooting in 5, 4, 3, 2, 1")
        os.system('reboot')
        
        
    
    elif 'game' in command:
        reg_ex = re.search('game (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.miniclip.com/games/search/en/?query=' + domain
            webbrowser.open(url)
            os.system('clear && clear')
            print(banner)
            print('Done!')
            speak("Done,,How can i help you more sir?")
        else:
            pass

    elif 'who are you' in command:
        os.system('clear && clear')
        print(banner)
        speak('I am Cleoh, your personal assistant')

    elif 'play' in command:
        reg_ex = re.search('play (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://gaana.com/search/' + domain
            webbrowser.open(url)
            os.system('clear && clear')
            print(banner)
            print('Done!')
            speak("Done,,How can i help you more sir?")
        else:
            pass

    
    elif 'read' in command:
        reg_ex = re.search('read (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://en.wikipedia.org/wiki/' + domain
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            summary = soup.find('div', class_ = 'mw-body').p.text
            webbrowser.open(url)
            speak(summary)


    elif 'joke' in command:
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"}
        )
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('oops!, I ran out of jokes')

    elif "how are you" in command:
        os.system('clear && clear')
        print(banner)
        speak("I am fine, how about you sir?")

    elif "time" in command:
        os.system('clear && clear')
        print(banner)
        speak(ctime())
    else:
        speak("Just google it sir!")

banner = """
 ██████╗██╗     ███████╗ ██████╗ ██╗  ██╗       █████╗ ██╗
██╔════╝██║     ██╔════╝██╔═══██╗██║  ██║      ██╔══██╗██║
██║     ██║     █████╗  ██║   ██║███████║█████╗███████║██║
██║     ██║     ██╔══╝  ██║   ██║██╔══██║╚════╝██╔══██║██║
╚██████╗███████╗███████╗╚██████╔╝██║  ██║      ██║  ██║██║
 ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝      ╚═╝  ╚═╝╚═╝"""
os.system('clear && clear')
print('')
print(banner)
speak('Hello sir, i am ready for your command.')

# loop to continue executing multiple commands
while True:
    assistant(my_command())
