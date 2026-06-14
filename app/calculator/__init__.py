from app.operations import Operations
from app.calculation import CalculationFactory

def calculator() -> None:
    """
    Runs an interactive calculator REPL (Read-Eval-Print Loop).

    Prompts the user to enter an operation and two numbers in the format
    <operation> <a> <b>, computes the result, and prints it. Continues
    until the user types 'exit'.

    Supported operations:
        - add: Adds a and b.
        - subtract: Subtracts b from a.
        - multiply: Multiplies a and b.
        - divide: Divides a by b.

    Raises:
        ZeroDivisionError: If divide is used and b is zero (handled internally).
        ValueError: If the input format is invalid (handled internally).

    Example:
        >>> calculator()
        Enter an operation and two numbers, or 'exit' to quit: add 5 3
        Result: 8.0
    """
    print("Welcome to the calculator REPL. Type 'exit' to quit.")
    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")
        user_input = user_input.lower()
        if user_input == "exit":
            print("Exiting calculator... Goodbye ~")
            break

        try:
            operation, a, b = user_input.split()
            a, b = float(a), float(b)
        except ValueError:
            print("Invalid input. Please follow <operation> <a> <b> syntax.")
            continue

        try:
            calculation = CalculationFactory.build_calculation(operation, a, b)
            print(f"Result: {calculation.execute()}")
        except ValueError as err:
            print(err)
            continue
        except ZeroDivisionError as err:
            print(err)
            continue
        