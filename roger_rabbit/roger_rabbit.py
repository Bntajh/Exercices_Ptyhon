def roger_rabbit(n: int) -> list[str]:
    tab = []
    for i in range(1,n+1):
        binary = bin(i)[2:]
        tab.append(binary)
    return tab


print(roger_rabbit(5))