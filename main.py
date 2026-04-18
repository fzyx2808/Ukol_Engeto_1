import random
import time
from typing import Tuple

DIGITS = 4
LINES = "-" *40

def print_intro() -> None:
    print(LINES)
    print("Hi there! Welcome to the game.")
    print(f"I have generated a random {DIGITS} digit number for you.")
    print("Let's see if you can guess it!")
    print(LINES)
    print("Enter a number.")
    print(LINES)

def generate_secret_amazing_number() -> str:
    numbers = list("0123456789")

    start = 1
    stop = len(numbers)
    step = 1
    Subset = numbers[start:stop:step]

    first_number = random.choice(Subset)
    numbers.remove(first_number)

    secret_number = first_number
    for _ in range(DIGITS - 1):
        next_number = random.choice(numbers)
        secret_number = secret_number + next_number
        numbers.remove(next_number)
    return secret_number

def validate_input(user_input: str) -> str:

    if len(user_input) != DIGITS:
        return f"Number must have exactly {DIGITS} digits. Try again."
    
    if not user_input.isdigit():
        return "Input must be a number. Try again."
    
    if user_input[0] == "0":
        return "Number cannot start with 0. Try again."
    
    if len(set(user_input)) != DIGITS:            # Používám set, protože nemůže obsahovat duplicitní čísla, ale musí být přesně 4 čísla, proto porovnávám délku setu s DIGITS.
        return "All digits must be unique. Try again."
    
    return "valid"

def count_bulls_and_cows(secret: str, user_input: str) -> Tuple[int, int]:
    bulls = 0
    cows = 0

    for i in range(DIGITS):
        if user_input[i] == secret[i]:
            bulls +=1
        elif user_input[i] in secret:
            cows +=1
    
    return bulls, cows

def get_bull_word(count: int) -> str:
    if count == 1:
        return "bull"
    else:
        return "bulls"
def get_cow_word(count: int) -> str:
    if count == 1:
        return "cow"
    else:
        return "cows"
    

def play_one_game() -> None:
    secret_number = generate_secret_amazing_number()
    attempts = 0
    print(f"DEBUG: tajné číslo je {secret_number}") #Kvůli testování, aby bylo vidět, jestli se počítají správně bulls a cows. Můžeš to zakomentovat nebo odstranit, až budeš mít jistotu, že hra funguje správně.
    start_time = time.time()

    print_intro()

    while True:
            user_input = input("Your guess:")
            validation_result = validate_input(user_input)
    
            if validation_result != "valid":
                print(validation_result)
                continue
            
            attempts += 1
            bulls, cows = count_bulls_and_cows(secret_number, user_input)

            if bulls == DIGITS:
                end_time = time.time()
                game_time = end_time - start_time
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts and {game_time:.2f} seconds.")
                print("Thats amazing!")
                break

            print(f"{bulls} {get_bull_word(bulls)}, {cows} {get_cow_word(cows)}")
            print(LINES)


def ask_to_play_again() -> bool:
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main() -> None:
    while True:
        play_one_game()
        if not ask_to_play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()


