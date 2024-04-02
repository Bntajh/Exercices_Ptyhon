def open_closed(s: str) -> bool:
    ouvrant = "({<["
    fermant = ")}>]"

    simple_cote = "'"
    double_cote = '"'
    count_simple = 0
    count_double = 0
    count_ouvrant = 0
    count_fermant = 0

    if s == "" or len(s) % 2 != 0:
        return False

    for char in s:
        if char in ouvrant:
            count_ouvrant += ouvrant.index(char) + 1
        elif char in fermant:
            count_fermant += fermant.index(char) + 1
        elif char == simple_cote:
            count_simple += 1
        elif char == double_cote:
            count_double += 1 
        else:
            return False

        if count_ouvrant < count_fermant:
            return False

    if count_ouvrant == count_fermant and count_double % 2 == 0 and count_simple % 2 == 0:
        return True
    else:
        return False

tests = [
    "()",
    "][",
    "([])",
    "(",
    "(()",
    "[(])",
    "[)",
    '""',
    "'\""
]

#for test in tests:
 #   result = open_closed(test)
  #  print(f"result:{test}: {result}")
