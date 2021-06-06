import os
import pyttsx3
import speech_recognition as sr

#Creating classes
class PythonHub:
    # Method to take voice commands as input
    def takeCommands(self):
        #Using recognizer and microphone method for input voice commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')
            # Number of seconds of non-speaking audio before a phrase is considered complete
            r.pause_threshold = 0.7
            audio = r.listen(source)
            # voice input is identified
            try:
                # Listening voice commands in English
                print("Recognizing")
                Query = r.recognize_google(audio,language='en-us')

                # Displaying the voice command
                print("The query is printed= ",Query,"")
            except Exception as e:
                # Displaying Exception
                print(e)
                # Handling exception
                print('Say that again Sir or Madam')
                return "None"
            return Query
    # method for voice output
    def Speak(self,audio):
        # Constructor call for pyttsx3.init()
        engine = pyttsx3.init('sapi5')
        # Setting voice type and id
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    # Method to shut down system
    def quitSelf(self):
        self.Speak("Do you want to switch off the computer?")
        # Input voice command
        take = self.takeCommands()
        choice = take
        if "yes" in choice:
            # Shutting down 
            print("Shutting down the computer")
            self.Speak("Shutting the computer")
            os.system("Shutdown /s /t 30")
        if "no" in choice:
            print("Thanks for choosing to staying on")
            self.Speak("Thanks for choosing to staying on")

# Driver Code
if __name__ == '__main__':
    obj = PythonHub()
    obj.quitSelf()
