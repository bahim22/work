# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Define constants for tax and insurance rates

TAX_RATE = 0.22
INSURANCE_RATE = 0.07

# Define a function to calculate the salary for a full-time employee


def calculate_full_time_salary(hours, rate):
    # Calculate the gross salary
    gross_salary = hours * rate

    # Calculate the tax amount
    tax = gross_salary * TAX_RATE

    # Calculate the insurance amount
    insurance = gross_salary * INSURANCE_RATE

    # Calculate the net salary
    net_salary = ((gross_salary - (tax - insurance)) * 4) + 200

    return net_salary

# Define a function to calculate the salary for a part-time employee


def calculate_part_time_salary(hours, rate):
    # Calculate the gross salary
    gross_salary = hours * rate

    # Calculate the tax amount
    tax, insurance = gross_salary * TAX_RATE, 50

    # Calculate the net salary
    net_salary = ((gross_salary - tax) * 4) - insurance

    return net_salary


# Compare the salaries of full-time and part-time employees
full_time_hours = 40
full_time_rate = 17
monthy_hours_ft = (full_time_hours * 4) - 16
full_time_salary = calculate_full_time_salary(full_time_hours, full_time_rate)

part_time_hours = 25
monthy_hours_pt = part_time_hours * 4
part_time_rate = 17
part_time_salary = calculate_part_time_salary(part_time_hours, part_time_rate)

if full_time_salary > part_time_salary:
    print(f"The full-time employee has a higher salary at {full_time_salary} \
        and works {monthy_hours_ft} hours \
        the pt employee makes: {part_time_salary} \
        and works {monthy_hours_pt}.")
elif full_time_salary < part_time_salary:
    print("The part-time employee has a higher salary.")
else:
    print("The full-time and part-time employees have the same salary.")

# %%
print("full time salary: ", full_time_salary)
print("part time salary: ", part_time_salary)
