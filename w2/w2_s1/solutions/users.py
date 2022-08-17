class User: # inheritance
    def __init__(self, f_name:str = 'John', l_name:str = 'Doe') -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.abilities = self.collect_abilities()
        # association

    def __repr__(self) -> str:
        return f'This object has a name of: {self.f_name} {self.l_name}\nand it has these abilities: {self.abilities}'

    def collect_abilities(self) -> list:
        return [attribute for attribute in dir(self) if callable(getattr(self, attribute)) and attribute.startswith('__') is False]

    def introduce(self) -> None:
        print(f'Hi! My name is {self.f_name} {self.l_name}!')



jonathan = User()

print(jonathan)
