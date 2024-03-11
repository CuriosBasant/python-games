import pyttsx3
import datetime
import speech_recognition as SR
print('\n---------------------------')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def wish_me():
    hour = datetime.datetime.now().hour
    wish_text = 'Morning' if hour < 12 else 'Afternoon' if hour < 18 else 'Evening'
    speak('Good ' + wish_text)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = SR.Recognizer()
    with SR.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 500
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in')
        print('Query :', query)
    except Exception as err:
        print(err, 'Say that again please!')
        return 'None'

    return query.lower()


if __name__ == "__main__":
    wish_me()
    command = take_command()
