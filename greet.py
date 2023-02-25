names = input('Write some names separated by a space(name name1 name2 etc)\n')

spaces = [x for x, v in enumerate(names) if v == ' ']
spaces.insert(0, 0)
spaces.append(len(names))

for space in range(len(spaces)-1):
    print(f'Hi {names[spaces[space]:spaces[space+1]]}')

namelist = names.split(" ")
for i in range(len(namelist)-1):
    print(f"Hi {namelist[i]}")
