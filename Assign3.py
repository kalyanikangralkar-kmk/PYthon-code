# Experiment 3
# 1
a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
if (a>b and a>c):
    print ("a is greatest.") 
elif (b>c and b>a):
    print("b is greatest.")
elif (a==b or b==c):
    print("2 number are same.\nEnter different numbers. ")
else:
    print("c is greatest.")

# 2
n=int(input("Enter number :"))
if n%2==0:
    print("Even number.")
else:
    print( "Odd number.")

# 3
v=input("enter :")
if v.isupper():
    print("uppercase")
else:
    print("lowercase")
   
# 4
q=(input("Enter :"))
if q.isalpha():
    print("Character")
else : 
    print("Digit")