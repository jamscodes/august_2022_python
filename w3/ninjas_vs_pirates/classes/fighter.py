from random import randint

class Fighter:
    turn_order = []

    def __init__(self, name, stats):
        self.name = name
        self.health = 100
        self.strength = stats['strength']
        self.defense = stats['defense']
        self.speed = stats['speed']

        self.turn_order.append(self)

    @classmethod
    def determine_initiative(cls):
        for fighter in cls.turn_order:
            fighter.initiative = fighter.speed + randint(1, 20)

        if cls.turn_order[0].initiative < cls.turn_order[1].initiative:
            cls.turn_order[0], cls.turn_order[1] = cls.turn_order[1], cls.turn_order[0]

    
    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, fighter):
        attack_roll = randint(1, 20) + self.strength

        if attack_roll > fighter.defense:
            fighter.health -= self.strength
        return self