from random import randint
from csv import reader
 
#IMPORT WORD LIST FORM words.csv
word_list = []
with open('words.csv') as file:
    csv_reader = reader(file)
    for word in csv_reader:
        word_list.append(word[0])
 
#FUNCTIONS
def hangman(i):
    picture = (
        '\n    =====\n    |    \n    O    \n   /|\\   \n    |    \n   / \\   \n',
        '\n    =====\n    |    \n    O    \n   /|\\   \n    |    \n   /     \n',
        '\n    =====\n    |    \n    O    \n   /|\\   \n    |    \n         \n',
        '\n    =====\n    |    \n    O    \n   /|    \n    |    \n         \n',
        '\n    =====\n    |    \n    O    \n    |    \n    |    \n         \n',
        '\n    =====\n    |    \n    O    \n         \n         \n         \n',
        '\n    =====\n         \n         \n         \n         \n         \n'
    )
    print(picture[i])
    
def check_answer(available_letter, correct_word):
    for letter in correct_word:
        if letter in available_letter: return False
    return True
 
def input_guess():
    guess = input('input guess letter (lowercase): ')
    while guess not in available_letters or len(guess) > 1:
        guess = input('input another guess letter (lowercase): ')
    return guess

def display_game_status():
    hangman(wrong_chance)
    print( f'chance : {wrong_chance}/6 \n' )
    if not check_answer(available_letters, correct_word) and wrong_chance:
        print( ' '.join( ['_' if letter in available_letters else letter for letter in correct_word] ) )
        print( f"\n{' '.join(available_letters[0:9])}\n{' '.join(available_letters[9:18])}\n{' '.join(available_letters[18:])}\n")
        guess = input_guess()
        return guess
    else: 
        print( f"{' '.join( correct_word)} \n" )
        if not wrong_chance: 
            print( '====== YOU LOSE ======\n' )
        else: 
            print( '====== YOU WIN ======\n' )
        return input('Play again? y/n: ')
 
def update_game_status(wrong_chance):
    if guess not in correct_word: 
        wrong_chance -= 1
    for i in range(0, len(available_letters)):
        if guess == available_letters[i]: 
            available_letters[i] = '_'
    return wrong_chance
   
# APP RUNS HERE
play_again = 'y'
while play_again.lower() == 'y':
    # Initialization
    correct_word = word_list[ randint(0, len(word_list)-1) ]
    available_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    wrong_chance = 6
    # Running Game
    while not check_answer(available_letters, correct_word) and wrong_chance:
        guess = display_game_status()
        wrong_chance = update_game_status(wrong_chance)
    play_again = display_game_status()


    
    
