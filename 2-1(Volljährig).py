try:
    if int(input("Wie alt bist du?")) > 17:
        print("Du bist älter als 18.")
    else:
        print("Du bist jünger als 18")
except ValueError:
    print("Please enter a number")
