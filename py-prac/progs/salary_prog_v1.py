#! /home/ib-ub/flow/work/.venv/bin/python3
# %%
# salary prog v 1

def full_time_employee():
    """
        Function for full time employees total salary
    """

    # salary = 17 * 40
    monthly = 35000 / 12
    # biweekly = monthly / 2
    vacation = (17 * 8) * 2
    insurance = 50 * 4
    ft_total = (monthly + vacation)
    net = (ft_total - insurance) - 700
    print(net)


# full_time_employee()

# %%
vacation = (17 * 8) * 2
print(vacation)

# %%


def black():
    full_time = {
        "salary": 10000,
        "vacation": 20,
        "insurance": 1000
    }
    return full_time

# %%


def employee2():
    """
        Create the function for the part time employees total salary
    """

    salary = 17 * 25
    # yearly = 35000 / 12
    # monthly = (yearly / 4) / 4
    vacation = 0
    insurance = 20 * 4
    pt_total = (salary + vacation) - insurance
    return pt_total


# %%
def salary_diff(ft_total1, pt_total1):
    print(f'{ft_total1 - pt_total1}')


# %%
def full_time_employee2():
    """
        Function for full time employees total salary
    """

    # salary = 17 * 40
    monthly = 35000 / 12
    # biweekly = monthly / 2
    vacation = (17 * 8) * 2
    insurance = 50 * 4
    ft_total = (monthly + vacation)
    net = (ft_total - insurance) - 700
    print(net)


full_time_employee2()


def employee22():
    """
        Create the function for the part time employees total salary
    """

    salary = 17 * 25
    # yearly = 35000 / 12
    # monthly = (yearly / 4) / 4
    vacation = 0
    insurance = 20 * 4
    pt_total = (salary + vacation) - insurance
    return pt_total

# call func
# employee2()


def main():
    """
        main func to call the other funcs
    """
    ft_total = full_time_employee2()
    pt_total = employee22()
    print(f'The full time employee makes $: {ft_total}, per month and \
        {ft_total * 12} per year.')
    print("The part time employee makes $", pt_total, "per year.")
    print(f"The full time employee makes $, {ft_total - pt_total}, more than \
            the part time employee.")


main()

# call func
# print(main())
