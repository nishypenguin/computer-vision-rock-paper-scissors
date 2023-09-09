import random 

#def get_computer_choice():
    #rps_list = ["rock", "paper", "scissors"]
    #computer_choice = random.choice(rps_list)
    #return computer_choice

#def get_user_choice():
    #user_choice = input("Choose rock, paper or scissors: ")
    #if user_choice.lower() == "rock" or "paper" or "scissors":
        #return user_choice
    #else:
       # print("Invalid input, make sure you choose rock, paper or scissors")
        

def play():

    rps_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_list)
    
    user_choice = input("Choose rock, paper or scissors: ")


    
    if computer_choice.lower() == user_choice.lower():
        print("It's a tie")
    elif computer_choice.lower() == "rock" and user_choice.lower() == "scissors":
        print("You lost!")
    elif computer_choice.lower() == "paper" and user_choice.lower() == "rock":
        print("You lost!") 
    elif computer_choice.lower() == "scissors" and user_choice.lower() == "paper":
        print("You lost!")
    elif user_choice.lower() not in rps_list:
        print("Invalid input, please enter either rock, paper or scissors: ")
        play()
    else:
        print("You won!")
        
play()