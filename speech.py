import speech_recognition as sr 

def listen_mic():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Por favor, diga um comando:")
        audio = mic.listen(source)
    
    try:
        comand = mic.recognize_google(audio, language='pt-BR')
        print("Voce disse: " + comand)
    except sr.UnknowValueError:
        print("Não entendi")
    
    return comand

listen_mic()