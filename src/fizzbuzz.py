import sys
from typing import Iterable, Iterator


def parse_cli(argv: list[str]) -> range:
    try:
        start, stop = int(argv[1]), int(argv[2])
    except IndexError:
        sys.exit("usage: python fizzbuzz <start> <stop>")
    except ValueError:
        sys.exit("error: start and stop must be integers")

    step = 1 if start < stop else -1

    return range(start, stop + step, step)


def fizzbuzz(numbers: Iterable[int]) -> Iterator[str]:
    for number in numbers:
        fizz = "fizz" if number % 3 == 0 else ""
        buzz = "buzz" if number % 5 == 0 else ""
        yield f"{fizz}{buzz}" or f"{number}"


def main(argv: list[str]) -> None:
    numbers = parse_cli(argv)
    results = fizzbuzz(numbers)
    print(*results)


if __name__ == "__main__":
    main(sys.argv)
