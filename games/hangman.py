
def play():
    print("*****************************")
    print("***Welcome to the Hangman!***")
    print("*****************************")

    secrect_word = "banana"

    hanged = False
    hit = False

    while((not hanged) and (not hit)):

        guess = input("Which letter?")
        guess = guess.strip()

        index = 0
        for letter in secrect_word:
            if(guess.upper() == letter.upper()):
                print("I found the letter {} in position {}".format(letter, index))
            index = index + 1
        print("Playing...")

    print("Game Over")


if(__name__ == "__main__"):
    play()
