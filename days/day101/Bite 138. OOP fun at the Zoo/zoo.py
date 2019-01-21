import itertools

class Animal:
    _index = itertools.count(10001)
    _zoo = []

    def __init__(self, name):
        self.name = name
        self.index = self._index.__next__()
        self._zoo.append(self)

    def __str__(self):
        return f'{self.index}. {self.name.capitalize()}'

    @classmethod
    def zoo(self):
        return '\n'.join([str(animal) for animal in self._zoo])



if __name__ == "__main__":
    dog = Animal('dog')
    cat = Animal('cat')
    fish = Animal('fish')
    lion = Animal('lion')
    mouse = Animal('mouse')
    horse = Animal('horse')
    print(Animal.zoo())
