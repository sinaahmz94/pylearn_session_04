number = int(input("please enter your number: "))
factorialed_numbers = [1]
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
    factorialed_numbers.append(factorial)
if number in factorialed_numbers:
    print("your numer is factorialed")
else:
    print("the number is not factorialed")