#!/usr/bin/python3
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1=my_dna.replace("A","t")
replacement2=replacement1.replace("T","a")
replacement3=replacement2.replace("C","g")
replacement4=replacement3.replace("G","c")
print(replacement4)
print(replacement4.upper())
