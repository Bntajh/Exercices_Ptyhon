from typing import List

def daemon(numbers: List[int], k: int) -> bool:
    if not numbers or k < 0 or k >= len(numbers):
        return False  
    pivot = numbers[k]
    max_avant_k = max(numbers[:k], default=pivot)
    min_apres_k = min(numbers[k+1:], default=pivot)
    
    return max_avant_k < pivot and min_apres_k >= pivot


#test = [
 #   ([100, 97, 101, 109, 111, 110], 1), 
  #  ([100, 97, 101, 109, 111, 110], 2),  
  #  ([100, 97, 101, 109, 111, 110], 3)  
#]

#for numbers, k in test:
#    print(daemon(numbers, k))
