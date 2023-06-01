#Write a program to scan a number and check whether it is Odd, Even or Neutral (Zero)
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if num%2==0 and num!=0:
   print("its an even ")
elif num==0:
   print("Its neutral")
else:
   print("Its odd")
