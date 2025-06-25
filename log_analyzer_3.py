import sys
from typing import List, Dict
from collections import Counter


def parse_log_line(line: str) -> dict:
    """
    Parses a single log line into its components.

    :param line: A line from the log file.
    :return: A dictionary with 'date', 'time', 'level', 'message'.
    """
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3],
    }


def load_logs(file_path: str) -> List[dict]:
    """
    Loads and parses log entries from a file.

    :param file_path: Path to the log file.
    :return: A list of log entries as dictionaries.
    """
    logs = []
    try:
        with open(file_path, encoding="utf-8") as file:
            return list(filter(None, map(parse_log_line, file)))
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to load logs: {e}")
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Filters logs by the given level.

    :param logs: List of log entries.
    :param level: Log level to filter by (e.g., "ERROR").
    :return: Filtered list of logs.
    """
    level = level.upper()
    return list(filter(lambda log: log.get("level") == level, logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    return dict(Counter(log["level"] for log in logs if log.get("level")))


def display_log_counts(counts: dict) -> None:
    """
    Displays log counts in a well-formatted table.
    """
    header_level = "Рівень логування"
    header_count = "Кількість"

    print(f"\n{header_level:<20} | {header_count:>8}")
    print("-" * 20 + "-+-" + "-" * 9)

    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level:<20} | {counts.get(level, 0):>8}")



def display_logs(logs: List[dict], level: str) -> None:
    """
    Displays detailed log messages for a specific level.

    :param logs: List of log entries.
    :param level: Log level to display.
    """
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py /шлях/до/лог_файлу.log [рівень_логування]")
        return

    file_path = sys.argv[1]
    level_arg = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_arg:
        filtered_logs = filter_logs_by_level(logs, level_arg)
        if filtered_logs:
            display_logs(filtered_logs, level_arg)
        else:
            print(f"\nНемає записів рівня '{level_arg.upper()}'.")


if __name__ == "__main__":
    main()