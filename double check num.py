num=int(input("Enter your attendance percentage: "))
a=input("Do you have any extra curriculars: ")

if num<75:
    print ("Not eligible for exam")
    if a=="yes":
        print("But talk to HOD")
    else:
        print("Try again next semister")
else:
    print("You are eligible for exam , collect your hall ticket ")
