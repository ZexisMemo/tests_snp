class Dessert:
    def __init__(self, name = "", calories = "", flavor = ""):
        self.name = name
        self.calories = calories
        self.flavor = flavor

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_calories(self, calories):
        self.calories = calories

    def get_calories(self):
        return self.calories

    def is_healthy(self):
        if type(self.calories) == int or type(self.calories) == float:
            if self.calories < 200:
                return True
        return False

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        return True

class JellyBean(Dessert):
    
    def set_flavor(self, flavor):
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor

