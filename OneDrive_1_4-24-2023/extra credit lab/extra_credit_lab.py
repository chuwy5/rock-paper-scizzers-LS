#imort the random system
import random

def main():
    #declare variables
    rpsls = 0
    computer = 0
    user = 0
    tie = 0
    choice = 1
    while (choice == 1):
        
        #get random number for computer to wipe you with
        rpsls = random.randint (1, 5)

        userRpsls = getUser()
       
        #if and else statments to find the right match 
        if (rpsls == 1):
            if (userRpsls == 1):
                print ("rock vs rock what a tie")
                tie += 1
            elif (userRpsls == 2):
                print("paper covers rock you win")
                user += 1
            elif (userRpsls == 3):
                print ("rock crushes scissors sorry you lost to the computer")
                computer += 1
            elif (userRpsls == 4):
                print ("rock crushes lizard sorry you lost to the computer in a terrible death")
                computer += 1
            else:
                print ("spock vaporizes the rock, that poor rock never had a chance. you win")
                user += 1
        elif (rpsls == 2):
            if (userRpsls == 1):
                print ("paper vs rock what a way to to loose")
                computer += 1
            elif (userRpsls == 2):
                print("paper vs paper. well maby you wrote about 2 different things. you tied")
                tie += 1
            elif (userRpsls == 3):
                print ("scissors cuts paper and computer is crying cues all that work is down the drain. you win")
                user += 1
            elif (userRpsls == 4):
                print ("lizard eats paper and now the computer can say a lizard ate the homework. you win")
                user += 1
            else:
                print ("paper disproves spock and spock is crying in the corner. you loose")
                computer += 1
        elif (rpsls == 3):
            if (userRpsls == 1):
                print ("rock crushes scissors and you win")
                user += 1
            elif (userRpsls == 2):
                print("scissors cuts paper and now your homwork is in shreds. you loose")
                computer += 1
            elif (userRpsls == 3):
                print ("scissers vs scissers. sword fight! you are tied")
                tie += 1
            elif (userRpsls == 4):
                print ("lizard is decapitated by the scissors. what a way to go. you loose")
                computer += 1
            else:
                print ("spock smashes scissors. I would of thought he would use the phaser! you win")
                user += 1

        elif (rpsls == 4):
            if (userRpsls == 1):
                print ("rock crushes lizard and you win")
                user += 1
            elif (userRpsls == 2):
                print("lizard eats your paper and now you can say a lizard ate your homework. you loose")
                computer += 1
            elif (userRpsls == 3):
                print ("lizard is decapitated by the scissors. wow you just went there! you win")
                user += 1
            elif (userRpsls == 4):
                print ("lizard vs lizard. oh you have a male and a female and they leave you both... you are tied")
                tie += 1
            else:
                print ("spock missed the lizard with the phaser and is poisoned by the lizard. you loose")
                computer += 1
        else:
            if (userRpsls == 1):
                print ("spock vaporizes the rock. you loose")
                computer += 1
            elif (userRpsls == 2):
                print("spock is disproven by the paper and you see spock disapear. you win")
                user += 1
            elif (userRpsls == 3):
                print ("spock crushs the scissors and for good messure vaporizes them. you loose")
                computer += 1
            elif (userRpsls == 4):
                print ("spock looses his cool and screams when he sees the lizard and faints. spoke is now poisoned. you win")
                user += 1
            else:
                print ("spock vs spock. wow now theres 2 of them. im gona need a drink. you are tied")
                tie += 1
        choice = display(user, computer, tie)


def getUser():
    user = int(input("please make your choice for (1)rock (2)paper (3)scissers (4)lizard (5)spock"))
    return user

def display(user, computer, tie):
    print("user score: ", user, "computer score: ", computer, "tie score: ", tie)
    choice = int(input("would you like to play again y=1 n=2"))
    return choice


main()