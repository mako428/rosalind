# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa

# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

# Sample Dataset:
# 1 0 0 1 0 1
# (i.e. there is a total population of 3 couples, 1 couple is AA-AA, 1 couple is Aa-Aa, and 1 couple is aa-aa.)

# Sample output:
# 3.5

def iev(AAAA,AAAa,AAaa,AaAa,Aaaa,aaaa) :
    pop = AAAA + AAAa + AAaa + AaAa + Aaaa + aaaa
    print(AAAA * 2 +
          AAAa * 2 +
          AAaa * 2 +
          AaAa * 2 * (0.75) +
          Aaaa * 2 * (0.5) +
          aaaa * 2 * (0))

iev(18471, 17729, 16801, 17429, 16532, 19428)

        
    # probability of 1 or more dominant alleles after 2 randomly selected mating pairs in a population
    # AA = number of homozygous dominant organisms
    # Aa = number of heterozygous
    # aa = number of homozygous recesive organisms

""" print(AA / pop +
      Aa / pop * (1 * AA / (pop - 1) + 0.75 * (Aa - 1) / (pop - 1) + 0.5 * aa / (pop - 1)) +
      aa / pop * (0 * (aa-1) / (pop - 1) + 0.5*Aa/(pop - 1) + 1*(AA/(pop - 1)))) """