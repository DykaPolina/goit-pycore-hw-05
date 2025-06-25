# goit-pycore-hw-05

Each task demonstrates a different Python concept, including decorators, recursion with caching, generator functions, and log file parsing.

## Project Structure

- `assistant_error_handling_4.py` — Console assistant bot for managing contacts with input error handling using a custom `@input_error` decorator.
- `caching_fibonacci_1.py` — Recursive Fibonacci number generator with caching using closures.
- `log_analyzer_3.py` — Command-line log analyzer that parses a `.log` file, counts log levels, and optionally displays logs of a specific level.
- `sum_profit_2.py` — Parses text and extracts floating-point numbers using generators and regular expressions; sums them with input validation.
- `test.log` — Sample log file used for testing the analyzer.

## Usage

Run each script from the command line:

```bash
python3 assistant_error_handling_4.py
python3 caching_fibonacci_1.py
python3 sum_profit_2.py
python3 log_analyzer_3.py test.log
python3 log_analyzer_3.py test.log error    # Optional: filter by log level
````

You can provide a second argument to `log_analyzer_3.py` to filter logs by level (`INFO`, `DEBUG`, `WARNING`, `ERROR`).

