def tux(numbers: list[int]) -> int:
    longueur_n = len(numbers)

    if longueur_n == 0:
        return -1

    if longueur_n == 1:
        return 0

    max_val = numbers[0]
    max_index = 0

    for i in range(1, longueur_n):
        if numbers[i] > max_val:
            max_val = numbers[i]
            max_index = i

    if max_index == 0:
        return max_index

    if max_index == longueur_n - 1:
        if max_val > numbers[longueur_n - 2]:
            return max_index
        else:
            return -1

    min_val = max_val
    for i in range(max_index - 1, -1, -1):
        min_val = min(min_val, numbers[i])

    if max_val > min_val:
        return max_index

    min_val = max_val
    for i in range(max_index + 1, longueur_n):
        min_val = min(min_val, numbers[i])

    return max_index if max_val > min_val else -1



num = [0, 1, -1]
print(tux(num))