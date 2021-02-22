"""
File: hangman.py
-------------------------------
This file demonstrates a Python Console hangman game.
At the beginning of the game, users are asked to input
one letter at a time to guess out a dashed vocabulary (answer).
If the letter is in the answer, the Console updates the
dashed word to its current status. 7 wrong guesses end the game.
"""

import random

# Constant
N_TURNS = 7


def main():
    """
    TODO:
    """
    lives = N_TURNS

    answer = random_word()

    dashed = ""

    # answer.index('h')
    # answer[0]
    # answer[0:2] => ha
    # answer[0:2] + 'ts' => hats

    for char in answer:
        dashed += "_"

    while lives > 0:

        print("the word looks like:" + dashed)
        print("You have " + str(lives) + " guesses left.")

        input_ch = input()

        print("Your guess:" + input_ch)

        # if input_ch == answer.indexOf(input_ch)


        if input_ch in answer:

            pos = answer.index(input_ch)
            if pos >= 0:
                dashed[0:pos] + answer[pos] + dashed[pos:]
                print("the word looks like:" + dashed[0:pos] + answer[pos] + dashed[pos + 1:])
                dashed = dashed[0:pos] + answer[pos] + dashed[pos + 1:]
            else:
                print("there is no " + input_ch + "'s in the word.")
                x -= 1
        else:

            lives -= 1





def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
