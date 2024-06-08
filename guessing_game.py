# Guessing Game

guess_num = 5

user_guess = None

# while user_guess != guess_num:
#     user_guess = int(input("What's your guess (betweeen 1 and 10)? "))

# print("Correct!")

# Make it better
# Give guesses 

while user_guess != guess_num:
    user_guess = int(input("What's your guess (betweeen 1 and 10)? "))

    if user_guess < guess_num:
        print("Too low!")
    if user_guess > guess_num:
        print("Too high!")
    else:
        print("Correct!")
    