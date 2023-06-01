#WAP to scan N and print Sum of Odd and Sum of Even numbers till
max=int(input("please enter the maximum value: "))
even_Sum=0
odd_Sum=0
for i in range(1,max+1):
    if (i%2==0):
        even_Sum=even_Sum+i
    else:
        odd_Sum=odd_Sum+i
print("The sum of Even numbers 1 to {0} = {1}".format(i,even_Sum))
print("The sum of odd numbers 1 to {0} = {1}".format(i,odd_Sum))

