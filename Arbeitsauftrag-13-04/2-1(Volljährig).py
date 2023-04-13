"""

Überprüfung der Volljährigkeit (Aufgabe 2.1)

"""

# try to ask for input. If the user doesn't enter a int it exits
try:
    if int(input("How old are you")) > 17:
        print("You are older than 18.")
    else:
        print("You are younger than 18.")
except ValueError:
    print("Please enter a number")
