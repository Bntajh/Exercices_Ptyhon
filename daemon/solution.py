def daemon(numbers, k):
    if k < 0 or k >= len(numbers):
        return False

    for i in range(len(numbers)):
        if i < k and numbers[i] >= numbers[k]:
            return False

        if i > k and numbers[i] < numbers[k]:
            return False

    return True
# numbers = [100, 97, 101, 109, 111, 110]
# k = 2
# print(daemon(numbers, k))  
