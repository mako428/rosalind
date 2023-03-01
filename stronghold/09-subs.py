# Given: Two DNA strings s and t (each of length at most 1 kbp).

# Return: All locations of t as a substring of s.

# Sample Dataset
# GATATATGCATATACTT
# ATAT
# Sample Output
# 2 4 10

# JUNK CODE
# file = input('Enter filepath:')
# if len(file) < 1 :
#     file = '09-subs-sample.txt'
# fh = open(file)
# fh.readline().strip()

def motifsearch(DNAstring,motif) :
    DNAstring = str(DNAstring) 
    motif = str(motif)
    lst = list()
    DNAstring.find(motif)
    position = 0
    while position != -1 :
        nt = DNAstring.find(motif,position) + 1
        if nt == 0 :
            break
        # print(nt)
        lst.append(nt)
        position = nt
        # if position == -1 :
        #     break
    print(lst)
    
    # trying to print the formatting how rosalind wants it: as a single line with only a space between the integers
    # output = str(print(lst))
    # print(output)
    # output = output.replace(',','')
    # output = output.replace('[','')
    # output = output.replace(']','')
    # print(output)
    # doesn't work

print('----- Sample output -----')
motifsearch('GATATATGCATATACTT','ATAT')
print('----- End sample -----')

# solved answer
# motifsearch('GGCGCAATGTGGCGCAAGGCGCAACATGGCGCAATGGCGCAAAGGGCGCAAGGTTCACCTAAGGGCGCAAGGCGCAAGGCGCAAGGCGCAATCTTAGCGGCGCAAGGCGCAAGTGGCGCAAGGCGCAAGGCTCACCGGCGCAACTTTGGGGCGCAACGTATCGTGTGGCGCAATGGCGCAAGGCGCAATCAAGGCGCAATGGCGCAACGTCGACGGCGCAAAGGCGCAAGGCGCAATTTGGCGCAAACGGCGCAATATAACTGTGAGGCGCAAAGGCGCAACCTGGCGCAACTGTGGCCGAGGCGCAATTGGCTATGGCGCAAAGGGCGCAATTGGCGCAACGGCGCAAAGGCGCAAGCCGGGGCGCAAAAGGCGCAAATTAACGCGGCGCAAAGAAGGCGCAAGGCGCAAATGGCGCAAAGTCGGTTGGCGCAAGGGCGCAAGGCGCAAATGAACCGGGCGCAAGGCGCAATGGGCGCAAGGCGCAATGTGAGGCGCAAGCATGGCGCAATGGCGCAAAGGCGCAAGGGCGCAAGGCCGGCGCAACGTGGCGCAAGGCGCAAGGGCGCAACCTTAGGCGCAAAGGCGCAACTCCTGGGCGCAAGGGCGCAACCATCGGCGCAAAGGCGCAAAAGGGCGCAAGGCGCAAGGCGCAATCATATCGGCGGCGCAATGGCGCAACCGGGCGCAAGGCGCAAAGGCGCAACGGCGCAAATAGGCGCAAGTGGGCGCAATCAGGCGCAAAAGGGCGCAAAGGCGCAATACCTGGCGCAAGGAGGCGCAAGTTCGCTGGCGCAAGGCGCAAGGCGCAAGCAAGGGCGCAAATGTATAGGGCGCAAAGGATGGCGCAAGGCGCAACCCAATTCACTCTAACCGAACGGCGCAAGGCGCAAGGCGCAAGGCGCAAACGGCGCAAATAAGGCGCAATCTGGCGCAAAGGCGCAAGTATTGAGGCGCAAGGCGCAACTAGGCGCAAGAC','GGCGCAAGG')