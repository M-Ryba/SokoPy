import csv


# ładowanie poziomu z pliku do listy zagnieżdżonej
# 0 = gracz, 1 = ściana, 2 = skrzynka, 3 = cel
def load(level_number):
    level = []
    with open(f"assets/levels/level{level_number}.csv", "r") as file:
        for row in csv.reader(file, delimiter=","):
            level.append([int(e) for e in row])
    return level
