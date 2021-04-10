import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    human_guesses = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        human_guesses += 1
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
    return human_guesses

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    computer_guesses = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        computer_guesses += 1
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
    return computer_guesses

human_guesses = guess(100)
computer_guesses = computer_guess(100)

if (human_guesses < computer_guesses):
    print("Human beats the machine!")
elif (computer_guesses < human_guesses):
    print("The computer takes the round!")
else:
    print("Folks, looks like we have a tie!")
