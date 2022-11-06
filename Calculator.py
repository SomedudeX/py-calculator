# This Python file uses the following encoding: utf-8

#This is a basic calculator
#Last edited Sat, Oct 1
#By Zichen

import os;
import sys;
import time;
import webbrowser;
from math import sqrt;
from inspect import currentframe;

#Error needed to print error type
Error = "An unknown fatal error";
#Operators needed for printing the answer
Operators = [" + ", " - ", " x ", " / ", " ^ ", "√"];
#History needed for printing the history, as a list
History = [];
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

#Getting line number for debug
def get_linenumber():
    cf = currentframe();
    return cf.f_back.f_lineno;

#Clearing the console
def clear_console():
    os.system('clear');

#Re-asking the user to input if they inputted a wrong value. Don't ask how it works, I had a hard time trying to get it work. 
#Make sure that you include the variable, the compare, and the type exactly as it is, otherwise it will NOT work. 
def invalidInput(_variable = "", _compare = "", question = "Press enter to continue", type = "str", length = None, special = 0): 
    global Error
    while True: 
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
                        variable = int(input(question));
                    elif type == "str": 
                        variable = int(input(question));
                    else: 
                        print(f"Program error: {Error} [{get_linenumber()}]");
                        input("Press enter to continue...");
                    temp = str(variable)
                    for i in range(len(temp)): 
                        if temp[i] not in compare: 
                            int("a")
                        if length != None and len(temp) != length: 
                            int("a")
                    if special == 1 and currentOperation == 4 and variable == 0: 
                        int("a")
                except: 
                    break;
                else:
                    return variable;

#Rick Astley simulator at rickastleysim.com/dQw4w9WgXcq
def easter_egg(): 
        clear_console();
        print("\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀");
        time.sleep(2);
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
        input("\nPress enter to continue...");

#Init: Asking the user the operation as well as the number and checking that those are valid etc. 
def init(_num_a = None): 
    global Error;
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
                Num_a = invalidInput(Num_a, "1234567890.", "0.0 \n\nPlease input a valid value: ", "float");
        #Printing everything
        clear_console();
        print(f"{str(Num_a)}\n");
        #User inputting the operation 
        try: 
            currentOperation = int(input("Please specify which operations you want to perform: \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n[6]Root \n"));
        #If the operation the user inputted is invalid, it asks the user to input a new valid value
        except:
            currentOperation = invalidInput(currentOperation, "123456", f"{str(Num_a)} \n\nPlease input a valid value: \n[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exponent \n[6]Root \n", "int", 1);
        #If user entered square root, return. 
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
            Num_b = invalidInput(Num_b, "1234567890.", f"{Num_a}{Operators[currentOperation - 1]} \n\nPlease input a valid value: ", "float", None, 1);
        finally: 
            #Checking if there is a zero division error
            if currentOperation == 4 and Num_b == 0: 
                Num_b = invalidInput(Num_b, "1234567890.", f"{Num_a}{Operators[currentOperation - 1]} \n\nPlease input a valid value: ", "float", None, 1);
        #Printing the inputs
        clear_console();
        print(f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)}");
    #Any errors will get caught here (really, there should be no errors unless something really happens)
    except Exception as e: 
        clear_console();
        Error = e;
        currentOperation = 7;
        return;

#####################################################################################

#Start of program
clear_console();
print("You are currently running Python", sys.version);
print("Welcome and thank you for using Calculator.py");
time.sleep(1.65);

while True: 
    #Initializing and resetting
    clear_console();
    init();
    while True:
        #Looping the calculator until the user closes the application
        #Calculating the inputs the user gave
        if currentOperation == 1: 
            #Addition
            Ans = Num_a + Num_b
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
                print(f"ERROR \n\nProgram error: Couldn't divide by zero [{get_linenumber()}]");
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
            print(f"Program error: {Error} [{get_linenumber()}]");
            input("Press enter to continue...");
            Error = "An unknown fatal error";
            break
        else: 
            clear_console();
            print(f"\nProgram error: {Error} [{get_linenumber()}]");
            input("Press enter to continue...");
            Error = "An unknown fatal error";
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
            repeatAction = invalidInput(repeatAction, "1234", f"{str(Num_a)}{Operators[currentOperation - 1]}{str(Num_b)} = {Ans} \n\nPlease input a valid value: \n\n[1]Clear Operation \n[2]Continue Operation \n[3]View History \n[4]Quit \n", "int", 1)
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
                print(f"Program error: {Error} [{get_linenumber()}]")
                input("Press enter to continue...")
                Error = "An unknown fatal error";
                break
        elif repeatAction == 2: 
            Num_a = Ans
            isSquareRoot = False
            init(Ans)
            #If an error occured, restart (break this loop)
            if currentOperation == 7: 
                clear_console()
                print(f"Program error: {Error} [{get_linenumber()}]")
                input("Press enter to continue...")
                Error = "An unknown fatal error";
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
            print("Program exited: User terminated operation")
            time.sleep(2.5)
            clear_console()
            exit()
        else: 
            clear_console()
            print(f"Program restarted: {Error} [{get_linenumber()}]")
            input("Press enter to continue...")
            Error = "An unknown fatal error";
            break