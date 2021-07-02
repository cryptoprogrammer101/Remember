import os

def error(string):
    input("Invalid input. " + string)

try:
    _ = open("database.txt", "x")
except:
    pass

while True:

    fhand = open("database.txt", "r")

    os.system("clear")

    data = fhand.read()
    fhand.close()

    lst = data.split("\n")

    print("Your reminders:\n")

    if data == "":
        print("No current reminders.")

    else:
        for i, n in enumerate(lst):
            print(str(i + 1) + ". " + n)

    print("\n")

    usr = input("Enter: ")

    if usr == "":
        error("Please enter a command.")
        continue

    if usr.startswith("rm"):

        try:
            num = usr.split("rm ")[1]
        except:
            error("Please enter an index to remove.")
            continue

        try:
            num = float(num) - 1
        except:
            error("Please enter an index to remove.")
            continue

        try:
            test_int = int(num)
        except:
            error("Index must be an integer.")
            continue

        if num != test_int:
            error("Index must be an integer.")
            continue

        num = test_int

        if num >= len(lst):
            error("Index is too high.")
            continue

        if num < 0:
            error("Index is too low.")
            continue

        for i, n in enumerate(lst):
            if i == num:
                lst.remove(n)

        fhand = open("database.txt", "w")

        for i, n in enumerate(lst):
            fhand.write(n)
            if i + 1 < len(lst):
                fhand.write("\n")

        fhand.close()

        continue

    if usr == "q":
        print("\nClosing...\n")
        quit()

    if usr == "clear all":
        usr = input("Are you sure you want to clear all reminders (y/n): ")

        if usr == "y":
            fhand = open("database.txt", "w")
            fhand.write("")
            fhand.close()
            continue

        if usr == "n":
            continue

        error("")
        continue

    fhand = open("database.txt", "a")

    if data != "":
        fhand.write("\n")

    fhand.write(usr)

    fhand.close()
