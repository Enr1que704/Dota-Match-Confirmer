import HEROES as h


def get_location(hero):
    attribute = get_main_attr(hero)

    match attribute:
        case "STRENGTH":
            position = h.STRENGTH.index(hero)
        case "AGILITY":
            position = h.AGILITY.index(hero)
        case "INTELLIGENCE":
            position = h.INTELLIGENCE.index(hero)
        case "UNIVERSAL":
            position = h.UNIVERSAL.index(hero)
        case _:
            position = -1

    column = position % 11
    row = position // 11
    print(str(column) + " " + str(row))


def get_main_attr(hero):
    if hero in h.STRENGTH:
        return "STRENGTH"
    elif hero in h.AGILITY:
        return "AGILITY"
    elif hero in h.INTELLIGENCE:
        return "INTELLIGENCE"
    elif hero in h.UNIVERSAL:
        return "UNIVERSAL"
    else:
        return "Not found"