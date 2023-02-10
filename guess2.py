x = 10
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == x:
        print('you guess correct')
        break

else:
    print('Sorry wrong guess')
