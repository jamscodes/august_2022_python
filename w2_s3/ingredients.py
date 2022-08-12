# Make a class (or classes) that will allow a user to create ingredients objects
# The ingredients will need a name, a calorie amount, and a measurement (measurement should
# be calculated in metric). There should also be a helper method that will simplify
# an ingredient's measurement on demand (e.g. simplify_measurement(1500) -> 1.5 (this would
# simplify 1500 grams/milliliters to 1.5 kilograms/liters))

from ast import In


class Ingredient:
    def __init__(self, name, calories, measurement, measurement_type):
        self.name = name
        self.calories = calories
        self.measurement = measurement
        self.measurement_type = measurement_type

    def __repr__(self):
        return f'Ingredient: {self.name}'

    @staticmethod
    def simplify_measurement(measure):
        return measure / 1000



class IngredientImperial(Ingredient):
    def __init__(self, name, calories, measurement, measurement_type):
        super().__init__(name, calories, measurement, measurement_type)

    # @staticmethod
    # def simplify_measurement(measure, measurement_type):
    #     if measurement_type == 'Ounce':
    #         return measure / 16
    #     else:
    #         return 'this is ridiculous, use metric!'


coffee = IngredientImperial('Whole coffee beans', 10, 4, 'Ounce')
wheat_flour = Ingredient('Whole wheat flour', 100, 1500, 'grams')


# print(coffee.simplify_measurement(coffee.measurement, coffee.measurement_type))
# print(IngredientImperial.simplify_measurement(coffee.measurement))
print(IngredientImperial.simplify_measurement(coffee.measurement, coffee.measurement_type))