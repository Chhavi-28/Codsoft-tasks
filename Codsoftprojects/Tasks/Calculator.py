#Simple Calculator
print("....Welcome To Simple Calculator....")
print("Chose Which Operation You Want To Perform -->")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = input("Enter Operation Symbol (+,-,*,/):")
num1 =float(input("Enter First Number :"))
num2 =float(input("Enter Second Number:"))
if operation =='+':
    print(num1,"+",num2,"=",num1+num2)
elif operation == '-':
    print(num1,"-",num2,"=",num1-num2)
elif operation == '*':
    print(num1,"*",num2,"=",num1*num2)
elif operation =='/':
    if num2==0:
        print("Error Division By Zero Not Possible")
    else:
        print(num1/num2,"=",num1/num2)
else:
    print("Invalid Operation symbol")
    

        



