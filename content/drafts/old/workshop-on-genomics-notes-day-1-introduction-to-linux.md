Title:  Workshop on Genomics (Notes, Day 1) - Introduction to Linux
Date: 2014-01-13 15:56
Author: monsterbashseq
Category: Genomics Workshop, Linux
Slug: workshop-on-genomics-notes-day-1-introduction-to-linux
Status: published

http://www.flickr.com/photos/lpcohen/11932547005/

![](http://imgs.xkcd.com/comics/regular_expressions.png){.alignnone
width="510" height="515"}

Lecture slides:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2014/01/2014\_genomics\_IntroUnixPart1.pdf

Linux tutorial: http://evomics.org/learning/unix-tutorial/

Bioinformatics analysis, computational biology requires knowing
UNIX/Linux.

Try to work in 2 terminals: one to keep track of files, one to execute
commands

Slides, practice commands, navigating through paths

tab completion: auto-complete

up-arrow: history

variants to ls:

    ls -l
    ls -la
    ls -lh

Four ways to view text file:

Assignment:

<div dir="ltr">

1\. Move to the directory /etc

</div>

<div dir="ltr">

• What is the first line of the files ‘hosts’ in the directory /etc?

</div>

    127.0.0.1 localhost

<div dir="ltr">

• What is the relative file path to get to /var/log from here?

</div>

    ../var/log

<div dir="ltr">

• What is the absolute path?

</div>

    127.0.0.1 localhost

<div dir="ltr">

2\. Move to the directory /var/log/

</div>

<div dir="ltr">

• What is the contents on line 73 of the dmesg file?

</div>

    ubuntu@ip-10-234-15-248:/var/log$ sed -n '73,73p' dmesg
    [5536105.882829] No AGP bridge found

<div dir="ltr">

•  Without changing directories, what is the second line of the cpuinfo
file in the proc directory?

</div>

    ubuntu@ip-10-234-15-248:/var/log$ sed -n '2,2p' ../../proc/cpuinfo
    vendor_id    : GenuineIntel

<div dir="ltr">

• What is the command to read this file with a relative path?

</div>

    ubuntu@ip-10-234-15-248:/var/log$ cat ../../proc/cpuinfo

<div dir="ltr">

• An absolute path?

</div>

    /proc/cpuinfo

<div dir="ltr">

3\. Move back to the root, what directories do you see?

</div>

    ubuntu@ip-10-234-15-248:~$ ls
    assembly             include   shell
    bin                  install   shotgun_metagenomics
    build                lib       software
    conf                 libexec   stacks
    configure_freenx.sh  logs      Templates
    Desktop              Music     tmp
    Documents            nxsetup   transcriptomics
    Downloads            Pictures  tutorial_materials
    etc                  Public    var
    genomics_tutorial    qc        Videos
    html                 sbin
    igv                  share

<div dir="ltr">

4\. Move back home, what are three ways to move home from the root?

</div>

<div dir="ltr">

This is moving from home to root:

</div>

    ubuntu@ip-10-234-15-248:~$ cd ../..

To move from root to home:

    ubuntu@ip-10-234-15-248:/$ cd
    ubuntu@ip-10-234-15-248:/$ cd ~/
    ubuntu@ip-10-234-15-248:/$ cd ~

http://www.flickr.com/photos/lpcohen/11934544713/

Mixed, 'Sequencing on illumina' slide, Phred Quality Score is a measure
of how clean peaks are . Q=-10(log10)p  
Phred scores are not magical. can use to get rid of worst data, but hard
to tell correctness  
Translated into probability  
10=1 in 10,  
20=1 in 100,  
30=1 in 1000

FASTQ,  
quality score series of letters, use ASCII code (8 bits = 2\^8
combinations = 256)

[Wiki on FASTQ](http://en.wikipedia.org/wiki/FASTQ_format) is really
good.  
IonTorrent is Phred+33  
grep -c is counting everything with '@'  
grep -c -v is counting everything except '@'  
wc is "word count"  
wc -l is line

important commands, \^C and 'man gzip' (displays manual)

Pipes, think of water moving to different steps:
program1|program2|program3

'Cut' will let you take data from specific columns:

    cut -f 10 batch_1.genotypes_1.loc

Cut, capture the output:

    cut -f 1-10 batch_1.genotypes_1.loc > genos

cut, pipe the output to grep

    cut -f 2 batch_1.genotypes_1.loc | grep -c "nnxnp"
    cut -f 1-10,15,17 batch_1.genotypes_1.loc|grep "nnxnp" > genos2

Examine a marker, translating the output

    cat batch_1.genotypes_1.loc|tr "     " "," | grep "^96053"

Ctl-v then 'Tab' will tell shell to override actual keyboard Tab command
and read Tab from file

Useful exercise, can be written in one line with | :

s\_1\_sequence.txt.gz

1\. Decompress the file  
2. Count the number of raw reads (250,000)  
3. Count the number of reads with barcode: CGATA  
(19,501)  
4. Capture all FASTQ records for ACCAT into a file called  
sample\_01.fq (you should get 18352 records, 73408 lines)  
5. Determine the count of all barcodes in the file  
286 CTAGT  
7900 TCAGA  
10659 ACTGC  
10931 TGACC  
11536 GAGAT  
11871 CTGAA  
14409 CGGCG  
14508 TGGTT  
18226 GAAGC  
18352 ACCAT  
18375 TCGAG  
19501 CGATA  
23012 AATTT  
26336 GCATT  
31136 CTAGG

Hints:  
1. Use head when building a command, cat once the command is working  
2. Look at the -n option for the head command, the -l  
option for wc  
3. The “\^” character means “must occur at beginning of line” in a grep
search  
4. Look at the grep options: -c, -v, -A, -B  
5. Read the man pages forsort and uniq to learn how to combine them

Ion Torrent is Phred+33:
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2847217/?tool=pubmed

First:  
1. grep out readlines (only the 2nd line) -&gt; pipe  
2. cut first 5 characters -&gt;pipe  
3. sort (automatically) alphabetically -&gt;pipe  
4. use uniq function with count, tells you how many times it counts &gt;
to file answer.txt  
5. open file

    head -n 100 s_1_sequence.txt | grep -A 1 '^@' | grep -v "^@" | grep -v "^--" | cut -c 1-5
