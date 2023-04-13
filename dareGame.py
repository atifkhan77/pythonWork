#Using random module
#Using functions
import random
from time import sleep # From time Module and Module is python file consisitng of d/f functions , bla bla ....
from array import *
from os import sys #For Quit, sys module 
def play_Dare_game():
    count = 0
    print(" ----------------------------------------")
    print("   WELCOME TO WORLD OF DARE. HAVE FUN.   ")
    print("-----------------------------------------")

    sleep(1)

    arr = []
    players = int(input("\nEnter the number of players: "))

    while count < players:
            count += 1
            name = str(count)
            x = input("Enter the name of player" +name +": ")
            arr.append(x) #appending every name entered, in the array

    print("\n The name(s) of the player(s) who are currently playing this game is/are: ")
    print(arr)  #printing array of names
    sleep(0.5)

    def dare_game():
        print("\nPress ENTER to see who have to do the DARE.")
        a_1 = input()  #for pressing enter key 

        choosen = random.choice(arr) #choosing person randomly

        print("Hey, "+choosen +" it's your turn...")
        print("press enter to see your Dare")

        press_enter = input() #for pressing any alphabet for dare

        number = random.randint(1,30)
        if number == 1:
            print("Peel an apple with your fingers ony.")
        if number == 2:
            print("act like a newborn baby .")
        if number == 3:
            print("Eat a piece of mixed spices.")
        if number == 4:
            print("Dance like a choreographer")
        if number == 5:
            print("Tell a secret of yours.")
        if number == 6:
            print("show us your ugly pictures")
        if number == 7:
            print("Allow your gamming friends to ask you whatever they \nwant and you have to answer it truly.")
        if number == 8:
            print("message random people on facebook.")
        if number == 9:
            print("Full your mouth with watermelon and singing a song.")
        if number == 10:
            print("Do 10 chin ups.")
        if number == 11:
            print("sing a song for your partener .")
        if number == 12:
            print("Stand like a begger.")
        if number == 13:
            print("Smell a dirty sock for 10 seconds.")
        if number == 14:
            print("Act like Mr.bean")
        if number == 15:
            print("Do a runway walk like gigi hadid.")
        if number == 16:
            print("Eat a teaspoon full of Soy sauce.")
        if number == 17:
            print("Tell a lie about someone.")
        if number == 18:
            print("Howl like a wolf .")
        if number == 19:
            print("Let someone else style your hair .")
        if number == 20:
            print("Spin around 10 times and try to walk straight.")
        if number == 21:
            print("cut your own hair.")
        if number == 22:
            print("Do 20 situps.")
        if number == 23:
            print("wink 10 times with same eye.")
        if number == 24:
            print("Keep your eyes open for 30 seconds without blinking.")
        if number == 25:
            print("Tell sentences on crow but replace 'Crow' with 'I'.")
        if number == 26:
            print("Sing your Favorite song by tapping your mouth with two fingers.")
        if number == 27:
            print("Dubbing your Favorite actor or actress.")
        if number == 28:
            print("Write 'I'm engaged' on your WhatsApp status and set it as public." )
        if number == 29:
            print("Slap the person sitting next to you.")
        if number == 30:
            print("wash 5 dishes in kitchen.")

        print("\n Press ENTER to CONTINUE the GAME. \nPress 'Q', if you want to QUIT the GAME.\n")
        action3 = input().lower()
        if action3 == 'q': #if user want to exit from here
                sys.exit(0)
        else:
            dare_game() #for entering key other than q will execute program again
    dare_game()


               
#function for the survival game
def main_survival_game_menu():
    print("WELCOME TO WORLD OF ADVENTURE! ")
    name=input("WHAT IS YOUR NAME:  ")
    age=eval(input("WHAT IS YOUR AGE:  "))

    lifelines=10

    if age>=18:
        print("LETS PLAY! YOU ARE OLD ENOUGH TO PLAY THIS GAME.....")
        # wait for 1 second
        sleep(1)
        print("......")
   
        wants_to_play=input("DO YOU WANT TO PLAY THIS GAME? ").lower()
        sleep(1)
        if wants_to_play=="yes":
            print ("YOU ARE STARTING WITH",lifelines,"lifelines") 
            print("LET'S PLAY!")
            choices = ("left" , "right") #using tuple because values are fixed and tuple is faster than list
            randoms = random.choice(choices)

            left_or_right=input("FIRST CHOICE... left or right (left/right)? ").lower()
            
            if left_or_right == randoms: 
                ans=input("YOU ARE ON THE SEASIDE...WILL YOU CHOOSE A SHIP OR A CAR(SHIP/CAR)? ").lower()

                if ans=="ship":
                    print("YOU REACHED THE OTHER SIDE OF THE LAKE.")
                
                elif ans=="car":
                    print("you lost 5 lifelines.")

                    lifelines-=5

                ans=input("YOU ARE HUNGRY, THEE IS A HOUSE AND A LIONCAGE.WHICH WAY DO YOU WANT TO GO (HOUSE/LIONCAGE)? ").lower()
                if ans=="house":
                    print("YOU FOUND SOME FOOD TO EAT. YOU SURVIVED.")
                
                    if lifelines>=5:
                        print("YOU HAVE SURVIVED....YOU WON!")

                else:
                    print("LION ATE YOU AND YOU LOST.....")

        
            else:
                print("YOU HAVE LOST YOUR LIFELINES.....")

        else:
            print("HAVE A NICE DAY! SEE YOU LATER....." )
    else:
        print("YOU ARE NOT OLD ENOUGH TO PLAY THIS GAME.....")
        exit()

   


def get_statement():
    print("\n USE ALPHABETS 'T' FOR TRUE AND 'F' FOR FALSE\n ")
    #Using two dimentional lists
    statements=[]
    statements.append(["most beautiful bridge in the world is in turkey","T"])
    statements.append(["june has 31 days","F"])
    statements.append(["The capital of pakistan is Islamabad","T"])
    statements.append(["sparrows can fly to the highest heights","F"])
    statements.append([" Humans have four hearts.","F"])
    statements.append([" A sneeze is faster than the blink of an eye.","T"])
    statements.append([" The Earth’s oceanic water is divided in 6 ocean.","F"])
    statements.append(["The amount of time taken by a device to begin reading data is named Acess time","T"])
    statements.append(["Each day human body breathe in 15,000 to 20,000 liters of air","T"])
    statements.append(["the second most populus city on the earth is Shanghai","F"])
    statements.append(["The Lowest part of the Earth is Dead Sea","T"])
    statements.append(["According to the scientists, the Earth was formed about 5.6 billion year ago","F"])
    statements.append(["All tigers have yellow eyes.","T"])
    statements.append(["Dodo is an endangered bird.","F"])
    statements.append(["Roman Calendar is named as Julian Calendar.","T"])
    statements.append([" Laika, the dog is the first animal to go to space.","T"])
    statements.append(["Washington DC is the capital of China.","F"])
    statements.append(["June 5 is celebrated as Environment Day.","T"])
    statements.append(["Bhagat Singh is a Freedom fighter of India.","T"])
    statements.append(["Arachnophobia is the fear of dogs","F"])

    return statements
def play_quiz():
   
    quiz_statements=get_statement()
    
    random.shuffle(quiz_statements)
    score=0
    for s in quiz_statements:  #an element in the quiz statement list
       
        print("True or False: "+s[0])
       
        guess=input("Enter T or F: ").upper()
        
        if guess==s[1]:
            print("Correct! :)")
            #update the score
            score+=1
        else:
            print("Incorrect :(")
    #show the final score
    sleep(1)
    print("Your final score is: "+str(score),"OUT OF 20")



def GAMES():
    print("|__________________________________|")
    print("|                                  |")
    print("|    * Welcome to the GAMES!*      |")
    print("|__________________________________|")
    print("|                                  |")
    print("| Please select an option:         |")
    print("| 1. dare game                     |")
    print("| 2. quiz                          |")
    print("| 3. survival game                 |")
    print("| 0. Quit                          |")
    print("|__________________________________|")
    print()
    
    while True:
        choice=input("Enter 1 for Dare game or 2 for quiz or 3 to play survival game or 0 to quit : ")
        if choice=="1":
            play_Dare_game()
        elif choice=="2":
            play_quiz()
        elif choice == "3":
            main_survival_game_menu()
        elif choice=="0":
                print("Thanks for playing")
                sys.exit(0)
        else:
            print("sorry wrong choice")
       
#function for exiting the program
def EXIT():
    sys.exit(0)
#working on the main function of this program        
def main():

    
    while True:
        print("|________________________________________|")
        print("|                                        |")
        print("|     ***welcome to games***             |")
        print("|________________________________________|")
        print("|        1) GAMES                        |")
        print("|        2) EXIT                         |")
        print("|                                        |")
        print("|________________________________________|")

        print(".......")
        sleep(1)
   
        choice=eval(input("Select choice 1 or 2: "))
        if  choice==1:
            GAMES()
        elif choice==2:
            EXIT()
        else:
            print("sorry wrong choice")
#calling the main function of the program
main()
