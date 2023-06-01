# Python3 Program to
# accept marks for 5 subjects and calculate average
# collecting and storing the data of marks per subject
name=input("enter your Name =")
standard=input("Enter the class and section =")
ENGLISH = float(input("Enter the marks of english: "))
MATHS = float(input("Enter the marks of math: "))
SOCIALSCIENCE = float(input("Enter the marks of Social Science: "))
SCIENCE = float(input("Enter the marks of Science: "))
HINDI = float(input("Enter the marks of Hindi: "))

# storing the total marks in the variable 'total'
total = ENGLISH + MATHS + SOCIALSCIENCE + SCIENCE + HINDI
# calulating the average of marks
average= total/5

print("***/***REPORT CARD***\***")
print("Name if student",name)
print("class /section",standard)
print("Marks for all subjects u entered =")
print("English =",ENGLISH)
print("Maths =",MATHS)
print("Social Science",SOCIALSCIENCE)
print("Science =",SCIENCE)
print("Hindi ", HINDI)
print("Your total marks is =",total)
print("Your average marks is =",average)

