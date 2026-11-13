import Factorial
fact = 1
num = int(input("Enter a Number:"))
for i in range(1,num+1):
    fact = fact*i
    print("The fact is:",num,fact)
