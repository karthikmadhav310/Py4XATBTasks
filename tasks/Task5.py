# ### Task #5
#
#
#
# - Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.
from gc import get_referents

# numberone = int(input("Enter the numberone"))
# numbertwo = int(input("Enter the numbertwo"))
#
# if numberone >= numbertwo :
#     print("numberone is greater than numbertwo",numberone)
# else :
#     print("Numbertwo is greater than numberone",numbertwo)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is lesser than {num2}")
else:
    print(f"{num1} is equal to {num2}")
