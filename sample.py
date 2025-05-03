# begin sample.py
# This file is to show how we can use the functions defined in exercise.py
# This file is not to be evaluated.

import random


# Import the module containing the functions
import exercise

# Set the random seed
random.seed()


def main():
    # Tests with random numbers
    for _ in range(5):  # Run 5 random tests
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        # Skip division by zero in random tests for now
        if b == 0:
            continue

        print(f"Testing with random numbers: a = {a}, b = {b}")

        # Addition
        result = exercise.add(a, b)
        print(f"  add({a}, {b}) = {result}")

        # Subtraction
        result = exercise.sub(a, b)
        print(f"  sub({a}, {b}) = {result}")

        # Multiplication
        result = exercise.mul(a, b)
        print(f"  mul({a}, {b}) = {result}")

        # Division
        result = exercise.div(a, b)
        print(f"  div({a}, {b}) = {result}")

        print("-----")

    # Divide by zero
    result = exercise.div(a, 0)
    print(f"  div({a}, {0}) = {result}")


if __name__ == "__main__":
    # Lines below are executed only when this file is run directly
    # When this file is imported, the lines below are not executed.
    main()

# end sample.py
