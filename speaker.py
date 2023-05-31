import speech_recognition as sr

recognizer=sr.Recognizer()
microphone=sr.Microphone()

sr.LANGUAGE='ru-RU'

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Вы можете говорить")
    audio=recognizer.listen(source)

text=recognizer.recognize_google(audio, language='ru-RU')

print(f"Вы сказали: {text}")


