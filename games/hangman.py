
def play():
    print("*****************************")
    print("***Welcome to the Hangman!***")
    print("*****************************")

    secrect_word = "banana".upper()
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

    print("Game Over")


if(__name__ == "__main__"):
    play()
