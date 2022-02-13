import os

from ship import Ship

class Field:
    correct_coord = {'0': 0, '1': 2, '2': 4, '3': 6, '4': 8, '5': 10, '6': 12, '7': 14}
    icon_ship = '\u25a0'
    count_hit = 0

    def __init__(self, list_deck_ship):
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
        self.list_deck_ship = list_deck_ship
        self.shot_list = []
        self.place = None
        self.sum_deck = 0

    def build_field(self):
        for i in self._field:
            print(*i, sep=' ')

    def checks_coords(self, coords):  # [[x, y], [a, b]...]
        '''Проверяет свободные ли клетки вокруг точки'''
        result = []
        for coord in coords:
            result.append(True) if self._field[coord[0]][self.correct_coord[str(coord[1])]] != self.icon_ship else result.append(False)
        if all(result):
            return True
        return False

    def create_ship(self):
        for deck in self.list_deck_ship:
            count = 0
            while True:
                count += 1
                if count < 1000:
                    ship = Ship(deck)
                    # print(ship.coords())
                    if self.checks_coords(ship.get_around_coord(ship.coords())):
                        self.places_ship(ship.coords())
                        break
                else:
                    # print('Неполучается расставить корабли. Попробуй еще раз')
                    self.place = False
                    break

    def places_ship(self, coords):
        for coord in coords:
            if coord:
                self._field[coord[0]][self.correct_coord[str(coord[1])]] = self.icon_ship
                self.sum_deck += 1


    def check_shot(self, shot):
        if self._field[shot[0]][self.correct_coord[str(shot[1])]] == self.icon_ship:
            os.system('cls')
            self.count_hit += 1
            self._field[shot[0]][self.correct_coord[str(shot[1])]] = 'X'
            self.shot_list.append(shot)
            print()
            print('Попал!')
            print()
            return True
        elif self._field[shot[0]][self.correct_coord[str(shot[1])]] == 'o':
            os.system('cls')
            self._field[shot[0]][self.correct_coord[str(shot[1])]] = 'T'
            self.shot_list.append(shot)
            print()
            print('Мимо!')
            print()
            return True
        else:
            os.system('cls')
            print()
            print('Уже стреляли сюда')
            print()
            return False




