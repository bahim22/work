#! ./work/.venv/bin/python3

# name = input("Enter your name: ")

# test var for quicker exe
name = "Hima"
xh, xr = 40, 20

# xh, xr = input("Enter Hours: "), input("Enter rate: ")

xp = float(xh) * float(xr)

mp = (xp * 4) * .75

# created func to print variables to stdout more efficiently


def print_pay(name, xp, mp):
    print(f"{name}, your weekly pay is ${xp} \
    \n and your monthly net pay is ${mp}")


print_pay(name, xp, mp)
