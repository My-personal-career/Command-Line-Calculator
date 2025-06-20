# NUMBER GUESSING GAME
import random

def print_intro():
    print("=" * 50)
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("=" * 50)
    print("The system has picked a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.\n")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def play_game():
    target_num = random.randint(1, 100)
    total_guesses = 0

    print_intro()

    while True:
        guess = get_user_guess()
        total_guesses += 1

        if guess < target_num:
            print("🔻 Too low! Try again.\n")
        elif guess > target_num:
            print("🔺 Too high! Try again.\n")
        else:
            print(f"\n✅ Congratulations! You guessed the number {target_num} correctly.")
            print(f"🎉 Total guesses: {total_guesses}")
            break

def main():
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
