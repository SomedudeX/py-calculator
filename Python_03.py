#This is a basic calculator
#Last edited Sep. 11 @ 9:52PM

import os


answer = 0
repeatAction = 0
Operators = [" + ", " - ", " x ", " / ", " ^ "]

#####################################################################################
#                                    FUNCTIONS                                      #
def clear_console():
    os.system('clear')

def OperationCheck(): 
    global currentOperation
    if currentOperation == 1 or currentOperation == 2 or currentOperation == 3 or currentOperation == 4 or currentOperation == 5:
        return
    else: 
        print("Program exited: Could not find a valid operation")

def Calculate(): 
    global currentOperation
    global answer
    if currentOperation == 1: 
        answer = num_a + num_b
    elif currentOperation == 2:
        answer = num_a - num_b
    elif currentOperation == 3: 
        answer = num_a * num_b
    elif currentOperation == 4:
        try: 
            answer = num_a / num_b
        except ZeroDivisionError: 
            print("Program exited: Could'nt divide by zero")
            exit()
    elif currentOperation == 5: 
        answer = num_a ** num_b
    else: 
        print("Program exited: Couldn't decide which operation to use")
        exit()

def repeatCaculation(): 
    global repeatAction
    global currentOperation
    global num_a
    global num_b
    repeatAction = int(input("Input the next action - \n[1]Continue Operation \n[2]Quit Operation \n"))
    clear_console()
    if repeatAction == 2: 
        print("Program exited: User terminated operation")
        exit()
    elif repeatAction == 1: 
        num_a = answer
        print(f"Answer - {answer}")
        try: 
            num_b = int(input("Input number B - "))
        except ValueError: 
            clear_console()
            print("Program exited: The value you entered is not accepted")
            exit()
        currentOperation = int(input("Input Operation - \n[1] addition \n[2] subtraction \n[3] multiplication \n[4] division \n[5] exponent \n"))
        clear_console()
    else: 
        print("Program exited: Could not find a valid action")
        exit()

#                                     FUNCTIONS                                     #
#####################################################################################
#                                   START OF CODE                                   #



try: 
    num_a = int(input("Input number A - "))
    num_b = int(input("Input number B - "))
except ValueError: 
    clear_console()
    print("Program exited: The value you entered is not accepted")
    exit()

currentOperation = int(input("Input Operation - \n[1] addition \n[2] subtraction \n[3] multiplication \n[4] division \n[5] exponent \n"))
clear_console()

while True:
    OperationCheck()
    Calculate()
    print(f"{num_a}{Operators[currentOperation - 1]}{num_b} = {answer}\n")
    repeatCaculation()
