from brain import Brain

def main():
    brain = Brain()
    print("Deathroll bot is running")

    # test inputs
    while True:
        user_input = input("You: ")
        reply = brain.think(user_input)
        print("Bot:", reply)

if __name__ == "__main__":
    main()
