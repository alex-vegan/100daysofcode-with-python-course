from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        for value in self.values():
            #if birthday.month == value.month and birthday.day == value.day:
            if birthday.strftime('%d/%m') == value.strftime('%d/%m'):
                print(MSG.format(name))
                break
        #self.update({name:birthday})
        super().__setitem__(name, birthday)


if __name__ == "__main__":
    bd = BirthdayDict()
    bd['bob'] = date(1987, 6, 15)
    bd['tim'] = date(1984, 7, 15)
    bd['mary'] = date(1987, 6, 15)
    bd['sara'] = date(1987, 6, 14)
    bd['mike'] = date(1981, 7, 15)
