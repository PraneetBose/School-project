#Write a program to check if the entered year is Leap year or not
year = int(input("Enter the number ="))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a leap year !!")
        else:
            print("Its not a leap year !!")
    else:
        print("Its a leap year !!")
else:
    print("Its not a leap year !!")
