# VARIABLES & DATA TYPES

name = "John"      # string (text)
age = 21           # integer (whole number)
height = 1.75      # float (decimal number)
is_student = True  # boolean (True/False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)





# 01_variables.py
# Demonstrates variables, basic types, casting, and f-strings

def basics():
    # Numbers
    a_int = 10
    a_float = 3.14

    # Strings
    greeting = "Hello"
    name = "Student"

    # Boolean
    is_learning = True

    # None
    nothing = None

    print("Types:")
    print(type(a_int), type(a_float), type(greeting), type(is_learning), type(nothing))

    # Casting
    s_number = "42"
    converted = int(s_number)  # string -> int
    print("\nCasting example: '42' ->", converted, "type:", type(converted))

    # f-strings (recommended for readability)
    print(f"\n{greeting}, {name}! You have {a_int} points and pi approx {a_float}.")

    # Multiple assignment
    x, y, z = 1, 2, 3
    print("Multiple assignment:", x, y, z)

    # Swap values (Pythonic)
    x, y = y, x
    print("After swap:", x, y)

if __name__ == "__main__":
    print("=== VARIABLES & TYPES ===")
    basics()
