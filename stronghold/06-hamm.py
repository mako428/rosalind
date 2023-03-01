## Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t)

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output 7

file = input("Enter filepath:")
if len(file) < 1 :
    file = "C:/Users/mak/Documents/coding-misc/rosalind/stronghold/06-hamm-sample.txt"
fh = open(file)

lst = []
count = 0
for line in fh :
    lst.append(line.strip())
print(len(lst[0]),"nt",lst)
if len(lst[0]) != len(lst[1]) :
    print("Error, sequences not equal in length")
    quit()
if len(lst[0]) > 1000 or len(lst[1]) > 1000 :
    print("Error, sequences longer than 1kb")
    quit()
seq1 = lst[0] 
seq2 = lst[1]
i = 0
while len(seq1) == len(seq2) :
    if seq1[i] != seq2[i] :
        count = count + 1
    i = i + 1
    # print(i)
    if i >= len( seq1 ) :  
        break 

print("dH =",count)

# finished

# there is also a trick with the zip() function to join two lists to iterate the 1st items in each list at the same time
# zip() creates a list of tuples...

# one ChatGPT solution
# def hamming_distance(s, t):
#    """
#    Calculate the Hamming distance between two DNA strings s and t.
#    """
#    return sum(1 for x, y in zip(s, t) if x != y)

# Example usage:
# s = "GAGCCTACTAACGGGAT"
# t = "CATCGTAATGACGGCCT"
# print(hamming_distance(s, t))



