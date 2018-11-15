class Player:
    def __init__(self, name, height, experience, guardians):
        self.name = name
        self.height = height
        self.experience = experience
        self.guardians = guardians

    def __lt__(self, other):
        return self.experience > other.experience

