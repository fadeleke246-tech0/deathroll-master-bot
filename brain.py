class Brain:
    def __init__(self):
        self.memory = []

    def think(self, text: str) -> str:
        self.memory.append(text.lower())

        if "hello" in text.lower():
            return "Hello 👋 I am Deathroll bot."

        if "help" in text.lower():
            return "I can scan, analyze, and report. More features coming."

        if "status" in text.lower():
            return "I'm alive and running smoothly 😎"

        return "I heard you. I'm still learning."
