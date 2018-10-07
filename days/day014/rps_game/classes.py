class Roll():
    def __init__(self, roll:str, defeat:tuple):
        self.roll = roll
        self.defeat = defeat
    
    def candefeat(self, other):
        if other.roll in self.defeat:
            return True
        return False

class Player():
    def __init__(self, name):
        self.name = name
        self.count = 0
