class Piece:
    def __init__(self, name:str, color:str) -> None:
        self.name = name
        self.color = color

    def __repr__(self) -> str:
        return f'This is the {self.color} {self.name}'

    def move(self) -> None:
        pass

    @staticmethod
    def check_legal_move(move:str, legal_moves:list[str], spaces:int = 1) -> bool:
        return True if move in legal_moves else False


class King(Piece):
    legal_directions = ['forward', 'backward', 'left', 'right']

    def __init__(self, name:str, color:str) -> None:
        super().__init__(name, color)

    
    def move(self) -> None:
        move = input("What direction would you like to move? ")

        if self.check_legal_move(move, self.legal_directions):
            print(f'The {self.color} {self.name} moves {move} one space')
        else:
            print('Your move was illegal. Please try again.')
            self.move()


class Queen(Piece):
    legal_directions = ['forward', 'backward', 'left', 'right']

    def __init__(self, name:str, color:str) -> None:
        super().__init__(name, color)

    def move(self) -> None:
        move = input("What direction would you like to move? ")
        spaces = input("How many spaces would you like to move? ")

        if self.check_legal_move(move, self.legal_directions):
            print(f'The {self.color} {self.name} moves {move} {spaces} spaces')
        else:
            print('Your move was illegal. Please try again.')
            self.move()


black_king = King('King', 'Black')
white_queen = Queen('Queen', 'White')

black_king.move()
# white_queen.move()