import random


class Ship:
    icon = '\u25a0'
    count = 0

    def __init__(self, n):
        Ship.count += 1
        self.n = n
        self.coord = self.get_coords_ship()
        self.a = self.coord[0]
        self.b = self.coord[1] if len(self.coord) > 1 else self.a
        self.c = self.coord[2] if len(self.coord) > 2 else self.a

    def coords(self):
        return (self.a, self.b, self.c)

    def get_coords_ship(self):
        return self.get_ship(self.n)[2]

    @staticmethod
    def random_ship_coord(n):
        '''Случайный срез n длины'''
        lst = [1, 2, 3, 4, 5, 6]
        slice_stop = random.randint(n, 5)
        slice_start = slice_stop - n
        slice_object = slice(slice_start, slice_stop)
        result = lst[slice_object]
        return result

    @staticmethod
    def get_random_coord_x_y():
        '''Горизонтально или вертикально'''
        return True if random.randint(1, 2) == 1 else False

    @staticmethod
    def get_random_coord():
        '''Случайная координата [x, y]'''
        coord = [random.randint(1, 6) for _ in range(2)]
        return coord

    @staticmethod
    def get_random_number_row_or_column():
        '''Случайный номер столбца/строки'''
        return random.randint(1, 6)

    @staticmethod
    def get_around_coord(coords):
        '''Получает координаты вокруг корабля'''
        result = []
        for coord in coords:
            result.append([coord[0] - 1, coord[1] - 1])
            result.append([coord[0] - 1, coord[1]])
            result.append([coord[0] - 1, coord[1] + 1])
            result.append([coord[0], coord[1] - 1])
            result.append([coord[0], coord[1]])
            result.append([coord[0], coord[1] + 1])
            result.append([coord[0] + 1, coord[1] - 1])
            result.append([coord[0] + 1, coord[1]])
            result.append([coord[0] + 1, coord[1] + 1])
        return result

    def get_ship(self, n):
        '''Получает координаты корабля'''
        first_coord = self.random_ship_coord(3)
        row_or_column = self.get_random_number_row_or_column()
        if n == 3:
            if self.get_random_coord_x_y():
                ship_coords = [(first_coord[0], row_or_column),
                               (first_coord[1], row_or_column),
                               (first_coord[2], row_or_column)]
            else:
                ship_coords = [(row_or_column, first_coord[0]),
                               (row_or_column, first_coord[1]),
                               (row_or_column, first_coord[2])]
        elif n == 2:
            if self.get_random_coord_x_y():
                ship_coords = [(first_coord[0], row_or_column),
                               (first_coord[1], row_or_column)]
            else:
                ship_coords = [(row_or_column, first_coord[0]),
                               (row_or_column, first_coord[1])]
        elif n == 1:
            ship_coords = [self.get_random_coord()]
        around_coords = self.get_around_coord(ship_coords)
        return first_coord, row_or_column, ship_coords, around_coords
