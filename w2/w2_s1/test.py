class User:
    def __init__(self, f_name:str, l_name:str, age:int) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def __repr__(self) -> str:
        return f'This object is named {self.f_name} {self.l_name}'

    def introduce_yourself(self) -> None:
        print(f'Hi! My name is {self.f_name} {self.l_name}')


jonathan = User(f_name = 'Jonathan', l_name = 'Moore', age = 26)
rene = User(f_name = 'Rene', l_name = 'Marino', age = 48)

jonathan.introduce_yourself()
print(rene)