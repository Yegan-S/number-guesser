import random

rand_num = random.randint(1, 100)



while True:
    user_guess = input("guess a number between 1 and 100")
    if user_guess == "q":
        print("Thank you, Goodbye")
        break
    elif not user_guess.isdigit():
        print("Invalid input, please try again.")
        continue
    
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print("You're out of range, enter a digit between 1 and 100")
        continue

    if rand_num > user_guess:
        print("Your guess is too low.Please try again.")
    elif rand_num < user_guess:
        print("Your guess is too high.Please try again.")
    else:
        print("Congratulations! You guessed the correct number.") 
        break       


