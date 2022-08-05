def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Not an Number! Try again.")
            continue
        else:
            return userInput

def inputletters(message):

    while True:
        l = input(message)
        if l.isalpha():
            return l
        else:
            print("Enter letters only")

a=inputletters("Enter First Order:")
a1=inputNumber("Enter First Order Quantity:")
a2=inputNumber("Enter First Order Price:")
a3=int(a1) * float(a2)
b=inputletters("Enter Second Order:")
b1=inputNumber("Enter Second Order Quantity:")
b2=inputNumber("Enter Second Order Price:")
b3=int(b1) * float(b2)
c=inputletters("Enter Third Order:")
c1=inputNumber("Enter Third Order Quantity:")
c2=inputNumber("Enter Third Order Price:")
c3=int(c1) * float(c2)
total = a3 + b3 + c3
Tax = total * 0.15
TC = total + Tax
print("SEHHA & HANAA \nRestaurant:")
print(f"1:{a} = {a1} X {a2} = {a3}$")
print(f"2:{b} = {b1} X {b2} = {b3}$")
print(f"3:{c} = {c1} X {c2} = {c3}$")
print("-" * 13)
print(f"Total = {round(total,2)}$\nTax = {round(Tax,2)}$")
print("-" * 13)
print(f"Total Cost = {round(TC,2)}$\nThank you")
