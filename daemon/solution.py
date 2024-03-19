from typing import List

def daemon(numbers: List[int], k: int)  -> bool:

    left = 0
    right = len(numbers) - 1

    while  left < k:
        if numbers [left] > numbers[k]:
            return False
        left += 1
    while  right > k:
        if numbers[right] < numbers[k]:
            return False
        right -= 1
    return True

numbers = [100, 97, 101, 109, 111, 110]
print(daemon(numbers, 3))
