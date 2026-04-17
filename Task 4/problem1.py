def safe_divide(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except TypeError:
        print("Input must be a number")

safe_divide(1, 2)
safe_divide(1, 0)
safe_divide(1, "x")