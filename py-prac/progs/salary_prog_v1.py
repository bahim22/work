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


full_time_employee()

# %%
full_time_employee()

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

# %%


# %%
full_time_employee()

# %%


def employee2():
    """
        Create the function for the part time employees total salary
    """

    salary = 17 * 25
    yearly = 35000 / 12
    monthly = (yearly / 4) / 4
    vacation = 0
    insurance = 20 * 4
    pt_total = (salary + vacation) - insurance
    return pt_total


# %%
def salary_diff():
    """
        The part time employee makes $17 per hour, pays $20 per week for insurance, gets 0 vacation days, and works 25 hours per week. The full time employee makes the same amount per hour, pays $50 per week for insurance and gets 25 vacation days per year
    """

    print(f'{ft_total - pt_total}')


# %%
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


full_time_employee()


def employee2():
    """
        Create the function for the part time employees total salary
    """

    salary = 17 * 25
    yearly = 35000 / 12
    monthly = (yearly / 4) / 4
    vacation = 0
    insurance = 20 * 4
    pt_total = (salary + vacation) - insurance
    return pt_total


employee2()

"""
def salary_diff():
    ""
        The part time employee makes $17 per hour, pays $20 per week for insurance, gets 0 vacation days, and works 25 hours per week. The full time employee makes the same amount per hour, pays $50 per week for insurance and gets 25 vacation days per year
    ""

    print(f'{ft_total - pt_total}')
"""


def main():
    """
        Create the main function to call the other functions
    """

    ft_total = full_time_employee()
    pt_total = employee2()
    print(
        f'The full time employee makes $: {ft_total}, per month and {ft_total * 12} per year.')
    print("The part time employee makes $", pt_total, "per year.")
    print(
        f"The full time employee makes $, {ft_total - pt_total}, more than the part time employee.")


main()

print(main())
