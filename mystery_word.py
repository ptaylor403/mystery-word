import random
import re
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def difficulty(level, words, right, wrong):
    if level == 'E':
        easy_word(words, right, wrong)
    elif level == 'N':
        normal_word(words, right, wrong)
    elif level == 'H':
        hard_word(words, right, wrong)
    elif level == 'Q':
        print("Maybe we can play later.")
        return False
    else:
        print("That wasn't one of your choices. Try again.")
        main()

def easy_word(words, right, wrong):
    word = random.choice(words).upper()
    if len(word) >= 4 and len(word) <= 6:
        print("\nAlright, let's take it easy. Here's the word.\n")
        print("_ "*len(word))
        print("\nCan you guess the word I'm thinking of in 8 guesses?\n")
        user_input(word, right, wrong)
    else:
        easy_word(words, right, wrong)

def normal_word(words, right, wrong):
    word = random.choice(words).upper()
    if len(word) >=6 and len(word) <= 8:
        print("\nNormal. You think you're pretty smart huh? Here's the word.\n")
        print("_ "*len(word))
        print("\nCan you guess the word I'm thinking of in 8 guesses?\n")
        user_input(word, right, wrong)
    else:
        normal_word(words, right, wrong)

def hard_word(words, right, wrong):
    if len(word) >= 8:
        print("\nHard?! You must be a genious! Here's the word.\n")
        print("_ "*len(word))
        print("\nCan you guess the word I'm thinking of in 8 guesses?")
        user_input(word, right, wrong)
    else:
        hard_word(words, right, wrong)

def user_input(word, right, wrong):
    if len(wrong) < 8:
        guess = input("Guess a letter in my word: ").upper()
        if is_letter(guess, word, right, wrong):
            if guess == '':
                print("\nIf you didn't want to play, you could have just said so.\n")
                return False
            if len(guess) > 1:
                print("\nYou can only guess one letter at a time. Try again.\n")
                user_input(word, right, wrong)
            else:
                letter_in_word(guess, word, right, wrong)
                return True
    else:
        print("You ran out of guesses. You lose. The word was {}.".format(word))
        return False
    return guess

def word_visual(word, guess, right, wrong):
    display = ("_"*len(word))
    print()
    for i in range(len(word)):
        if word[i] in right:
            display = display[:i] + word[i] + display [i+1:]
    for guess in display:
        print(guess, end=' ')
    is_word_complete(display, right, wrong, word)

def is_letter(guess, word, right, wrong):
    try:
        if bool(re.match('[a-zA-Z]+$', guess)):
            return True
        else:
            clear()
            print("\nYou can only guess letters in the aplphabet. Try again.\n")
            word_visual(word, guess, right, wrong)
    except ValueError:
        return True

def letter_in_word(guess, word, right, wrong):
    if guess not in right and guess not in wrong:
        if guess in word:
            clear()
            print("\nYou're right! {} is in my word!\n".format(guess))
            right.append(guess)
        else:
            clear()
            print("\nNope. {} is not in my word\n".format(guess))
            wrong.append(guess)
        word_visual(word, guess, right, wrong)

    elif guess in right or guess in wrong:
        clear()
        print("\nYou already guessed that letter. Try again.\n")
        word_visual(word, guess, right, wrong)
    return guess

def is_word_complete(display, right, wrong, word):
    if "_" not in display:
        print("\nYou won! Way to go!")
        return False
    else:
        print("\n\nYou have {} guesses left.\n".format(8 - len(wrong)))
        user_input(word, right, wrong)

def main():
    words = [line.strip() for line in open('/usr/share/dict/words')]
    right = []
    wrong = []
    clear()
    level = input("\nLet's play a game.\nChoose a difficulty level [E]asy, [N]ormal, [H]ard or [Q]uit to quit: ").upper()
    clear()
    difficulty(level, words, right, wrong)

if __name__ == '__main__':
    main()
