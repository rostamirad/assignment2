input = int(input("Plese enter your time in second: "))
x = input // 3600
y = (input - x * 3600) // 60
z = (input - (x * 3600) - (y * 60))
print("Your answer is:", x, ":", y, ":", z)
