#Python Program to Find Factorial of Number Using Recursion
def recur_factorial(a):
    if a == 1:
        return a
    else:
        return a*recur_factorial(a-1)

n = int(input("Enter a number: "))
if n < 0:
    print("The number is negative")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of" , n , "is: " , recur_factorial(n))


