import random

def is_int(num):
    try:
        return 0 < int(num) < 101
    except ValueError:
        print("Try again!")
        return False

def is_choice(num):
    try:
        return 1 <= int(num) <= 3
    except ValueError:
        print("Try again!")
        return False

def game_mode(difficulty, attempts, random_number):
    print(f"""
    Great! You have selected the {difficulty} difficulty level.
    Let's start the game!
    """)
    cnt = 0
    while True:
        guess = input("Enter your guess: ")
        if is_int(guess):
            guess = int(guess)
            cnt += 1
            if random_number == guess:
                print(f"Congratulations! You guessed the correct number in {cnt} attempts.")
                break
            elif random_number < guess:
                print(f"Incorrect! The number is less than {guess}. You have {attempts - cnt} attempts left")
            elif random_number > guess:
                print(f"Incorrect! The number is greater than {guess}. You have {attempts - cnt} attempts left")
        if cnt == attempts:
            print(f"""
                        Unfortunately, you did not guess the number
                        The answer is: {random_number}
                        """)
            break


while True:
    print("""
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """)

    numbers = [x for x in range(1, 101)]
    random_number = random.choice(numbers)

    choice = input("Enter your choice: ")

    if is_choice(choice):
        choice = int(choice)

        if choice == 1:
            game_mode("Eazy", 10, random_number)

        elif choice == 2:
            game_mode("Medium", 5, random_number)

        elif choice == 3:
            game_mode("Hard", 3, random_number)