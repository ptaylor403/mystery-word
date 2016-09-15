# import random
# import re
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def difficulty(level):
    pass


def main():
    words = [line.strip() for line in open('/usr/share/dict/words')]
    right = []
    wrong = []
    clear()
    level = input("\nLet's play a game.\nChoose a difficulty level [E]asy, [N]ormal, [H]ard or [Q]uit to quit: ").upper()
    difficulty(level)

if __name__ == '__main__':
    main()
