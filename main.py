import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low. ')
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly! ')

def computer_guess(x):
    print('Now Its Computer Turn To Guess')
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h' or feedback == 'H':
            high = guess - 1
        elif feedback == 'l' or feedback == 'L':
            low = guess + 1
        
    print(f'Yay! The computer guessed your number, {guess}, correctly!!')

# give user to input limit guess number
input1 = int(input('Input your limit number to guess: '))
guess(input1)
computer_guess(input1)

#option for replay game again
while True:
    input2 = input('Still wanna play ? (y/n) ')
    if input2 == 'Y' or input2 == 'y':
        input3 = int(input('Input your limit number to guess: '))
        guess(input3)
        computer_guess(input3)
    else:
        quit()
