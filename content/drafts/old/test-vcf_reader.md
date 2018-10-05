Title: test vcf_reader
Date: 2013-06-18 22:10
Author: monsterbashseq
Category: Bioinformatics, Python, virtualenv
Slug: test-vcf_reader
Status: published

once you get a virtualenv set up and pyvcf installed, you can work with
vcf files:

import vcf

with open('F0--R0.vcf') as vcf\_reader:  
for record in vcf\_reader:  
print(record)
