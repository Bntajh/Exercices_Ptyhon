from typing import List

def daemon(numbers: List[int], k: int) -> bool:
    pivot = numbers[k]
    left = all(numbers[i] <= pivot for i in range(k))
    right = all(numbers[i] >= pivot for i in range(k + 1, len(numbers)))
    return left and right



# numbers = [100, 97, 101, 109, 111, 110]
# k = 3
# print(daemon(numbers, k))



