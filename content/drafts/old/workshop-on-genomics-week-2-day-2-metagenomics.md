Title: Workshop on Genomics (Week 2, Day 2) - Metagenomics
Date: 2014-01-21 10:19
Author: monsterbashseq
Category: Bioinformatics, Genomics Workshop, software
Slug: workshop-on-genomics-week-2-day-2-metagenomics
Status: published

Interesting argument for the importance of social media. Rapid analysis
of data for diagnosis of public health-related issues before
publications/reports can be written/submitted. Also, public record of
conversations and advice that might help people learning.

Dr. Nick Loman: <http://pathogenomics.bham.ac.uk/blog/>  
http://www.flickr.com/photos/lpcohen/12066175364/

Metagenomics Lab 1 Exercise:
http://nickloman.github.io/2014/01/18/evomics-2014-metagenomics-three-hour-practical/

Using [MetaPhlan](http://huttenhower.sph.harvard.edu/metaphlan) (marker
gene method) [MEGAN](http://ab.inf.uni-tuebingen.de/software/megan5/)
(least common ancestor parameters)

Datasets from
[article](http://jama.jamanetwork.com/article.aspx?articleid=1677374):

[![Screenshot from 2014-01-21
14:06:12](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-21-140612.png?w=640){.alignnone
.size-large .wp-image-786 width="640"
height="366"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-21-140612.png)

Paired-end Illumina sequencing data, with sample ID and species names in
data files.

    ubuntu@ip-10-151-69-171:~/shotgun_metagenomics$ seqtk

    Usage:   seqtk  
    Version: 1.0-r32

    Command: seq       common transformation of FASTA/Q
             comp      get the nucleotide composition of FASTA/Q
             sample    subsample sequences
             subseq    extract subsequences from FASTA/Q
             trimfq    trim FASTQ using the Phred algorithm

             hety      regional heterozygosity
             mutfa     point mutate FASTA at specified positions
             mergefa   merge two FASTA/Q files
             randbase  choose a random base from hets
             cutN      cut sequence at long N
             listhet   extract the position of each het

    Usage: seqtk sample [-s seed=11]  |

Subsample 1000, 10000, 100000, 100000 sequences from dataset:

    %seqtk sample -s 1234 2638-H-STEC_1_final.fastq.gz 1000 > 2638_1000_1.fastq
    %seqtk sample -s 1234 2638-H-STEC_2_final.fastq.gz 1000 > 2638_1000_2.fastq
    %cat 2638_1000_1.fastq 2638_1000_2.fastq > 2638_1000.fastq

    ubuntu@ip-10-151-69-171:~/shotgun_metagenomics$ metaphlan.py 2638_1000.fastq --bowtie2db ~/software/metaphlan/bowtie2db/mpa --bt2_ps sensitive-local --nproc 8
    k__Bacteria     100.0
    k__Bacteria|p__Proteobacteria   100.0
    k__Bacteria|p__Proteobacteria|c__Gammaproteobacteria    100.0
    k__Bacteria|p__Proteobacteria|c__Gammaproteobacteria|o__Enterobacteriales       100.0
    k__Bacteria|p__Proteobacteria|c__Gammaproteobacteria|o__Enterobacteriales|f__Enterobacteriaceae 100.0
    k__Bacteria|p__Proteobacteria|c__Gammaproteobacteria|o__Enterobacteriales|f__Enterobacteriaceae|g__Escherichia  100.0
    k__Bacteria|p__Proteobacteria|c__Gammaproteobacteria|o__Enterobacteriales|f__Enterobacteriaceae|g__Escherichia|s__Escherichia_unclassified 100.0

More reads change taxonomic assignment (presumably makes them more
accurate):  
[![Screenshot from 2014-01-21
15:10:11](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-21-151011.png?w=640){.alignnone
.size-large .wp-image-787 width="640"
height="116"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-21-151011.png)

MEGAN (Metagenomics Analysis tool)  
Demonstration:  
http://youtu.be/R8dpD\_lj6Ts

Manual:
http://ab.inf.uni-tuebingen.de/data/software/megan5/download/manual.pdf

This is a GUI software package available under the "Other" menu of the
AWS virtual ubuntu instance.

[![Screenshot from 2014-01-21
16:18:39](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-21-161839.png?w=640){.alignnone
.size-large .wp-image-788 width="640"
height="342"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-21-161839.png)
