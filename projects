import random
def hangman():
    word = random.choice(["python","world","earth","friday","weather",
                          "rain","life","love","panda","hangman"])
    valid = 'abcdefghijklmnopqrstuvwxyz'
    turn = 10
    guessmade = ''
    while len(word)>0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main+letter
            else:
                main = main+"_"+""
        if main == word:
            print(main)
            print("you WIN")
            break
        print("Guess the word ",main)
        guess = input()
        if guess in valid :
            guessmade = guessmade+guess
        else:
            print("enter a valid character")
            guess = input()
        if guess not in word:
            turn = turn -1
            if turn==9:
                print("9 turn left")
                print("  ----------  ")
                
            if turn==8:
                print("8 turn left")
                print("  ----------  ")
                print("      0       ")
            if turn==7:
                print("7 turn left")
                print("  ----------  ")
                print("      0       ")
                print("      |       ")
            if turn==6:
                print("6 turn left")
                print("  ----------  ")
                print("      0       ")
                print("      |       ")
                print("     /        ")
            if turn==5:
                print("5 turn left")
                print("  ----------  ")
                print("      0       ")
                print("      |       ")
                print("     / \      ")
                
            if turn==4:
                print("4 turn left")
                print("  ----------  ")
                print("    \ 0       ")
                print("      |       ")
                print("     / \      ")
            if turn==3:
                print("3 turn left")
                print("  ----------  ")
                print("    \ 0 /     ")
                print("      |       ")
                print("     / \      ")
            if turn==2:
                print("2 turn left")
                print("  ----------  ")
                print("    \ 0 /|    ")
                print("      |       ")
                print("     / \      ")
            if turn==1:
                print("1 turn left")
                print("last breath counting ...")
                print("  ----------  ")
                print("    \ 0_|/    ")
                print("      |       ")
                print("     / \      ")
            if turn==0:
                print("YOU LOSE")
                print("you let a kind man DIE")
                print("  ---------- ")
                print("      0_|    ")
                print("     /|\     ")
                print("     / \     ")
                break
            
