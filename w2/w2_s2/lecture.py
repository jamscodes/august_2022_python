class Pokemon:
    necessary_stats = ['health', 'attack', 'defense']

    def __init__(self, type:list, name:str, stats:dict) -> None:
        if self.validate_stats(stats, self.necessary_stats):
            self.type = type
            self.name = name
            self.stats = stats
        else:
            raise Exception('Invalid stats')

    def __repr__(self) -> str:
        return f'{self.name}'

    @staticmethod
    def validate_stats(stats_given:dict, required_stats:list) -> bool:
        for stat in required_stats:
            if stat not in stats_given:
                print(f'stat: {stat} is missing!')
                return False
            
        return True






bulbasaur = Pokemon(type = ['grass', 'poison'], name = 'Bulbasaur', stats = {'attack': 10, 'defense': 10})

print(bulbasaur.type[0])