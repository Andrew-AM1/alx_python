#!/usr/bin/python3
def fibonacci_sequence(n):
    if n == 0:
        return []
    sequence = [0, 1]
    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)

    return sequence[:n]