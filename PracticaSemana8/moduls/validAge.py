
def validationAge():

    YEAR = 2022
    message = ""
    while True:

        yearOfBirth = int(input("Please enter your year of birth: "))

        if(len(str(yearOfBirth)) < 4 or len(str(yearOfBirth)) > 4):
            print("Please enter a valid year\n")
            print("Invalid Date.\n")
            continue
        elif(yearOfBirth >= YEAR):
            print("Please enter a valid year\n")
            print("Invalid Date.\n")
            continue
        else:
            age = YEAR - yearOfBirth
            break

    if(age >= 18):
        message = "You're of age."
    else:
        message = "You're underage."

    return print(message)
