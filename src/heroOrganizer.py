import HEROES as h


def get_location(hero):
    position = h.STRENGTH.index(hero)
    column = position % 11
    row = position // 11
    print(str(column) + " " + str(row))


