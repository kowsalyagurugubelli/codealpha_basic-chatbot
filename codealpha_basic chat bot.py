def chatbot():
    print("Chatbot started")
    while True:
        user = input().lower()
        if user == "hello":
            print("Hi")
        elif user == "how are you":
            print("I'm fine, thanks")
        elif user == "bye":
            print("Goodbye")
            break
        else:
            print("Can't understand")
chatbot()