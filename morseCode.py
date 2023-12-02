import random
import time

print("---------------------------------------------------")
print("------------ Welcome to the MorseZone! ------------")
print("---------------------------------------------------")


# Define Morse code patterns and their corresponding letters
morse_codes = {".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd', ".": 'e',
               "..-.": 'f', "--.": 'g', "....": 'h',
               "..": 'i', ".---": 'j', "-.-": 'k', ".-..": 'l', "--": 'm',
               "-.": 'n', "---": 'o', ".--.": 'p',
               "--.-": 'q', ".-.": 'r', "...": 's', "-": 't', "..-": 'u',
               "...-": 'v', ".--": 'w', "-..-": 'x',
               "-.--": 'y', "--..": 'z'}


# Handle gamemode choice
def menu():

    choice = input("\n-------------------- Main Menu --------------------"
                   "\nNormal [1] | Timed [2] | Morse codes [M] | Quit [Q]\n").upper()

    print("-------------------------------")

    if choice == "1":
        normal()
    elif choice == "2":
        timed()
    elif choice == "M":
        hint()
    elif choice == "Q":
        print("Okay, see you next time!")

    else:
        print(f"Invalid choice\n")
        menu()

    return" "


# handle rerun
def rerun():

    choice1 = input("\nWould you like to play again Y|N?\n").upper()

    if choice1 == "Y":
        print(menu())
    elif choice1 == "N":
        print("\nOkay! see you next time!")
    else:
        print("That is invalid!")
        rerun()

def hint():
    print(  "A = .-","   J = .--- ","S = ...",
          "\nB = -..."," K = -.-","  T = -",
          "\nC = -.-."," L = .-.."," U = ..-",
          "\nD = -..","  M = --","   V = ...-",
          "\nE = .","    N = -.","   W = .--",
          "\nF = ..-."," O = ---","  X = -..-",
          "\nG = --.","  P = .--."," Y = -.--"
          "\nH = ...."," Q = --.-"," Z = --..",
          "\nL = ..","   R = .-.")

    choice = input("\ntype [B] to go back to the main menu\n").upper()
    if choice == "B":
        menu()
    else:
        print("Sorry user, the only option is 'b'\n")
        hint()


# handle normal game mode with 10 questions
def normal():
    # Initialize the score
    score = 0

    for x in range(10):
        # Randomly select a Morse code pattern
        random_morse = random.choice(list(morse_codes.keys()))

        # Print a message to the user
        print("\nGuess the letter for the following Morse code:")
        print("\t", random_morse)

        # Get user input
        user_input = input(">> ").lower()

        # Check if the user's input matches the correct answer
        correct_answer = morse_codes[random_morse]

        if user_input == correct_answer:
            score += 1
            print("⭐ Nice! You guessed it correctly! ⭐")

        else:
            print(f"Wrong. The correct answer is '{correct_answer}'.")
    print("\n-------------------------------")
    print(f"your score is: {score}")
    print("-------------------------------")

    rerun()

    return " "


# handle timed gamemode with timer
def timed():
    # Initialize Score
    score = 0

    # Setting the time limit
    game_duration = 30

    # Formula
    start_time = time.time()
    end_time = start_time + game_duration

    while time.time() < end_time:
        # Calculates time
        remaining_time = int(end_time - time.time())

        # Randomly select a Morse code pattern
        random_morse = random.choice(list(morse_codes.keys()))

        # Print a message to the user
        print("\nRemaining time: {} seconds".format(remaining_time))
        print("Guess the letter for the following Morse code:")
        print("\t", random_morse)

        # Get user input
        user_input = input(">> ").lower()

        # Check if the user's input matches the correct answer
        correct_answer = morse_codes[random_morse]

        if user_input == correct_answer:
            print("⭐ Nice! You guessed it correctly! ⭐")
            score += 1
        else:
            print(f"Wrong. The correct answer is '{correct_answer}'.")

    # Displaying the score
    print("\n-------------------------------")
    print(f"Time's up! Your total score is {score}.")
    print("-------------------------------")

    rerun()

    return" "


menu()