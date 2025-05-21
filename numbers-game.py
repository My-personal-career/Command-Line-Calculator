# NUMBER GUESSING GAME
import random

target_num  = random.randint(1, 100)
total_guess = 0
user_input = None

# Random number between 0 to 100

print("Welcome to the number guessing game, the system pick a number from 1 to 100 and you have to guess what number that is.\n")
print("System's number: #")
while user_input != target_num:
    user_input = int(input("Guess the number: "))
    total_guess += 1


    # condition
    if user_input < target_num:
        print("Your number is lesser, try again!")

    elif user_input > target_num:
        print("Your number is higher, try again!")
    else:
        print("\nCongrate, you guess right")
        print(f"Total guess: {total_guess}")
        print(f"System's number: {target_num}")
