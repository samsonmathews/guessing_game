secret_word="giraffe"
your_guess=''
i=1
while your_guess!=secret_word and i<=3:
    i+=1
    your_guess=input('Guess your word: ')
    if your_guess=='giraffe':
        print('You win!')
if your_guess!=secret_word:
    print('Game over!')
