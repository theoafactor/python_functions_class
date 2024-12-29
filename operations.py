def operateTwoNumbers(a, b, operation="add"):
    
    if operation == "add":
        result = a + b

        print(result)
    
    elif operation == "subtract":
        result = a - b

        print(result)


def collectNumbers():
    ## collect two numbers from the user
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))

    return [number1, number2]

collectedNumbers = collectNumbers()


operateTwoNumbers(collectedNumbers[0], collectedNumbers[1], "subtract")