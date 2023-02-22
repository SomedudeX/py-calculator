#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

#This is a basic calculator
#Last edited Sat, Oct 1
#By Zichen

import os;
import sys;
import time; 
import webbrowser; 

from Functions.Addition import *;
from math import sqrt; 

#Error needed to print error type
Error = "an unknown fatal error";
#Error Number needed to print error line
Er_Number = 0
#Operators needed for printing the answer
Operators = [" + ", " - ", " x ", " / ", " ^ ", "√"];
#History needed for printing the history, as a list
History = [];
#Repeat Action needed for repeating the calculator. Declare here unless you want errors
repeatAction = None
#Square Root needed for square roots
isSquareRoot = False;
#Operations needed for calculating
currentOperation = None;
#Number needed for, well the basics of calculator
Num_a = None;
#Number needed for the basics of calculator
Num_b = None;
#Answers that is not currently populated
Ans = 0;

#####################################################################################

def easter_egg(args = None): 
    """Rick Astley simulator at rickastleysim.com/dQw4w9WgXcq. 
       Use empty arguments to crash the program"""
    clear_console();
    #Printing the ASCII Art
    print("\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀");
    time.sleep(1.65);
    #Opening the rickroll
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
    input("\nPress enter to continue...");
    #Crashing the program if arguments are empty
    if args == None: 
        int("a")
    else: 
        return

def clear_console():
    """Clearing the console"""
    os.system('clear');

def invalidInput(_variable = "", _compare = "",  type = "str", question = "Press enter to continue", length = None): 
    """Re-asking the user to input if they inputted an unsupported value. 
       Usage: 1 - Variable to be checked, 2 - Values to compare the variable to, 3 - Type of variable, 4 - String to display to the user, 5 - Desired length of variable (optional)
       
       Supported types of variable: int, float, str"""
    global Error
    #While the variable does not satisfy the requirements, keep on running
    while True: 
        #Casting the variable into a string to compare it against the requirements
        _variable = str(_variable);
        _compare = str(_compare);
        variable = [];
        compare = [];
        for i in range(len(_variable)): 
            variable.append(_variable[i]);
        for i in range(len(_compare)): 
            compare.append(_compare[i]);
        for i in range(len(variable)): 
            if variable[i] not in compare: 
                clear_console()
                try: 
                    if type == "int": 
                        variable = int(input(question));
                    elif type == "float": 
                        variable = float(input(question));
                    elif type == "str": 
                        variable = str(input(question));
                    else: 
                        Error = "No type given at invalidInput"
                        print(f"FATAL ERROR \n\nProgram error: {Error}");
                        input("Press enter to continue...");
                        sys.exit(1)
                    temp = str(variable)
                    for i in range(len(temp)): 
                        if temp[i] not in compare: 
                            int("a")
                        if length != None and len(temp) != length: 
                            int("a")
                except: 
                    break;
                else: 
                    return variable;

def init(_num_a = None): 
    """Asking the user the operation as well as the number and checking that those are valid etc. """
    global Error
    global Er_Number
    global Num_a;
    global Num_b;
    global currentOperation;
    global isSquareRoot;
    global Ans;
    #Try is needed because of a value error that occurs when the user enters invalid characters such as letters
    try: 
        #Checking if it's the second time running the look (if number A is the answer)
        if _num_a != Ans: 
            try: 
                Num_a = float(input("0.0 \n\nInput number A: "));
                #If the user input is invalid, run invalidInput
            except: 
                Num_a = invalidInput(Num_a, "1234567890.", "float", "0.0 \n\nPlease input a valid value: ");
        #Printing everything
        clear_console();
        print(f"{str(Num_a)}\n");
        #User inputting the operation 
        try: 
            currentOperation = int(input("Please specify which operations you want to perform: \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n[6]Root \n"));
        #If the operation the user inputted is invalid, it asks the user to input a new valid value
        except:
            currentOperation = invalidInput(currentOperation, "123456", "int", f"{str(Num_a)} \n\nPlease input a valid value: \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n[6]Root \n", 1);
        #If user entered square root, return. 
        else: 
            if currentOperation not in [1, 2, 3, 4, 5, 6] or len(str(currentOperation)) != 1: 
                while currentOperation not in [1, 2, 3, 4, 5, 6] or len(str(currentOperation)) != 1: 
                    currentOperation = invalidInput(currentOperation, "123456", "int", f"{str(Num_a)} \n\nPlease input a valid value: \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n[6]Root \n", 1);
        finally: 
            if currentOperation == 6: 
                isSquareRoot = True;
                return;
        #Printing the inputs
        clear_console();
        print(f"{Num_a}{Operators[currentOperation - 1]}\n");
        #Inputting the second number
        try: 
            Num_b = float(input("Input number B: "));
        #Checking if user input is valid
        except: 
            Num_b = invalidInput(Num_b, "1234567890.", "float", f"{Num_a}{Operators[currentOperation - 1]} \n\nPlease input a valid value: ", None);
        finally: 
            #Checking if there is a zero division error
            while currentOperation == 4 and Num_b == 0: 
                Num_b = "a"
                Num_b = invalidInput(Num_b, "1234567890.", "float", f"{Num_a}{Operators[currentOperation - 1]} \n\nPlease input a valid value: ", None);
        #Printing the inputs
        clear_console();
        print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)}");
    #Any errors will get caught here (really, there should be no errors unless something really happens)
    except Exception as e: 
        clear_console();
        Er_Number = sys.exc_info()[-1].tb_lineno
        Error = str(e)
        currentOperation = 7;
        return;

#####################################################################################

#Start of program
clear_console();
print("You are currently running Python", sys.version);
print("Welcome and thank you for using Python Calculator");

input("\nYou are currently running an experimental version, which is highly unstable. Press enter to confirm...")
#time.sleep(1.65)

while True: 
    #Initializing and resetting
    clear_console();
    init();
    while True:
        #Looping the calculator until the user closes the application
        #Calculating the inputs the user gave
        if currentOperation == 1: 
            #Addition
            Ans = Addition(Num_a, Num_b)
            Ans = round(Ans,8);
        elif currentOperation == 2:
            #Subtraction
            Ans = Num_a - Num_b;
            Ans = round(Ans, 8);
        elif currentOperation == 3: 
            #Multiplication
            Ans = Num_a * Num_b;
            Ans = round(Ans, 8);
        elif currentOperation == 4:
            #Division
            try: 
                Ans = Num_a / Num_b;
                round(Ans,8);
            except ZeroDivisionError: 
                #Restart the program if the user tries to divide by zero. 
                clear_console();
                print(f"ERROR \n\nProgram error: Couldn't divide by zero");
                input("Press enter to continue...");
                break;
        elif currentOperation == 5: 
            #Exponents
            Ans = Num_a ** Num_b;
            Ans = round(Ans,8);
        elif currentOperation == 6: 
            #Square Root
            Ans = sqrt(Num_a);
            Ans = round(Ans, 8);
        elif currentOperation == 7: 
            #If there's an error during the input phase, it will catch them here
            clear_console();
            print(f"ERROR \n\nProgram error: {Error.capitalize()}");
            input("Press enter to continue...");
            Error = "An unknown error";
            break
        else: 
            clear_console();
            print(f"\nERROR \n\nProgram error: {Error.capitalize()}");
            input("Press enter to continue...");
            Error = "An unknown error";
            break;
        #Printing Answer
        clear_console();
        if isSquareRoot: 
            print(f"{Operators[5]}{Num_a} = {Ans}");
            History.append(f"{Operators[5]}{Num_a} = {Ans}");
        else: 
            print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}");
            History.append(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}");
        #Deleting the earliest history if history exceeds 5
        while len(History) > 5:
            del History[0]; 
        #If the operation the user inputted is invalid, it asks the user to input a new valid value
        try: 
            repeatAction = int(input("\nInput the next action: \n[1]Clear Operation \n[2]Continue Operation \n[3]View History \n[4]Quit \n"));
            if repeatAction == 69: easter_egg();
        except: 
            repeatAction = invalidInput(repeatAction, "1234", "int", f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans} \n\nPlease input a valid value: \n[1]Clear Operation \n[2]Continue Operation \n[3]View History \n[4]Quit \n", 1)
        else:
            if len(str(repeatAction)) != 1 or repeatAction not in [1, 2, 3, 4]: 
                while len(str(repeatAction)) != 1 or repeatAction not in [1, 2, 3, 4]: 
                    repeatAction = invalidInput(repeatAction, "1234", "int", f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans} \n\nPlease input a valid value: \n[1]Clear Operation \n[2]Continue Operation \n[3]View History \n[4]Quit \n", 1)
        finally:
            if isSquareRoot: 
                print(f"{Operators[5]}{Num_a} = {Ans}");
            else: 
                print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}");
        #If the user clears the calculator
        if repeatAction == 1: 
            #Clearing variables
            Ans = 0
            Num_a = 0
            Num_b = 0
            currentOperation = 0
            isSquareRoot = False
            #Clearing console
            clear_console()
            #Reinitializing
            init()
            #If an error occured, restart (break this loop)
            if currentOperation == 7: 
                clear_console()
                print(f"ERROR \n\nProgram error: {Error.capitalize()} [{Er_Number}]")
                input("Press enter to continue...")
                Error = "An unknown error";
                break
        elif repeatAction == 2: 
            Num_a = Ans
            isSquareRoot = False
            init(Ans)
            #If an error occured, restart (break this loop)
            if currentOperation == 7: 
                clear_console()
                print(f"ERROR \n\nProgram error: {Error.capitalize()} [{Er_Number}]")
                input("Press enter to continue...")
                Error = "An unknown error";
                break
        elif repeatAction == 3: 
            isSquareRoot = False
            clear_console()
            print("HISTORY")
            print(*History, sep = "\n")
            input("\nPress enter to continue...")
            break
        elif repeatAction == 4: 
            clear_console()
            if isSquareRoot: 
                print(f"{Operators[5]}{Num_a} = {Ans}");
            else: 
                print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}");
            print("\nProgram exited: User terminated operation")
            time.sleep(1.65)
            clear_console()
            sys.exit(0)
        else: 
            clear_console()
            if isSquareRoot: 
                print(f"{Operators[5]}{Num_a} = {Ans}");
            else: 
                print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans}");
            print(f"\nProgram restarted: {Error.capitalize()}")
            input("Press enter to continue...")
            Error = "An unknown error";
            break
