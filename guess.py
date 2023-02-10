secret_number = 9
guess_count = 0
guess_list = 3
while guess_count < guess_list:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break
else:

    print('wrong guess')
