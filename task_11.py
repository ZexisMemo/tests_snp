class Dessert:
    def __init__(self, name = "", calories = 0):
        self._name = name
        self._calories = calories

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
        return True




Cake = Dessert("Cake", 500)
Cake2 = Dessert("Cake", 450)
Jelly = Dessert("Jelly", 150)
