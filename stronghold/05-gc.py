# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# Sample Dataset
#
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# 
# Sample Output
#
# Rosalind_0808
# 60.919540

# finished

file = input("Enter filepath of file:")
if len(file) < 1 :
    file = "C:/Users/mak/Documents/coding-misc/rosalind/stronghold/05-gc-sample.txt"
fh = open(file)
highest_id = ""
highest_gc = 0
gc = None
length = None

for line in fh :
    if line[0] == ">" :
        if gc != None or length != None :
            #print(name)
            #print( gc / length * 100)
            if gc / length * 100 > highest_gc :
                highest_gc = gc / length * 100
                highest_id = name
        name = line[1:].rstrip()
        gc = 0
        length = 0
    else :
        gc = gc + line.count("G") + line.count("C")
        length = length + len(line.rstrip())

        #for nt in line :
            #if nt == "G" or nt == "C" :
                #gc = gc + 1
            #if nt == "\n" :
        # print ( name,"GC %",100 * (gc / length))

#print(name)
#print(gc/length * 100)        
if gc / length *100 > highest_gc :
                highest_gc = gc / length * 100
                highest_id = name
print("Top GC content:",highest_id)
print(highest_gc)