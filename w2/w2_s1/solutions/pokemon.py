class Pokemon:
    necessary_stats = ['health', 'attack', 'defense', 'special_attack', 'special_defense', 'speed']
    
    def __init__(self, id:str, name:str, type:list, stats=dict[str]) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.stats = stats if self.validate_stats(stats) else None

    def check_health(self) -> None:
        print('#'*40)
        print('{:10}'.format(self.stats['health']))
        print('#'*40)

    def validate_stats(self, stats:dict[str]) -> bool:
        for stat in self.necessary_stats:
            if stat not in stats:
                print('#'*40)
                print('{:20}'.format(f'Stat: {stat} missing!'))
                print('#'*40)
                return False
        return True

class Abilities:
    def __init__(self, name:str) -> None:
        pass


bulbasaur = Pokemon(id = '001', name="Bulbasaur", type=['grass','poison'], stats={'attack': 3, 'defense': 3, 'special_attack': 4, 'special_defense': 4, 'speed': 3})
ivysaur = Pokemon(id = '002', name="Ivysaur", type=['grass','poison'], stats={'health': 3, 'attack': 3, 'defense': 3, 'special_attack': 4, 'special_defense': 4, 'speed': 3})

print(bulbasaur.stats)
print(ivysaur.id)