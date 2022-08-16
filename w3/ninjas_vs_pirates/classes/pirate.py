from .fighter import Fighter

class Pirate(Fighter):
    def __init__(self, name, stats):
        super().__init__(name, stats)
