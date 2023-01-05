# %%
import random as rd
import random
a_l1 = ['a', 'e', 'i']
print(a_l1)

# %%
a_l1 += ['vet', 'dog']
print(a_l1)


# %%
a_l = a_l1
a_l += ['vet', 'dog']


def str_add():
    print(a_l)


str_add()


# %%
sorted({
    1: 'D', 2: 'B', 3: 'B', 4: 'K', 5: 'A'
})

# sorted

# %%
sorted("One flew over the".split(), key=str.lower)

# %%
staffTuples = [
    ('hima', 'front', 30),
    ('adam', 'front', 10),
    ('hickory', 'side', 20),
]

sorted(staffTuples, key=lambda staff: staff[2])

# %% [markdown]
# Return a new list containing all items from the iterable in ascending order.

# list.sort() method is only for lists, sorted() function accepts any iterable

# %%
sorted([5, 2, 3, 1, 4])
a = [5, 2, 3, 1, 4]
a.sort()
a

# %%
random.choice(a)

# %%
a += [22]
print(a)

# %%

for _ in range(10):
    x = rd.random()
    print(x)

# %%
a = rd.randint(22, 50)


b = [7, 8, 9, 12, 3]
b.sort(reverse=True)
b

# %%
# b.append([13,15])
# b.extend((18,19))
b.append((18, 19))
b

# %%
del (b[0])
b

# %%
b.sort
b

# %%
del (b[3][1])
b

# %%
aa = b
aa

# %%
aa == b

# %%
aa

# %%
# sorted([aa], reverse=True)
del (aa[3])
# sorted(aa)
aa

# %%
sorted(a, reverse=True)


# %%
a.sort()
a

# %%
len(a)

# %%
ha = 'Hima Balde\''
hha = "Hima Balde'"

print('''\
    Topic: Python
    height:"6 ' 3"
    height:6 \' 3
    version = 3.10
    Date: Oct. 06
''' + ha)

# %%
if ha == hha:
    print('Statement is true')

# %%
h = 'hasn\'t'
hh = "hasn't"
h == hh


# %%
print(hha + ' ' + h + ' ' + hh)

# %%


def lstr():
    dataText = [{"word": "kentucky", "score": 129541},
                {"word": "pitt", "score": 64667}]
    lst = []

    # for i in data.text:
    for i in dataText:
        lst.insert(2, {"Hima": "kdkkd"})
        # lst.append({"word": "Hima", "score": 13235})

    print(lst)

    # print(dataText)


lstr()


# %%


def lstr():
    dataText = [{"word": "kentucky", "score": 129541},
                {"word": "pitt", "score": 64667}]
    lst = []

    # for i in data.text:
    for i in dataText:
        # lst.insert(2, {"Hima":"kdkkd"})
        lst.append({"word": "Hima", "score": 13235})

    print(lst)

    # print(dataText)


lstr()


# %%
# Naming slices (slice(start, end, step))

# create list w/ int in a range


def makeLst(r1, r2):
    if (r1 == r2):
        return r1
    else:
        res = []

        while (r1 < r2 + 1):
            res.append(r1)
            r1 += 1
        return res

# r1, r2 = -1, 2
# print(makeLst(r1, r2))


# %%
print(makeLst(r1=1, r2=4))

# %%
r1, r2 = 0, 22
a = makeLst(r1, r2)
print(a)

# %%
last3 = slice(-3, None)
print(last3)
a[last3]

# %%
print(a)
