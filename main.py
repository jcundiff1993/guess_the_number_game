from ascii_art import logo
import random

def guessing_start ():
    """Starts the Guess Game"""

    #Default values for the game
    game_over = False

    #Gameplay start
    while not game_over:
        # Default values for the game
        lives = 0
        rando_number = 0

        #Starting values for Difficulty
        print(logo)
        print("Welcome to the number guessing game!")
        difficulty = input("Choose a difficulty. \nEasy = 10 attempts Hard = 5 Attempts \n")
        difficulty = difficulty.title()
        print(difficulty)

        if difficulty == "Easy":
            lives = 10
        elif difficulty == "Hard":
            lives = 5

        rando_number = random.randint(1 , 100)
        print(f"I'm thinking of a number 1 through 100. Can you guess it in {lives} tries?")
        print(rando_number) #****Uncomment for troubleshooting****
        while lives > 0:
            is_winner = False
            guess = 0
            guess = int(input(f"You have {lives} guesses, so pick a number.\n"))

            if guess > rando_number:
                print(f"{guess} is too high, try again.")
                lives = lives - 1
            elif guess < rando_number:
                print(f"{guess} is too low, try again.")
                lives = lives - 1
            elif guess == rando_number:
                # print(f"You guess {rando_number} correctly!!!! You Win!!!")
                is_winner = True
                lives = 0

        if is_winner:
            print(f"You guess {rando_number} correctly!!!! You Win!!!")
        elif not is_winner:
            print(f"The correct number was {rando_number}. Want to play again?")

        new_round = input("Want to play again? Yes or No\n")
        new_round = new_round.title()

        if new_round == "No":
            break

guessing_start()

print("Game Over! Come back soon!!!")