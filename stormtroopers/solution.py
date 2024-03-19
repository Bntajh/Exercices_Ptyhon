from typing import List

def stormtroopers(numbers: List[int]) -> List[int]:
    result = []
    
    for number in numbers:
        if number not in result:
            result.append(number)
    
    return result

numbers = [1, 2, 2, 3, 4, 4, 9]
result = stormtroopers(numbers)

print(result)
