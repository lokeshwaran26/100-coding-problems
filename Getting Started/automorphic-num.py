# Example
# Input : number = 5
# Output : It's an Automorphic number.
# Explanation : Number = 5
# Square of number = 25
# as the square of the number ends with the number itself, It's an Automorphic number.

n = int(input('Enter the number:'))
sqr = n**n
mod = sqr % 10
if n == mod:
    print("Automorphic number!")
else:
    print("Not a Automorphic number!")
