from typing import List

def daemon(numbers: List[int], k: int)  -> bool:
    for i in range(len(numbers)):
        if i != k:
            if i < k and numbers[i] >= numbers[k]:
                return False
            elif i > k and numbers[i] <= numbers[k]:
                return False
    return True


# numbers = [100, 97, 101, 109, 111, 110]
# k = 1
# print(daemon(numbers, k))



