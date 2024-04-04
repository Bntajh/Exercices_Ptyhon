from typing import List

def daemon(numbers: List[int], k: int) -> bool:
    if not numbers or k < 0 or k >= len(numbers):
        return False  

    pivot = numbers[k]
    

    if all(x == pivot for x in numbers):
        return True
    

    max_avant_k = max((x for x in numbers[:k] if x < pivot), default=pivot)
    

    min_apres_k = min((x for x in numbers[k+1:] if x > pivot), default=pivot)
    
    return max_avant_k < pivot and min_apres_k >= pivot

# test_cases = [
#     ([100, 97, 101, 109, 111, 110], 1), 
#     ([100, 97, 101, 109, 111, 110], 2),
#     ([100, 97, 101, 109, 111, 110], 3), 
#     ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0)  ]


# for numbers, k in test_cases:
#     print(daemon(numbers, k))
