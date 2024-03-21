def roger_rabbit(n: int) -> list[str]:
    tab = []
    for i in range(1, n + 1):
        binary = ""
        while i > 0:
            binary = str(i % 2) + binary
            i //= 2
        tab.append(binary)
    return tab

# print(roger_rabbit(5))