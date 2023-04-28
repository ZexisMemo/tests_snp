class Dessert:
    def __init__(self, name = "", calories = 0, flavor = ""):
        self._name = name
        self._calories = calories
        self._flavor = flavor

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_calories(self, calories):
        self._calories = calories

    def get_calories(self):
        return self._calories

    def is_healthy(self):
        if self._calories < 200:
            return True
        return False

    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True

class JellyBean(Dessert):
    
    def set_flavor(self, flavor):
        self._flavor = flavor

    def get_flavor(self):
        return self._flavor


Cake = Dessert("Cake", 500)
Cake2 = Dessert("Cake", 450)
Jelly = JellyBean("Jelly", 150)
