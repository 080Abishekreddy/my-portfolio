import random
from words import word_list
def hangman():
    word=(random.choice(word_list)).upper()
    turns=10
    guess=["_"]*len(word)
    print("you need to guess tha word computer had chosen")
    print("you will be given 10 chances")
    print("for each wrong guess an innocent person will get closer to his death")
    print("you can save him by guessing the word correctly")
    while(turns!=0):
        x=input()
        if x in word:
            if x  not in guess:
                for index,elem in enumerate(word):
                    if x==elem:
                        guess[index]=x
                    elif "".join(guess)==word:
                        print("congratulations! you won")
                        print("the correct word is:",word)
                        break
            else:
                print("you had guessed this word before")
        else:
            print("wrong guess")
            turns-=1
            if turns==9:
                print("9 turns left")
                print("------------")
            if turns==8:
                print("8 turns left")
                print("------------")
                print("      O     ")
            if turns==7:
                print("7 turns left")
                print("------------")
                print("      O     ")
                print("      |     ")
            if turns==6:
                print("6 turns left")
                print("------------")
                print("      O     ")
                print("      |     ")
                print("     /      ")
            if turns==5:
                print("5 turns left")
                print("------------")
                print("      O     ")
                print("      |     ")
                print("     / \     ")
            if turns==4:
                print("4 turns left")
                print("------------")
                print("     \O     ")
                print("      |     ")
                print("     / \    ")
            if turns==3:
                print("3 turns left")
                print("------------")
                print("     \O/     ")
                print("      |     ")
                print("     / \    ")
            if turns==2:
                print("2 turns left")
                print("------------")
                print("     \O/ |     ")
                print("      |     ")
                print("     / \    ")
            if turns==1:
                print("1 turn left!!!!hangman breathing his last breath!!!")
                print("------------")
                print("     \O/ _|     ")
                print("      |     ")
                print("     / \    ")
            if turns==0:
                print("you lose")
                print("------------")
                print("      O_|     ")
                print("     /|\     ")
                print("     / \    ")
                print("you let a kind man die")
                print("your word is:",words)
                break
        print(" ".join(guess))
            
    
name=input("ENTER YOUR NAME->")
hangman()