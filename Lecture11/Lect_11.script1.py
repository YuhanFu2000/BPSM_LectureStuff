#!/usr/bin/python3

# Program to take a DNA sequence and calculate A+T content
# Written by s123456 on 22 Oct 2024
#--------------------------------------------#
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("A+T content is " + str(at_content))
A+T content is 0.685185185185
