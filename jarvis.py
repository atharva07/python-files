import pyttsx3

engine = pyttsx3.init('Sapi5')
voice = engine.getProperty('voice')
print(voice[1].id)
engine.setProperty('voice', voice[0].id)

# def speak(audio):
