def calculation():
    number1 = int(input("please enter your number:"))
    number2 = int(input("please enter your number2:"))
    oprate = input("please enter the operations /, *, -, +:")

    if oprate == '+':
        print(number1 + number2)
    elif oprate == '-':
        print(number1 - number2)
    elif oprate == '*':
        print(number1 * number2)
    elif oprate == '/':
        print(number1 / number2)
    else:
        print("error")

result = calculation()

while True:
    again = input("do you want to continue? enter yes or no:")
    if again == "yes":
        calculation()
    elif again == "no":
        break
    else:
        print("error")
        continue

print("done!")