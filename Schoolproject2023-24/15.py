#WAP to scan a Number and print the sum of all the digits of the entered number

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)