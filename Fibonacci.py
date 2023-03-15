print("for Fibonacci series you shoud choose your number in the set of natural numbers:) ")
n = int(input("Enter your number: "))
a = 0
b = 1
sum = 0
counter = 1
print("Fibonacci series is: ", end = " ")
while(counter <= n) :
    print(sum, end = " ")
    counter += 1
    a = b
    b = sum
    sum = a + b
