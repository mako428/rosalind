# find overlapping DNA strings, like a shotgun DNA-seq fragment pileup

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

# Return: The adjacency list corresponding to O3. You may return edges in any order.

# DNA string with a suffix of 3bp that overlaps/matches a prefix of 3bp in another DNA string. Print this pairing.

# Sample Dataset
# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG

# Sample Output
# Rosalind_0498 Rosalind_2391
# Rosalind_0498 Rosalind_0442
# Rosalind_2391 Rosalind_2323

file = input('Input file name:')
if len(file) < 1 :
    file = 'C:/Users/mak/Documents/coding-misc/rosalind/stronghold/12-grph-sample.txt'
fh = open(file)

dict_fastas = dict()
# read document and add fasta ids and their DNA sequences to a dictionary as key/values
for line in fh :
    if line[0] == '>' :
        # if line contains new >fasta id, add previous id and dnastring to dictionary unless it is the first entry
        try :
            print(len(dnastring),'nt :',dnastring)
            dict_fastas[fasta_id]= dnastring
            dnastring = ''
        # if dnastring does not yet exist because it is the first fasta id of the document, create empty dna string
        except :
            dnastring = ''
        # save fasta id as a variable to be used as dictionary key
        fasta_id = line[1:].strip()
    # add dna strings in consecutive lines to a single string until a new >fasta id is found, or document ends
    else :
        if len(dnastring) > 1000 :
            print("Error: 1kb sequence length exceeded -",fasta_id)
            break
        else :
            dnastring = dnastring + line.strip()
# adds the last fasta entry to the dictionary at end of file
print(len(dnastring),'nt :',dnastring)
dict_fastas[fasta_id]= dnastring
print(dict_fastas)
print('Number of sequences:',len(dict_fastas))

# parse_fasta_dict(fh1)

# read through fasta dictionary
for k, v, in dict_fastas.items() :
    for key, value in dict_fastas.items() :
        # find matching prefix/suffix
        if k == key :
            continue
        # print(v, value)
        # print(v[:3],value[-3:])
        if v[-3:] == value[:3] :
            print(k,key)
            # print(v, value)