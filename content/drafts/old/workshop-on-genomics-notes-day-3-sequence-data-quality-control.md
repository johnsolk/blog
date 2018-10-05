Title: Workshop on Genomics (Notes, Day 3) – Sequence Data Quality Control
Date: 2014-01-15 09:23
Author: monsterbashseq
Category: Genomics Workshop
Slug: workshop-on-genomics-notes-day-3-sequence-data-quality-control
Status: published

Use this link for starting AWS instance:
http://www.google.com/url?q=http%3A%2F%2Fbit.ly%2Fevomics2014&sa=D&sntz=1&usg=AFQjCNHw6fapggOZ33Pu5k5cSJeiduXRZg

Today's lab topic:
http://evomics.org/learning/quality-assessment-and-control-of-sequence-data/

http://www.flickr.com/photos/lpcohen/11964515385/

Quality control is important: sequencing, library prep

Given sequence files from instruments, quality scores, Phred - Wiki is
good: http://en.wikipedia.org/wiki/FASTQ\_format

Quiz: What are phred scores (and probability of error) of first bases of
sequence?  
(Only latest Illumina data has stars at the end.)

Generate quality plots, quality vs. position in read (bp). Towards end
of sequence, quality drops.

Make decisions:  
- trim to certain length  
- trim bad bases  
- discard bad quality reads

Stacks has program to clean data and remove low-quality reads.

Programs for data cleaning: list: FASTX-Toolkit, other programs (links
on powerpoint)

Nucleotide composition, are they what you expect? Consider barcodes,
restriction enzymes.

Problem Set, 3 Illumina datasets: "The goal of this exercise is to
inspect the sequence data of an Illumina run."

DATASET 1  
*bartonella\_illumina.fastq: a small subset of an Illumina run (v.1.5)
belonging to a bovine isolate of the intracellular bacterium Bartonella*

1\. Launch FastQC by typing fastqc in the terminal window. (If you want
to run fastqc in commandline, run:

    fastqc -h

Then, send commands to outfile to open and view results.

[![Screenshot from 2014-01-15
14:59:48](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-145948.png?w=640){.alignnone
.size-large .wp-image-755 width="640"
height="577"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-145948.png)

This is the GUI:  
[![Screenshot from 2014-01-15
14:30:25](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143025.png?w=640){width="640"
height="380"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143025.png)

2\. Load the bartonella\_illumina.fastq file into FastQC (File-&gt;Open).
You can view the results either within the FastQC application or the
exported report.  
3. Inspect the data contained in the sequence file,
bartonella\_illumina.fastq. Have a look at the numbers output on the
“Basic Statistics” page. How many sequences do we have?

    1000

What is the sequence length?

    38

And the GC content?

    %GC = 37

Examine the “Per base sequence quality” and ”Per sequence quality
scores” pages.

[![Screenshot from 2014-01-15
14:33:13](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143313.png?w=640){.alignnone
.size-large .wp-image-748 width="640"
height="481"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143313.png)

Roughly, how many incorrect base calls are expected at most positions?

    Between 34-36

Do you think this run gave good quality sequences?

    Yes, towards the upper range (40)

Examine the “Per base sequence content”, “Per base GC content” and “Per
sequence GC content” pages. FastQC points out a “potential problem” with
an orange exclamation mark. Do you think we should worry about it in
this particular case?
[Hint.](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/2%20Basic%20Operations/2.2%20Evaluating%20Results.html)

[![Screenshot from 2014-01-15
14:37:59](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143759.png?w=640){.alignnone
.wp-image-749 width="451"
height="337"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143759.png)

[![Screenshot from 2014-01-15
14:38:18](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143818.png?w=640){.alignnone
.wp-image-750 width="369"
height="277"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143818.png)
[![Screenshot from 2014-01-15
14:38:33](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143833.png?w=640){.alignnone
.wp-image-751 width="368"
height="275"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-143833.png)

     
    It depends on the dataset, if the results are expected.

Examine the “Overrepresented sequences” page. Why does FastQC give a
warning message?

[![Screenshot from 2014-01-15
14:45:18](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-144518.png?w=640){.alignnone
.size-large .wp-image-753 width="640"
height="125"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-144518.png)

    Possible adapter sequence, look this up to see if it makes sense to be in the dataset.

DATASET 2  
*EMP\_Misc\_16v4EMP\_NoIndex\_L005\_R1\_001-sample.fastq.gz: a small
subset of an Illumina run (v.1.9) belonging to one Earth Microbiome
Project environmental sample sequenced for 16S amplicons (demultiplexed
from a set of pooled samples).*

1\. Load the data into FASTQC (note that there is no need to unzip it
first).  
2. What can explain the nucleotide frequency pattern observed in the 8
first bases?

[![Screenshot from 2014-01-15
14:50:06](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-145006.png?w=640){.alignnone
.size-large .wp-image-754 width="640"
height="486"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-15-145006.png)

    Barcode?

3.What can explain the nucleotide frequency pattern observed in the rest
of the sequence?

    Environmental sample with community of bacteria, conserved region of 16S

4\. Would you be worried in this case about the sequence duplications
levels, overrepresented sequences and kmer content? Why?

    Frequencies of different bacteria in sample.

Exercise 2:  
http://hannonlab.cshl.edu/fastx\_toolkit/commandline.html  
Remove the sequences that have more than 25% of the bases with Q &lt; 30
using the appropiate fastx-toolkit program (once you find it, use “-h”
option for usage). Note that you need to add “-Q 33″ to the command as
the sequences have a different encoding (Phred + 33) than the default of
fastx-toolkit (Phred + 64). How many reads are kept at the end of the
process?

    ubuntu@domU-12-31-39-02-88-C1:~/qc$ fastq_quality_filter -i SRR026762-sample.fastq -q 30 -Q 33 -v -p 75 -o output.fastq
    Quality cut-off: 30
    Minimum percentage: 75
    Input: 100000 reads.
    Output: 53832 reads.
    discarded 46168 (46%) low-quality reads.

Clip the adaptor sequence of the quality filtered file using the
appropiate fastx-toolkit program (once you find it, use “-h” option for
usage). Set the options so that you remove the sequences that are
shorter than 8 nucleotides and that you see the number of kept and
discarded sequences on screen. Note that you need to add “-Q 33″ to the
command as the sequences have a different encoding (Phred + 33) than the
default of fastx-toolkit (Phred + 64). How many reads are kept at the
end of the process?

    ubuntu@domU-12-31-39-02-88-C1:~/qc$ fastx_clipper -a ATCTCGTATGCCGTCTTCTGCTTG -l 8 -v -Q 33 -i output.fastq -o SRR026762-sample-qf-at.fastq
    Clipping Adapter: ATCTCGTATGCCGTCTTCTGCTTG
    Min. Length: 8
    Input: 53832 reads.
    Output: 52701 reads.
    discarded 461 too-short reads.
    discarded 553 adapter-only reads.
    discarded 117 N reads.

Trimming the adapter sequences sometimes may worsen the overall quality
scores. There are two types of overrepresented sequences, Library prep
and others have no hit. Sequencing primers, primer dimers, are being
added to library and being sequenced. This happens in microRNA
sequencing often because they're so small. Remove these by aligning to
see if they all match, then trim. Use program designed to work with
microRNA and take into account adapter sequences and primer dimers.
