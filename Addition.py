def floatConvert(x): 
    if isinstance(x, int): 
        return int(x)
    global fl
    fl = False
    x = str(x)
    for i in range(len(x)): 
        if x[i] == ".": 
            fl = True
        elif fl and x[i] != "0": 
            return float(x)
        elif fl and x[i] == "0" and i + 1 == len(x): 
            fl = False
            x = float(x)
            return int(x)

def Addition(_a, _b): 
    global a
    global b
    a = []
    b = []
    #Convert a and b into integeres (if possible)
    _a = floatConvert(_a)
    _b = floatConvert(_b)
    #If either a or b is a float after the conversion, cancel the operation (does not support float currently)
    if isinstance(_a, float) or isinstance(_b, float): 
        return _a + _b
    #If both a and b is an integer, continue
    else: 
        #Converting the inputs so as to subscript them in line 37 and 39 in order to put them in a list
        _a = str(_a)
        _b = str(_b)
        #Converting a and b from a number into a list
        for i in range(len(_a)): 
            a.append(int(_a[i]))
        for i in range(len(_b)): 
            b.append(int(_b[i]))
        #Converting the numbers into the same place value
        if len(a) != len(b): 
            #If a has more digits than b, then add 0s in front of b to equilize the place values
            if len(a) > len(b): 
                for i in range(len(a) - len(b)): 
                    b.insert(0, 0)
            #If b has more digits than a, then add 0s in front of a to equilize the place values
            else: 
                for i in range(len(b) - len(a)): 
                    a.insert(0, 0)
        #Adding the numbers
        for i in range(len(a) - 1, -1, -1): 
            #If the digits carry, then add 1 to the next digit
            if a[len(a) - 1] + b[i] >= 10: 
                #If it is already the leftmost digit, add to the digit
                if i == 0: 
                    a.insert(0, a[len(a) - 1] + b[i])
                #If it's not the left most digit, subtract 10 from the current digit and add 1 to the next digit (carry)
                else: 
                    a.insert(0, a[len(a) - 1] + b[i] - 10); 
                    a[len(a) - 2] += 1; 
            #Else do not add to the next digit and continue with the operation
            else: 
                a.insert(0, a[len(a) - 1] + b[i]); 
            del a[len(a) - 1]
        #Converting list back into integer and returning it
        for i in range(len(a)): 
            lst = a
            s = [str(i) for i in lst]
            s = "".join(s)
            return int(s)