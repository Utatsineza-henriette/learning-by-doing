secret_number = 9
guess_number = int(input('guess the number: '))
if guess_number < secret_number:
    print('your guess is too low')
elif guess_number > secret_number:
    print('your guess is too high')
else:
    print('you guess is correct')