import random

def ask_question():
    input("Ask a magic 8-ball question (press enter to quit): ")

def get_fortune():
    responses = [
        "Yes, definitely.",
        "It is certain.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    return random.choice(responses)

def main():
    print("Welcome to the Magic 8-Ball!")
    
    while True:
        ask_question()
        print("Thinking...")
        print(get_fortune())
        print()
        if input("Would you like to ask another question? (yes/no): ").lower() != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
