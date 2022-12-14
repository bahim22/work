def fOpen(open_file):
    # open('./data/DelveData.jsonc')
    open_file = open('./dev.env')
    count = 0
    for _ in open_file:
        count += 1
    print('Line Count: ', count)

""" print(len(fOpen.read()))
inp = fOpen.read()
print(len(inp)) """