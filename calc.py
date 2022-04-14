def addition(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def percen(num1,num2):
    return num1 % num2
def divide(num1,num2):
    return num1 / num2


print("select the operation \n" \
    "1.additon\n" \
        "2.subraction\n "\
        "3.multiplication\n"\
        "4.divide\n" )

choice=int(input("select the operation 1,2,3,4 "))

number_1=input('enter the number')
number_2=input('enter the number')

if choice ==1:
    print(addition(number_1,number_2))
