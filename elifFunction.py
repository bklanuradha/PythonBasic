num = int(input("Enter Marks: "))

if 100 >= num >= 0:
    if num >= 75:
        print("Grade A")
    elif num >= 65:
        print("Grade B")
    elif num >= 50:
        print("Grade C")
    elif num >= 35:
        print("Grade S")
    else:
        print("Fail")
else:
    print("Invalid marks")
