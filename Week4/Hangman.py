import sys


def welcome():

    print("----- Hangman Game -----")

    print("1. Start Game")

    print("\n2. End")

    option = input("\nEnter option: ")

    print("\n----------------------------------------------------")

    if option == "1":
        gamestart()

    elif option == "2":
        sys.exit()


def gamestart():

    secret = "secret"
    stars = "*"*len(secret)
    guesses = 0
    guesses = int(guesses)

    print("\nWord is ",len(secret)," letters long")

    while guesses < 10 and not stars == secret:

        print("\n"+stars)

        guess = input("\nGuess a letter: ")

        if guess in secret:
            print("\nCorrect!")
            stars = update(secret,stars,guess)
        else:
            print("\nIncorrect")
            guesses += 1

    if stars == secret:
        print("\nCongrats!")
        print("\nWord is :",secret)

    else:
        print("\nLoser")
        print("----------------------------------------------------")


def update(secret, u_stars, u_guess):

    result = ""

    for i in range(len(secret)):
        if secret[i] == u_guess:
            result = result + u_guess
        else:
            result = result + u_stars[i]

    return result


welcome()
