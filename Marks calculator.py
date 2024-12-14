a=float(input("Enter your Math marks: "))
b=float(input("Enter your Physics marks: "))
c=float(input("Enter your Chemistry marks: "))

total=(a+b+c)/3

if total <= 34:
    print("You fail...")
elif total <= 36:
    print("just pass")
elif total <= 70:
    print("Pass")
elif total <= 85:
    print("Pass with good marks")
elif total <= 95:
    print("Distiction")
elif total <= 100:
    print("Excellent")
else:
    print("Enter the marks out of 100")
