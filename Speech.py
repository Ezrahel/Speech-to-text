import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

try:
    # Perform speech recognition
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand audio.")
except sr.RequestError as e:
    print("Sorry, an error occurred. {0}".format(e))
