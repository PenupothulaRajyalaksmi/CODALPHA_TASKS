"""
Project    : Basic Rule-Based Chatbot
Developer  : Raji
Description: A simple chatbot using
             functions, loops, if-elif,
             and input/output.
"""


def chatbot():
    print("=" * 50)
    print("Welcome to Raji Chatbot")
    print("=" * 50)

    # Ask user's name
    print("Bot : Hello! What's your name?")
    name = input("You : ")

    print(f"\nBot : Nice to meet you, {name}!")
    print("Bot : What do you want to learn today?")

    while True:
        message = input("You : ").strip().lower()

        if "python" in message:
            print("Bot : Of course! I can help you learn Python.")
            print("Bot : Ask me about variables, loops, functions, or basic programs.")

        elif "java" in message:
            print("Bot : Sure! I can also help you learn Java basics.")

        elif "how are you" in message:
            print("Bot : I'm doing great. Thanks for asking!")

        elif "thank" in message:
            print("Bot : You're welcome!")

        elif message in ["bye", "exit", "quit"]:
            print(f"Bot : Goodbye, {name}! Happy Coding.")
            break

        else:
            print("Bot : Sorry, I don't understand that.")
            print("Bot : Please ask about Python or Java, or type 'bye' to exit.")


def main():
    chatbot()


if __name__ == "__main__":
    main()