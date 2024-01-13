import csv


# ładowanie poziomu z pliku do listy zagnieżdżonej
# 0 = gracz, 1 = ściana, 2 = skrzynka, 3 = cel
def load_level(level_number):
    level = []
    with open(f"assets/levels/level{level_number}.csv", "r") as file:
        for row in csv.reader(file, delimiter=","):
            level.append([int(e) for e in row])
    return level


# znajdowanie pozycji startowej gracza na podanym poziomie
def get_starting_position(level):
    for i in range(0, len(level)-1):
        if 0 in level[i]:
            return level[i].index(0), i  # zwraca koordynaty x i y w krotce pozycji startowej gracza
    return -1  # nie znaleziono pozycji startowej gracza na mapie
