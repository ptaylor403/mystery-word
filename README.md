# Mystery Word
## Goal of the code
Mystery word is a form of a hangman game run in command line, where the player chooses the difficulty level and is given 8 guesses to guess the word. The difficulty level corresponds to the length, not the simplicity or complexity, of the word.
- Easy is 4-6 letters
- Medium is 6-8 letters or less
- Hard is more that 8 letters

The words are chosen randomly from the /usr/share/dict/words file. The player is only allowed to guess one letter at a time, upper or lower case. No special characters, numbers, multiple letters or blank submissions are accepted as guesses. The player is prompted to guess again without a penalty in this case. 

If the player guesses a letter that is not in the word, they are penalized a guess. If the player guesses correctly, the letter is displayed in the proper location for the word and they are not penalized a guess. The number of remaining guesses is displayed below the word throughout the game.
