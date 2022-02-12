
class Field:
    correct_coord = {'0': 0, '1': 2, '2': 4, '3': 6, '4': 8, '5': 10, '6': 12, '7': 14}
    icon_ship = '\u25a0'

    def __init__(self):
        self._field = [
        [' ', '|', '1', '|', '2', '|', '3', '|', '4', '|', '5', '|', '6', '|', ' '],
        ['1', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', ' '],
        ['2', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', ' '],
        ['3', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', ' '],
        ['4', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', ' '],
        ['5', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', ' '],
        ['6', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', 'o', '|', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]


    def build_field(self):
        for i in self._field:
            print(*i, sep=' ')

    def checks_coords(self, coords):  # [[x, y], [a, b]...]
        '''Проверяет свободные ли клетки вокруг точки'''
        result = []
        for coord in coords:
            result.append(True) if self.field[coord[0]][self.correct_coord[str(coord[1])]] != self.icon_ship else result.append(False)
        if all(result):
            return True
        return False

    def places_ship(self, coords):
        for coord in coords:
            self._field[coord[0]][self.correct_coord[str(coord[1])]] = self.icon_ship

    @property
    def field(self):
        return self._field

    # @field.setter
    # def field(self, positions):
    #     if Field._checkPosition(self, positions):
    #         for position in positions:
    #             self._field[position[0]][self.correct_coord[str(position[1])]] = self.icon_ship
    #     else:
    #         print('hren')


    # def _checkPosition(self, positions):
    #     result = []
    #     for position in positions:
    #         if self._field[position[0]][self.correct_coord[str(position[1])]] != self.icon_ship:
    #             result.append(True)
    #         else:
    #             result.append(False)
    #     return True if all(result) else False


    def __getPosition(self):
        return