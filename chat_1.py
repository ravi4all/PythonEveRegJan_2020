print("Welcome",name := input("Enter your name : "))

while (msg := input("Enter your message : ")) != "bye":
    if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hi there":
        print("Hello",name)
    else:
        print("I don't understand")
