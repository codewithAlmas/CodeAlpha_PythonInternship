# Display chatbot title
print("Simple Chatbot")

# Instruction for the user to exit the chatbot
print("Type 'bye' to exit")

# Infinite loop to keep chatbot running
while True:

    # Take user input and convert it to lowercase
    user = input("You: ").lower()

    # Check if user says hello
    if user == "hello":
        print("Bot: Hi!")

    # Check if user asks about chatbot's condition
    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    # Check if user asks chatbot's name
    elif user == "what is your name":
        print("Bot: I am a Python chatbot.")

    # Exit condition
    elif user == "bye":
        print("Bot: Goodbye!")
        break

    # Default response for unknown inputs
    else:
        print("Bot: I don't understand.")







