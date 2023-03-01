# Given: Three positive integers k, m, and n, representing a pop containing k+m+n organisms:  
# k individuals are homozygous dominant for a factor,
# m are heterozygous,
# and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample Dataset
# 2 2 2
# Sample Output
# 0.78333

def iprb(AA,Aa,aa) :
    pop = AA + Aa + aa
    # probability of 1 or more dominant alleles after 2 randomly selected mating pairs in a population
    # AA = number of homozygous dominant organisms
    # Aa = number of heterozygous
    # aa = number of homozygous recesive organisms

    print(AA / pop +
          Aa / pop * (1 * AA / (pop - 1) + 0.75 * (Aa - 1) / (pop - 1) + 0.5 * aa / (pop - 1)) +
          aa / pop * (0 * (aa-1) / (pop - 1) + 0.5*Aa/(pop - 1) + 1*(AA/(pop - 1))))

iprb(2,2,2)
iprb(28,21,24)

# Workflow for a population of 2 AA, 2 Aa, 2 aa
# AA     2/6 are 100% with 5/5 pairs
# Aa     2/6 are 50% with 2/5, 100% with 2/5, and 75% with 1/5, 
# aa     2/6 are 0% with 1/5, 50% with 2/5, and 100% with 2/5

#      2/6 +
#      2/6 * (0.5 * 2/5 + 1 * 2/5 + 0.75 * 1/5) +
#      2/6 * (0 * 1/5 + 0.5 * 2/5 + 1 * 2/5 )


