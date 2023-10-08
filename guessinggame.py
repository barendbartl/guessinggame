import random

cpu_num = random.randint(1,10)
user_num = int(input("Enter a number between 1 and 10: "))
number_guesses = 1

while user_num != cpu_num:
    if user_num > 0 and user_num < 11:
        number_guesses += 1
        user_num = int(input("Enter a number between 1 and 10: "))
    else:
        print("You broke the game!")
        break
else:
    print("You guessed correctly! It only took " + str(number_guesses)
           + " tries!")