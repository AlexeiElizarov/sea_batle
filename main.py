from field import Field
from ship import Ship


def create_and_places_ship(field):
    sh_1 = Ship(3, field)
    sh_1.ship()
    sh_2 = Ship(2, field)
    sh_2.ship()
    sh_3 = Ship(2, field)
    sh_3.ship()
    sh_4 = Ship(1, field)
    sh_4.ship()
    sh_5 = Ship(1, field)
    sh_5.ship()
    sh_6 = Ship(1, field)
    sh_6.ship()
    sh_7 = Ship(1, field)
    sh_7.ship()
    return field.build_field()

def main():
    field_our = Field()
    field_opponent = Field()
    print('Ваше поле: ')
    create_and_places_ship(field_our)
    print('Поле противника: ')
    create_and_places_ship(field_opponent)


if __name__ == '__main__':
    main()