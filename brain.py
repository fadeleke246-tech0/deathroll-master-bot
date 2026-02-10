from datetime import datetime

class Brain:
    def __init__(self):
        self.memory = []

    def remember(self, item):
        if item not in self.memory:
            self.memory.append(item)

    def has_seen(self, item):
        return item in self.memory

    def decide_if_good(self, text):
        bad_words = ["hack", "crack", "pirated", "illegal"]
        return not any(word in text.lower() for word in bad_words)

    def stamp(self, text):
        return f"{text}\n\n🔗 Powered by deathroll.co\n🕒 {datetime.utcnow()} UTC"
