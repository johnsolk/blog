Title: Workshop on Genomics (Week 2, Day 3) - Transcriptomics
Date: 2014-01-22 09:27
Author: monsterbashseq
Category: Genomics Workshop
Slug: workshop-on-genomics-week-2-day-3-transcriptomics
Status: published

Dr. Manual Garber:

http://www.flickr.com/photos/lpcohen/12086234516/

Lecture slides:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2013/03/evomics\_krumlov\_2014.pdf

Exercises: http://evomics.org/learning/genomics/transcriptomics/\#part1

Exercise 1: Prepare for genomic alignment (when there is reference
genome)  
Exercise 2: Genome alignment of RNA-seq reads

> Question: What percent of reads were mapped for each library?

    ubuntu@ip-10-151-69-171:~/transcriptomics/tophat$ cat th.quant.ctrl1/align_summary.txt th.quant.ctrl2/align_summary.txt th.quant.ctrl3/align_summary.txt th.quant.expr1/align_summary.txt th.quant.expr2/align_summary.txt th.quant.expr3/align_summary.txt
    Left reads:
              Input     :     24288
               Mapped   :     23768 (97.9% of input)
                of these:       511 ( 2.1%) have multiple alignments (65 have >20)
    Right reads:
              Input     :     24288
               Mapped   :     23770 (97.9% of input)
                of these:       515 ( 2.2%) have multiple alignments (65 have >20)
    97.9% overall read mapping rate.

Aligned pairs: 23746  
of these: 505 ( 2.1%) have multiple alignments  
442 ( 1.9%) are discordant alignments  
95.9% concordant pair alignment rate.  
Left reads:  
Input : 15693  
Mapped : 15181 (96.7% of input)  
of these: 388 ( 2.6%) have multiple alignments (50 have &gt;20)  
Right reads:  
Input : 15693  
Mapped : 15164 (96.6% of input)  
of these: 387 ( 2.6%) have multiple alignments (50 have &gt;20)  
96.7% overall read mapping rate.

Aligned pairs: 15143  
of these: 381 ( 2.5%) have multiple alignments  
286 ( 1.9%) are discordant alignments  
94.7% concordant pair alignment rate.  
Left reads:  
Input : 17008  
Mapped : 16497 (97.0% of input)  
of these: 300 ( 1.8%) have multiple alignments (32 have &gt;20)  
Right reads:  
Input : 17008  
Mapped : 16500 (97.0% of input)  
of these: 299 ( 1.8%) have multiple alignments (32 have &gt;20)  
97.0% overall read mapping rate.

Aligned pairs: 16478  
of these: 295 ( 1.8%) have multiple alignments  
270 ( 1.6%) are discordant alignments  
95.3% concordant pair alignment rate.  
Left reads:  
Input : 17568  
Mapped : 17068 (97.2% of input)  
of these: 225 ( 1.3%) have multiple alignments (13 have &gt;20)  
Right reads:  
Input : 17568  
Mapped : 17070 (97.2% of input)  
of these: 225 ( 1.3%) have multiple alignments (13 have &gt;20)  
97.2% overall read mapping rate.

Aligned pairs: 17047  
of these: 223 ( 1.3%) have multiple alignments  
185 ( 1.1%) are discordant alignments  
96.0% concordant pair alignment rate.  
Left reads:  
Input : 21020  
Mapped : 20497 (97.5% of input)  
of these: 238 ( 1.2%) have multiple alignments (13 have &gt;20)  
Right reads:  
Input : 21020  
Mapped : 20499 (97.5% of input)  
of these: 243 ( 1.2%) have multiple alignments (13 have &gt;20)  
97.5% overall read mapping rate.

Aligned pairs: 20463  
of these: 237 ( 1.2%) have multiple alignments  
216 ( 1.1%) are discordant alignments  
96.3% concordant pair alignment rate.  
Left reads:  
Input : 9101  
Mapped : 8598 (94.5% of input)  
of these: 88 ( 1.0%) have multiple alignments (6 have &gt;20)  
Right reads:  
Input : 9101  
Mapped : 8597 (94.5% of input)  
of these: 91 ( 1.1%) have multiple alignments (6 have &gt;20)  
94.5% overall read mapping rate.

Aligned pairs: 8583  
of these: 88 ( 1.0%) have multiple alignments  
86 ( 1.0%) are discordant alignments  
93.4% concordant pair alignment rate.
