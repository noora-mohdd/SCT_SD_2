#number guessing game

import random
 
amount_of_guesses=0
is_running=True
comp_guess=random.randint(1,101) #guesses a random number between 1-100

while is_running: 

    try:

        guess=int(input("guess a number (1-100): "))
        if guess not in range(1,101):
            print("enter a valid number")
            continue
        else:
            amount_of_guesses+=1 

        if guess>comp_guess:
            print("too high! try again")
        elif guess<comp_guess:
            print("too low! try again")
        else:
            print("yes you got it!")
            print("you won!")
            play_again=input("do you want to play again?(y/n): ").lower() 
            if play_again=="n":
                is_running=False #end the game
            else:
                comp_guess = random.randint(1, 100)  # New game
                amount_of_guesses = 0 

    except ValueError:
        print("please enter a valid number, not text.")

print(f"amount of guesses it took = {amount_of_guesses}")
if amount_of_guesses>=10:
    print("so many guesses😕 better luck next time.")
else:
    print("Good Job!")




