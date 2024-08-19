# Task #2 Assignment
#
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}
#from mailcap import subst

number1 = int(input("Please enter the First Number :"))
number2 = int(input("Please enter the Second Number :"))

# # /Programme to Verify Maximum between 2 inputs given and format with it\

Maximum_Value = max(number1,number2)
print("\nThe Max Value between 2 Numbers is: ",Maximum_Value)

# pow num1 to num2
Poweroff_Value = pow(number1,number2)
print("The Power off value between 2 Numbers is: ",Poweroff_Value)

#Subtraction
Subtraction_Value = (number1-number2)
print("The Subtracted Value between given numbers are:", Subtraction_Value)

#Multiplication
Multiplication_Value = (number1*number2)
print("The Multiplied Values between 2 given numbers are :", Multiplication_Value)


#Sum or Additon
Additon_Value = (number1+number2)
print("The Sum of two numbers is: ", Additon_Value)


#Division
Division_Value = (number1/number2)
print("The Dividened Value is: ", Division_Value)

print("\nAll the formatted Values are Displayed Here:")
print("\nThe Formatted Value is ",f"{Maximum_Value}")
print("The Formatted Value is ",f"{Poweroff_Value}")
print("The Formatted Value is ",f"{Subtraction_Value}")
print("The Formatted Value is ",f"{Multiplication_Value}")
print("The Formatted Value is ",f"{Additon_Value}")
print("The Formatted Value is ",f"{Additon_Value}")

