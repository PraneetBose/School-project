#Write a progr# Python program to find the largest number among the three input numbers
num1 = float(input("Enter the 1st no ="))
num2 = float(input("Enter the 2st no ="))
num3 = float(input("Enter the 3st no ="))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3 
print("The largest number is", largest)
