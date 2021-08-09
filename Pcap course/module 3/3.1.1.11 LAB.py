income = float(input("Enter the annual income: "))

if income <= 85528:
    tax=18/100*income-556.02
elif income >85528:
    tax=14839.02+32/100*(income-85528)


if tax > 0:
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")
else:
    tax = 0.0
    print("The tax is:", tax, "thalers")

