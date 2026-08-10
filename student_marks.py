name = input("Enter your name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

total = maths + python + english
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)