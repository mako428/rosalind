# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# Sample Output
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6
import re

file = input('Input file name:')
if len(file) < 1 :
    file = 'C:/Users/mak/Documents/coding-misc/rosalind/stronghold/10-cons-sample.txt'
fh = open(file)

dict_fastas = dict()

# read document and add fasta ids and corresponding DNA sequences to a dictionary as key/values
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

lengths_list = list()
list_dstrings = list()

totals = dict()
ntdict = dict()

# totals = dictionary of number of occurences of a nucleotide by position in sequence.
# key is 'nt position' + 'nucelotide' (e.g. 2A, 3C, etc.)
# value is number of occurences
maxseq = max(len(v) for k,v in (dict_fastas.items()))
# print(maxseq)
for x in range(maxseq) :
    for id, seq in dict_fastas.items() :
        lengths_list.append(len(seq))
        if f'{x}A' not in totals :
            totals[f'{x}A'] = 0
        if f'{x}C' not in totals :
            totals[f'{x}C'] = 0
        if f'{x}G' not in totals :
            totals[f'{x}G'] = 0
        if f'{x}T' not in totals :
            totals[f'{x}T'] = 0
        if seq[x] == 'A' :
            totals[f'{x}A'] += 1
        elif seq[x] == 'C' :
            totals[f'{x}C'] += 1
        elif seq[x] == 'G' :
            totals[f'{x}G'] += 1
        elif seq[x] == 'T' :
            totals[f'{x}T'] += 1
    
    # ntdict = a dictionary with nt position as key, and a list of number of occurences as values, ordered by A, C, G, T
    ntdict[x] = [totals[f'{x}A'],totals[f'{x}C'],totals[f'{x}G'],totals[f'{x}T']]
print(ntdict)
print(totals)

# for x in range(maxseq) :
#     print('max occurences:',max(totals[f'{x}A'],totals[f'{x}C'],totals[f'{x}G'],totals[f'{x}T']))

# find consensus seq
conseq = ''
for k, v in ntdict.items() :
    # print(k, v),# print(type(v))
    if max(v) == v[0] :
        # print('A')
        conseq = conseq + 'A'
    elif max(v) == v[1] :
        # print('C')
        conseq = conseq + 'C'
    elif max(v) == v[2] :
        # print('G')
        conseq = conseq + 'G'
    elif max(v) == v[3] :
        # print('T')
        conseq = conseq + 'T'
print(f'{len(conseq)} nt:',conseq)


# for i in range(len())

# for k, v in totals.items() :
#     for i in range(len())
    
            
            
    
         
        
# print(list_dstrings)
# for a, b, c, d, e, f, g, in zip(list_dstrings[0],list_dstrings[1],list_dstrings[2],list_dstrings[3],list_dstrings[4],list_dstrings[5],list_dstrings[6]) :
#     count 'A'
