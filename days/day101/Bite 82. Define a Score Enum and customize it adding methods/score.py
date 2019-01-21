from enum import Enum

THUMBS_UP = '+'  # in case you go f-string ...

class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f'{self.name} => {THUMBS_UP * self.value}'

    @classmethod
    def average(cls):
        return sum([score.value for score in cls]) / len(cls.__members__)


if __name__ == "__main__":
    for score in Score:
        print(f'{score.name:12} : {score.value}')
    print(list(Score.__members__))
