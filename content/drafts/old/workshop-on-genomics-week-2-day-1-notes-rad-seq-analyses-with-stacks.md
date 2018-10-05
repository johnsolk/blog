Title: Workshop on Genomics (Week 2, Day 1, Notes) - RAD-Seq analyses with STACKS
Date: 2014-01-20 10:58
Author: monsterbashseq
Category: Genomics Workshop
Slug: workshop-on-genomics-week-2-day-1-notes-rad-seq-analyses-with-stacks
Status: published

Czech food:

http://www.flickr.com/photos/lpcohen/12057609436/

Exercise:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2013/03/cesky\_2014\_RAD\_tutorial.pdf

Start Amazon instance:
https://console.aws.amazon.com/ec2/v2/home?region=us-east-1\#Instances:

STACKS Pipeline:

Part 1. Cleaning raw data:  
- take raw reads, process RAD-tags to throw away  
- Illumina big digital camera, clusters can sometimes interfere with
each other to give mixed signals  
- Phred quality scores interpret sequences: 0-40 on log scale, series of
ASCII code letters  
- difference between fasta and fastq  
- "process RAD-tags" will convert ASCII to numbers

Data sets we will be working with from
[stickleback](http://en.wikipedia.org/wiki/Stickleback): samples have
in-line (first 5 nucleotides, in this case) bar codes, then also indexed
bar code with special Illumina bar codes get put by software in special
place at second and third passes of each paired ends - this gets put
into ID header line of the fastq file, you tell the "process RAD-tags"
program which barcode to use

When cleaning data, want to get rid of worst of worst data - use
process\_shortreads or STACKS "process RAD-tags" to clean data

Stay organized in shell by setting up hierarchy directory structure for
each step. "...each step of the analysis takes its input from one
directory and places it into another directory, this is known as a
‘waterfall workspace'... A well-organized workspace makes analyses
easier and prevents data from being overwritten. "

[Unzip](http://www.cyberciti.biz/faq/howto-open-a-tar-gz-file-in-linux-unix/)
files: multiple ways of tar, one is: tar -zxvf

    ubuntu@ip-10-151-69-171:~/stacks/clean/lane1$ tar -xvf /stacks_data/clean/lane1.tar
    lane1_NoIndex_L001_R1_001.fastq.gz
    lane1_NoIndex_L001_R1_002.fastq.gz
    lane1_NoIndex_L001_R1_003.fastq.gz
    lane1_NoIndex_L001_R1_004.fastq.gz

Stacks manual, process\_radtags:  
http://creskolab.uoregon.edu/stacks/comp/process\_radtags.php

Fantastic Linux command line tool:
[explainshell.com](http://explainshell.com)  
Will explain command-line commands line part by part. Interactive and
easy to interpret.

(Advise: If you have problems with .gz files, sometimes you have to
gunzip and gzip them back again, the hardware with instances sometimes
is finicky.)

    ubuntu@ip-10-151-69-171:~/stacks/clean$ process_radtags -e 'sbfI' -p ./lane1 -b lane1_barcodes -o ./samples -c -q -r -E phred33
    Using Phred+33 encoding for quality scores.
    Found 4 input file(s).
    Searching for single-end, inlined barcodes.
    Loaded 95 barcodes (6bp).
    Processing file 1 of 4 [lane1_NoIndex_L001_R1_004.fastq]
      4000000 total reads; -225528 ambiguous barcodes; -167972 ambiguous RAD-Tags; +190285 recovered; -322184 low quality reads; 3284316 retained reads.
    Processing file 2 of 4 [lane1_NoIndex_L001_R1_001.fastq]
      4000000 total reads; -230133 ambiguous barcodes; -169979 ambiguous RAD-Tags; +187630 recovered; -380013 low quality reads; 3219875 retained reads.
    Processing file 3 of 4 [lane1_NoIndex_L001_R1_002.fastq]
      4000000 total reads; -235444 ambiguous barcodes; -172704 ambiguous RAD-Tags; +205939 recovered; -422009 low quality reads; 3169843 retained reads.
    Processing file 4 of 4 [lane1_NoIndex_L001_R1_003.fastq]
      4000000 total reads; -228896 ambiguous barcodes; -169804 ambiguous RAD-Tags; +201360 recovered; -348627 low quality reads; 3252673 retained reads.
    Closing files, flushing buffers...
    Outputing details to log: './samples/process_radtags.log'

    16000000 total sequences;
      920001 ambiguous barcode drops;
      1472833 low quality read drops;
      680459 ambiguous RAD-Tag drops;
    12926707 retained reads.

To perform dry run, to check if all parameters are entered correctly and
files are in the proper location, use -d for "dry run".

    Total Sequences 16000000
    Ambiguous Barcodes      920001
    Low Quality     1472833
    Ambiguous RAD-Tag       680459
    Retained Reads  12926707

Reasons why sequences were dropped: ambiguous barcode, ambiguous
RAD-Tag, low quality reads

Ambiguous barcodes are read by the software multiple times at the
beginning of reads but do not match against the input list of barcodes.
There is one in our list that occurs many times but was not specified by
the barcode list, so these were all thrown away. This might be a
mistake, so check with technician?

    Sequences not recorded
    Barcode Total
    AATATC  190381
    CCTCTG  10260
    TGTGTG  3266
    GTGTGT  2117

[rename
files](http://stackoverflow.com/questions/18686832/rename-all-files-in-folder-to-numbered-list-1-jpg-2-jpg):

    ls | cat -n | while read n f; do mv "$f" "file-$n.jpg"; done

Also, can use:

    ls -l

Paired reads are phased. If going through file by pairs, if one read
gets thrown away because of quality issues the other read will be out of
phase, therefore a remainder file .rem.fq is made to allow you to keep
track. The partner didn't match. These can be added back later.

Stacks flow chart:  
1. process\_radtags  
2. reference genome? -&gt; ustacks (no reference)/pstacks (reference)
-&gt; cstacks -&gt;sstacks  
3. genotypes program  
4.

Look at original STACKS paper.  
- stacks = alleles  
- break down into kmers, load into dictionary, reduce search space that
may match with other alleles (lowest connection), merge together, those
become loci

Could be more than one minimum spanning tree, de-leveraging algorithm

If there were some reads with not enough to make a stack, those are set
aside, and a more permissive algorithm is used later (these will be
divided into primary and secondary reads). SNP-calling model can handle
error. More depth/reads, differentiating SNP from error.

If you're running a job that takes several hours, if you disconnect from
terminal, your job will be terminated. Inside terminal, type 'screen',
which is another terminal, that will allow you to run your job over
several days, log on/off from different computers. Can have multiple
screens, screen -ls will tell you how many screens you have running,
communicate command to screen, use ctrl-a. ctrl-a ctrl-d disconnections.

View stacks data with backend database, program has database connection
through mysql.

(Unix convention: % means "prompt", don't have to actually type this.)

Daemon runs database in background. Indexing big datasets. Structured
query language allowing people to interact with database. Series of
tables connected. Structured query language links tables. .php files are
web-interface of sql files.

Use regular expressions to help build list of samples:

    # always beginning of line
    ^
    # always end of line
    $

Editing a file (these were used to add "-s samples/" onto beginning):

    cat stacks_script | sed -E 's/^/-s samples\//' > stacks_script_path

    Adding / onto end:
    cat stacks_script_path | sed -E 's/$/ \\/' > stacks_script_path

This was the final script to run:

    sh stacks_script_run

Contents of file:

    denovo_map.pl -o .. -B orphy_radtags -m 4 -M 2 -n 0 -b 1 -D "Stickleback RAD-Seq Workshop Part 1" -O po$
    -s samples/ms_2067.01.fa   
   -s samples/ms_2067.02.fa   
   -s samples/ms_2067.03.fa   
   -s samples/ms_2067.04.fa   
   -s samples/ms_2067.05.fa   
   -s samples/ms_2067.06.fa   
   -s samples/ms_2067.08.fa   
   -s samples/ms_2067.09.fa   
   -s samples/ms_2067.10.fa   
   -s samples/ms_2067.11.fa   
   -s samples/pcr_1193.00.fa   
   -s samples/pcr_1193.01.fa   
   -s samples/pcr_1193.08.fa   
   -s samples/pcr_1193.11.fa   
   -s samples/pcr_1210.05.fa   
   -s samples/pcr_1211.01.fa   
   -s samples/pcr_1211.02.fa   
   -s samples/pcr_1211.04.fa   
   -s samples/pcr_1211.05.fa   
   -s samples/pcr_1211.06.fa   
   -s samples/rb_2217.001.fa   
   -s samples/rb_2217.003.fa   
   -s samples/rb_2217.005.fa   
   -s samples/rb_2217.006.fa   
   -s samples/rb_2217.007.fa   
   -s samples/rb_2217.010.fa   
   -s samples/rb_2217.011.fa   
   -s samples/rb_2217.014.fa   
   -s samples/rb_2217.016.fa   
   -s samples/rb_2217.018.fa   

Screen! (really cool)

    screen

Will allow you to run processes and shut down terminal and computer
while processes are still running.  
Ctrl-A+D: returns to original screen

    ubuntu@ip-10-151-69-171:~/stacks/denovo$ screen -r
    [detached from 6226.pts-1.ip-10-151-69-171]

You can run multiple screens at the same time and keep track of them
with 4-digit number before ip address, e.g. 6309.pts-1.ip-10-151-69-171:

    ubuntu@ip-10-151-69-171:~/stacks/denovo$ screen
    [detached from 6309.pts-1.ip-10-151-69-171]
    ubuntu@ip-10-151-69-171:~/stacks/denovo$ screen -r
    There are several suitable screens on:
        6309.pts-1.ip-10-151-69-171 (01/20/2014 08:37:00 PM)    (Detached)
        6226.pts-1.ip-10-151-69-171 (01/20/2014 08:35:24 PM)    (Detached)
        5992.pts-1.ip-10-151-69-171 (01/20/2014 08:29:42 PM)    (Attached)
    Type "screen [-d] -r [pid.]tty.host" to resume one of them.

Ctrl-D: deletes screen
