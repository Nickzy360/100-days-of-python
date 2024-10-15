import random 
def guess_number():
    secret_number = random.randint(1, 1000) 
    attempts = 9 
    print("Welcome to the Guessing Game! You have 9 attempts to guess the secret number.")
    while attempts > 0: 
        try:
            guess = int(input("Enter your guessing number (between 1 and 1000.): ")) 
            if guess < 1 or guess > 1000:
                print("Error: Please enter a number between 1 and 1000.") 
                continue
            if guess < secret_number: 
                print("Higher!")
            elif guess > secret_number:
                print("Lower!")
            else:
                print("Congratulations! You guessed the secret number:", secret_number) 
                break
            attempts -= 1 
            print("Attempts left:", attempts)       
        except ValueError: 
            print("Error: Please enter a valid number.")    
    if attempts == 0:
        print("Game Over! The secret number was:", secret_number) 
guess_number()