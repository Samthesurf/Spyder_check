# objective is to create the time's table
i = 0
n = True
numbers = range(1, 13)
while n:
    i += 1
    if i == 13:
        n = False
    print(f"\033[4m{i} times table\033[0m\n")
    for x in numbers:
        print(f'{i} x {x} = {i*x}')
    print()
