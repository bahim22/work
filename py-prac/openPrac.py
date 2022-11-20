fOpen = open('./data/DelveData.jsonc')

count = 0

for _ in fOpen:
    count += 1
print('Line Count: ', count)

""" print(len(fOpen.read()))
inp = fOpen.read()
print(len(inp)) """