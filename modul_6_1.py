class Animal:
    def __init__(self, name, alive, fed):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food, edible):
        self.food = food
        if edible == True:
            print (f'{self.name} съел {food.name}')
            self.fed = True
            self.alive = True
        else:
            print (f'{self.name} не стал есть {food.name}')
            self.alive = False
            self.fed = False


class Plant:
    def __init__(self, name, edible):
        self.name = name
        self.edible = False


class Mammal (Animal):
    pass


class Predator (Animal):
    pass


class Flower (Plant):
    edible = False


class Fruit (Plant):
    edible = True


a1 = Predator ('Волк с Уолл-Стрит', True, False)
a2 = Mammal ('Хатико', True, False)
p1 = Flower ('Цветик семицветик', False)
p2 = Fruit ('Заводной апельсин', True)
print (a1.name)
print (p1.name)
print (a1.alive)
print (a2.fed)
a1.eat (p1, False)
a2.eat (p2, True)
print (a1.alive)
print (a2.fed)
