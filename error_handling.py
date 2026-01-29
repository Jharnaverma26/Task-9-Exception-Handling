import logging

# Logging configuration
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Division by zero error")
        print("Error: Cannot divide by zero")
    except TypeError:
        logging.error("Invalid input type")
        print("Error: Please enter numbers only")
    else:
        print("Result:", result)
    finally:
        print("Calculation completed")

# Main program
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    divide_numbers(x, y)
except ValueError:
    logging.error("User entered non-integer value")
    print("Error: Invalid input! Enter integers only.")