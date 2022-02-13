from field import Field
import random

icon_miss = 'T'
icon_hit = 'X'

def get_random_coord():
    '''Случайная координата [x, y]'''
    coord = [random.randint(1, 6) for _ in range(2)]
    return coord

def see_fields(field_our, field_opponent):
    '''Выводи поля на экран'''
    print('Твои корабли:')
    field_our.build_field()
    print('Корабли противника:')
    field_opponent.build_field()

def check_win(field):
    '''Проверяет колличество подбитых палуб'''
    if field.count_hit > 10:
        print('Конец игры!')
        exit()

def game(field_our, field_opponent):
    '''Игра'''
    while True:
        while True:
            shot_opponent = get_random_coord()
            if shot_opponent in field_our.shot_list:
                continue
            if field_our.check_shot(shot_opponent):
                break
        print(f'Ход противника: {shot_opponent}')
        see_fields(field_our, field_opponent)
        check_win(field_our)
        while True:
            try:
                shot_our = list(map(int, input('Твой ход: ').split()))
                if field_opponent.check_shot(shot_our):
                    break
                see_fields(field_our, field_opponent)
            except:
                print('Введите два числа (1,2,3,4,5 или 6)')



        check_win(field_opponent)

def main():
    '''Создает поле противника и твоё поле со случайным расположением кораблей '''
    print()
    print('Противник ходит первым')
    while True:
        field_our = Field([3, 2, 2, 1, 1, 1, 1])
        field_our.create_ship()
        if field_our.place == False:
            continue
        break
    while True:
        field_opponent = Field([3, 2, 2, 1, 1, 1, 1])
        field_opponent.create_ship()
        if field_opponent.place == False:
            continue
        break
    game(field_our, field_opponent)

if __name__ == '__main__':
    main()