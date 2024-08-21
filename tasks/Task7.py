### Task #7

# ✅ Leap Year Checker:
# ![img_1.png](img_1.png)
#
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.


    # A leap year is divisible by 4
    # but not divisible by 100, unless it is also divisible by 400

# Input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
