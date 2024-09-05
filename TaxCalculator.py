def getIncomeTax(salary):
    personal_allowance = 11850
    tax = 0
    
    if salary <= personal_allowance:
        return tax

    taxable_salary = salary - personal_allowance

    if taxable_salary <= 34500:
        tax = taxable_salary * 0.20
    else:
        tax = 34500 * 0.20

        if taxable_salary <= 150000:
            tax += (taxable_salary - 34500) * 0.40
        else:
            tax += (150000 - 34500) * 0.40
            tax += (taxable_salary - 150000) * 0.45

    return tax

salary1 = 30000
salary2 = 50000
salary3 = 160000

print(f"Income tax for salary £{salary1}: £{getIncomeTax(salary1):.2f}")
print(f"Income tax for salary £{salary2}: £{getIncomeTax(salary2):.2f}")
print(f"Income tax for salary £{salary3}: £{getIncomeTax(salary3):.2f}")
