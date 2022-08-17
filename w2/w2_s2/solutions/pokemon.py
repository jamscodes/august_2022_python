class Pokemon:
    necessary_stats = ['health', 'attack', 'defense', 'special_attack', 'special_defense', 'speed']
    
    def __init__(self, id:str, name:str, type:list, stats=dict[str]) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.stats = stats if self.validate_stats(stats, self.necessary_stats) else None

    @staticmethod
    def is_alive(health) -> None:
        print('#'*40)
        print('Your pokemon is still alive!' if health > 0 else 'Your pokemon has fainted.')
        print('#'*40)

    @staticmethod
    def validate_stats(stats:dict[str], necessary_stats) -> bool:
        for stat in necessary_stats:
            if stat not in stats:
                print('#'*40)
                print('{:20}'.format(f'Stat: {stat} missing!'))
                print('#'*40)
                return False
        return True


bulbasaur = Pokemon(id = '001', name="Bulbasaur", type=['grass','poison'], stats={'attack': 3, 'defense': 3, 'special_attack': 4, 'special_defense': 4, 'speed': 3})
ivysaur = Pokemon(id = '002', name="Ivysaur", type=['grass','poison'], stats={'health': 3, 'attack': 3, 'defense': 3, 'special_attack': 4, 'special_defense': 4, 'speed': 3})

print(bulbasaur.stats)
print(ivysaur.id)