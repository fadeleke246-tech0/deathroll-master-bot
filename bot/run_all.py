from brain import Brain
import time

def main():
    brain = Brain()
    print("Deathroll bot is running")

    tests = ["hello", "status", "help", "unknown command"]

    for text in tests:
        print("You:", text)
        reply = brain.think(text)
        print("Bot:", reply)
        time.sleep(1)

if __name__ == "__main__":
    main()
