print("u can enter the time by this format: ")
print("hour: between 0 to 23")
print("minute: between 0 to 59")
print("second: between 0 to 59")

x = int(input("Plese enter hour: "))
y = int(input("Plese enter minute: "))
z = int(input("Plese enter the second: "))

output = z + (y * 60) + (x * 3600)

print("Your input is: ", output, "seconds:) ")