# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# sample dataset = 5 3
# sample output = 19
# 1,1,4,7,19,f  (f-2)*3+(f-1)

n = int(input("Enter number of months:"))
k = int(input("Enter number of pairs per generation:"))

sequence = [1,1]
while n > len(sequence):
    # I don't think I need this try/except anymore
    try :
        sequence[n-2] * 3 + sequence[n-1]
    except :
        sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2]*3)
if len(sequence) >= n :
    print(sequence[n-1])