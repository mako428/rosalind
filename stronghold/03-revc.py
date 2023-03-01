# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s

# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT

# doesn't currently work as a file path to a .txt file
# file = input("Enter file path:")
# if file < 1:
# fh = open(file)

fh = input("Enter string:")
if len(fh) < 1 :
    fh = "AAAACCCGGT"
# print(fh)
# reverses a string
s = fh[::-1]
# print(s)
# sc = s.replace("A","T").replace("T","A").replace("G","C").replace("C","G")
sc = ""
for letter in s :
    if letter == 'A' :
        letter = 'T'
    elif letter == 'T' :
        letter = 'A'
    elif letter == 'C' :
        letter = 'G'
    elif letter == 'G' :
        letter = 'C'
    sc = sc + letter

print(sc)