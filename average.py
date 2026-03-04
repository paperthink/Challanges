import math
a, b, c = int(input("enter the 1st number\n")), int(input("enter the 2nd number\n")), int(input("enter the 3rd number\n"))

numbers = [a, b, c]

av = sum(numbers)/len(numbers)
print(av)
