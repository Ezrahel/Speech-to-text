# Speech-to-text
# Speech to Text Python Script

This Python script performs speech-to-text conversion using the `SpeechRecognition` library, which utilizes the Google Web Speech API. It takes an audio file as input and outputs the recognized text.

## Requirements

- Python 3.x
- `SpeechRecognition` library

## Installation

1. Clone this repository or download the script `speech_to_text.py` to your local machine.

2. Install the required `SpeechRecognition` library using the following command:


## Usage

1. Place your audio file (in WAV format) that you want to convert to text in the same directory as the `speech_to_text.py` script.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the following command:


4. The script will prompt you to provide the name of the audio file. Enter the name of the audio file (e.g., `your_audio.wav`) and press Enter.

5. The script will perform speech-to-text conversion using the Google Web Speech API and display the recognized text on the terminal.

## Notes

- The Google Web Speech API requires an internet connection to function.

- If the API cannot recognize the audio or encounters an error, the script will provide appropriate error messages.

- This script serves as a basic example of speech-to-text conversion. For more advanced features and customization, you might need to explore other speech recognition libraries and APIs.

## License

This project is licensed under the [MIT License](LICENSE).
