#This is a basic calculator
#Last edited Mon, Sep 12
#By Zichen

import os
import time


#Operators needed for printing the answer
Operators = [" + ", " - ", " x ", " / ", " ^ "]
currentOperation = None
Num_a = None
Num_b = None
Ans = 0

#####################################################################################

def clear_console():
    os.system('clear')

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
            Num_a = float(input("Input number A - "))
        clear_console()
        #Print the input
        print(f"{str(Num_a)}\n")
        #User inputting the operation
        currentOperation = int(input("Please specify which operations you want to perform - \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n"))
        clear_console()
        #Checking if the user inputted is valid
        if currentOperation == 1 or currentOperation == 2 or currentOperation == 3 or currentOperation == 4 or currentOperation == 5:
            pass
        else: 
            #If the operation the user inputted is invalid, it asks the user to input a new valid value
            while currentOperation not in [1, 2, 3, 4, 5]: 
                currentOperation = int(input("Please input a valid value - \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n"))
                clear_console()
            pass
        #Printing the inputs
        print(f"{Num_a}{Operators[currentOperation - 1]}\n")
        #Inputting the second number
        Num_b = float(input("Input number B - "))
        clear_console()
        #Printing the inputs
        print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)}\n")
    #If any of the values the user entered is not allowed, the program will restart. 
    except ValueError: 
        clear_console()
        print("Program restarting - A ValueError occured")
        currentOperation = 6
        return



#####################################################################################
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
            round(Ans,8)
        elif currentOperation == 2:
            #Subtraction
            Ans = Num_a - Num_b
            round(Ans, 8)
        elif currentOperation == 3: 
            #Multiplication
            Ans = Num_a * Num_b
            round(Ans, 8)
        elif currentOperation == 4:
            #Division
            try: 
                Ans = Num_a / Num_b
                round(Ans,8)
            except ZeroDivisionError: 
                #Restart the program if the user tries to divide by zero. 
                print("Program restarting - Couldn't divide by zero")
                time.sleep(2)
                break
        elif currentOperation == 5: 
            #Exponents
            Ans = Num_a ** Num_b
            round(Ans,8)
        else: 
            #Catching any unexpected errors. If this happens, then it means that there is most likely some problem with checking if the input is valid
            print("Program restarted - A fatal error occured")
            time.sleep(2)
            break
        #Printing Answer
        clear_console()
        try: 
            int(Num_a)
            int(Num_b)
            int(Ans)
        except ValueError: 
            pass
        finally: 
            print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}")
        #Repeating Action
        repeatAction = int(input("\nInput the next action - \n[1]Clear \n[2]Continue Operation \n[3]Quit Operation \n"))
        clear_console()
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
            print("Cleared")
            init()
            #If an error occured, restart (break this loop)
            if currentOperation == 6: 
                print("Program restarted - A fatal error occured at line 120")
                time.sleep(2)
                break
        elif repeatAction == 2: 
            Num_a = Ans
            init(Ans)
            #If an error occured, restart (break this loop)
            if currentOperation == 6: 
                print("Program restarted - A fatal error occured at line 126")
                time.sleep(2)
                break
        elif repeatAction == 3: 
            clear_console()
            print("Program exited - User terminated operation")
            time.sleep(2)
            clear_console()
            exit()
        else: 
            clear_console()
            print("Program restarted - A fatal error occured: Could not find a valid action")
            time.sleep(2)
            break
