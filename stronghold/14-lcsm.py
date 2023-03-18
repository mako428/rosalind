""" 
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC 
"""

# file = input('Input file path:')
# if len(file) < 1 :
#     file = 'C:/Users/mak/Documents/coding-misc/rosalind/stronghold/14-lcsm-sample.txt'
# file_handle = open(file)

def parse_fasta_dict(fasta_file_path, number_of_seqs_plz=None,) :
    if fasta_file_path == None :
        file = input('Input file path:')
        if len(file) < 1 :
            file = 'C:/Users/mak/Documents/coding-misc/rosalind/stronghold/14-lcsm-sample.txt'
    else :
        file = fasta_file_path
    fh = open(file)
    dict_fastas = dict()
    # read document and add fasta ids and their DNA sequences to a dictionary as key/values
    for line in fh :
        if line[0] == '>' :
            # if line contains new >fasta id, add previous id and dnastring to dictionary unless it is the first entry
            try :
                # print(len(dnastring),'nt :',dnastring)
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
    # print(len(dnastring),'nt :',dnastring)
    dict_fastas[fasta_id]= dnastring
    # prints final dictionary
    print('FASTA dictionary completed')
    # print optional summary stats on the FASTA parsing
    if number_of_seqs_plz == None :
        number_of_seqs_plz = input('Print basic stats on parsed FASTAs? (Y/N): ' )
    if number_of_seqs_plz == 'y' or number_of_seqs_plz == 'Y' :
        print('Number of sequences:',len(dict_fastas))
        import statistics
        lengths = list()
        for k, v in dict_fastas.items() :
            lengths.append(len(v))
        # print(lengths)
        print(f'Median: {statistics.median(lengths)} nt')
        print(f'Min: {min(lengths)} nt \nMax: {max(lengths)} nt')
    # print(dict_fastas)
    fh.close()
    return dict_fastas

# use FASTA parsing function on sample
path = 'C:/Users/mak/Downloads/rosalind_lcsm (1).txt'
# for k, v in parse_fasta_dict(path).items() :
#     print(k, v)

new_dict = parse_fasta_dict(path) 

search_LCSS = input('Search largest common substring? (Y/N): ')
if search_LCSS == 'y' or search_LCSS == 'Y' :

    lengths = list()
    for k, v in new_dict.items() :
        lengths.append(len(v))
        the_key = k

    error = False
    common_substr_list = list()
    largest_common_substrings = list()
    # loop through each FASTA seq using min length FASTA as starting substring search size
    for substr_len in range(min(lengths),0,-1) :
        if len(largest_common_substrings) > 0 :
            break
            if substr_len < len(largest_common_substrings[0]) :
                continue
        print(f'\n ~ Search SubString Length : {substr_len} nt ~')
        # for k, v in new_dict.items() :
        # print(f'priming {k} as substr search root\n')
        # print(f'length {len(new_dict[the_key])} - {substr_len} = {len(new_dict[the_key]) - substr_len + 1} windows')
        for x in range(len(new_dict[the_key]) - substr_len) :
            # print('sliding window incrementer...',x)
            search_string = new_dict[the_key][0 + x :substr_len + x + 1] # problem spot, define the search string
            # print('searching substring:',search_string)
            substr_count = 0
            for key, value in new_dict.items() :
                # print(f'searching {key} for substring')
                if search_string not in value :
                    continue
                if search_string in value :
                    substr_count = substr_count + 1
                    # print(f'found substring in {key} : {substr_count} / {len(new_dict)} queries')
                    if substr_count == len(new_dict) :
                        if search_string in common_substr_list :
                            print(f' --- repeat substring found --- \n{len(search_string)} nt\n\n')
                        if search_string not in common_substr_list :
                            print(f' ---- NEW COMMON SUBSTRING FOUND ---- \n{len(search_string)} nt\n\n')
                            # print(f'{search_string[0:5]}...{search_string[len(search_string - 2:len(search_string))]}' )
                            # if search_string not in common_substr_list :
                            common_substr_list.append(search_string)
                            for substr in common_substr_list :
                                if len(search_string) >= len(substr) :
                                    if substr not in largest_common_substrings :
                                        largest_common_substrings.append(search_string)
    print(f'total common substring count: {len(common_substr_list)}')
    print(f'total largest common substrings: {len(largest_common_substrings)}')
    for lcss in largest_common_substrings :
        for x in largest_common_substrings :
            if len(lcss) != len(x) :
                print(f'Error in LargestCommonSubStrings database\nLengths not equal: {len(lcss)}nt, {len(x)}')
                error = True
    if error != True :
        print(f'~ Length {len(largest_common_substrings[0])} nt ~')
        print(largest_common_substrings)
    





# longest_substr = ''
# for k, v in new_dict.items() :
#     for key, value in new_dict.items() :
#         # for i in range(min(lengths),0,-1) :
#         #     print(i)
            