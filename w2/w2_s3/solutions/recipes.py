class Recipe:
    def __init__(self, name:str, *args) -> None:
        self.name = name
        self.ingredients = []

        for arg in args:
            self.ingredients.append(arg)

    def make_shopping_list(self):
        shopping_list = f'The recipe for {self.name} calls for:\n'

        for ingredient in self.ingredients:
            shopping_list += f'{ingredient.name}\n'