
def play():
    print("*****************************")
    print("***Welcome to the Hangman!***")
    print("*****************************")

    secrect_word = "banana"
    letter_board = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    hit = False

    print(letter_board)
    
    while((not hanged) and (not hit)):

        guess = input("Which letter?")
        guess = guess.strip()

        index = 0
        for letter in secrect_word:
            if(guess.upper() == letter.upper()):
                letter_board[index] = letter
            index = index + 1
        print(letter_board)

    print("Game Over")


if(__name__ == "__main__"):
    play()
