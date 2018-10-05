Title: Workshop on Genomics (Notes, Day 4) - Genomics, Alignment, Assembly
Date: 2014-01-16 10:54
Author: monsterbashseq
Category: Bioinformatics, Genomics Workshop
Slug: workshop-on-genomics-notes-day-4-genomics-alignment-assembly
Status: published

View from road in front of our computer lab building:

http://www.flickr.com/photos/lpcohen/11979295043/

Thanks to [evomics](http://evomics.org/blog/) for linking this blog!

Today's alignment and assembly exercise:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2014/01/Evomics-2014-Workshop-on-Genomics-Final-Ver-2.pdf

Advice: Do not copy and paste from the document. It is important that
you learn the commands and create a muscle memory.

> Objectives:  
> By the end of the workshop you will be expected to:  
> • Interpret FASTQ quality metrics  
> • Remove poor quality data  
> • Trim adaptor/contaminant sequences from FASTQ data  
> • Count the number of reads before and after trimming and quality
> control  
> • Align reads to a reference sequence to form a SAM file (Sequence
> AlignMent file) using BWA  
> • Convert the SAM file to BAM format (Binary AlignMent format)  
> • Identify and select high quality SNPs and Indels using SAMtools  
> • Identify missing or truncated genes with respect to the reference
> genome  
> • Identify SNPs which overlap with known coding regions
>
> Quality control usually involves:  
> • Calculating the number of reads before quality control  
> • Calculating GC content, identifying over-represented sequences  
> • Remove or trim reads containing adaptor sequences  
> • Remove or trim reads containing low quality bases  
> • Calculating the number of reads after quality control  
> • Rechecking GC content, identifying over-represented sequences

fastqc

Another tutorial I found:
https://wiki.hpcc.msu.edu/display/Bioinfo/FastQC+Tutorial

fastqc documentation:
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/  
per base sequence quality, blue line is mean quality score, then yellow
box and whiskers plot with median, quartiles, 10% and 90%:
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/2%20Per%20Base%20Sequence%20Quality.html

Link to tools to download manually: http://code.google.com/p/ea-utils/

    ubuntu@domU-12-31-39-02-88-C1:~/genomics_tutorial/strain1/illumina_reads$ fastq-mcf ~/software/ea-utils/adaptors.fasta strain1_read1.fastq strain1_read2.fastq -o strain1_read1.filtered.fastq -o strain1_read2.filtered.fastq -C 1000000 -q 20 -p 10 -u -x 0.01
    Scale used: 2.2
    Filtering Illumina reads on purity field
    Phred: 33
    Threshold used: 2501 out of 1000000
    Files: 2
    Total reads: 3247450
    Too short after clip: 0
    Trimmed 708987 reads (strain1_read1.fastq) by an average of 1.22 bases on quality < 20
    Trimmed 1037979 reads (strain1_read2.fastq) by an average of 1.36 bases on quality < 20

BWA alignment:

    ubuntu@domU-12-31-39-02-88-C1:~/genomics_tutorial/strain1/remapping_to_reference$ bwa mem -t 8 /home/ubuntu/genomics_tutorial/reference_sequence/Ecoli_UTI89.fna /home/ubuntu/genomics_tutorial/strain1/illumina_reads/strain1_read1.filtered.fastq /home/ubuntu/genomics_tutorial/strain1/illumina_reads/strain1_read2.filtered.fastq > alignment.sam
    [M::main_mem] read 2017694 sequences (80000077 bp)...
    [M::mem_pestat] # candidate unique pairs for (FF, FR, RF, RR): (1, 599354, 3, 1)
    [M::mem_pestat] skip orientation FF as there are not enough pairs
    [M::mem_pestat] analyzing insert size distribution for orientation FR...
    [M::mem_pestat] (25, 50, 75) percentile: (421, 448, 475)
    [M::mem_pestat] low and high boundaries for computing mean and std.dev: (313, 583)
    [M::mem_pestat] mean and std.dev: (448.23, 39.87)
    [M::mem_pestat] low and high boundaries for proper pairs: (259, 637)
    [M::mem_pestat] skip orientation RF as there are not enough pairs
    [M::mem_pestat] skip orientation RR as there are not enough pairs
    [M::worker2@2] performed mate-SW for 48978 reads
    [M::worker2@5] performed mate-SW for 48948 reads
    [M::worker2@4] performed mate-SW for 49052 reads
    [M::worker2@0] performed mate-SW for 49151 reads
    [M::worker2@3] performed mate-SW for 48935 reads
    [M::worker2@7] performed mate-SW for 49225 reads
    [M::worker2@6] performed mate-SW for 49367 reads
    [M::worker2@1] performed mate-SW for 48997 reads
    [M::main_mem] read 2017708 sequences (80000030 bp)...
    [M::mem_pestat] # candidate unique pairs for (FF, FR, RF, RR): (2, 600371, 3, 1)
    [M::mem_pestat] skip orientation FF as there are not enough pairs
    [M::mem_pestat] analyzing insert size distribution for orientation FR...
    [M::mem_pestat] (25, 50, 75) percentile: (421, 448, 475)
    [M::mem_pestat] low and high boundaries for computing mean and std.dev: (313, 583)
    [M::mem_pestat] mean and std.dev: (448.20, 39.86)
    [M::mem_pestat] low and high boundaries for proper pairs: (259, 637)
    [M::mem_pestat] skip orientation RF as there are not enough pairs
    [M::mem_pestat] skip orientation RR as there are not enough pairs
    [M::worker2@4] performed mate-SW for 48996 reads
    [M::worker2@3] performed mate-SW for 48949 reads
    [M::worker2@7] performed mate-SW for 48263 reads
    [M::worker2@6] performed mate-SW for 48776 reads
    [M::worker2@5] performed mate-SW for 49361 reads
    [M::worker2@2] performed mate-SW for 48919 reads
    [M::worker2@0] performed mate-SW for 48428 reads
    [M::worker2@1] performed mate-SW for 48981 reads
    [M::main_mem] read 2017724 sequences (80000066 bp)...
    [M::mem_pestat] # candidate unique pairs for (FF, FR, RF, RR): (1, 598938, 0, 0)
    [M::mem_pestat] skip orientation FF as there are not enough pairs
    [M::mem_pestat] analyzing insert size distribution for orientation FR...
    [M::mem_pestat] (25, 50, 75) percentile: (421, 448, 475)
    [M::mem_pestat] low and high boundaries for computing mean and std.dev: (313, 583)
    [M::mem_pestat] mean and std.dev: (448.23, 39.82)
    [M::mem_pestat] low and high boundaries for proper pairs: (259, 637)
    [M::mem_pestat] skip orientation RF as there are not enough pairs
    [M::mem_pestat] skip orientation RR as there are not enough pairs
    [M::worker2@3] performed mate-SW for 48813 reads
    [M::worker2@1] performed mate-SW for 48907 reads
    [M::worker2@6] performed mate-SW for 48904 reads
    [M::worker2@7] performed mate-SW for 48713 reads
    [M::worker2@0] performed mate-SW for 49468 reads
    [M::worker2@5] performed mate-SW for 49242 reads
    [M::worker2@4] performed mate-SW for 48874 reads
    [M::worker2@2] performed mate-SW for 49195 reads
    [M::main_mem] read 441774 sequences (17523121 bp)...
    [M::mem_pestat] # candidate unique pairs for (FF, FR, RF, RR): (0, 121991, 1, 0)
    [M::mem_pestat] skip orientation FF as there are not enough pairs
    [M::mem_pestat] analyzing insert size distribution for orientation FR...
    [M::mem_pestat] (25, 50, 75) percentile: (421, 448, 475)
    [M::mem_pestat] low and high boundaries for computing mean and std.dev: (313, 583)
    [M::mem_pestat] mean and std.dev: (448.17, 39.89)
    [M::mem_pestat] low and high boundaries for proper pairs: (259, 637)
    [M::mem_pestat] skip orientation RF as there are not enough pairs
    [M::mem_pestat] skip orientation RR as there are not enough pairs
    [M::worker2@2] performed mate-SW for 10541 reads
    [M::worker2@1] performed mate-SW for 10463 reads
    [M::worker2@7] performed mate-SW for 10722 reads
    [M::worker2@6] performed mate-SW for 10687 reads
    [M::worker2@4] performed mate-SW for 10608 reads
    [M::worker2@3] performed mate-SW for 10770 reads
    [M::worker2@0] performed mate-SW for 10467 reads
    [M::worker2@5] performed mate-SW for 10540 reads
    [main] Version: 0.7.5a-r405
    [main] CMD: bwa mem -t 8 /home/ubuntu/genomics_tutorial/reference_sequence/Ecoli_UTI89.fna /home/ubuntu/genomics_tutorial/strain1/illumina_reads/strain1_read1.filtered.fastq /home/ubuntu/genomics_tutorial/strain1/illumina_reads/strain1_read2.filtered.fastq
    [main] Real time: 109.392 sec; CPU: 290.150 sec

Details on sam alignment: http://samtools.sourceforge.net/SAMv1.pdf

Examine alignments with reference:[A![Screenshot from 2014-01-16
16:24:26](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-16-162426.png?w=640){.alignnone
.size-large .wp-image-761 width="640"
height="393"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-16-162426.png)

Alignment with sam or bam format:
http://www.broadinstitute.org/software/igv/AlignmentData

SNP and Indel identification, automated variant caller tools, samtools

ubuntu@domU-12-31-39-02-88-C1:\~/genomics\_tutorial/strain1/remapping\_to\_reference\$
samtools mpileup -uf
\~/genomics\_tutorial/reference\_sequence/Ecoli\_UTI89.fna
alignment.rmdup.sorted.bam | bcftools view -bvcg - &gt; var.raw.bcf  
\[mpileup\] 1 samples in 1 input files  
Set max per-file depth to 8000  
\[bcfview\] 100000 sites processed.  
\[afs\] 0:99985.000 1:0.118 2:14.883  
\[bcfview\] 200000 sites processed.  
\[afs\] 0:99999.999 1:0.000 2:0.001  
\[bcfview\] 300000 sites processed.  
\[afs\] 0:99999.998 1:0.000 2:0.002  
\[afs\] 0:53558.999 1:0.000 2:0.001

http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41
