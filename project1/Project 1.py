def calculate():
    num1 = input("First Number:\n")
    operator = input("Operator (+,-,*,/):\n")
    num2 = input("Second Number:\n")

    num1 = float(num1)
    num2 = float(num2)

    out = None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2


    print("The calculation result is " + str(result))


    return play_again()
def play_again():
    while True:
        again = input("Thank you for using this calculator, would you like to calculate again? y or n: ")
        if again not in {"y","n"}:
            print("Error, Try again!")
        elif again == "y":
            return calculate()
        elif again == "n":
            print("Thank you, bye!")
            break
calculate()

