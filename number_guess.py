import random
from colorama import Fore, Style, init

init(autoreset=True)

def set_difficulty():
    print(Fore.CYAN + Style.BRIGHT + "\n=== Difficulty Levels ===")
    print(Fore.GREEN + "1. Easy   (15 attempts | Max Score: 150)")
    print(Fore.YELLOW + "2. Medium (10 attempts | Max Score: 100)")
    print(Fore.RED + "3. Hard   (5 attempts  | Max Score: 50)")

    choice = input(Fore.WHITE + "\nChoose difficulty ( 1 - 3 ): ").strip()
    difficulties = {
        "1": (15, 150),
        "2": (10, 100),
        "3": (5, 50)
    }
    return difficulties.get(choice, (10, 100))

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts, starting_score = set_difficulty()
    attempts = 0
    print(Fore.YELLOW + f"\nGuess the number (1 - 100). Attempts: {max_attempts}, Max score: {starting_score}")

    while attempts < max_attempts:
        try:
            guess = int(input(Fore.WHITE + "\nEnter your guess: "))
            attempts += 1
            current_score = max(0, starting_score - (attempts * 10))

            if guess < secret_number:
                print(Fore.BLUE + "Too low! ↡")
            elif guess > secret_number:
                print(Fore.RED + "Too high! ↟")
            else:
                print(Fore.GREEN + Style.BRIGHT + f"★ Correct! Score: {current_score} ({attempts}/{max_attempts} attempts) ★")
                return
            print(Fore.MAGENTA + 
                  f"Attempts left: {max_attempts - attempts} | Current score: {current_score}")
        except ValueError:
            print(Fore.RED + "✗ Please enter a valid number!")
    
    print(Fore.RED + Style.BRIGHT + f"\nGame Over! The number was {secret_number}. Final score: 0")

if __name__ == "__main__":
    play_game()