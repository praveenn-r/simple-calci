def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    # Use a try-except block to handle division by zero
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

def get_user_input():
    """Prompts the user for two numbers and an operator."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    while True:
        operator = input("Choose an operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operator. Please choose from +, -, *, /")
    
    return num1, num2, operator

def main():
    """Main function to run the calculator program."""
    print("Welcome to the simple command-line calculator.")
    
    # Get user input for the calculation
    num1, num2, operator = get_user_input()

    # Perform the calculation based on the chosen operator
    result = None
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    
    # Print the result
    if result is not None:
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()

hello praveen this is a pull request