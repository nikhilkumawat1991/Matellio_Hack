import os  # accessing the os functions
import lcd_function
import functionKeypress
import sys
import Recognition_function
import led_function
from select import select
# creating the title bar function
# creating the user main menu function

def mainMenu():
    led_function.door_close()
    lcd_function.welcome()
    led_function.door_close()
    while True:
        try:
            choice = int(input("Enter Choice: "))
            id_name=functionKeypress.id_verification(choice)
            User_id=id_name[0]
            x=id_name[1]
            
            #print(User_id)

            if User_id =="WrongId":
                WrongId(x)
                break
            elif User_id!="WrongId":
                led_function.door_verify_open()
                Verify(User_id)
                break
            else:
                print("Invalid")
                mainMenu()
        except ValueError:
            #NumId()
            print("Invalid Choice")
        exit


# ---------------------------------------------------------4
def WrongId(x):
    lcd_function.key_input(str(x)+"\n is Wrong_ID")
    led_function.door_fail_open()
    key = input("Enter any key to return main menu")
    mainMenu()
def Verify(x):
    lcd_function.key_input(str(x)+"\nlook at camera")
    Recognition_function.recognize_attendence()
    led_function.door_open()
    key = input("Enter any key to return main menu")
    mainMenu()
def NumId():
    lcd_function.idFormat()
    key = input("Enter any key to return main menu")
    mainMenu()





# ---------------main driver ------------------
mainMenu()
