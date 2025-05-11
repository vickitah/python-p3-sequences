#!/usr/bin/env python3


def print_fibonacci(length):
    """
    Generates and prints a Fibonacci sequence of the given length.
    """
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    fibonacci_sequence = [0, 1]
    for _ in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    print(fibonacci_sequence)