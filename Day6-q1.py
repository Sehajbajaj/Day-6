#Calculate power of a number using a while loop
a = float(input("Enter the base number: "))
b = float(input("Enter the exponent: "))
answer = 1
while b != 0:
    answer *= a
    b = b-1
print("The Answer is: " , answer)
