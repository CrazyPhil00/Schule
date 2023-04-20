def calculate_(note):
    if note == 4:
        return "mangelhaft"
    elif note == 5:
        return "ungenügend"
    elif note == 6:
        return "ausreichend"
    elif note == 7:
        return "befriedigend"
    elif note == 8:
        return "gut"
    elif note == 9:
        return "sehr gut"
    elif note == 10:
        return "hervorragend"
    else:
        return "Ungültige Eingabe"


print(calculate_(int(input("Gib die umzurechende note ein:"))))
