def yin_yang(s: str) -> bool:
    stack = []
    opening_chars = {'(', '[', '{', '"', "'"}
    closing_chars = {')', ']', '}', '"', "'"}
    matching_pairs = {')': '(', ']': '[', '}': '{', '"': '"', "'": "'"}
    
    for char in s:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if not stack or stack.pop() != matching_pairs[char]:
                return False

    return not stack 
    
'''input_str = "([])"
result = yin_yang(input_str)
print(result)'''