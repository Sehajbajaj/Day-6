#Count Number of Digits in an Integer using while loop
x = int(input("Enter a number:  "))
ct = 0
while x > 0:
    x = x // 10
    ct = ct +1
print("The number of digits are: " , ct)
