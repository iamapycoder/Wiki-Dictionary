
import wikipedia

wikipedia.set_lang("en")
ans = wikipedia.summary(input(), sentences=1)
print(wikipedia.summary(ans, sentences=1))
import pyttsx3
engine = pyttsx3.init()
engine.say(ans)
engine.runAndWait()
