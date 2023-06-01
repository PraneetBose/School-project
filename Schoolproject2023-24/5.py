#Write a program to print all the numbers divisible by 7 between two numbers scanned by user.
num1=int(input("Enter the lower limit ="))
num2=int(input("Enter the Upper limit ="))
for i in range (num1,num2+1):
    if i%7==0:
        print(i)
    else:

        ("NOT possible ")

