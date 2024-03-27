from typing import List

def morning_sunshine(numbers: List[int]) -> List[int]:
    result = []
    max_value = float('-inf')

    for num in reversed(numbers):
        if num > max_value:
            result.append(num)
            max_value = num

    return result[::-1]

'''input_numbers = [5, 4, 3, 2, 1]
output_result = morning_sunshine(input_numbers)
print(output_result)'''
