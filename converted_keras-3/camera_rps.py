
import time     

def get_prediction():

    import cv2
    from keras.models import load_model
    import numpy as np
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start_time = time.time()
    integer_to_choice_list = ["rock", "paper", "scissors","nothing"]

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
            user_int_choice = np.argmax(prediction)
            user_choice = integer_to_choice_list[user_int_choice]
            print(f"Shoot. You chose {user_choice}")
        if elapsed_time >= 8:
            break

         # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
            

       
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    print(user_choice)
    return user_choice


    


get_prediction()



