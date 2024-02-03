""" 
Independent Alleles - Mendel's 2nd Law


Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

Sample Dataset
2 1

Sample Output
0.684 
"""

def lia(k, N) : # k = generation, N = minimum number of AaBb organisms in the k-th generation (excluding mates)
    pop_genk = 2 ** k
    # pop_total = pop_genk
    basic_prob_AaBb_AaBb = dict()
    basic_prob_AaBb_AaBb['AA'] = 0.25
    basic_prob_AaBb_AaBb['Aa'] = 0.5
    basic_prob_AaBb_AaBb['aa'] = 0.25
    basic_prob_AaBb_AaBb['BB'] = 0.25
    basic_prob_AaBb_AaBb['Bb'] = 0.5
    basic_prob_AaBb_AaBb['bb'] = 0.25
    basic_prob_AaBb_AaBb['AaBb'] = 0.50 * 0.50
    basic_prob_AaBb_AaBb['AABB'] = 0.25 * 0.25
    basic_prob_AaBb_AaBb['AABb'] = 0.25 * 0.5
    basic_prob_AaBb_AaBb['AAbb'] = 0.25 * 0.25
    basic_prob_AaBb_AaBb['AaBB'] = 0.5 * 0.25
    basic_prob_AaBb_AaBb['Aabb'] = 0.5 * 0.25
    basic_prob_AaBb_AaBb['aaBB'] = 0.25 * 0.25
    basic_prob_AaBb_AaBb['aaBb'] = 0.25 * 0.5
    basic_prob_AaBb_AaBb['aabb'] = 0.25 * 0.25

    basic_prob_xxxx_AaBb = dict()
    basic_prob_xxxx_AaBb['Aa'] = 0.5 # ???
    basic_prob_xxxx_AaBb['Bb'] = 0.5 # ???

    gen_probs_dict = dict()
    total = 0
    for i in range(k+1) :
        if i == 0 :
            continue
        # if i == 1 :
        gen_probs_dict[f'gen{i}_AaBb'] = (
            (basic_prob_AaBb_AaBb['Aa'] * basic_prob_AaBb_AaBb['Bb']))
        # print(gen_probs_dict[f'{i}_AaBb'])
        # gen_probs_dict[f'{i}_AABb'] = (
        #     (basic_prob_AaBb_AaBb['AA'] * basic_prob_AaBb_AaBb['Bb']))
        # # print(gen_probs_dict[f'{i}_AABb'])
        # gen_probs_dict[f'{i}_AABB'] = (
        #     (basic_prob_AaBb_AaBb['AA'] * basic_prob_AaBb_AaBb['BB']))
        # # print(gen_probs_dict[f'{i}_AABB'])
        print(f'individual probability for AaBb in Gen {i}:',gen_probs_dict[f'gen{i}_AaBb'])
            
        if i == k :
            for x in range(N, pop_genk+1) :
                total += gen_probs_dict[f'gen{i}_AaBb'] ** x
            print(total)
                


        # pop_total =+ i ** 2

lia(2,1)



     
