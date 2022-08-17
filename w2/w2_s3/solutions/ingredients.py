class Ingredient:
    def __init__(self, name:str, calories:int, amount:int) -> None:
        self.name = name
        self.calories = calories
        self.amount = amount

    @staticmethod
    def simplify_measurement(measure) -> None:
        pass


class IngredientWeight(Ingredient):
    def __init__(self, name:str, calories:int, grams:int) -> None:
        super().__init__(name = name, calories = calories)
        self.grams = grams


class IngredientLiquidVolume(Ingredient):
    def __init__(self, name:str, calories:int, mils:int) -> None:
        super().__init__(name = name, calories = calories)
        self.mils = mils




# def simplify_measurement(measure:int) -> int:
#     return measure / 1000


# class Ingredient:
#     def __init__(self, name:str, calories:int) -> None:
#         self.name = name
#         self.calories = calories



# class IngredientWeight:
#     def __init__(self, name:str, calories:int, ounces:int) -> None:
#         self.name = name
#         self.calories = calories
#         self.ounces = ounces


# class IngredientLiquidVolume:
#     def __init__(self, name:str, calories:int, cups:int) -> None:
#         self.name = name
#         self.calories = calories
#         self.cups = cups