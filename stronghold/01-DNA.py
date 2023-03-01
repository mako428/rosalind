# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 20 12 17 21

# it works as a single string input without multiple lines...

file = input("Input file name:")
if len(file) < 1 :
    fh = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC\nblahblah"
else:
    fh = open(file)
  

for line in fh :
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    line1 = line.rstrip()
    line1 = str(line1)
    # print("Length",len(line1),"nt")
    if len(line1) > 1000 :
        print("Input line > 1000 nt")
        continue
    # print(line1)
    for letter in line1 :
        # print(letter)
        if letter == "A" :
            countA = countA + 1
        elif letter == "C" :
            countC = countC + 1
        elif letter == "G" :
            countG = countG + 1
        elif letter == "T" :
            countT = countT + 1
            
    print(countA,countC,countG,countT)
        
