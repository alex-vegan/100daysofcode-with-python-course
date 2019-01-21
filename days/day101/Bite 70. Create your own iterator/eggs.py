from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, num):
        self._eggs = []
        for i in range(num):
            self._eggs.append(f'{choice(COLORS)} egg')
        self._index = 0


    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self._eggs[self._index]
            self._index += 1
            return result
        except IndexError:
            raise StopIteration





if __name__ == "__main__":
    for egg in EggCreator(5):
        print(egg)
