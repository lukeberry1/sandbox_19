MENU = """C - Convert Celcius to Fahranheit
F - Convert Fahranheit to Celcius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "F":
            fahranheit_to_celcius()
        elif choice == "C":
            celcius_to_fahranheit()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def celcius_to_fahranheit():
    celcius = float(input("Celcius: "))
    fahranheit = celcius * 9 / 5 + 32
    print("Result {:.2f}F".format(fahranheit))


def fahranheit_to_celcius():
    fahranheit = float(input("Fahranheit: "))
    celcius = 5 / 9 * (fahranheit - 32)
    print("Result {:.2f}C.".format(celcius))


main()
