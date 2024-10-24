import pyttsx3
import sys

tts = pyttsx3.init()
print('Enter the text to speak, or QUIT to quit.')

while True:
    userInput = input(">_ ")
    if userInput.upper() == "QUIT":
        print("Goodbye!")
        sys.exit()
    else:
        tts.say(userInput)
        tts.runAndWait()