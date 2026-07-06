# CODSOFT-Task1-RuleBasedChafrom datetime import datetime

from datetime import datetime 
print("=" * 50)
print("🤖 Welcome to Rule-Based Chatbot")
print("Type 'bye' or 'exit' to end the conversation.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day. 😊")
        break

    elif any(word in user for word in ["hello", "hi", "hey"]):
        print("Bot: Hello! How can I help you today?")

    elif "your name" in user or "who are you" in user:
        print("Bot: I am a Rule-Based Chatbot created using Python.")

    elif "my name" in user:
        print("Bot: Nice to meet you!")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking. How about you?")

    elif "good" in user or "fine" in user:
        print("Bot: That's wonderful to hear!")

    elif "bad" in user or "sad" in user:
        print("Bot: I'm sorry to hear that. I hope things get better soon.")

    elif "help" in user:
        print("Bot: I can answer simple questions like greetings, date, time, Python, AI, and more.")

    elif "time" in user:
        print("Bot: Current time is", datetime.now().strftime("%I:%M %p"))

    elif "date" in user:
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif "python" in user:
        print("Bot: Python is a popular programming language known for its simplicity and versatility.")

    elif "artificial intelligence" in user or user == "ai":
        print("Bot: Artificial Intelligence (AI) enables machines to perform tasks that normally require human intelligence.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI where computers learn from data without being explicitly programmed.")

    elif "weather" in user:
        print("Bot: Sorry, I cannot check live weather because I'm a rule-based chatbot.")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    elif "your age" in user:
        print("Bot: I don't have an age. I was created as a Python chatbot.")

    elif "created you" in user or "made you" in user:
        print("Bot: I was created by a Python programmer as a rule-based chatbot project.")

    elif "joke" in user:
        print("Bot: Why do programmers prefer Python?")
        print("Bot: Because it's easy to understand and fun to code! 😄")

    else:
        print("Bot: Sorry, I didn't understand that.")
        print("Bot: Please try asking something else.")tbot
