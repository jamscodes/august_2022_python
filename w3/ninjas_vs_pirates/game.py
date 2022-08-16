from classes.fighter import Fighter
from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo", {'strength': 10, 'speed': 5, 'defense': 12})

jack_sparrow = Pirate("Jack Sparrow", {'strength': 15, 'speed': 3, 'defense': 15})

def run_game(ninja, pirate):
    Fighter.determine_initiative()

    first_fighter = Fighter.turn_order[0]
    second_fighter = Fighter.turn_order[1]
    # make some code that loops through an attack sequence
    while ninja.health > 0 and pirate.health > 0:
        # game loop

        first_fighter.attack(second_fighter)
        second_fighter.attack(first_fighter)

        print('#' * 60)
        ninja.show_stats()
        print('#' * 30)
        pirate.show_stats()
        print('#' * 60)

run_game(ninja = michelangelo, pirate = jack_sparrow)
