# %%
d11, d22, d33 = {1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}
print(d11, d22, d33)

# %%
d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}
d4 = {}

for x in (d1, d2, d3):
    d4.update(x)
print(d4)

# %%


def lister2(r1, r2):
    return [item for item in range(r1, r2+1)]


# %%
r1, r2 = 0, 10

# %%
print(lister2(r1, r2))

# %%


def lister4(r1, r2):
    return list(range(r1, r2+1))


def lister2(r1, r2):
    return [item for item in range(r1, r2+1)]


# %%
r1, r2 = 0, 10
print(lister4(r1, r2))
