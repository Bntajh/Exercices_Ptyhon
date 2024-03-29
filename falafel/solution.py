def falafel (s: str) -> bool:
    if len(s) <= 1:
        return True

    char_count = {}
    middle = len(s) // 2

    for i in range(middle):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1

    for j in range(middle, len(s)):
        if s[j] in char_count:
            char_count[s[j]] -= 1
            if char_count[s[j]] == 0:
                del char_count[s[j]]
        if len(char_count) > 1:
            return False

    return True