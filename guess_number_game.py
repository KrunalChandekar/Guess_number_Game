import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = input("Enter your guess (or 'exit' to end the game): ")
        
        # Check if the user wants to exit the game
        if guess.lower() == 'exit':
            print("Exiting the game. The number was:", secret_number)
            break
        
        # Check if the input is a valid integer
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # Compare the user's guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break

if __name__ == "__main__":
    guess_number()
