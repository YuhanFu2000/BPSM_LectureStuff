#!/user/bin
my_dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=my_dna[0:63]
exon2=my_dna[90:]
print("### Exons joined ###\n" + exon1 + exon2)
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print("### Coding percentage (rounded) ###\n" + str(int((coding_length / total_length) * 100)))
intron=my_dna[63:90]
print("### Exon intron exon ###\n" + exon1 + intron.lower() + exon2)
