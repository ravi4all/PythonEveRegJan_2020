import speech_recognition as sr
from gtts import gTTS
import pygame

pygame.mixer.init()

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()
device_id = None

while True:
    #user_msg = input("Enter your message : ")

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:

        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Waiting for connection")
        text = r.recognize_google(audio)
        text = text.lower()
        print("you said: " + text)
        if text == "hello":
            reply = "Hello, How are you"
        else:
            reply = "I am unable to understand what you said...Please try again"
        tts = gTTS(text=reply, lang='en')
        tts.save("file.mp3")
        pygame.mixer.music.load('file.mp3')
        pygame.mixer.music.play(1)
