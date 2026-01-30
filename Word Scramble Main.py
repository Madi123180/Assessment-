import random
import sys

#word = 'selenium'
#scrambled = "".join(random.sample(word, len(word))) # this code is used to scramble only one word at a time
print("\n" + "Hi, Welcome to Scramble Game 🎉 Are you excited?  \n\n")
ProgramLanguages = ['Python','javascript','java','automation','pytest','guvi','selenium']
scrambled = ["".join(random.sample(word, len(word))) for word  in ProgramLanguages]  #Since scrambling each word from list we have
#to use for loop to pick each word from list
print(scrambled)
while True:
    Player=input("\n" + "Its your time, Please enter your guess" + "\n").split(',')
    PlayerList=list(Player) 
    if ProgramLanguages == PlayerList:
        print("\n"  + "Hooray, you found it 🎉!!! ")
        print("\n" + "Thank you for your time 🤝")
        sys.exit("\n" + "See you next time 👋")
    else:
        print("\n" + "You have missed something. Please give a chance one more time 🎉!!!")
      

            
   


                            


