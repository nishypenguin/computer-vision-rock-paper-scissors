import random 

def get_computer_choice():
    rps_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_list)
    return computer_choice

def get_user_choice():
    user_choice = input("Choose rock, paper or scissors: ")
    return user_choice
    
        

def get_winner(user_choice, computer_choice):


    
    if computer_choice.lower() == user_choice.lower():
        print("It's a tie")
    elif (
         (computer_choice.lower() == "rock" and user_choice.lower() == "scissors") or
         (computer_choice.lower() == "paper" and user_choice.lower() == "rock") or
         (computer_choice.lower() == "scissors" and user_choice.lower() == "paper")
    ):
                                                                            
        return "You lost!"
    else:
        return "You won!"
        
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    if user_choice.lower() not in ["rock", "paper", "scissors"]:
        print("Invalid input, please enter either rock, paper or scissors.")
        play()
    else:
        result = get_winner(user_choice, computer_choice)
        return result
    

play()