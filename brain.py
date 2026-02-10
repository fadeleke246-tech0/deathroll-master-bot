class Brain:
    def __init__(self):
        self.state = "idle"

    def think(self):
        if self.state == "idle":
            return "Waiting for tasks..."
        elif self.state == "scanning":
            return "Scanning for new content..."
        elif self.state == "posting":
            return "Posting content..."
        else:
            return "Unknown state"

    def set_state(self, new_state):
        self.state = new_state
