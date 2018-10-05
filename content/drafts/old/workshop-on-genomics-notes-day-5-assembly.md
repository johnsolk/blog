Title: Workshop on Genomics (Notes, Day 5) - Assembly
Date: 2014-01-17 10:00
Author: monsterbashseq
Category: Bioinformatics, Genomics Workshop
Slug: workshop-on-genomics-notes-day-5-assembly
Status: published

Bridge will be under construction tomorrow, so we must find a
cut-through:  
http://www.flickr.com/photos/lpcohen/11995110086/

Trying different assembly methods with bacterial sequences:
http://evomics.org/learning/assembly-and-alignment/2014-assembly-lab/

Using Velvet:  
http://www.ebi.ac.uk/\~zerbino/velvet/  
Manual: http://www.ebi.ac.uk/\~zerbino/velvet/Manual.pdf

Here's another tutorial on Velvet:  
https://wiki.hpcc.msu.edu/display/Bioinfo/Velvet+Short+Read+Assembly

Article: http://www.ncbi.nlm.nih.gov/pubmed/20836074

There are two main commands: velveth and velvetg

First use trimmed and split data set (about half of the reads), then try
whole dataset and see the difference.

    ubuntu@domU-12-31-39-0C-6C-E1:~$ velveth
    velveth - simple hashing program
    Version 1.2.10

    Copyright 2007, 2008 Daniel Zerbino (zerbino@ebi.ac.uk)
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    Compilation settings:
    CATEGORIES = 9
    MAXKMERLENGTH = 101

    Usage:
    ./velveth directory hash_length {[-file_format][-read_type][-separate|-interleaved] filename1 [filename2 ...]} {...} [options]

        directory   : directory name for output files
        hash_length : EITHER an odd integer (if even, it will be decremented) <= 101 (if above, will be reduced)
                : OR: m,M,s where m and M are odd integers (if not, they will be decremented) with m < M <= 101 (if above, will be reduced)
                    and s is a step (even number). Velvet will then hash from k=m to k=M with a step of s
        filename    : path to sequence file or - for standard input

    File format options:
        -fasta  -fastq  -raw    -fasta.gz   -fastq.gz   -raw.gz -sam    -bam    -fmtAuto
        (Note: -fmtAuto will detect fasta or fastq, and will try the following programs for decompression : gunzip, pbunzip2, bunzip2

    File layout options for paired reads (only for fasta and fastq formats):
        -interleaved    : File contains paired reads interleaved in the one file (default)
        -separate   : Read 2 separate files for paired reads

    Read type options:
        -short  -shortPaired
        ...
        -short8 -shortPaired8
        -short9 -shortPaired9
        -long   -longPaired
        -reference

    Options:
        -strand_specific    : for strand specific transcriptome sequencing data (default: off)
        -reuse_Sequences    : reuse Sequences file (or link) already in directory (no need to provide original filenames in this case (default: off)
        -reuse_binary   : reuse binary sequences file (or link) already in directory (no need to provide original filenames in this case (default: off)
        -noHash         : simply prepare Sequences file, do not hash reads or prepare Roadmaps file (default: off)
        -create_binary      : create binary CnyUnifiedSeq file (default: off)

    Synopsis:

    - Short single end reads:
        velveth Assem 29 -short -fastq s_1_sequence.txt

    - Paired-end short reads (remember to interleave paired reads):
        velveth Assem 31 -shortPaired -fasta interleaved.fna

    - Paired-end short reads (using separate files for the paired reads)
        velveth Assem 31 -shortPaired -fasta -separate left.fa right.fa

    - Two channels and some long reads:
        velveth Assem 43 -short -fastq unmapped.fna -longPaired -fasta SangerReads.fasta

    - Three channels:
        velveth Assem 35 -shortPaired -fasta pe_lib1.fasta -shortPaired2 pe_lib2.fasta -short3 se_lib1.fa

    Output:
        directory/Roadmaps
        directory/Sequences
            [Both files are picked up by graph, so please leave them there]
    ubuntu@domU-12-31-39-0C-6C-E1:~$ ls
    assembly             include   shell
    bin                  install   shotgun_metagenomics
    build                lib       software
    conf                 libexec   stacks
    configure_freenx.sh  logs      Templates
    Desktop              Music     tmp
    Documents            nxsetup   transcriptomics
    Downloads            Pictures  tutorial_materials
    etc                  Public    UTI189.genome
    genomics_tutorial    qc        var
    html                 sbin      Videos
    igv                  share
    ubuntu@domU-12-31-39-0C-6C-E1:~$ cd assembly
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ ls
    vcholerae_reads_1.trimmed.fastq.gz
    vcholerae_reads_1.trimmed.subsampled.250k.fastq.gz
    vcholerae_reads_2.trimmed.fastq.gz
    vcholerae_reads_2.trimmed.subsampled.250k.fastq.gz
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ gunzip vcholerae_reads_1.trimmed.subsampled.250k.fastq.gz 
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ gunzip vcholerae_reads_2.trimmed.subsampled.250k.fastq.gz 
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ gzip --help
    Usage: gzip [OPTION]... [FILE]...
    Compress or uncompress FILEs (by default, compress FILES in-place).

    Mandatory arguments to long options are mandatory for short options too.

      -c, --stdout      write on standard output, keep original files unchanged
      -d, --decompress  decompress
      -f, --force       force overwrite of output file and compress links
      -h, --help        give this help
      -l, --list        list compressed file contents
      -L, --license     display software license
      -n, --no-name     do not save or restore the original name and time stamp
      -N, --name        save or restore the original name and time stamp
      -q, --quiet       suppress all warnings
      -r, --recursive   operate recursively on directories
      -S, --suffix=SUF  use suffix SUF on compressed files
      -t, --test        test compressed file integrity
      -v, --verbose     verbose mode
      -V, --version     display version number
      -1, --fast        compress faster
      -9, --best        compress better
      --rsyncable       Make rsync-friendly archive

    With no FILE, or when FILE is -, read standard input.

    Report bugs to .
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ ls
    vcholerae_reads_1.trimmed.fastq.gz               vcholerae_reads_2.trimmed.fastq.gz
    vcholerae_reads_1.trimmed.subsampled.250k.fastq  vcholerae_reads_2.trimmed.subsampled.250k.fastq
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ velveth
    velveth - simple hashing program
    Version 1.2.10

    Copyright 2007, 2008 Daniel Zerbino (zerbino@ebi.ac.uk)
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    Compilation settings:
    CATEGORIES = 9
    MAXKMERLENGTH = 101

    Usage:
    ./velveth directory hash_length {[-file_format][-read_type][-separate|-interleaved] filename1 [filename2 ...]} {...} [options]

        directory   : directory name for output files
        hash_length : EITHER an odd integer (if even, it will be decremented) <= 101 (if above, will be reduced)
                : OR: m,M,s where m and M are odd integers (if not, they will be decremented) with m < M <= 101 (if above, will be reduced)
                    and s is a step (even number). Velvet will then hash from k=m to k=M with a step of s
        filename    : path to sequence file or - for standard input

    File format options:
        -fasta  -fastq  -raw    -fasta.gz   -fastq.gz   -raw.gz -sam    -bam    -fmtAuto
        (Note: -fmtAuto will detect fasta or fastq, and will try the following programs for decompression : gunzip, pbunzip2, bunzip2

    File layout options for paired reads (only for fasta and fastq formats):
        -interleaved    : File contains paired reads interleaved in the one file (default)
        -separate   : Read 2 separate files for paired reads

    Read type options:
        -short  -shortPaired
        ...
        -short8 -shortPaired8
        -short9 -shortPaired9
        -long   -longPaired
        -reference

    Options:
        -strand_specific    : for strand specific transcriptome sequencing data (default: off)
        -reuse_Sequences    : reuse Sequences file (or link) already in directory (no need to provide original filenames in this case (default: off)
        -reuse_binary   : reuse binary sequences file (or link) already in directory (no need to provide original filenames in this case (default: off)
        -noHash         : simply prepare Sequences file, do not hash reads or prepare Roadmaps file (default: off)
        -create_binary      : create binary CnyUnifiedSeq file (default: off)

    Synopsis:

    - Short single end reads:
        velveth Assem 29 -short -fastq s_1_sequence.txt

    - Paired-end short reads (remember to interleave paired reads):
        velveth Assem 31 -shortPaired -fasta interleaved.fna

    - Paired-end short reads (using separate files for the paired reads)
        velveth Assem 31 -shortPaired -fasta -separate left.fa right.fa

    - Two channels and some long reads:
        velveth Assem 43 -short -fastq unmapped.fna -longPaired -fasta SangerReads.fasta

    - Three channels:
        velveth Assem 35 -shortPaired -fasta pe_lib1.fasta -shortPaired2 pe_lib2.fasta -short3 se_lib1.fa

    Output:
        directory/Roadmaps
        directory/Sequences
            [Both files are picked up by graph, so please leave them there]
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ velveth Assem 30 -shortPaired -fastq -separate vcholerae_reads_1.trimmed.subsampled.250k.fastq vcholerae_reads_2.trimmed.subsampled.250k.fastq 
    [0.000001] Velvet can't work with even length k-mers, such as 30. We'll use 29 instead, if you don't mind.
    [0.000494] Reading FastQ file vcholerae_reads_1.trimmed.subsampled.250k.fastq;
    [0.000564] Reading FastQ file vcholerae_reads_2.trimmed.subsampled.250k.fastq;
    [4.058952] 500000 sequences found in total in the paired sequence files
    [4.058994] Done
    [4.059122] Reading read set file Assem/Sequences;
    [4.345354] 500000 sequences found
    [5.657970] Done
    [5.658036] 500000 sequences in total.
    [5.658136] Writing into roadmap file Assem/Roadmaps...
    [6.622388] Inputting sequences...
    [6.622457] Inputting sequence 0 / 500000
    [26.905454]  === Sequences loaded in 20.283071 s
    [26.905572] Done inputting sequences
    [26.905587] Destroying splay table
    [27.013449] Splay table destroyed
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ ls
    Assem                               vcholerae_reads_1.trimmed.subsampled.250k.fastq  vcholerae_reads_2.trimmed.subsampled.250k.fastq
    vcholerae_reads_1.trimmed.fastq.gz  vcholerae_reads_2.trimmed.fastq.gz
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ cd Assem
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem$ ls
    Log  Roadmaps  Sequences
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem$ cd ..
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ #velveth Assem2 43 -shortPaired -fastq -separate vcholerae_reads_1.trimmed.
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ ls
    Assem                                            vcholerae_reads_2.trimmed.fastq.gz
    vcholerae_reads_1.trimmed.fastq.gz               vcholerae_reads_2.trimmed.subsampled.250k.fastq
    vcholerae_reads_1.trimmed.subsampled.250k.fastq
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ velveth Assem2 43 -shortPaired -fastq -separate vcholerae_reads_1.trimmed.subsampled.250k.fastq vcholerae_reads_2.trimmed.subsampled.250k.fastq 
    [0.000001] Reading FastQ file vcholerae_reads_1.trimmed.subsampled.250k.fastq;
    [0.000083] Reading FastQ file vcholerae_reads_2.trimmed.subsampled.250k.fastq;
    [4.437596] 500000 sequences found in total in the paired sequence files
    [4.437774] Done
    [4.437949] Reading read set file Assem2/Sequences;
    [4.727121] 500000 sequences found
    [6.080263] Done
    [6.080430] 500000 sequences in total.
    [6.080525] Writing into roadmap file Assem2/Roadmaps...
    [6.962806] Inputting sequences...
    [6.962869] Inputting sequence 0 / 500000
    [26.192815]  === Sequences loaded in 19.230015 s
    [26.192937] Done inputting sequences
    [26.192952] Destroying splay table
    [26.374562] Splay table destroyed
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ ls
    Assem   vcholerae_reads_1.trimmed.fastq.gz               vcholerae_reads_2.trimmed.fastq.gz
    Assem2  vcholerae_reads_1.trimmed.subsampled.250k.fastq  vcholerae_reads_2.trimmed.subsampled.250k.fastq
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ cd Assem2
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ ls
    Log  Roadmaps  Sequences
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ less Road^C
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ ls -l
    total 146616
    -rw-rw-r-- 1 ubuntu ubuntu       450 Jan 17 14:00 Log
    -rw-rw-r-- 1 ubuntu ubuntu  28038956 Jan 17 14:00 Roadmaps
    -rw-rw-r-- 1 ubuntu ubuntu 122086683 Jan 17 14:00 Sequences
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ velvetg
    velvetg - de Bruijn graph construction, error removal and repeat resolution
    Version 1.2.10
    Copyright 2007, 2008 Daniel Zerbino (zerbino@ebi.ac.uk)
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    Compilation settings:
    CATEGORIES = 9
    MAXKMERLENGTH = 101

    Usage:
    ./velvetg directory [options]

        directory           : working directory name

    Standard options:
        -cov_cutoff     : removal of low coverage nodes AFTER tour bus or allow the system to infer it
            (default: no removal)
        -ins_length         : expected distance between two paired end reads (default: no read pairing)
        -read_trkg      : tracking of short read positions in assembly (default: no tracking)
        -min_contig_lgth    : minimum contig length exported to contigs.fa file (default: hash length * 2)
        -amos_file      : export assembly to AMOS file (default: no export)
        -exp_cov    : expected coverage of unique regions or allow the system to infer it
            (default: no long or paired-end read resolution)
        -long_cov_cutoff : removal of nodes with low long-read coverage AFTER tour bus
            (default: no removal)

    Advanced options:
        -ins_length*        : expected distance between two paired-end reads in the respective short-read dataset (default: no read pairing)
        -ins_length_long    : expected distance between two long paired-end reads (default: no read pairing)
        -ins_length*_sd     : est. standard deviation of respective dataset (default: 10% of corresponding length)
            [replace '*' by nothing, '2' or '_long' as necessary]
        -scaffolding        : scaffolding of contigs used paired end information (default: on)
        -max_branch_length  : maximum length in base pair of bubble (default: 100)
        -max_divergence : maximum divergence rate between two branches in a bubble (default: 0.2)
        -max_gap_count  : maximum number of gaps allowed in the alignment of the two branches of a bubble (default: 3)
        -min_pair_count     : minimum number of paired end connections to justify the scaffolding of two long contigs (default: 5)
        -max_coverage   : removal of high coverage nodes AFTER tour bus (default: no removal)
        -coverage_mask  : minimum coverage required for confident regions of contigs (default: 1)
        -long_mult_cutoff       : minimum number of long reads required to merge contigs (default: 2)
        -unused_reads       : export unused reads in UnusedReads.fa file (default: no)
        -alignments         : export a summary of contig alignment to the reference sequences (default: no)
        -exportFiltered     : export the long nodes which were eliminated by the coverage filters (default: no)
        -clean          : remove all the intermediary files which are useless for recalculation (default : no)
        -very_clean         : remove all the intermediary files (no recalculation possible) (default: no)
        -paired_exp_fraction    : remove all the paired end connections which less than the specified fraction of the expected count (default: 0.1)
        -shortMatePaired*   : for mate-pair libraries, indicate that the library might be contaminated with paired-end reads (default no)
        -conserveLong       : preserve sequences with long reads in them (default no)

    Output:
        directory/contigs.fa        : fasta file of contigs longer than twice hash length
        directory/stats.txt     : stats file (tab-spaced) useful for determining appropriate coverage cutoff
        directory/LastGraph     : special formatted file with all the information on the final graph
        directory/velvet_asm.afg    : (if requested) AMOS compatible assembly file
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ velvetg Assem2^C
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ cd ..
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ velvetg Assem2
    [0.000000] Reading roadmap file Assem2/Roadmaps
    [1.484147] 500000 roadmaps read
    [1.486378] Creating insertion markers
    [1.768271] Ordering insertion markers
    [2.364767] Counting preNodes
    [2.530988] 676517 preNodes counted, creating them now
    [6.879732] Adjusting marker info...
    [7.060320] Connecting preNodes
    [7.934708] Cleaning up memory
    [7.944252] Done creating preGraph
    [7.944308] Concatenation...
    [8.343361] Renumbering preNodes
    [8.343439] Initial preNode count 676517
    [8.374341] Destroyed 520721 preNodes
    [8.374397] Concatenation over!
    [8.374408] Clipping short tips off preGraph
    [8.401486] Concatenation...
    [8.570460] Renumbering preNodes
    [8.570541] Initial preNode count 155796
    [8.586582] Destroyed 65542 preNodes
    [8.586655] Concatenation over!
    [8.586666] 33212 tips cut off
    [8.586677] 90254 nodes left
    [8.586770] Writing into pregraph file Assem2/PreGraph...
    [9.378458] Reading read set file Assem2/Sequences;
    [9.655885] 500000 sequences found
    [10.973079] Done
    [11.869294] Reading pre-graph file Assem2/PreGraph
    [11.869671] Graph has 90254 nodes and 500000 sequences
    [12.343412] Scanning pre-graph file Assem2/PreGraph for k-mers
    [12.453898] 5377080 kmers found
    [13.302362] Sorting kmer occurence table ... 
    [20.429577] Sorting done.
    [20.429730] Computing acceleration table... 
    [20.626156] Computing offsets... 
    [20.717901] Ghost Threading through reads 0 / 500000
    [44.404327]  === Ghost-Threaded in 23.686426 s
    [44.404418] Threading through reads 0 / 500000
    [69.452870]  === Threaded in 25.048452 s
    [69.521949] Correcting graph with cutoff 0.200000
    [69.594345] Determining eligible starting points
    [69.737418] Done listing starting nodes
    [69.737495] Initializing todo lists
    [69.842537] Done with initilization
    [69.842618] Activating arc lookup table
    [69.899442] Done activating arc lookup table
    [70.120761] 10000 / 90254 nodes visited
    [70.377353] 20000 / 90254 nodes visited
    [70.649430] 30000 / 90254 nodes visited
    [70.937784] 40000 / 90254 nodes visited
    [71.235976] 50000 / 90254 nodes visited
    [71.592198] 60000 / 90254 nodes visited
    [71.855646] 70000 / 90254 nodes visited
    [72.106759] 80000 / 90254 nodes visited
    [72.238511] 90000 / 90254 nodes visited
    [72.239477] Concatenation...
    [72.244643] Renumbering nodes
    [72.244712] Initial node count 90254
    [72.247962] Removed 74445 null nodes
    [72.248024] Concatenation over!
    [72.248035] Clipping short tips off graph, drastic
    [72.329202] Concatenation...
    [72.384609] Renumbering nodes
    [72.384682] Initial node count 15809
    [72.385532] Removed 8109 null nodes
    [72.385549] Concatenation over!
    [72.385600] 7700 nodes left
    [72.385699] Writing into graph file Assem2/Graph...
    [73.095382] WARNING: NO COVERAGE CUTOFF PROVIDED
    [73.095433] Velvet will probably leave behind many detectable errors
    [73.095445] See manual for instructions on how to set the coverage cutoff parameter
    [73.095470] Removing contigs with coverage < -1.000000...
    [73.096428] Concatenation...
    [73.097377] Renumbering nodes
    [73.097396] Initial node count 7700
    [73.097438] Removed 0 null nodes
    [73.097450] Concatenation over!
    [73.097847] Concatenation...
    [73.098374] Renumbering nodes
    [73.098388] Initial node count 7700
    [73.098421] Removed 0 null nodes
    [73.098432] Concatenation over!
    [73.098464] Clipping short tips off graph, drastic
    [73.098682] Concatenation...
    [73.099134] Renumbering nodes
    [73.099153] Initial node count 7700
    [73.099178] Removed 0 null nodes
    [73.099188] Concatenation over!
    [73.099201] 7700 nodes left
    [73.099214] WARNING: NO EXPECTED COVERAGE PROVIDED
    [73.099228] Velvet will be unable to resolve any repeats
    [73.099241] See manual for instructions on how to set the expected coverage parameter
    [73.099257] Concatenation...
    [73.099672] Renumbering nodes
    [73.099687] Initial node count 7700
    [73.099711] Removed 0 null nodes
    [73.099722] Concatenation over!
    [73.099734] Removing reference contigs with coverage  contigs

    2014-01-17 14:06:37
    Running Basic statistics processor...
      Contig files: 
        contigs
      Calculating N50 and L50...
        contigs, N50 = 3768, L50 = 286, Total length = 3722836, GC % = 47.70, # N's per 100 kbp =  0.00
      Drawing cumulative plot...
        saved to /home/ubuntu/assembly/Assem2/output1/basic_stats/cumulative_plot.pdf
      Drawing GC content plot...
        saved to /home/ubuntu/assembly/Assem2/output1/basic_stats/GC_content_plot.pdf
      Drawing Nx plot...
        saved to /home/ubuntu/assembly/Assem2/output1/basic_stats/Nx_plot.pdf
    Done.

    NOTICE: Genes are not predicted by default. Use --gene-finding option to enable it.

    2014-01-17 14:06:39
    Summarizing...
      Creating total report...
        saved to /home/ubuntu/assembly/Assem2/output1/report.txt, report.tsv, and report.tex
      Transposed version of total report...
        saved to /home/ubuntu/assembly/Assem2/output1/transposed_report.txt, transposed_report.tsv, and transposed_report.tex
      HTML version saved to /home/ubuntu/assembly/Assem2/output1/report.html
      All pdf files are merged to /home/ubuntu/assembly/Assem2/output1/plots.pdf
    Log saved to /home/ubuntu/assembly/Assem2/output1/quast.log

    Finished: 2014-01-17 14:06:39
    Elapsed time: 0:00:03.139799
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ ls
    contigs.fa  Graph  LastGraph  Log  output1  PreGraph  Roadmaps  Sequences  stats.txt
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ cd output1
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2/output1$ ls
    basic_stats  plots.pdf  report.html      report.tex  report.txt             transposed_report.tsv
    json         quast.log  report_html_aux  report.tsv  transposed_report.tex  transposed_report.txt
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2/output1$ firefox report.html
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2/output1$ cd ..
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ cd ..
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ velvetg Assem
    [0.000000] Reading roadmap file Assem/Roadmaps
    [1.612518] 500000 roadmaps read
    [1.614553] Creating insertion markers
    [1.888414] Ordering insertion markers
    [2.566517] Counting preNodes
    [2.675889] 717318 preNodes counted, creating them now
    [6.942157] Adjusting marker info...
    [7.124399] Connecting preNodes
    [8.191134] Cleaning up memory
    [8.199661] Done creating preGraph
    [8.199697] Concatenation...
    [8.626041] Renumbering preNodes
    [8.626299] Initial preNode count 717318
    [8.666926] Destroyed 516170 preNodes
    [8.666986] Concatenation over!
    [8.666998] Clipping short tips off preGraph
    [8.695092] Concatenation...
    [8.871705] Renumbering preNodes
    [8.871780] Initial preNode count 201148
    [8.894360] Destroyed 56619 preNodes
    [8.894433] Concatenation over!
    [8.894444] 28813 tips cut off
    [8.894477] 144529 nodes left
    [8.894578] Writing into pregraph file Assem/PreGraph...
    [9.745634] Reading read set file Assem/Sequences;
    [10.079567] 500000 sequences found
    [11.316718] Done
    [12.211954] Reading pre-graph file Assem/PreGraph
    [12.212491] Graph has 144529 nodes and 500000 sequences
    [12.668231] Scanning pre-graph file Assem/PreGraph for k-mers
    [12.846345] 5526378 kmers found
    [13.653035] Sorting kmer occurence table ... 
    [21.506031] Sorting done.
    [21.506102] Computing acceleration table... 
    [21.637177] Computing offsets... 
    [21.791207] Ghost Threading through reads 0 / 500000
    [47.672287]  === Ghost-Threaded in 25.881080 s
    [47.672357] Threading through reads 0 / 500000
    [75.090878]  === Threaded in 27.418520 s
    [75.216504] Correcting graph with cutoff 0.200000
    [75.236141] Determining eligible starting points
    [75.518660] Done listing starting nodes
    [75.518713] Initializing todo lists
    [75.589577] Done with initilization
    [75.589649] Activating arc lookup table
    [75.739150] Done activating arc lookup table
    [75.919068] 10000 / 144529 nodes visited
    [76.042347] 20000 / 144529 nodes visited
    [76.239176] 30000 / 144529 nodes visited
    [76.441351] 40000 / 144529 nodes visited
    [76.648717] 50000 / 144529 nodes visited
    [76.818537] 60000 / 144529 nodes visited
    [77.046706] 70000 / 144529 nodes visited
    [77.264235] 80000 / 144529 nodes visited
    [77.489694] 90000 / 144529 nodes visited
    [77.727152] 100000 / 144529 nodes visited
    [77.939256] 110000 / 144529 nodes visited
    [78.063556] 120000 / 144529 nodes visited
    [78.248555] 130000 / 144529 nodes visited
    [78.428864] 140000 / 144529 nodes visited
    [78.456981] Concatenation...
    [78.464772] Renumbering nodes
    [78.464847] Initial node count 144529
    [78.469508] Removed 123321 null nodes
    [78.469594] Concatenation over!
    [78.469645] Clipping short tips off graph, drastic
    [78.478382] Concatenation...
    [78.485871] Renumbering nodes
    [78.485917] Initial node count 21208
    [78.489142] Removed 747 null nodes
    [78.489196] Concatenation over!
    [78.489213] 20461 nodes left
    [78.489319] Writing into graph file Assem/Graph...
    [79.259328] WARNING: NO COVERAGE CUTOFF PROVIDED
    [79.259424] Velvet will probably leave behind many detectable errors
    [79.259437] See manual for instructions on how to set the coverage cutoff parameter
    [79.259463] Removing contigs with coverage < -1.000000...
    [79.262157] Concatenation...
    [79.267144] Renumbering nodes
    [79.267224] Initial node count 20461
    [79.267328] Removed 0 null nodes
    [79.267353] Concatenation over!
    [79.269908] Concatenation...
    [79.275061] Renumbering nodes
    [79.275150] Initial node count 20461
    [79.275213] Removed 0 null nodes
    [79.275239] Concatenation over!
    [79.275275] Clipping short tips off graph, drastic
    [79.277257] Concatenation...
    [79.282549] Renumbering nodes
    [79.282653] Initial node count 20461
    [79.282762] Removed 0 null nodes
    [79.282786] Concatenation over!
    [79.282797] 20461 nodes left
    [79.282822] WARNING: NO EXPECTED COVERAGE PROVIDED
    [79.282847] Velvet will be unable to resolve any repeats
    [79.282872] See manual for instructions on how to set the expected coverage parameter
    [79.282904] Concatenation...
    [79.287785] Renumbering nodes
    [79.287850] Initial node count 20461
    [79.287917] Removed 0 null nodes
    [79.287932] Concatenation over!
    [79.287949] Removing reference contigs with coverage  contigs

    2014-01-17 14:10:01
    Running Basic statistics processor...
      Contig files: 
        contigs
      Calculating N50 and L50...
        contigs, N50 = 1344, L50 = 772, Total length = 3195658, GC % = 47.64, # N's per 100 kbp =  0.00
      Drawing cumulative plot...
        saved to /home/ubuntu/assembly/Assem/quastoutput/basic_stats/cumulative_plot.pdf
      Drawing GC content plot...
        saved to /home/ubuntu/assembly/Assem/quastoutput/basic_stats/GC_content_plot.pdf
      Drawing Nx plot...
        saved to /home/ubuntu/assembly/Assem/quastoutput/basic_stats/Nx_plot.pdf
    Done.

    NOTICE: Genes are not predicted by default. Use --gene-finding option to enable it.

    2014-01-17 14:10:02
    Summarizing...
      Creating total report...
        saved to /home/ubuntu/assembly/Assem/quastoutput/report.txt, report.tsv, and report.tex
      Transposed version of total report...
        saved to /home/ubuntu/assembly/Assem/quastoutput/transposed_report.txt, transposed_report.tsv, and transposed_report.tex
      HTML version saved to /home/ubuntu/assembly/Assem/quastoutput/report.html
      All pdf files are merged to /home/ubuntu/assembly/Assem/quastoutput/plots.pdf
    Log saved to /home/ubuntu/assembly/Assem/quastoutput/quast.log

    Finished: 2014-01-17 14:10:02
    Elapsed time: 0:00:01.954170
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem$ cd output
    bash: cd: output: No such file or directory
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem$ cd quastoutput
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem/quastoutput$ ls
    basic_stats  plots.pdf  report.html      report.tex  report.txt             transposed_report.tsv
    json         quast.log  report_html_aux  report.tsv  transposed_report.tex  transposed_report.txt
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem/quastoutput$ firefox report.html
    ^C
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem/quastoutput$ ls
    basic_stats  plots.pdf  report.html      report.tex  report.txt             transposed_report.tsv
    json         quast.log  report_html_aux  report.tsv  transposed_report.tex  transposed_report.txt
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem/quastoutput$ cd ..
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem$ 
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem$ cd ..
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ ls
    Assem   vcholerae_reads_1.trimmed.fastq.gz               vcholerae_reads_2.trimmed.fastq.gz
    Assem2  vcholerae_reads_1.trimmed.subsampled.250k.fastq  vcholerae_reads_2.trimmed.subsampled.250k.fastq
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly$ cd Assem2
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ ls
    contigs.fa  Graph  LastGraph  Log  output1  PreGraph  Roadmaps  Sequences  stats.txt
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ cd output1
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2/output1$ firefox report.html
    ^C
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2/output1$ cd ..
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ ls
    contigs.fa  Graph  LastGraph  Log  output1  PreGraph  Roadmaps  Sequences  stats.txt

Prokaryotic genome annotation program, prokka (very cool):
http://www.vicbioinformatics.com/software.prokka.shtml

    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ prokka contigs.fa
    [14:55:05] This is prokka 1.8
    [14:55:05] Written by Torsten Seemann 
    [14:55:05] Victorian Bioinformatics Consortium - http://www.vicbioinformatics.com
    [14:55:05] Local time is Fri Jan 17 14:55:05 2014
    [14:55:05] You are ubuntu
    [14:55:05] Operating system is linux
    [14:55:05] You have BioPerl 1.006923
    [14:55:05] System has 4 cores.
    [14:55:05] Option --cpu asked for 8 cores, but system only has 4
    [14:55:05] Will use maximum of 4 cores.
    [14:55:05] Annotating as >>> Bacteria <<<
    [14:55:05] Folder 'PROKKA_01172014' already exists! Please change --outdir or use --force
    ubuntu@domU-12-31-39-0C-6C-E1:~/assembly/Assem2$ prokka contigs.fa --force
    [14:55:15] This is prokka 1.8
    [14:55:15] Written by Torsten Seemann 
    [14:55:15] Victorian Bioinformatics Consortium - http://www.vicbioinformatics.com
    [14:55:15] Local time is Fri Jan 17 14:55:15 2014
    [14:55:15] You are ubuntu
    [14:55:15] Operating system is linux
    [14:55:15] You have BioPerl 1.006923
    [14:55:15] System has 4 cores.
    [14:55:15] Option --cpu asked for 8 cores, but system only has 4
    [14:55:15] Will use maximum of 4 cores.
    [14:55:15] Annotating as >>> Bacteria << end (21) - skipping.
    [14:55:19] 1 tRNA-Gln [65,139] 33 (ttg)
    [14:55:19] 1 tRNA-Arg [5147,5223] 35 (tct)
    [14:55:19] 1 tRNA-Asp [16,92] 35 (gtc)
    [14:55:19] 1 tRNA-Trp c[3832,3908] 35 (cca)
    [14:55:19] 1 tRNA-Cys c[66,38] 30 (gca)
    [14:55:19] tRNA c[66,38] has start(66) > end (38) - skipping.
    [14:55:19] 1 tRNA-Leu c[3,89] 35 (taa)
    [14:55:20] 1 tRNA-Gln [148,69] 33 (ttg)
    [14:55:20] tRNA [148,69] has start(148) > end (69) - skipping.
    [14:55:20] 1 tRNA-Thr [50,125] 34 (ggt)
    [14:55:20] 1 tRNA-Asp c[77,36] 35 (atc)
    [14:55:20] tRNA c[77,36] has start(77) > end (36) - skipping.
    [14:55:20] 1 tRNA-Cys [116,73] 33 (gca)
    [14:55:20] tRNA [116,73] has start(116) > end (73) - skipping.
    [14:55:20] 1 tRNA-Ser c[2,92] 35 (tga)
    [14:55:20] 1 tRNA-Ser [642,729] 35 (gga)
    [14:55:20] 1 tRNA-Ile [48,124] 35 (gat)
    [14:55:20] 1 tRNA-Leu c[33,10] 37 (tag)
    [14:55:20] tRNA c[33,10] has start(33) > end (10) - skipping.
    [14:55:20] 1 tRNA-Lys [25,99] 33 (ttt)
    [14:55:20] 2 tRNA-Val [130,205] 34 (tac)
    [14:55:20] 1 tRNA-Ala [49,42] 33 (tgc)
    [14:55:20] tRNA [49,42] has start(49) > end (42) - skipping.
    [14:55:20] 1 tRNA-Ala c[35,110] 34 (ggc)
    [14:55:20] 1 tRNA-Gly [65,30] 34 (gcc)
    [14:55:20] tRNA [65,30] has start(65) > end (30) - skipping.
    [14:55:20] 1 tRNA-Ala c[35,110] 34 (tgc)
    [14:55:20] 1 tRNA-Thr c[167,12] 39 (ggt)
    [14:55:20] tRNA c[167,12] has start(167) > end (12) - skipping.
    [14:55:20] 1 tRNA-Thr c[63,49] 34 (ggt)
    [14:55:20] tRNA c[63,49] has start(63) > end (49) - skipping.
    [14:55:20] 1 tRNA-Leu c[92,2] 35 (gag)
    [14:55:20] tRNA c[92,2] has start(92) > end (2) - skipping.
    [14:55:20] 1 tRNA-Arg c[84,72] 35 (acg)
    [14:55:20] tRNA c[84,72] has start(84) > end (72) - skipping.
    [14:55:20] 1 tRNA-Arg [81,72] 35 (acg)
    [14:55:20] tRNA [81,72] has start(81) > end (72) - skipping.
    [14:55:20] 1 tRNA-Ala [9,84] 34 (ggc)
    [14:55:20] 1 tRNA-Val c[47,122] 34 (gac)
    [14:55:21] 1 tRNA-Met [11,82] 34 (cat)
    [14:55:21] 1 tRNA-Gln c[11,85] 33 (ttg)
    [14:55:21] Found 19 tRNAs
    [14:55:21] Predicting Ribosomal RNAs
    [14:55:21] You need either Barrnap or RNAmmer installed to predict rRNAs!
    [14:55:21] Skipping ncRNA search, enable with --rfam if desired.
    [14:55:21] Total of 18 tRNA + rRNA features
    [14:55:21] Predicting coding sequences
    [14:55:21] Contigs total 4290423 bp, so using single mode
    [14:55:21] Running: prodigal -i PROKKA_01172014/PROKKA_01172014.fna -c -m -g 11 -p single -f sco -q
    [14:55:31] Excluding CDS which overlaps existing RNA (tRNA) at NODE_528_length_150_cov_25.833334:17..127 on - strand
    [14:55:33] Found 3342 CDS
    [14:55:33] Connecting features back to sequences
    [14:55:33] Option --gram not specified, will NOT check for signal peptides.
    [14:55:33] Not using genus-specific database. Try --usegenus to enable it.
    [14:55:33] Annotating CDS, please be patient.
    [14:55:33] Will use 4 CPUs for similarity searching.
    [14:55:35] There are still 3342 unannotated CDS left (started with 3342)
    [14:55:35] Will use blast to search against /home/ubuntu/software/prokka-1.7/bin/../db/kingdom/Bacteria/sprot with 4 CPUs
    [14:55:35] Running: cat PROKKA_01172014/proteins.faa | parallel --gnu -j 4 --block 110869 --recstart '>' --pipe blastp -query - -db /home/ubuntu/software/prokka-1.7/bin/../db/kingdom/Bacteria/sprot -evalue 1e-06 -num_threads 1 -num_descriptions 1 -num_alignments 1 > PROKKA_01172014/proteins.bls 2> /dev/null
    [14:57:03] Modify product: Probable TonB-dependent receptor HI_1217 precursor => putative TonB-dependent receptor precursor
    [14:57:03] Modify product: Probable cysteine desulfurase => putative cysteine desulfurase
    [14:57:03] Modify product: Probable GTP-binding protein EngB => putative GTP-binding protein EngB
    [14:57:03] Modify product: Stress response UPF0229 protein YhbH => hypothetical protein
    [14:57:03] Modify product: Probable diguanylate cyclase YdaM => putative diguanylate cyclase YdaM
    [14:57:03] Modify product: Probable glutamine ABC transporter permease protein GlnM => putative glutamine ABC transporter permease protein GlnM
    [14:57:03] Modify product: Probable diguanylate cyclase AdrA => putative diguanylate cyclase AdrA
    [14:57:03] Modify product: Cytochrome b561 homolog 2 => hypothetical protein
    [14:57:03] Modify product: Probable L-ascorbate-6-phosphate lactonase UlaG => putative L-ascorbate-6-phosphate lactonase UlaG
    [14:57:03] Modify product: Probable phospholipid-binding protein MlaC precursor => putative phospholipid-binding protein MlaC precursor
    [14:57:03] Modify product: Probable phospholipid ABC transporter-binding protein MlaD => putative phospholipid ABC transporter-binding protein MlaD
    [14:57:03] Modify product: Probable phospholipid ABC transporter permease protein MlaE => putative phospholipid ABC transporter permease protein MlaE
    [14:57:03] Modify product: Probable phospholipid import ATP-binding protein MlaF => putative phospholipid import ATP-binding protein MlaF
    [14:57:03] Modify product: Probable sulfate transporter Rv1739c/MT1781 => putative sulfate transporterc/MT1781
    [14:57:03] Modify product: Phosphorylated carbohydrates phosphatase TM_1254 => Phosphorylated carbohydrates phosphatase
    [14:57:03] Modify product: Uncharacterized membrane protein YjcC => putative membrane protein YjcC
    [14:57:03] Modify product: Uncharacterized oxidoreductase YdgJ => putative oxidoreductase YdgJ
    [14:57:03] Modify product: Probable phospholipid-binding lipoprotein MlaA precursor => putative phospholipid-binding lipoprotein MlaA precursor
    [14:57:03] Modify product: Probable diguanylate cyclase YeaP => putative diguanylate cyclase YeaP
    [14:57:03] Modify product: Uncharacterized ABC transporter ATP-binding protein Rv0986/MT1014 => putative ABC transporter ATP-binding protein/MT1014
    [14:57:03] Modify product: Putative reductase CA_C0462 => Putative reductase
    [14:57:03] Modify product: Probable amino-acid permease protein YxeN => putative amino-acid permease protein YxeN
    [14:57:03] Modify product: Probable amino-acid import ATP-binding protein YxeO => putative amino-acid import ATP-binding protein YxeO
    [14:57:04] Modify product: Probable tRNA-dihydrouridine synthase => putative tRNA-dihydrouridine synthase
    [14:57:04] Modify product: 21K => hypothetical protein
    [14:57:04] Modify product: Uncharacterized acyl-CoA thioester hydrolase HI_0827 => putative acyl-CoA thioester hydrolase
    [14:57:04] Modify product: Probable diguanylate cyclase YdaM => putative diguanylate cyclase YdaM
    [14:57:04] Modify product: Probable diguanylate cyclase YegE => putative diguanylate cyclase YegE
    [14:57:04] Modify product: Probable diguanylate cyclase AdrA => putative diguanylate cyclase AdrA
    [14:57:04] Modify product: Probable tRNA-dihydrouridine synthase => putative tRNA-dihydrouridine synthase
    [14:57:04] Modify product: P20 => hypothetical protein
    [14:57:04] Modify product: Cyclic di-GMP binding protein VCA0042 => Cyclic di-GMP binding protein
    [14:57:04] Modify product: Probable enoyl-CoA hydratase 1 => putative enoyl-CoA hydratase 1
    [14:57:04] Modify product: Uncharacterized ABC transporter ATP-binding protein YheS => putative ABC transporter ATP-binding protein YheS
    [14:57:04] Modify product: Uncharacterized inner membrane transporter yiJE => putative inner membrane transporter yiJE
    [14:57:04] Modify product: Probable diguanylate cyclase AdrA => putative diguanylate cyclase AdrA
    [14:57:04] Modify product: Probable aromatic acid decarboxylase => putative aromatic acid decarboxylase
    [14:57:04] Modify product: Uncharacterized HTH-type transcriptional regulator YdfH => putative HTH-type transcriptional regulator YdfH
    [14:57:04] Modify product: Probable peroxiredoxin => putative peroxiredoxin
    [14:57:04] Modify product: Probable ATP-dependent helicase DinG homolog => hypothetical protein
    [14:57:04] Modify product: Probable diguanylate cyclase YdaM => putative diguanylate cyclase YdaM
    [14:57:05] Modify product: Transcription termination/antitermination L factor => hypothetical protein
    [14:57:05] Modify product: Probable acyltransferase YihG => putative acyltransferase YihG
    [14:57:05] Modify product: Putative multidrug export ATP-binding/permease protein SAV1866 => Putative multidrug export ATP-binding/permease protein
    [14:57:05] Modify product: Probable transcriptional regulatory protein YeeN => putative transcriptional regulatory protein YeeN
    [14:57:05] Modify product: Probable diguanylate cyclase YcdT => putative diguanylate cyclase YcdT
    [14:57:05] Modify product: Cytochrome c oxidase subunit 1 homolog, bacteroid => hypothetical protein
    [14:57:05] Modify product: Cytochrome b561 homolog 2 => hypothetical protein
    [14:57:05] Modify product: Tricorn protease homolog 1 => hypothetical protein
    [14:57:05] Modify product: Uncharacterized ABC transporter ATP-binding protein YbhF => putative ABC transporter ATP-binding protein YbhF
    [14:57:05] Modify product: Probable phosphatase YcdX => putative phosphatase YcdX
    [14:57:05] Modify product: Uncharacterized ferredoxin-like protein YfhL => putative ferredoxin-like protein YfhL
    [14:57:05] Modify product: Uncharacterized protease YhbU precursor => putative protease YhbU precursor
    [14:57:05] Modify product: Probable peptidoglycan biosynthesis protein MurJ => putative peptidoglycan biosynthesis protein MurJ
    [14:57:05] Modify product: Uncharacterized protease YhbU precursor => putative protease YhbU precursor
    [14:57:05] Modify product: G20.3 => hypothetical protein
    [14:57:05] Modify product: Probable L,D-transpeptidase YcfS precursor => putative L,D-transpeptidase YcfS precursor
    [14:57:05] Modify product: Probable inorganic polyphosphate/ATP-NAD kinase => putative inorganic polyphosphate/ATP-NAD kinase
    [14:57:06] Modify product: Probable diguanylate cyclase YdaM => putative diguanylate cyclase YdaM
    [14:57:06] Modify product: Probable DNA endonuclease SmrA => putative DNA endonuclease SmrA
    [14:57:06] Modify product: Probable galacturonate locus repressor => putative galacturonate locus repressor
    [14:57:06] Modify product: Probable siderophore transport system ATP-binding protein YusV => putative siderophore transport system ATP-binding protein YusV
    [14:57:06] Modify product: Probable siderophore transport system permease protein YfiZ precursor => putative siderophore transport system permease protein YfiZ precursor
    [14:57:06] Modify product: Probable DNA endonuclease SmrA => putative DNA endonuclease SmrA
    [14:57:06] Modify product: Putative 2-hydroxyacid dehydrogenase HI_1556 => Putative 2-hydroxyacid dehydrogenase
    [14:57:06] Modify product: Uncharacterized sugar transferase EpsL => putative sugar transferase EpsL
    [14:57:06] Modify product: Uncharacterized HTH-type transcriptional regulator YbbH => putative HTH-type transcriptional regulator YbbH
    [14:57:06] Modify product: Uncharacterized oxidoreductase SAV2478 => putative oxidoreductase
    [14:57:06] Modify product: Probable transcriptional regulatory protein NarL => putative transcriptional regulatory protein NarL
    [14:57:06] Modify product: H1 => hypothetical protein
    [14:57:06] Modify product: Uncharacterized ABC transporter solute-binding protein YclQ precursor => putative ABC transporter solute-binding protein YclQ precursor
    [14:57:06] Modify product: H3 => hypothetical protein
    [14:57:06] Modify product: Uncharacterized acyl-CoA thioester hydrolase HI_0827 => putative acyl-CoA thioester hydrolase
    [14:57:06] Modify product: Probable intracellular septation protein A => putative intracellular septation protein A
    [14:57:06] Modify product: Probable polyketide biosynthesis zinc-dependent hydrolase PksB => putative polyketide biosynthesis zinc-dependent hydrolase PksB
    [14:57:06] Modify product: Uncharacterized HTH-type transcriptional regulator YbbH => putative HTH-type transcriptional regulator YbbH
    [14:57:06] Modify product: Putative reductase XOO0026 => Putative reductase
    [14:57:06] Modify product: Probable 6-phospho-beta-glucosidase => putative 6-phospho-beta-glucosidase
    [14:57:07] Modify product: Uncharacterized HTH-type transcriptional regulator HI_0893 => putative HTH-type transcriptional regulator
    [14:57:07] Modify product: Uncharacterized SufE-like protein YgdK => putative SufE-like protein YgdK
    [14:57:07] Modify product: Probable chromosome-partitioning protein ParB => putative chromosome-partitioning protein ParB
    [14:57:07] Modify product: Putative acetyltransferase SACOL2570 => Putative acetyltransferase
    [14:57:07] Modify product: Chemotaxis protein CheY homolog => hypothetical protein
    [14:57:07] Modify product: P-43 => hypothetical protein
    [14:57:07] Modify product: Probable diguanylate cyclase YcdT => putative diguanylate cyclase YcdT
    [14:57:07] Modify product: Uncharacterized ABC transporter ATP-binding protein YbhF => putative ABC transporter ATP-binding protein YbhF
    [14:57:07] Modify product: Uncharacterized ABC transporter ATP-binding protein YheS => putative ABC transporter ATP-binding protein YheS
    [14:57:07] Modify product: Putative monooxygenase Rv0793 => Putative monooxygenase
    [14:57:07] Modify product: Probable amino-acid-binding protein YxeM precursor => putative amino-acid-binding protein YxeM precursor
    [14:57:07] Modify product: Probable Fe(2+)-trafficking protein => putative Fe(2+)-trafficking protein
    [14:57:07] Modify product: L8 => hypothetical protein
    [14:57:07] Modify product: Transcription termination/antitermination protein NusG => hypothetical protein
    [14:57:07] Modify product: H1 => hypothetical protein
    [14:57:07] Modify product: Transcription termination factor Rho => hypothetical protein
    [14:57:07] Modify product: H1 => hypothetical protein
    [14:57:07] Modify product: Symbiotic regulator homolog 1 => hypothetical protein
    [14:57:07] Modify product: Probable diguanylate cyclase YcdT => putative diguanylate cyclase YcdT
    [14:57:07] Modify product: Probable endopeptidase Spr precursor => putative endopeptidase Spr precursor
    [14:57:07] Modify product: H3 => hypothetical protein
    [14:57:08] Modify product: Uncharacterized membrane protein YjcC => putative membrane protein YjcC
    [14:57:08] Modify product: Ribonuclease TTHA0252 => Ribonuclease
    [14:57:08] Modify product: Uncharacterized deoxyribonuclease YcfH => putative deoxyribonuclease YcfH
    [14:57:08] Modify product: Zinc-type alcohol dehydrogenase-like protein SA1988 => Zinc-type alcohol dehydrogenase-like protein
    [14:57:08] Modify product: Uncharacterized EAL-domain containing protein YkuI => putative EAL-domain containing protein YkuI
    [14:57:08] Modify product: Probable ferritin-1 => putative ferritin-1
    [14:57:08] Modify product: Probable acrylyl-CoA reductase AcuI => putative acrylyl-CoA reductase AcuI
    [14:57:08] Modify product: Co-chaperone protein HscB homolog => hypothetical protein
    [14:57:08] Modify product: NS1 => hypothetical protein
    [14:57:08] Modify product: HIT-like protein HI_0961 => HIT-like protein
    [14:57:08] Modify product: Probable diguanylate cyclase YcdT => putative diguanylate cyclase YcdT
    [14:57:08] Modify product: Uncharacterized FAD-linked oxidoreductase Rv2280 => putative FAD-linked oxidoreductase
    [14:57:08] Modify product: NS2 => hypothetical protein
    [14:57:08] Modify product: Probable cadaverine/lysine antiporter => putative cadaverine/lysine antiporter
    [14:57:09] Modify product: Epimerase family protein SA0724 => Epimerase family protein
    [14:57:09] Modify product: Probable deferrochelatase/peroxidase YfeX => putative deferrochelatase/peroxidase YfeX
    [14:57:09] Modify product: Probable diguanylate cyclase AdrA => putative diguanylate cyclase AdrA
    [14:57:09] Modify product: Probable diguanylate cyclase YcdT => putative diguanylate cyclase YcdT
    [14:57:09] Modify product: Uncharacterized HTH-type transcriptional regulator BA_1941/GBAA_1941/BAS1801 => putative HTH-type transcriptional regulator/GBAA_1941/BAS1801
    [14:57:09] Modify product: Probable diguanylate cyclase YdaM => putative diguanylate cyclase YdaM
    [14:57:09] Modify product: DPS protein homolog => hypothetical protein
    [14:57:09] Modify product: Probable ubiquinone biosynthesis protein UbiB => putative ubiquinone biosynthesis protein UbiB
    [14:57:09] Modify product: Probable protease SohB => putative protease SohB
    [14:57:09] Modify product: Uncharacterized oxidoreductase YciK => putative oxidoreductase YciK
    [14:57:09] Modify product: Uncharacterized MFS-type transporter YcaD => putative MFS-type transporter YcaD
    [14:57:09] Modify product: Putative multidrug export ATP-binding/permease protein SAV1866 => Putative multidrug export ATP-binding/permease protein
    [14:57:09] Modify product: PPDC => hypothetical protein
    [14:57:09] Modify product: Probable chromate transport protein => putative chromate transport protein
    [14:57:09] Modify product: Probable diguanylate cyclase YfiN => putative diguanylate cyclase YfiN
    [14:57:09] Modify product: Uncharacterized deoxyribonuclease YcfH => putative deoxyribonuclease YcfH
    [14:57:09] Modify product: Probable diguanylate cyclase AdrA => putative diguanylate cyclase AdrA
    [14:57:09] Modify product: Uncharacterized PIN and TRAM-domain containing protein TTHA0540 precursor => putative PIN and TRAM-domain containing protein precursor
    [14:57:09] Cleaned 131 /product names
    [14:57:09] Deleting temporary file: PROKKA_01172014/proteins.faa
    [14:57:09] Deleting temporary file: PROKKA_01172014/proteins.bls
    [14:57:10] There are still 1252 unannotated CDS left (started with 3342)
    [14:57:10] Will use hmmer3 to search against /home/ubuntu/software/prokka-1.7/bin/../db/hmm/CLUSTERS.hmm with 4 CPUs
    [14:57:10] Running: cat PROKKA_01172014/proteins.faa | parallel --gnu -j 4 --block 28927 --recstart '>' --pipe hmmscan --noali --notextw --acc -E 1e-06 --cpu 1 /home/ubuntu/software/prokka-1.7/bin/../db/hmm/CLUSTERS.hmm /dev/stdin > PROKKA_01172014/proteins.bls 2> /dev/null
    [15:03:43] Deleting temporary file: PROKKA_01172014/proteins.faa
    [15:03:43] Deleting temporary file: PROKKA_01172014/proteins.bls
    [15:03:43] There are still 1058 unannotated CDS left (started with 3342)
    [15:03:43] Will use hmmer3 to search against /home/ubuntu/software/prokka-1.7/bin/../db/hmm/TIGRFAMs.hmm with 4 CPUs
    [15:03:43] Running: cat PROKKA_01172014/proteins.faa | parallel --gnu -j 4 --block 23637 --recstart '>' --pipe hmmscan --noali --notextw --acc -E 1e-06 --cpu 1 /home/ubuntu/software/prokka-1.7/bin/../db/hmm/TIGRFAMs.hmm /dev/stdin > PROKKA_01172014/proteins.bls 2> /dev/null
    [15:06:59] Modify product: type VI secretion protein, VC_A0114 family => type VI secretion protein, family
    [15:06:59] Modify product: type VI secretion lipoprotein, VC_A0113 family => type VI secretion lipoprotein, family
    [15:06:59] Modify product: type VI secretion protein, VC_A0111 family => type VI secretion protein, family
    [15:06:59] Modify product: type VI secretion protein, VC_A0110 family => type VI secretion protein, family
    [15:06:59] Modify product: type VI secretion protein, VC_A0107 family => type VI secretion protein, family
    [15:06:59] Modify product: type VI secretion protein, EvpB/VC_A0108 family => type VI secretion protein, EvpB/ family
    [15:06:59] Modify product: putative thioesterase domain => putative thioesterase domain protein
    [15:06:59] Modify product: 4-hydroxyphenylacetate degradation bifunctional isomerase/decarboxylase, C-terminal subunit => hypothetical protein
    [15:06:59] Modify product: flavoprotein, HI0933 family => flavoprotein, family
    [15:07:00] Modify product: peroxiredoxin, SACOL1771 subfamily => peroxiredoxin, subfamily
    [15:07:00] Modify product: VWFA-related Acidobacterial domain => VWFA-related Acidobacterial domain protein
    [15:07:00] Modify product: FimV C-terminal domain => hypothetical protein
    [15:07:00] Modify product: selT/selW/selH selenoprotein domain => selT/selW/selH selenoprotein domain protein
    [15:07:00] Modify product: type VI secretion-associated protein, VC_A0118 family => type VI secretion-associated protein, family
    [15:07:00] Modify product: probable O-glycosylation ligase, exosortase A-associated => putative O-glycosylation ligase, exosortase A-associated
    [15:07:00] Modify product: 4-hydroxyphenylacetate degradation bifunctional isomerase/decarboxylase, C-terminal subunit => hypothetical protein
    [15:07:00] Cleaned 16 /product names
    [15:07:00] Deleting temporary file: PROKKA_01172014/proteins.faa
    [15:07:00] Deleting temporary file: PROKKA_01172014/proteins.bls
    [15:07:00] There are still 943 unannotated CDS left (started with 3342)
    [15:07:00] Will use hmmer3 to search against /home/ubuntu/software/prokka-1.7/bin/../db/hmm/Cdd.hmm with 4 CPUs
    [15:07:00] Running: cat PROKKA_01172014/proteins.faa | parallel --gnu -j 4 --block 20095 --recstart '>' --pipe hmmscan --noali --notextw --acc -E 1e-06 --cpu 1 /home/ubuntu/software/prokka-1.7/bin/../db/hmm/Cdd.hmm /dev/stdin > PROKKA_01172014/proteins.bls 2> /dev/null
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: Phosphoglycerol transferase and related proteins, alkaline phosphatase superfamily => Phosphoglycerol transferase, alkaline phosphatase superfamily
    [15:09:25] Modify product: Transposase and inactivated derivatives => Transposase
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative esterase of the alpha/beta hydrolase fold => putative esterase of the alpha/beta hydrolase fold protein
    [15:09:25] Modify product: Arsenate reductase and related proteins, glutaredoxin family => Arsenate reductase, glutaredoxin family
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: Na+-dependent transporters of the SNF family => Na+-dependent transporters of the SNF family protein
    [15:09:25] Modify product: Response regulator containing a CheY-like receiver domain and an HD-GYP domain => Response regulator containing a CheY-like receiver domain and an HD-GYP domain protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: Arsenate reductase and related proteins, glutaredoxin family => Arsenate reductase, glutaredoxin family
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein, contains double-stranded beta-helix domain => hypothetical protein
    [15:09:25] Modify product: Na+-dependent transporters of the SNF family => Na+-dependent transporters of the SNF family protein
    [15:09:25] Modify product: putative conserved protein (some members contain a von Willebrand factor type A (vWA) domain) => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: Transposase and inactivated derivatives => Transposase
    [15:09:25] Modify product: Penicillin V acylase and related amidases => Penicillin V acylase
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative protein containing caspase domain => putative protein containing caspase domain protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative protein, similar to the N-terminal domain of Lon protease => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: Na+-dependent transporters of the SNF family => Na+-dependent transporters of the SNF family protein
    [15:09:25] Modify product: Lipid A core - O-antigen ligase and related enzymes => Lipid A core - O-antigen ligase
    [15:09:25] Modify product: Mannosyltransferase OCH1 and related enzymes => Mannosyltransferase OCH1
    [15:09:25] Modify product: putative conserved protein => hypothetical protein
    [15:09:25] Modify product: Phosphate transport regulator (distant homolog of PhoU) => hypothetical protein
    [15:09:25] Cleaned 41 /product names
    [15:09:25] Deleting temporary file: PROKKA_01172014/proteins.faa
    [15:09:25] Deleting temporary file: PROKKA_01172014/proteins.bls
    [15:09:26] There are still 808 unannotated CDS left (started with 3342)
    [15:09:26] Will use hmmer3 to search against /home/ubuntu/software/prokka-1.7/bin/../db/hmm/Pfam.hmm with 4 CPUs
    [15:09:26] Running: cat PROKKA_01172014/proteins.faa | parallel --gnu -j 4 --block 15836 --recstart '>' --pipe hmmscan --noali --notextw --acc -E 1e-06 --cpu 1 /home/ubuntu/software/prokka-1.7/bin/../db/hmm/Pfam.hmm /dev/stdin > PROKKA_01172014/proteins.bls 2> /dev/null
    [15:13:12] Modify product: YHS domain => YHS domain protein
    [15:13:12] Modify product: PAS fold => PAS fold protein
    [15:13:12] Modify product: Na+/H+ antiporter family => Na+/H+ antiporter family protein
    [15:13:12] Modify product: Phage antirepressor protein KilAC domain => Phage antirepressor protein KilAC domain protein
    [15:13:12] Modify product: Hpt domain => Hpt domain protein
    [15:13:12] Modify product: IclR helix-turn-helix domain => IclR helix-turn-helix domain protein
    [15:13:12] Modify product: Phosphorylase superfamily => Phosphorylase superfamily protein
    [15:13:12] Modify product: TraB family => TraB family protein
    [15:13:12] Modify product: Cyclic nucleotide-binding domain => Cyclic nucleotide-binding domain protein
    [15:13:12] Modify product: Modulator of Rho-dependent transcription termination (ROF) => hypothetical protein
    [15:13:12] Modify product: Endonuclease/Exonuclease/phosphatase family => Endonuclease/Exonuclease/phosphatase family protein
    [15:13:12] Modify product: PilZ domain => PilZ domain protein
    [15:13:12] Modify product: Methyltransferase domain => Methyltransferase domain protein
    [15:13:12] Modify product: ASCH domain => ASCH domain protein
    [15:13:12] Modify product: Peptidase M16 inactive domain => Peptidase M16 inactive domain protein
    [15:13:12] Modify product: DSBA-like thioredoxin domain => DSBA-like thioredoxin domain protein
    [15:13:12] Modify product: YheO-like PAS domain => YheO-like PAS domain protein
    [15:13:12] Modify product: Peptidase M16 inactive domain => Peptidase M16 inactive domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: YGGT family => YGGT family protein
    [15:13:12] Modify product: Protein of unknown function (Duf2374) => hypothetical protein
    [15:13:12] Modify product: CheW-like domain => CheW-like domain protein
    [15:13:12] Modify product: Na+/H+ antiporter family => Na+/H+ antiporter family protein
    [15:13:12] Modify product: RDD family => RDD family protein
    [15:13:12] Modify product: Metallo-beta-lactamase superfamily => Metallo-beta-lactamase superfamily protein
    [15:13:12] Modify product: PEGA domain => PEGA domain protein
    [15:13:12] Modify product: Sporulation related domain => Sporulation related domain protein
    [15:13:12] Modify product: HDOD domain => HDOD domain protein
    [15:13:12] Modify product: Metallo-beta-lactamase superfamily => Metallo-beta-lactamase superfamily protein
    [15:13:12] Modify product: OmpA-like transmembrane domain => OmpA-like transmembrane domain protein
    [15:13:12] Modify product: Helix-turn-helix domain => Helix-turn-helix domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: Fatty acid hydroxylase superfamily => Fatty acid hydroxylase superfamily protein
    [15:13:12] Modify product: Uracil DNA glycosylase superfamily => Uracil DNA glycosylase superfamily protein
    [15:13:12] Modify product: Heme NO binding => Heme NO binding protein
    [15:13:12] Modify product: Transposase DDE domain => Transposase DDE domain protein
    [15:13:12] Modify product: HDOD domain => HDOD domain protein
    [15:13:12] Modify product: FtsX-like permease family => FtsX-like permease family protein
    [15:13:12] Modify product: SCP-2 sterol transfer family => SCP-2 sterol transfer family protein
    [15:13:12] Modify product: Tim44-like domain => Tim44-like domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: Phage Conserved Open Reading Frame 51 => hypothetical protein
    [15:13:12] Modify product: Oxidoreductase molybdopterin binding domain => Oxidoreductase molybdopterin binding domain protein
    [15:13:12] Modify product: Acetyltransferase (GNAT) family => Acetyltransferase (GNAT) family protein
    [15:13:12] Modify product: OmpA-like transmembrane domain => OmpA-like transmembrane domain protein
    [15:13:12] Modify product: PBP superfamily domain => PBP superfamily domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: NYN domain => NYN domain protein
    [15:13:12] Modify product: Beta-lactamase superfamily domain => Beta-lactamase superfamily domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: Methyl-accepting chemotaxis protein (MCP) signaling domain => Methyl-accepting chemotaxis protein (MCP) signaling domain protein
    [15:13:12] Modify product: SprT-like family => SprT-like family protein
    [15:13:12] Modify product: TrkA-N domain => TrkA-N domain protein
    [15:13:12] Modify product: Virulence activator alpha C-term => hypothetical protein
    [15:13:12] Modify product: Glyoxalase-like domain => Glyoxalase-like domain protein
    [15:13:12] Modify product: YcgL domain => YcgL domain protein
    [15:13:12] Modify product: Tripartite tricarboxylate transporter TctB family => Tripartite tricarboxylate transporter TctB family protein
    [15:13:12] Cleaned 59 /product names
    [15:13:12] Deleting temporary file: PROKKA_01172014/proteins.faa
    [15:13:12] Deleting temporary file: PROKKA_01172014/proteins.bls
    [15:13:12] Labelling remaining 676 proteins as 'hypothetical protein'
    [15:13:12] Possible /pseudo 'Putative proximal rod protein' at NODE_1314_length_3223_cov_16.290724 position 2430
    [15:13:12] Possible /pseudo 'Spermidine/putrescine-binding periplasmic protein precursor' at NODE_144_length_5930_cov_20.574535 position 5531
    [15:13:12] Possible /pseudo 'Cytochrome c-type biogenesis protein CcmH precursor' at NODE_1480_length_8526_cov_16.777269 position 5312
    [15:13:12] Possible /pseudo 'type VI secretion protein, family' at NODE_16_length_8293_cov_17.180031 position 6886
    [15:13:12] Possible /pseudo 'Putative arginine/ornithine antiporter' at NODE_2133_length_3831_cov_17.600887 position 658
    [15:13:12] Possible /pseudo 'Macrolide export ATP-binding/permease protein MacB' at NODE_2683_length_3894_cov_16.632769 position 3387
    [15:13:12] Possible /pseudo 'GTP-binding protein HflX' at NODE_287_length_6749_cov_20.247740 position 5379
    [15:13:12] Possible /pseudo 'Chemotaxis protein CheW' at NODE_297_length_8309_cov_17.877724 position 5598
    [15:13:12] Possible /pseudo 'Twitching mobility protein' at NODE_36_length_6252_cov_21.742002 position 5964
    [15:13:12] Possible /pseudo 'WavE lipopolysaccharide synthesis' at NODE_4043_length_3732_cov_16.747589 position 2930
    [15:13:12] Possible /pseudo 'Alpha-galactosidase' at NODE_40_length_8322_cov_15.877434 position 5568
    [15:13:12] Possible /pseudo 'Macrolide export ATP-binding/permease protein MacB' at NODE_548_length_2766_cov_22.198843 position 1406
    [15:13:12] Possible /pseudo 'Molecular chaperone Hsp31 and glyoxalase 3' at NODE_622_length_3974_cov_16.775038 position 2827
    [15:13:12] Possible /pseudo 'Alpha-acetolactate decarboxylase' at NODE_911_length_17073_cov_13.548586 position 11937
    [15:13:12] Possible /pseudo 'RNA polymerase sigma factor RpoS' at NODE_979_length_7686_cov_22.014442 position 3041
    [15:13:12] Found 1738 unique /gene codes.
    [15:13:12] Fixed 200 colliding /gene names.
    [15:13:12] Adding /locus_tag identifiers
    [15:13:13] Assigned 3361 locus_tags to CDS and RNA features.
    [15:13:13] Writing outputs to PROKKA_01172014/
    [15:13:17] Generating annotation statistics file
    [15:13:17] Generating Genbank and Sequin files
    [15:13:17] Running: tbl2asn -V b -a s -N 1 -y 'Annotated using prokka 1.8 from http://www.vicbioinformatics.com' -Z PROKKA_01172014/PROKKA_01172014.err -i PROKKA_01172014/PROKKA_01172014.fsa 2> /dev/null
    [15:13:50] Deleting temporary file: PROKKA_01172014/errorsummary.val
    [15:13:50] Deleting temporary file: PROKKA_01172014/PROKKA_01172014.dr
    [15:13:50] Deleting temporary file: PROKKA_01172014/PROKKA_01172014.fixedproducts
    [15:13:50] Deleting temporary file: PROKKA_01172014/PROKKA_01172014.ecn
    [15:13:50] Deleting temporary file: PROKKA_01172014/PROKKA_01172014.val
    [15:13:50] Output files:
    [15:13:50] PROKKA_01172014/PROKKA_01172014.txt
    [15:13:50] PROKKA_01172014/PROKKA_01172014.ffn
    [15:13:50] PROKKA_01172014/PROKKA_01172014.gff
    [15:13:50] PROKKA_01172014/PROKKA_01172014.fna
    [15:13:50] PROKKA_01172014/PROKKA_01172014.err
    [15:13:50] PROKKA_01172014/PROKKA_01172014.sqn
    [15:13:50] PROKKA_01172014/PROKKA_01172014.gbk
    [15:13:50] PROKKA_01172014/PROKKA_01172014.faa
    [15:13:50] PROKKA_01172014/PROKKA_01172014.tbl
    [15:13:50] PROKKA_01172014/PROKKA_01172014.log
    [15:13:50] PROKKA_01172014/PROKKA_01172014.fsa
    [15:13:50] Walltime used: 18.58 minutes
    [15:13:50] Share and enjoy!
