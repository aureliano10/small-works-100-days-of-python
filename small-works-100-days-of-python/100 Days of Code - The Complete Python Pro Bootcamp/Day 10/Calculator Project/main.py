from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

#print(operations["*"]( 8, 2))
calculator = True
result = 0
while calculator:
    print(logo)
    number1 = float(input("Type first number\n"))
    same_number = True
    while same_number:
        for symbols in operations:
            print(symbols)
        operation_choice = input("choose operation\n")
        number2 = float(input("Type your second number\n"))
        result = operations[operation_choice](number1, number2)
        print(f"The result of your operation is {number2} {operation_choice} {number2} = {result}")
        choose_same_number = input("if you want use same number type 'yes'\nif you want choose first number type 'no'\n").lower()
        if choose_same_number == "no":
            same_number = False
            print("\n" * 20)
        number1 = result