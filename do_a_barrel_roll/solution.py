from typing import List

def do_a_barrel_roll(numbers: List[int], k: int) -> List[int]:
    n = len(numbers)
    k = k % n 

    rotated_array = numbers[k:] + numbers[:k]

    return rotated_array

arr = [0, 1, 2, 3, 4, 5]
k = 3
result = do_a_barrel_roll(arr, k)
print(result)


