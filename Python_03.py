#This is a basic calculator
#Last edited Sun, Sep 18
#By Zichen

import os
import sys
import time
import webbrowser
from inspect import currentframe

#Operators needed for printing the answer
Operators = [" + ", " - ", " x ", " / ", " ^ "]
#Operations needed for calculating
currentOperation = None
#Number needed for, well the basics of calculator
Num_a = None
#Number needed for the basics of calculator
Num_b = None
#Answers that is not currently populated
Ans = 0

#####################################################################################

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

def clear_console():
    os.system('clear')

def easter_egg(_variable): 
    if _variable.lower() == "that's what she said" or _variable.lower() == "thats what she said": 
        clear_console()
        print("\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        time.sleep(2)
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        input("\nPress enter to continue...")

#Init: Asking the user the operation as well as the number and checking that those are valid etc. 
def init(_num_a = None): 
    global Num_a
    global Num_b
    global currentOperation
    global Ans
    #Try is needed because of a value error that occurs when the user enters invalid characters such as letters
    try: 
        #Checking if it's the second time running the look (if number A is the answer)
        if _num_a != Ans: 
            Num_a = input("0.0 \n\nInput number A: ")
            clear_console()
            easter_egg(Num_a)
            Num_a = float(Num_a)
            print(f"{str(Num_a)}\n")
        #If it is the second time running, skip asking for a number
        else: 
            clear_console()
            print(f"{str(Num_a)}\n")
        #User inputting the operation
        currentOperation = input("Please specify which operations you want to perform: \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n")
        easter_egg(currentOperation)
        #Checking if the user inputted is valid
        clear_console()
        if currentOperation == 1 or currentOperation == 2 or currentOperation == 3 or currentOperation == 4 or currentOperation == 5:
            pass
        else: 
            #If the operation the user inputted is invalid, it asks the user to input a new valid value
            while currentOperation not in ["1", "2", "3", "4", "5"]: 
                print(f"{str(Num_a)}\n")
                currentOperation = input("Please input a valid value: \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n")
                clear_console()
        currentOperation = int(currentOperation)
        #Printing the inputs
        print(f"{Num_a}{Operators[currentOperation - 1]}\n")
        #Inputting the second number
        Num_b = input("Input number B: ")
        easter_egg(Num_b)
        #Printing the inputs
        clear_console()
        print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)}")
        Num_b = float(Num_b)
    #If any of the values the user entered is not allowed, the program will restart. 
    except ValueError: 
        clear_console()
        print("ERROR\n")
        currentOperation = 6
        return

#####################################################################################

#Start of program
clear_console()
print("You are currently running Python ", sys.version)
print("Welcome and thank you for using Calculator.py")
time.sleep(2)

while True: 
    #Initializing and resetting
    clear_console()
    init()
    while True:
        #Looping the calculator until the user closes the application
        #Calculating the inputs the user gave
        if currentOperation == 1: 
            #Addition
            Ans = Num_a + Num_b
            Ans = round(Ans,8)
        elif currentOperation == 2:
            #Subtraction
            Ans = Num_a - Num_b
            Ans = round(Ans, 8)
        elif currentOperation == 3: 
            #Multiplication
            Ans = Num_a * Num_b
            Ans = round(Ans, 8)
        elif currentOperation == 4:
            #Division
            try: 
                Ans = Num_a / Num_b
                round(Ans,8)
            except ZeroDivisionError: 
                #Restart the program if the user tries to divide by zero. 
                clear_console()
                print(f"ERROR\nProgram error: Couldn't divide by zero [{get_linenumber()}]")
                input("Press enter to continue...")
                break
        elif currentOperation == 5: 
            #Exponents
            Ans = Num_a ** Num_b
            Ans = round(Ans,8)
        elif currentOperation == 6: 
            #If there's an error during the input phase, it will catch them here
            print(f"Program error: A fatal error occured [{get_linenumber()}]")
            input("Press enter to restart...")
            break
        else: 
            clear_console()
            print(f"\nProgram error: An unknown fatal error occured - Debug is necessary [{get_linenumber()}]")
            input("Press enter to continue...")
            break
        #Printing Answer
        clear_console()
        print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}")
        #Repeating Action
        repeatAction = input("\nInput the next action: \n[1]Clear Operation \n[2]Continue Operation \n[3]Quit Operation \n")
        clear_console()
        easter_egg(repeatAction)
        #Checking if the input is valid
        if repeatAction == 1 or repeatAction == 2 or repeatAction == 3:
            pass
        else: 
            #If the operation the user inputted is invalid, it asks the user to input a new valid value
            while repeatAction not in ["1", "2", "3"]: 
                print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}")
                repeatAction = input("\nPlease input a valid value: \n[1]Clear \n[2]Continue Operation \n[3]Quit Operation \n")
                clear_console()
            repeatAction = int(repeatAction)
        print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}")
        #If the user clears the calculator
        if repeatAction == 1: 
            #Clearing variables
            Ans = 0
            Num_a = 0
            Num_b = 0
            currentOperation = 0
            #Clearing console
            clear_console()
            #Reinitializing
            init()
            #If an error occured, restart (break this loop)
            if currentOperation == 6: 
                print(f"Program error: A fatal error occured [{get_linenumber()}]")
                input("Press enter to continue...")
                break
        elif repeatAction == 2: 
            Num_a = Ans
            init(Ans)
            #If an error occured, restart (break this loop)
            if currentOperation == 6: 
                print(f"Program error: A fatal error occured [{get_linenumber()}]")
                input("Press enter to continue...")
                break
        elif repeatAction == 3: 
            clear_console()
            print("Program exited: User terminated operation")
            time.sleep(2.5)
            clear_console()
            exit()
        else: 
            clear_console()
            print(f"Program restarted: An unknown fatal error occured - Debug is necessary [{get_linenumber()}]")
            input("Press enter to continue...")
            break
