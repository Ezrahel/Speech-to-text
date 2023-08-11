# import speech_recognition as sr

# # Create a recognizer object
# r = sr.Recognizer()

# # Use the microphone as the audio source
# with sr.Microphone() as source:
#     print("Speak something...")
#     audio = r.listen(source)

# try:
#     # Perform speech recognition
#     text = r.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Sorry, I could not understand audio.")
# except sr.RequestError as e:
#     print("Sorry, an error occurred. {0}".format(e))

import speech_recognition as sr

def speech_to_text(audio_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        # Record the audio data from the file
        audio_data = recognizer.record(source)
        
        try:
            # Use Google Web Speech API to perform speech recognition
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"

if __name__ == "__main__":
    audio_file_path = "path_to_your_audio_file.wav"  # Replace with the actual path to your audio file
    recognized_text = speech_to_text(audio_file_path)
    
    print("Recognized Text:")
    print(recognized_text)


