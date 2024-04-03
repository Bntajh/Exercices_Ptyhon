def yulaw(s: str) -> str:

    result = ''

    for i in s:
   
        if i not in result:
            result += i
    return result

'''test_strings = ['abbcde', 'abbcdde', 'abcdeab', 'GABELAWGABRIELYULAW']
for test in test_strings:
      print(yulaw(test))
'''