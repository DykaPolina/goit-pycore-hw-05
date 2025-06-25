from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a function that computes Fibonacci numbers using recursion with caching.

    :return: A function that calculates the nth Fibonacci number with memoization.
    """
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")

        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    try:
        print(fib(10))
        print(fib(15))
    except ValueError as e:
        print(f"[ERROR] {e}")
