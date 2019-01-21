class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        length = int(length)
        self._table = {}
        for x in range(1,length+1):
            for y in range(1,length+1):
                self._table.update({(x,y):x*y})
        #print(self._table)

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table)

    def __str__(self):
        """Returns a string representation of the table"""
        _table_str = ''
        x_y = int(len(self._table) ** 0.5)
        for x in range(1, x_y+1):
            _table_list = []
            for y in range(1, x_y+1):
                _table_list.append(str(self._table[(x,y)]))
            _table_str += ' | '.join(_table_list) + '\n'
        return _table_str.strip()


    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        try:
            return self._table[(x,y)]
        except KeyError:
            raise IndexError


if __name__ == "__main__":
    print("-===========================8<")
    x_y = input("input x/y size please: ")
    mult_table = MultiplicationTable(x_y)
    print('-'*30)
    print(mult_table.__len__())
    print('-'*30)
    print(mult_table.__str__())
    print('-'*30)
    x = int(input('input X of table: '))
    y = int(input('input Y of table: '))
    print(mult_table.calc_cell(x,y))
