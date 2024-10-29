class Animal:
    alive = []

    def __init__(self, name, health=100,):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(Animal, animal):
        if isinstance(animal, Herbivore):
            if animal.hidden is False:
                animal.health -= 50
                if animal.health <= 0:
                    if animal in Animal.alive:
                        Animal.alive.remove(animal)
