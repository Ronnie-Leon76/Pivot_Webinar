import random
 
hidden = random.randrange(1, 10)
print(hidden)

guess_count = 0
guess_limit = 3
out_of_count = False

guess = int(input("Please enter your guess: "))
while guess != hidden and not out_of_count:
    if guess_count < guess_limit:
        guess = int(input("Please enter your guess: "))
        guess_count += 1
        if guess == hidden:
            print('Nailed it!')
        elif guess < hidden:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
    else:
        out_of_count = True

if out_of_count:
    print("Out of guesses, You lose")
else:
    print("Completed game successfully")

 

 
