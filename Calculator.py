#This is a basic calculator
#Last edited Mon, Sep 12

import os

#Operators needed for printing the answer
Operators = [" + ", " - ", " x ", " / ", " ^ "]
Num_a = None
Num_b = None
Ans = 0

#####################################################################################

def clear_console():
    os.system('clear')

def init(_num_a = None): 
    global Num_a
    global Num_b
    global currentOperation
    global Ans
    #Try is needed because of a value error that occurs when the user enters invalid characters such as letters
    try: 
        #Checking if number A is the answer
        if _num_a != Ans: 
            Num_a = float(input("Input number A - "))
        clear_console()    
        print(f"{str(Num_a)}\n")
        #Inputting the operation
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
        print(f"{Num_a}{Operators[currentOperation - 1]}\n")
        #Inputting the second number
        Num_b = float(input("Input number B - "))
        clear_console()
        print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)}\n")
    #If the values the user entered is not allowed, the program will exit. 
    except ValueError: 
        clear_console()
        print("Program exited - An error occured: The value you entered is not accepted")
        exit()


#####################################################################################


init()
while True:
    #Calculating
    if currentOperation == 1: 
        Ans = Num_a + Num_b
    elif currentOperation == 2:
        Ans = Num_a - Num_b
    elif currentOperation == 3: 
        Ans = Num_a * Num_b
    elif currentOperation == 4:
        try: 
            Ans = Num_a / Num_b
        except ZeroDivisionError: 
            print("Program exited: Could'nt divide by zero")
            exit()
    elif currentOperation == 5: 
        Ans = Num_a ** Num_b
    else: 
        clear_console()
        print("Program exited - An unknown error occured")
        exit()
    #Printing Answer
    clear_console()
    print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}")
    #Repeating Action
    repeatAction = int(input("\nInput the next action - \n[1]Clear \n[2]Continue Operation \n[3]Quit Operation \n"))
    clear_console()
    print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}")
    if repeatAction == 1: 
        Ans = 0
        Num_a = 0
        Num_b = 0
        currentOperation = 0
        clear_console()
        print("Cleared")
        init()
    elif repeatAction == 2: 
        Num_a = Ans
        init(Ans)
    elif repeatAction == 3: 
        clear_console()
        print("Program exited - User terminated operation")
        exit()
    else: 
        clear_console()
        print("Program exited - An error occured: Could not find a valid action")
        exit()
