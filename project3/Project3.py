import sympy

result = 0.0
f_search = 0
x = 0
num1 = ""
num2 = ""
sym = ""
list_sym = ["+", "-", "*", "/", "!", "^", "%"]##operator symbol
gan = 0
while(1):
    function = input()
    while(1):
        if(function[f_search] in list_sym):
            sym = function[f_search]
            break##find operator
        else:
            f_search +=1

    length = len(function)
    num1 = function[0:f_search]##intercept the first number
    gan = 1 + f_search

    if(length != (f_search +1)):
        num2 = function[gan:length]##intercept the second number

    if(function[f_search] == list_sym[0]):
        result = float(num1) + float(num2)##addition
    if(function[f_search] == list_sym[1]):
        result = float(num1) - float(num2)##subtraction
    elif(function[f_search] == list_sym[2]):
        try:
            result = float(num1) * float(num2)##multiplication
        except OverflowError:
            print("Result too big! Error!")
            result = None
    elif(function[f_search] == list_sym[3]):
        result = float(num1) / float(num2)##division
    elif(function[f_search] == list_sym[4]):
        result = sympy.factorial(float(num1))##factorial
    elif(function[f_search] == list_sym[5]):
        try:
            result = float(num1) ** float(num2)##square
        except OverflowError:
            print("Result too big! Error!")
            result = None
    elif(function[f_search] == list_sym[6]):
        result = float(num1) % float(num2)##division remainder
    if(result !=None):
        print(result)
    else:
        pass
    f_search = 0
    result = 0 
