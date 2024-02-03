""" Given: A genus name, followed by two dates in YYYY/M/D format.

Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.

Sample Dataset
Anthoxanthum
2003/7/25
2005/12/27
Sample Output
7 """

# SAMPLE
from Bio import Entrez
# Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
record = Entrez.read(handle)
print(record["Count"])

handle1 = Entrez.esearch(db="nucleotide", term='"Anthoxanthum"[Organism] AND ("2003/7/25"[PDAT] : "2005/12/27"[PDAT])' )
record1 = Entrez.read(handle1)
print(record1["Count"])

handle2 = Entrez.esearch(db="nucleotide", term='"Iguana"[Organism] AND ("2001/12/12"[PDAT] : "2010/12/22"[PDAT])' )
record2 = Entrez.read(handle2)
print(record2["Count"])