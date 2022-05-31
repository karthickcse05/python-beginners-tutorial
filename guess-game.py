secret_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input('your guess? '))
    guess_count += 1
    if(guess == secret_number):
        print('you won')
        break
else:
    print('you have failed to guess !!!')