import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Yields all valid floating-point numbers from the given text.

    :param text: Input string containing numbers and text.
    :yield: Floating-point numbers found in the text.
    :raises ValueError: If input is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    for match in re.findall(r"\s(\d+\.\d+)\s", f" {text} "):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the total profit from text using a generator function.

    :param text: Input string containing income numbers.
    :param func: A function that extracts numbers from the text.
    :return: Sum of all numbers returned by the generator.
    :raises ValueError: If func is not callable.
    """
    if not callable(func):
        raise ValueError("Provided func argument must be callable.")

    return round(sum(func(text)), 2)


if __name__ == "__main__":
    test_cases = [
        "Ваш прибуток склав 100.50 і 200.75 у липні.",
        "Оклад: 123.45 ",
        " Зарплата  77.77  бонус 88.88  ",
        "Жодних доходів цього місяця не було.",
        " 99.99 ",

        12345,  # not a string
        "Отримано 500, але ще не 1000",  # no float
        "зарплата 123. і 456.7.8",  # malformed
        "дохід:100.50премія:200.25",  # no space

        "123.45 123.45",
        "Отримано 1000000000.99",
    ]

    for i, text in enumerate(test_cases, 1):
        print(f"\n[Test case #{i}]")
        try:
            total_income = sum_profit(text, generator_numbers)
            print(f"Загальний дохід: {total_income}")
        except ValueError as e:
            print(f"[ERROR] {e}")

    print("\n[Test case #func-not-callable]")
    try:
        sum_profit("якийсь текст", "not_a_function")
    except ValueError as e:
        print(f"[ERROR] {e}")
