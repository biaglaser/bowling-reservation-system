'''-------------- NOT USED IN THE MAIN FUNCTION --------------'''

class Extras:
    """extra purchases"""

    # dictionary of snacks in euros
    foods = {'LARGE POPCORN': 5.50, 'SMALL POPCORN': 3.0, 'CHOCOLATE': 2.5, 'CANDY': 2.0}
    # dictionary of beverages in euros
    drinks = {'LARGE SODA': 4.5, 'SMALL SODA': 3.0, 'WATER': 2.5, 'SMOOTHIE': 4.0}


    def __init__(self):
        self.snacks = []
        self.beverages = []
        self.price = 0

    def get_snacks(self):
        return self.snacks

    def get_beverages(self):
        return self.beverages

    def get_price(self):
        return self.price

    def add_snack(self, food):
        if food in Extras.foods.keys():
            self.snacks.append(food)
            self.price += Extras.foods[food]
        else:
            print("Snack does not exist")

    def add_beverages(self, drink):
        if drink in Extras.drinks.keys():
            self.beverages.append(drink)
            self.price += Extras.drinks[drink]
        else:
            print("Beverage does not exist")