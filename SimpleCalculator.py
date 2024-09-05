def simple_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    sum_result = num1 + num2
    sub_result = num1 - num2
    mul_result = num1 * num2

    print(f"Sum is {sum_result}, Subtraction is {sub_result}, Multiplication is {mul_result}.")

simple_calculator()