#!/usr/bin/env python3
"""Simple command-line calculator.

Accepts an operator (+, -, *, /) and two numbers from the user and prints the result.
"""

def get_operator():
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in ('+', '-', '*', '/'):
            return op
        print("Invalid operator. Please enter one of: + - * /")


def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            # Accept integers or floats
            if '.' in s or 'e' in s.lower():
                return float(s)
            return int(s)
        except ValueError:
            print("Invalid number. Try again.")


def calculate(op, a, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b


def main():
    print("Simple calculator — type Ctrl+C or Ctrl+D to exit")
    try:
        op = get_operator()
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        try:
            result = calculate(op, a, b)
        except ZeroDivisionError:
            print("Error: division by zero")
            return

        # Format result: show as int when whole, else show float
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(f"Result: {a} {op} {b} = {result}")
        print('\nGoodbye lovely mum!')

    except (EOFError, KeyboardInterrupt):
        print('\n Error detected')


if __name__ == '__main__':
    main()
