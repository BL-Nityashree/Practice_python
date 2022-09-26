num1 = int(input("enter the 1st num : "))
num2 = int(input("enter the 2nd num : "))
opr = input("Enter the operation that has to be performed : ")

print(num1, num2, opr)

if num1 == 45 and num2 == 3 and opr == '*' :
    print(num1, opr, num2, "= 555" )
elif num1 == 56 and num2 == 9 and opr == '+' :
    print(num1, opr, num2, "= 77" )
elif num1 == 56 and num2 == 6 and opr == '/' :
    print(num1, opr, num2, "= 4" )
else:
    if opr == "+":
        res = num1 + num2
        print(num1, opr, num2, "=", res)
    if opr == "-":
        res = num1 - num2
        print(num1, opr, num2, "=", res)
    if opr == "*":
        res = num1 * num2
        print(num1, opr, num2, "=", res)
    if opr == "/":
        res = num1 / num2
        print(num1, opr, num2, "=", res)
    if opr == "**":
        res = num1 ** num2
        print(num1, opr, num2, "=", res)
    if opr == "%":
        res = num1 % num2
        print(num1, opr, num2, "=", res)