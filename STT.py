import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to capture speech and convert to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            # Use Google Web Speech API
            text = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Call the function
speech_to_text()

# Continuous Speech Recognition
def continuous_speech_to_text():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language='th-TH')
                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Couldn't understand, please try again.")
            except sr.RequestError as e:
                print(f"Request error: {e}")
                break

continuous_speech_to_text()
