import pyttsx3
import random
import time
WAIT = 100
#ЭТО ЧИСЛО ОБОЗНАЧАЕТ ПРОМЕЖУТОК МЕЖДУ ФРАЗАМИ
tts = pyttsx3.init()
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
tts.setProperty('voice', ru_voice_id)
PHRASES = ["Это тестовое сообщение", "Это ещё тестовое сообщение", "Это е"]
#ЭТО МАССИВ СО СЛОВАМИ, КОТОРАЯ БУДЕТ ПРОИЗНОСИТЬ ПРОГРАММА
while(True):
    tosay = PHRASES[random.randint(0, len(PHRASES)-1)]
    print(tosay)
    tts.say(tosay)
    tts.runAndWait()
    time.sleep(WAIT)