#Assignment 4 
#1
y=0
while y<=10:
    print(y)
    y+=2

#2
sum=0
for num in range(1,10,2):
    if num%2==1:
        sum+=num         
print(sum)

#3
a=0
b=1

print("Fibonacci series between 0 to 50:")

while a <= 50:
    print(a, end=" ")
    a,b=b, a+b
     
#4
text=input("\nEnter a string : ")
result = ""
for i in range(len(text)):
        if i % 2 == 1:  
            result += text[i]
print (result)
