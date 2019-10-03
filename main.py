import typing as t
import bisect


# O(n * (log(n) + n))
def is_partitionable(numbers: t.List[int]) -> bool:

    if numbers is None:
        return False

    if any(n < 0 for n in numbers):
        raise Exception("Invalid numbers - should be a positive integers")

    if len(numbers) < 2:
        return False

    numbers.sort()

    while len(numbers) > 1:
        first = numbers.pop()
        second = numbers.pop()

        bisect.insort(numbers, first - second)

    return sum(numbers) == 0
