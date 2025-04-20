import pyautogui
import sys
import os

x = 1

name_value = 1


def New_name(Base,ext):
    counter = 1
    filename = f"{Base}.{ext}"

    while os.path.exists(filename):
        if counter == counter:
            counter += 1
        filename = f"{Base}{counter}.{ext}"
        

    return filename



text_output = New_name("Recording", "txt")




def Valid_option_menu():
    try_again = input("Would you like to record again? Y/N: ")

    if try_again.upper() == "Y":
                        
            mouse_record()

    elif try_again.upper() == "N":
                        
            print("Exiting....created by Ricardo Montoya 04/18/2025..................................................See Yah!")

            SystemExit
                
    else:

        print("Invalid option!")

        Valid_option_menu()


def exit_menu():

    try:
        

    
        try_again = input("Would you like to exit? Y/N: ")

        if try_again.upper() == "Y":
                        
            print("Exiting....created by Ricardo Montoya 04/18/2025..................................................See Yah!")

            SystemExit

        elif try_again.upper() == "N":

            start()
                
        else:

            print("Invalid option!")

            exit_menu()
            
    except KeyboardInterrupt:
        print("CTRL + C Pressed.")
        exit_menu()
        





def start():
    try:
        
        start = input("Would you like to Start Recording? Y/N: ")

        if start.upper() == "Y":
                        
            mouse_record()

        elif start.upper() == "N":
                        
            exit_menu()
                
        else:

            print("Invalid option!")


            start()
            
    except KeyboardInterrupt:
        print(" CTRL + C was pressed")
        exit_menu()
        
def counting():
    while x == 1:
        test = pyautogui.position()
        print(test)




def mouse_record():
    try:
        print("WARNING!")
        print("PRESS CTRL + C TO STOP RECORDING")
        print("THIS TEXT FILE WILL BE HUGE. IF YOU RUN THIS FOR A LONG TIME IT WILL HURT YOUR SYSTEM OR POSSIBLY RENDER THE SYSTEM UNUSABLE")
        print("BY USING THE APP, YOU AGREE THAT YOU'RE RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS APP. AND THE AUTHOR IS NOT RESPONSIBLE FOR ANY DAMAGE")
        confirmation = input("Do you understand? Y/N: ")

        if confirmation.upper() == "Y":
            print("RECORDING. PRESS CTRL + C TO STOP")

            
            text_output = New_name("Recording", "txt")

            with open(text_output, "w") as file:
                original_stdout = sys.stdout
                try:
                    sys.stdout = file
                    counting()
                except KeyboardInterrupt:
                    pass
                finally:
                    sys.stdout = original_stdout
                    print(f"Recording saved to: {text_output}")
                    exit_menu()

        elif confirmation.upper() == "N":
            print("Returning to the start....")
            start()
        else:
            print("Invalid Option typed.")
            mouse_record()

    except KeyboardInterrupt:
        print(" Early CTRL + C pressed")
        mouse_record()
                             
                             
            
        

def main():
    
    start()



if __name__ == "__main__":
    main()
        
        
    
