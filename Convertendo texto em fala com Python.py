#Convertendo texto em fala com Python

import pyttsx3

engine = pyttsx3.init()

engine.say("Coloque um texto aqui, que eu irei ler para você ")

engine.runAndWait()
