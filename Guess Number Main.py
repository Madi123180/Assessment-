import random
import sys
import math
Gamecount=0  #defining Global Variable

def GNG():
    Playerwins =0
    Computerwins =0  
  
    
    def GNGame(): 
        nonlocal Playerwins   #nonlocal keyword used to use the variable that is belongs to other function
        nonlocal Computerwins 
        print("*********Welcome to Guess Number Game*********")   
        Player1 = input ("Guess which number i am thinking of.....1 or 2 or 3? \n\n")
        Player=int(Player1) #getting input from User
        if Player != 1: #Validating the input value using if loop 
            if Player != 2:
                if Player != 3:
                    print("You have chosen incorrect value \n\nPlease choose correct value\n \n")
                    return GNGame() #When the value is not correct calling the function again from the beginning
        # print(type(Player1))
        Computerplayer = [1,2,3]  #Defining options for the computer
        Computerplayer = random.choice(Computerplayer) #writing code to choose random value
        print("")
        print(f"\n Player chose {Player1}" ) 
        print(f"\n I was thinking about the number {Computerplayer}") 
     
        print("")
        
        #validating the selected values by both computer and User using if statement

        if Player == 1 and Computerplayer == 1: 
            Playerwins =Playerwins+1 # increasing the player winning count
            print ("\n"  +"Player wins 🎉!!! ")    

            option() #to print some additional detail calling one more function here
        elif Player == 2 and Computerplayer == 2:
             Playerwins =Playerwins+1
             print ("\n" +"Player wins 🎉!!! ") 
             
             option()
        elif Player == 3 and Computerplayer == 3:
            Playerwins =Playerwins+1
            print ("\n" +"Plyer wins 🎉!!! ") 
            
            option()
        elif Player == Computerplayer:
            print (" Tie Game 🤝!!")
            option()
        else:           
            Computerwins=Computerwins+1
            print ("\n" +"Computer Wins 🎉!!!")  #increasing the computer winning count
            print(f"\n Sorry Better Luck Next time") 

            

        option() 
  
    

    def option():  #creating new function
        global Gamecount #Using the global variable
        Gamecount=Gamecount+1 #increaseing the overall game count
        print(f"\n Total Game count is {Gamecount}") 
        print(f"\n Player wins count:{Playerwins}") 
        print(f"\n Computer wins count: {Computerwins}") 
        print(f"\n Computer wins Percentage: {Computerwins/Gamecount:.2%}")
        print(f"\n Player wins Percentage:{Playerwins/Gamecount:.2%}") 
      
    
        while True: #using while loop to continue untill user selects the correct value
            Playagain= input("\n" + "Please type Yes to proceed or Quit to close the game \n \n") #getting input from user
            #to continue or quit the game
            if Playagain == 'Yes':
                return GNGame()           
            if Playagain not in ["Yes" and "Quit"]:
                print("\n" + "Please enter correct value")
            else:                
                print("\n" + "Thank you for your time 🤝")
                sys.exit("\n" + "See you next time 👋")               
          
   
        
    return GNGame #This return statement indicates that all fucntions are executed and values are returned.

Game=GNG()
Game() #calling the entire function


    


