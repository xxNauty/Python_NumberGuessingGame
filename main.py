from numpy import random

CHANCES = {
    "easy": 10,
    "medium": 6,
    "hard": 4
}
SIZE = {
    "easy": 100,
    "medium": 200,
    "hard": 500
}

level = input("Enter your level: ")

randomNumber = random.randint(0, SIZE[level.lower()])

attempts = 0
for i in range(CHANCES[level.lower()]):
    guess = input("Enter your guess: ")
    attempts += 1
    if int(guess) == randomNumber:
        print("You guessed it right!\nIt took you", attempts, "attempts")
        exit()
    else:
        if int(guess) < randomNumber:
            print("Your guess is too low.")
        elif int(guess) > randomNumber:
            print("Your guess is too high.")

print("Too many guesses, correct number was:", randomNumber)