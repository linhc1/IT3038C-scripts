import random

GuessNumber = 0

print('Hi! What your name?')
myName = input()

number = random.randint(1,100)
print('Now game start, guess number 1-100')

while GuessNumber < 100:
    print('Take a guess')
    guess = input()
    guess = int(guess)
    GuessNumber = GuessNumber + 1

    if guess < number:
        print('Your guess too low!')
    if guess > number:
        print('Your guess too high!')
    if guess == number:
        break

if guess == number:
    GuessNumber = str(GuessNumber)
    print('God job ' + myName + ', the number of you guessed is ' + GuessNumber + '.')

