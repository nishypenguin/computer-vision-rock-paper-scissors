import time  
import random 

class RPS:


    def __init__(self, user_wins = 0, computer_wins = 0):
        self.user_wins = user_wins
        self.computer_wins = computer_wins
        

    def get_prediction(self):

        import cv2
        from keras.models import load_model
        import numpy as np
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        start_time = time.time()
        integer_to_choice_list = ["rock", "paper", "scissors", "nothing"]

        while True: 
        
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            print(prediction)
            cv2.imshow('frame', frame)
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 3:
                print("Countown starting")
            if elapsed_time >= 4:
                print("Rock")
            if elapsed_time >= 5:
                print("Paper")
            if elapsed_time >= 6:
                print("Scissors")
            if elapsed_time >= 7:
               print("Shoot")
                
            if elapsed_time >= 8:
                break

            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                   
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        
        user_int_choice = np.argmax(prediction)
        user_choice = integer_to_choice_list[user_int_choice]
        print(f"Shoot. You chose {user_choice}")
        return user_choice
    


    def get_computer_choice(self):
        rps_list = ["rock", "paper", "scissors"]
        computer_choice = random.choice(rps_list)
        return computer_choice
          

    def get_winner(self, user_choice, computer_choice):
    
        if computer_choice == user_choice:
            print("It's a tie")
        elif (
            (computer_choice == "rock" and user_choice == "scissors") or
            (computer_choice == "paper" and user_choice == "rock") or
            (computer_choice == "scissors" and user_choice == "paper")
             ):
            self.computer_wins += 1                                                                    
            print (f"You lost! The computer chose {computer_choice}")
        elif user_choice == "nothing":
            print("Invalid input, please choose either rock, paper, or scissors")
        else:
            self.user_wins += 1
            print(f"You won! The computer chose {computer_choice}")


        
        
    def check_game(self):
        while self.user_wins < 3 and self.computer_wins < 3:
            user_choice = self.get_prediction()
            computer_choice = self.get_computer_choice()
            self.get_winner(user_choice, computer_choice)

        if self.user_wins == 3:
            return "Congratulations! You beat the computer to 3 games"
        elif self.computer_wins == 3:
            return "Unlucky! The computer beat you to three games"
            
def play():
    game = RPS(user_wins =0, computer_wins = 0)
    result = game.check_game()
    if result:
        print(result)

        
play()
        
    