import speech_recognition as sr
from gtts import gTTS 
import os
import playsound
import webbrowser

def get_audio():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.pause_threshold = 1
        mic.adjust_for_ambient_noise(source, duration=1)
        audio = mic.listen(source)
        said = ''
        try:
            said = mic.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak('Sorry, I didn\'t recognize')
        except sr.RequestError:
            speak('Sorry, this option is not available')
    
    return said.lower()

def speak(text):
    tts = gTTS(text, lang='en')
    filename = 'comand.mp3'
    try:
        os.remove(filename)
    except OSError:
        pass 
    tts.save(filename)
    playsound.playsound(filename)

def respond(text):
    print('Text from get audio: ' + text)
    if 'youtube' in text:
        speak('What do you want to search for:')
        keyword = get_audio()
        if keyword != '':
            url = f'https://www.youtube.com/results?search_query={keyword}'
            webbrowser.get().open(url)
            speak(f'Here is what I found for {keyword} on Youtube')
    elif 'exit' in text:
        speak('Goodbye, till next time')
        exit()

while True:
    print('I am listining....')
    text = get_audio()
    respond(text)