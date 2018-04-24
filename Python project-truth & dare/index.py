import random
import time
import truth_list
import dare_list


#A HARD Welcome


print("\n\n                            !!Hey!!\n                            Welcome\n                              To \n                           The Game\n")


#Loop for game


while(1):
    input("   \n                        Ready To Play?\n                    Press enter to continue:")


#Loop for player Entry

    
    while(1):
        input_string=input("\n Enter a list of players,separated by a comma.Hit enter when you finished:\n")
        my_list=input_string.replace(" "," ").split(",")
        print("  ",my_list)


#Confirming the players are correct or not

        
        print("\n                    Is that correct?(Y/N)")
        choice=input()
        if(choice=='Y' or choice=='y'):
            break


#Choosing the player

    while(1):
        print("\n                         Go?(Y/N)")
        choice=input()
        if(choice=='n' or choice=='N'):
            break
        print("\n                  The player to be Teased is:\n")
        player=random.choice(my_list)
        print("                             ",player)


#asking of choice(TRUTH or DARE?)

    
        print("\n                Hey",player,", How would you be like to be Teased?\n                          BY TRUTH(T)\n                             OR\n                           BY DARE(D)\n                            ?")
        choice=input()


#Showing a question on the basis of player's choice

    
        if(choice=="TRUTH" or choice=="truth" or choice=="Truth" or choice=='T' or choice=='t'):
            print("\n\n                   Here comes the Question:\n\n",random.choice(truth_list.truth_list))
            temp=input()
        elif(choice=="DARE" or choice=="dare" or choice=="Dare" or choice=='d' or choice=='D'):
            print("\n\n                   Here is the DARE:\n\n",
                  random.choice(dare_list.dare_list))
            time.sleep(12)


#braking game(Exit or Continue play?)

    
    print("\n\n\n                         Do you want to play again?(Y/N)")
    choice=input()
    if(choice=='N' or choice=='n'):
        break
