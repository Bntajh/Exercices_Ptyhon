from typing import List

def stormtroopers(numbers: List[int]) -> List[int]:
    occurrences = {}
    
    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1
    numbers_list = []
    for number in numbers:
        if occurrences[number] == 1:
            numbers_list.append(number)
    
    return numbers_list


# numbers = [1, 2, 2, 3, 4, 4, 5]
# result = stormtroopers(numbers)
# print(result)
