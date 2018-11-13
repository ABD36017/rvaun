import speech_recognition as sr
r = sr.recognize
with sr.Microphone() as source:
	r.adjust_for_ambient-noise(source,duration = 5)
	print("say something!")
	While True:#Creating a while loop
		audio = r.listen(source)#listening to microphone
		print("you said" + r.recognize_google(audio))#print output