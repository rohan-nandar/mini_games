import random


def startup():
    print("There are several games, which would you like to play?")
    print("(1) Guess the number")
    print("(2) Simple addition")
    print("(3) Times Tables")
    print("(4) Tic-Tac-Toe")
    game_num = int(input("Which game would you like to play? "))
    if game_num == 1:
        print("Okay, you picked guess the number!")
        guess_num()


def guess_num():
    largest = int(input("What is the largest number you want to include?: "))
    print("You get 10 guesses, here we go!")
    answer = random.randint(1, largest)
    guesses = 10
    while guesses > 0:
        print("You have " + str(guesses) + " guesses left")
        guesses -= 1
        x = int(input("Guess the number between 1 and " + str(largest) + ": "))
        if x == answer:
            print("You guessed the number!")
            play_again = input("Press x to play again or y to go back to startup: ")
            if play_again == "x":
                guess_num()
            elif play_again == "y":
                startup()
            break

    print("You ran out of guesses!")
    play_again = input("Press x to play again or y to go back to startup: ")
    if play_again == "x":
        guess_num()
    elif play_again == "y":
        startup()


startup()
