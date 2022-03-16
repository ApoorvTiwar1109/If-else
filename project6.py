print("Enter age in number -")
age = input()
if type(age)==str:
    print("Write in number")  
else:
    if age==18:
        print("Eligible to vote")
    elif age>18:
        print("Eligible to vote")
    else:
        print("Not eligible")
