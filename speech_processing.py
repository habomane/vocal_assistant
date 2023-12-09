import speech_recognition as sr


class SpeechProcessing: 
    
    def __init__(self):
        self.recongizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = None
            self.recongizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recongizer.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Are you speaking?")
            text = ""
            
            try: 
                print("Recognizing...")
                text = self.recongizer.recognize_google(audio)
                print(f"Did you say '{text}'? ")
            except sr.UnknownValueError:
                print("Google speech could not recongnize the audio") 
            except sr.RequestError:
                print("Could not complete error")
            except Exception:
                print("There was an error")
            


            return text


    def speak(self):
        pass