def tux(numbers: list[int]) -> int:
    if len(numbers) == 1:
        return 0

    if not numbers:
        return -1

    n = len(numbers)
    min_num = min(numbers)
    max_num = max(numbers)

    if max_num - min_num + 1 != n:
        return 0
    else:
        for i in range(1, n):
            if min_num + i != numbers[i]:
                return i
    return -1