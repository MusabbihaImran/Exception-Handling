print("Program Started\n")

# ArithmeticException (ZeroDivisionError)
try:
    print("Arithmetic Test")
    a = 10
    b = 0
    res = a / b
except ZeroDivisionError:
    print("Arithmetic Error: Cannot divide by zero!")
finally:
    print("Arithmetic block executed\n")

# NullPointerException (AttributeError)
try:
    print("Null Pointer Test")
    x = None
    x.upper()
except AttributeError:
    print("Null Pointer Error: Object is None!")
finally:
    print("Null block executed\n")


# NumberFormatException (ValueError)
try:
    print("Number Format Test")
    num = int("abc")
except ValueError:
    print("Number Format Error: Invalid input!")
finally:
    print("Number format block executed\n")

# ArrayIndexOutOfBoundsException (IndexError)
try:
    print("Array Index Test")
    arr = [1, 2, 3]
    print(arr[5])
except IndexError:
    print("Array Index Error: Index out of range!")
finally:
    print("Array block executed\n")


print("Program Ended")