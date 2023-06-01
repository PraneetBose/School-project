#Write a program to print HCF and LCM of 2 numbers entered by the user.

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def compute_hcf(z, v):
    # selecting the smaller number
    if z > v:
        smaller = v
    else:
        smaller = z
    for i in range(1,smaller + 1):
        if((z % i == 0) and (v % i == 0)):
            hcf = i
    return hcf

num1=int(input("Enter the 1st no ="))
num2=int(input("Enter the 2nd no ="))
print("The L.C.M. is =", compute_lcm(num1, num2))
print("The H.C.F. is =", compute_hcf(num1, num2))