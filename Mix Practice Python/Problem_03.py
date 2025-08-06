import pyjokes
joke=pyjokes.get_joke()
print(joke)

import pyttsx3
Engine= pyttsx3.init()
Engine.say("Hey I am Anees UL Rehman. Belong to Umerkot Sindh. What about you?")
Engine.runAndWait()

