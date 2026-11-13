Telugu = int(input("enter Telugu marks:"))
Hindi = int(input("enter Hindi marks:"))
English = int(input("enter English marks:"))
Maths = int(input("enter Maths marks:"))
Social = int(input("enter Social marks:"))
Science = int(input("enter Science marks:"))

total= Telugu + Hindi + English + Maths + Science + Social 
percentage= total / 600 * 100

if percentage>=90:
    grade ="A+"
elif percentage>=75:
    grade ="A"
elif percentage>=55:
    grade ="B"
elif percentage>=35:
    grade = "C"

print("percentage:", percentage)
print("Total:", total)
print("Grade:", grade)        