from brain import Brain

print("Deathroll bot is running")

brain = Brain()

tests = ["hello", "who are you", "status"]

for text in tests:
    print("\nYou:", text)
    reply = brain.think(text)
    print("Bot:", reply)
