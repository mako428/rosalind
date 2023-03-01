# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t

# Sample Dataset
# GATGGAACTTGACTACGTAAATT
# Sample Output
# GAUGGAACUUGACUACGUAAAUU

# there is a string.method called .replace which seems way easier
# string.replace("X","Y") replaces all "X" with "Y"

file = input("Input file path:")
if len(file) < 1:
    fh = "GATGGAACTTGACTACGTAAATT"
    # it doesn't actually work for this line 11-12 condition
    # had to be written differently for a file path .txt input
else:
    fh = open(file)
print(type(fh))

# much simpler
print(fh.replace("T","U"))

# original solution
newstring = ""
for line in fh :
    for nt in line :
        if nt == "T" :
            nt = "U"
        newstring = newstring + nt
print(newstring)