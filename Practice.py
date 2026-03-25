n=input('Enter a number:')
res=0
try:
 print('Try block')
 n = int(n)
 res=n/0
except ZeroDivisionError:
  print('Except block')
  print('Cannot divide by zero!')
except ValueError:
  print('Except block')
  print('Enter a valid number!')
else:
  print('Else block')
  print('Result is: ', res)
finally:
  print('Finally block')
  print('Execution complete.')
  del res
  del n

# ZeroDivisionError
try:
    number = 50
    result = number / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# ValueError
try:
    value = int("hello")
except ValueError:
    print("Error: Invalid integer conversion!")

# TypeError
try:
    data = [1, 2, 3]
    result = data + "text"
except TypeError:
    print("Error: Cannot add list and string!")

# IndexError
try:
    fruits = ["apple", "banana"]
    print(fruits[5])
except IndexError:
    print("Error: Index out of range!")

# KeyError
try:
    student = {"name": "Sara", "age": 20}
    print(student["grade"])
except KeyError:
    print("Error: Key does not exist!")

# NameError
try:
    print(my_variable)
except NameError:
    print("Error: Variable not defined!")

# AttributeError
try:
    text = "Python"
    text.append("3")
except AttributeError:
    print("Error: Strings have no append method!")

# ArithmeticError
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ArithmeticError:
    print("Error: Arithmetic problem detected!")

# Multiple Exceptions (separate handling)
try:
    x = int("100abc")
    y = 5 / 0
except ValueError:
    print("Error: Value conversion failed!")
except ZeroDivisionError:
    print("Error: Division by zero occurred!")

# Multiple Exceptions (combined)
try:
    numbers = ["5", "ten"]
    total = int(numbers[0]) + int(numbers[1])
except (ValueError, TypeError) as e:
    print("Error:", e)

# try-except-else-finally
try:
    num = int(input("Enter a number to divide 100: "))
    division = 100 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
else:
    print("Division result is:", division)
finally:
    print("Finished executing try-except-else-finally block.\n")

# Catch-all Exception
try:
    result = "50" / 5
except ArithmeticError:
    print("Error: Arithmetic issue!")
except:
    print("Error: Some unexpected problem occurred!")

# Raising Exception
def check_temperature(temp):
    if temp < -50 or temp > 100:
        raise ValueError("Temperature out of range!")
    print(f"Temperature is {temp}°C")

try:
    check_temperature(-100)
except ValueError as e:
    print("Error:", e)

# AssertionError
try:
    score = -10
    assert score >= 0
except AssertionError:
    print("Error: Score cannot be negative!")

# ModuleNotFoundError
try:
    import imaginary_module
except ModuleNotFoundError:
    print("Error: Module not found!")

print("\n=== End of Original Practical ===")