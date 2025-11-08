# ---- Basic Python ----

print("=== Welcome to Python Basics ===\n")

# 1. VARIABLES
name = "Student"
age = 20
is_learning = True

print("Your name is:", name)
print("Your age is:", age)
print("Are you learning Python?", is_learning)

print("\n--- USER INPUT ---")
# 2. INPUT
user_name = input("Enter your name: ")
print("Hello", user_name + "!\n")

# 3. IF / ELSE CONDITION
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print(" You are an adult!")
else:
    print(" You are not an adult yet!")

print("\n--- LOOPS ---")
# 4. LOOP EXAMPLE (for loop)
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\n--- WHILE LOOP ---")
count = 0
while count < 3:
    print("Loop number:", count)
    count += 1

print("\n--- LISTS ---")
# 5. LIST EXAMPLE
fruits = ["apple", "banana", "orange"]
print("Fruit list:", fruits)
print("First fruit:", fruits[0])

print("\n--- FUNCTION ---")
# 6. FUNCTION EXAMPLE
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("3 + 5 =", result)

print("\n=== End of Program ===")
