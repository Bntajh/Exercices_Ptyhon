from typing import List

def daemon(numbers: List[int], k: int) -> bool:
    pivot = numbers[k]
    left = all(num <= pivot for num in numbers[:k])
    right = all(num >= pivot for num in numbers[k + 1:])
    return left and right




# numbers = [100, 97, 101, 109, 111, 110]
# k = 3
# print(daemon(numbers, k))



