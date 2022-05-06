# we are going to generate a random number and track how many times it takes the user to guess this number
import random
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()
#random_number = random.randrange(-5,11)
# another way to do this is using randint, it runs the same way as randrange except that now 11 will be included which is the upper bound range
random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue #continue brings us back to the top of our loop
    if user_guess == random_number:
        print("You got it!")
        break

    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
