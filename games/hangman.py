import random


def play():
    print("*****************************")
    print("***Welcome to the Hangman!***")
    print("*****************************")

    words = []
    with open("words.txt", "r") as archive:
        for line in archive:
            line = line.strip()
            words.append(line)

    number = random.randrange(0, len(words))
    secrect_word = words[number].upper()

    letter_board = ["_" for letter in secrect_word]

    hanged = False
    hit = False
    mistakes = 0

    print(letter_board)
    
    while(not hanged and not hit):

        guess = input("Which letter?")
        guess = guess.strip().upper()

        if(guess in secrect_word):
            index = 0
            for letter in secrect_word:
                if(guess == letter):
                    letter_board[index] = letter
                index += 1
        else:
            mistakes += 1

        hanged = mistakes == 6
        hit = "_" not in letter_board
        print(letter_board)

        if(hit):
            print("You win!")
        elif(hanged):
            print("You lose!")

    print("End Game")


if(__name__ == "__main__"):
    play()
