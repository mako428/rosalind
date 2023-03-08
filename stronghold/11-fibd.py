# Given: Positive integers n≤100 and m≤20.

# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

# if rabbits live for three months they reproduce only twice before dying
# (lifespan - 1 = number of offspring pairs)
# example:
# 1 pair : 1, 1, 2, 2, 3, 4, 5

# 2 pair : 1, 1, 3, 4, 8, 8

# based on code from 04-fib.py

n = int(input("Enter number of months:"))
k = int(input("Enter number of pairs per generation:"))
m = int(input("Enter lifespan in months:"))

sequence = [1,1]
while n > len(sequence):
    if len(sequence) < m :
            sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2]*k) # sequence[len(sequence)-1] + k)
    else:
        sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2]*k - sequence[len(sequence)-(m)])
        
if len(sequence) >= n :
    print(sequence[n-1])
    print(sequence)