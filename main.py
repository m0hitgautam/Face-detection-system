import os  # accessing the os functions
import check_camera
import Capture_Image



# creating the title bar function

def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** Face Recognition  System *****")
    print("\t***** Made with    ❤️by  Mohit and Vivek *****")
    print("\t**********************************************")


# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Quit")


    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                checkCamera()
                break
            elif choice == 2:
                CaptureFaces()
                break


                mainMenu()
            elif choice == 3:
                print("Thank You for our program")
                break
            else:
                print("Invalid Choice. Enter 1-4")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")
    exit


# ---------------------------------------------------------
# calling the camera test function from check camera.py file

def checkCamera():
    check_camera.camer()
    key = input("Enter any key to return main menu")
    mainMenu()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()






# ---------------main driver ------------------
mainMenu()
