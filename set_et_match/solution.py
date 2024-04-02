from typing import List

def set_et_match(numbers: List[int], n: int) -> bool:
    seen = set()
    
    for num in numbers:
        complement = n - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False

numbers = [1, 2, 3, 4, 5]
'''target_sum = 9
result = set_et_match(numbers, target_sum)
print(result)'''