def tux(numbers: list[int]) -> int:
    if not numbers:
        return -1

    n = len(numbers)
    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num + 1
    count_num = [0] * range_num
    pos_num = [-1] * n

    for i in range(n):
        count_num[numbers[i] - min_num] += 1

    for i in range(1, range_num):
        count_num[i] += count_num[i - 1]

    for i in range(n - 1, -1, -1):
        count_num[numbers[i] - min_num] -= 1
        pos_num[count_num[numbers[i] - min_num]] = numbers[i]

    for i in range(n):
        if pos_num[i] > numbers[i]:
            return i

    return -1
