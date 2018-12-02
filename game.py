import random
import time
print("\t \t \t \t \t \t \t ROCK,PAPER,SCISSOR GAME")
print("\t \t \t------------------------------------------------------------------------------------------")
name=input("Enter your name=")
while len(name)==0:
    name=input("Enter your name=")
print("Hello",name)
print("\t \t \t \t \t \tWELCOME TO ROCK, PAPER AND SCISSOR GAME \t \t \t \t \t \t")
print("\t \t \t------------------------------------------------------------------------------------------")
score=[]                                                                             #To store the score for printing high score 
i=0
n=6
user_score=0                                                                                #To store the score
comp_score=0
start_time=time.time()

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
print("Enter 1 for rock,2 for paper and 3 for scissor")
ans='y'
while ans=='y':
    while i<n:                                                                      #loop will execute till the value of i is 6
        print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
        choice = int(input("Your turn.Enter the number(1 to 3): "))
        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'
        print("user choice is: " + choice_name)
        print("\nNow its computer turn.......")
        comp_choice = random.randint(1, 3)                                          #computer choses any random number from 1 to 3
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'     
        print("Computer choice is: " , comp_choice_name)
        print(choice_name , " V/s " , comp_choice_name)
        if((choice == 1 and comp_choice == 2) or
          (choice == 2 and comp_choice ==1 )):
    
            result = "paper"     
        elif((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
            result = "Rock"
        elif((choice==2 and comp_choice==3) or
             (choice==3 and comp_choice==2)):
            result = "scissor"
        else:
            result="Draw"
        i+=1
        if result == choice_name:
            print("<== You wins==>")
            user_score+=1                                                                   #user_score increement
          
        elif result==comp_choice_name:
            print("<== Computer wins ==>")
            comp_score+=1                                                                   #comp_score increements
        
            
        else:
            print("<== Draw ==>")
    i=0
    score.append(user_score)                                                                   #append the user score into list                                                             
    high_score=max(score)                                                                      #storing the highest score from the list                                                                  
    print("Your score is=",user_score)                                                         #print the user score                                                      
    print("Computer score=",comp_score)                                                        #print the computer score
    print("Your best score is=",high_score)                                                    #print the high score                                               
    if user_score>comp_score:
        print("\t \t \t \t \t \tCONGRAGTULATION! YOU WON \t \t \t \t \t \t")
    elif user_score<comp_score:
        print("\t \t \t \t \t \t OHH!,YOU LOSE.BETTER LUCK NEXT TIME\t \t \t \t \t \t")
    else:
        print("\t \t \t \t \t \t The match is tied\t \t \t \t \t \t \t")
    user_score=0
    comp_score=0
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans == 'n' or ans == 'N' or ans=='no' or ans=='NO':  
        break                                                                                 #if ans==n then it comes out from the loop
end_time=time.time()                                                                           #ending the timer
time=end_time-start_time
print("The total time taken to play=",time)                                                     #printing the time taken to play
