Title: Finding coding sequences in DNA
Date: 2013-11-29 20:33
Author: monsterbashseq
Category: Python
Slug: possible-combinations
Status: published

From the UCSD "Bioinformatics Algorithms" class, [programming
assignments week
2](https://beta.stepic.org/Bioinformatics-Algorithms-2/How-Do-Bacteria-Make-Antibiotics-96/#step-6).

Given a DNA sequence and an amino acid peptide sequence:

    DNA="ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
    aapeptide="MA"

I want to find all occurrences (including reverse compliment) of the
coding sequence in the DNA for that amino acid peptide sequence. Example
output:

         ATGGCC
         GGCCAT
         ATGGCC

Because the genetic code is
[degenerate](http://en.wikipedia.org/wiki/Codon_degeneracy), there may
be multiple possible coding sequences for the amino acid peptide in a
strand (sequence) of DNA.

Python coding steps:

1\. From a Python dictionary "aminos" with aa as keys and RNA codons as
values, make a new dictionary with aa position (depending on length of
aa sequence given) as keys and a list of possible RNA codons as values:

    def aminoacid_codons(aapeptide):
        aminos={'I':['AUU','AUC','AUA'],'L':['CUU','CUC','CUA','CUG','UUA','UUG'],  
               'V':['GUU','GUC','GUA','GUG'],'F':['UUU','UUC'],'M':['AUG'],  
               'C':['UGU','UGC'],'A':['GCU','GCC','GCA','GCG'],'G':['GGU','GGC','GGA','GGG'],  
               'P':['ACU','ACC','ACA','ACG'],'T':['ACU','ACC','ACA','ACG'],  
               'S':['UCU','UCC','UCA','UCG','ACU','AGC'],'Y':['UAU','UAC'],  
               'W':['UGG'],'Q':['CAA','CAG'],'N':['AAU','AAC'],'H':['CAU','CAC'],  
               'E':['GAA','GAG'],'D':['GAU','GAC'],'K':['AAA','AAG'],  
               'R':['CGU','CGC','CGA','CGG','AGA','AGG'],'X':['UAA','UAG','UGA']}
        codon_dict={}
        count=0
        for aa in aapeptide:
             count+=1
             codon_dict[count]=aminos[aa]         
        return codon_dict

    aapeptide="MA"
    print(aminoacid_codons(aapeptide))

Output from the above function:

    {1: ['AUG'], 2: ['GCU', 'GCC', 'GCA', 'GCG']}

2\. Construct different sequences with 2 codons each from all
possibilities. The reverse compliment should also be considered.

[How do I randomly select an item from a list in
Python](http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python)?
See Python, [pseudorandom
module](http://docs.python.org/3.1/library/random.html).

    import random

[How many dictionary keys are
there](http://stackoverflow.com/questions/2212433/counting-the-number-of-keywords-in-a-dictionary-in-python)?

    def aa_DNA(codon_dict):
       codon_positions=len(codon_dict)
       position=1
       codon_range=range(position,codon_positions)
       while position<=codon_positions:
          listofcodons=codon_dict[position]

3\. Randomly select an item from "listofcodons" so that when it is
selected it should be removed from the list and can't be selected again:

    This is where I'm stuck.

4\. Return a list of all RNA combinations.  
5. Convert to DNA

    DNA=RNAstring.replace('U','T')

6\. Deal with reverse compliment.

7\. Input DNA sequence, reverse compliment

8\. Compare input with possibilities
