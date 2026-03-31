import random

def play_guessing_game():
    """A simple number guessing game"""
    
    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    guess = None
    attempts = 0
    max_attempts = 10
    
    # Game title
    print("=" * 40)
    print("  WELCOME TO THE GUESSING GAME!")
    print("=" * 40)
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
    print("=" * 40)
    print()
    
    # Main game loop
    while guess != secret_number and attempts < max_attempts:
        attempts += 1
        
        try:
            # Ask player for their guess
            guess = int(input(f"Attempt {attempts}/{max_attempts} - What's your guess? "))
            
            # Check if guess is in valid range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                attempts -= 1  # Don't count invalid guesses
                continue
            
            # Give feedback
            if guess < secret_number:
                print(f"❌ Too low! Try a higher number.")
            elif guess > secret_number:
                print(f"❌ Too high! Try a lower number.")
            else:
                print(f"✅ You got it! The number was {secret_number}!")
                print(f"You won in {attempts} attempts!")
            
            print()
            
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid guesses
            continue
    
    # Game over messages
    if guess != secret_number:
        print(f"😢 Game Over! You ran out of attempts.")
        print(f"The number was {secret_number}.")
    
    print("=" * 40)

# Run the game
if __name__ == "__main__":
    play_guessing_game()
    
    # Ask if player wants to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            print("\n")
            play_guessing_game()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'.")
