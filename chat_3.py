from datetime import datetime
import os, random, glob

print("Welcome",name := input("Enter your name : "))

helloIntent = ["hi","hello","hey","hi there","hello there"]
timeIntent = ["time","tell me time","what's the time","please tell me time"]
dateIntent = ["date","tell me date","what's the date","please tell me date"]
musicIntent = ["play song","play music","please play a song"]

while (msg := input("Enter your message : ").lower()) != "bye":
    if msg in helloIntent:
        print("Hello",name)
    elif msg in timeIntent:
        cur_time = datetime.now().time()
        print("Time is",cur_time.strftime("%H:%M:%S,%p"))
    elif msg in dateIntent:
        cur_date = datetime.now().date()
        print("Date is",cur_date.strftime("%d/%m/%y,%a"))
    elif msg in musicIntent:
        os.chdir(r'C:\Users\asus\Music')
        songs = glob.glob('*.mp3')
        curr_song = random.choice(songs)
        os.startfile(curr_song)
    else:
        print("I don't understand")
