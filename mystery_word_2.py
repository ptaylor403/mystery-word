import random
import re
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def difficulty(level):
    if level == 'E':
        length = range(4, 7)
        easy_word(length)
        print("\nAlright, let's take it easy. Here's the word.\n")
        print("_ "*len(word))
        user_input(word)
    elif level == 'N':
        normal_word(words)
        print("\nNormal. You think you're pretty smart huh? Here's the word.\n")
        print("_ "*len(word))
        user_input(choice)
    elif level == 'H':
        hard_word(words)
        print("\nHard?! You must be a genious! Here's the word.\n")
        print("_ "*len(word))
        user_input(choice)
    elif level == 'Q':
        print("Maybe we can play later.")
        return False
    else:
        print("That wasn't one of your choices. Try again.")
        main()

def easy_word(length):
    words = [line.strip() for line in open('/usr/share/dict/words')]
    easy = []
    for word in words:
        word = word.strip()
        if len(word) == length:
            easy.append(word)
    if len(easy) == 0:
        return 0
    else:
        word = random.choice(easy)
        return word

def normal_word(words):
    normal_words = []
    word = random.choice(words)
    if len(word) >= 6 and len(word) <= 8:
        normal_words.append(word)
    else:
        normal_word(words)
    choice = random.choice(normal_words)
    return choice

def hard_word(words):
    hard_words = []
    word = random.choice(words)
    if len(word) >= 8:
        hard_words.append(word)
    else:
        easy_word(words)
    word = random.choice(hard_words)
    return choice

def user_input(word):
    right = []
    wrong = []
    if len(wrong) < 8:
        guess = input("Guess a letter in my word: ").upper()
        if is_letter(guess, word, right, wrong):
            if guess == '':
                print("\nIf you didn't want to play, you could have just said so.\n")
                return False
            if len(guess) > 1:
                print("\nYou can only guess one letter at a time. Try again.\n")
                user_input(word)
            else:
                letter_in_word(guess, word, right, wrong)
                return True

def is_letter(guess, word, right, wrong):
    try:
        if bool(re.match('[a-zA-Z]+$', guess)):
            return True
        else:
            clear()
            print("\nYou can only guess letters in the aplphabet. Try again.\n")
            user_input(word)
    except ValueError:
        return True

def letter_in_word(guess, word, right, wrong):
    if guess not in right and guess not in wrong:
        if guess in qord:
            clear()
            print("\nYou're right! {} is in my word!\n".format(guess))
            right.append(guess)
        else:
            clear()
            print("\nNope. {} is not in my word\n".format(guess))
            wrong.append(guess)
        word_visual(word, guess, right, wrong)

def word_visual(word, guess, right, wrong):
    display = ("_"*len(word))
    print()
    for i in range(len(word)):
        if word[i] in right:
            display = display[:i] + word[i] + display [i+1:]
    for guess in display:
        print(guess, end=' ')
    is_word_complete(display, right, wrong, word)

def is_word_complete(display, right, wrong, word):
    if "_" not in display:
        print("\nYou won! Way to go!")
        return False
    else:
        print("\n\nYou have {} guesses left.\n".format(8 - len(wrong)))
        user_input(word)

def main():
    clear()
    level = input("\nLet's play a game.\nChoose a difficulty level [E]asy, [N]ormal, [H]ard or [Q]uit to quit: ").upper()
    clear()
    difficulty(level)

if __name__ == '__main__':
    main()
