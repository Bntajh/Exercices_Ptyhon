from typing import List

def daemon(numbers: List[int], k: int) -> bool:
    if k < 0 or k >= len(numbers):
        return False

    for i in range(len(numbers)):
        if i != k:
            if k < i and numbers[k] > numbers[i]:
                return False
            if k > i and numbers[k] < numbers[i]:
                return False
    return True

# numbers = [100, 97, 101, 109, 111, 110]
# k = 3
# print(daemon(numbers, k))



