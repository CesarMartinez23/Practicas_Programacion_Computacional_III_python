

def validationDui():
    numbers = []
    message = "DUI Valido"

    while True:
        numbers.clear()
        duiUser = input("Please enter your DUI number unscripted: ")

        for i in duiUser:
            numbers.append(i)

        if(len(duiUser) != 9):
            print("The DUI number must be only 9 numbers.\n")

        elif(" " in numbers):
            print("Invalid DUI.\n")
            print("It must not have spaces.\n")
            continue

        elif("-" in numbers):
            print("Invalid DUI.\n")
            print("It must not have a script.\n")
            continue
        else:
            break

    return print(message)
