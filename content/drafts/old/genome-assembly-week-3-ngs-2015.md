Title: Genome Assembly - Week 3 NGS 2015
Date: 2015-08-25 16:01
Author: monsterbashseq
Category: Bioinformatics, Genomics Workshop
Slug: genome-assembly-week-3-ngs-2015
Status: published

Great experience participating in genome assembly tutorial by [Dr. Lex
Nederbragt, Norwegian Sequencing
Centre](http://www.mn.uio.no/cees/english/people/technical/alexajo/):

https://github.com/lexnederbragt  
http://flavors.me/flxlex  
https://flxlexblog.wordpress.com/

https://www.flickr.com/photos/lpcohen/20850074396/

Notes below, feel free to comment and correct!

Atlantic cod genome assembly!
http://www.nature.com/nature/journal/v477/n7363/full/nature10342.html  
Ensembl annotation:  
http://www.ensembl.org/Gadus\_morhua/Info/Index  
http://www.aquagenome.uio.no/

Experience switching to computational work from wet lab work, 2013:
http://www.nature.com/naturejobs/science/articles/10.1038/nj7479-319a

<http://genome.cshlp.org/content/20/9/1165.long>

Focus on nonmodel organisms!  
Visualization of developments in highthroughput sequencing:  
https://flxlexblog.wordpress.com/2013/10/01/developments-in-next-generation-sequencing-october-2013-edition/

Velvet is good tool for teaching assembly. Not the best to use
practically, but good for teaching.

http://ivory.idyll.org/blog/the-assembly-exercise.html

de Bruijn graphs described for limited alphabets. Suffix trees. One of
three types of graphs, (read, overlap, de Bruijn). [Schatz et al.
2010](http://genome.cshlp.org/content/20/9/1165.long).

**Start tutorial.**

Live coding - do not give students tutorial, follow along as he goes.
Different style from previous tutorials where students are given
tutorial pre-written then follow along. The idea is for collaborative
interaction during tutorial.

Launch EC2 instance, Ubuntu 14.04 m4.xlarge:

[![EC2\_genome\_Assembly](https://monsterbashseq.files.wordpress.com/2015/08/ec2_genome_assembly.png?w=660){.alignnone
.size-large .wp-image-1020 width="660"
height="294"}](https://monsterbashseq.files.wordpress.com/2015/08/ec2_genome_assembly.png)

    sudo apt-get update
    sudo apt-get install -y g++ gcc make git zlib1g-dev python

How do you remember that? Printed paper with notes!

Etherpad with typed commands:  
https://etherpad.mozilla.org/ngs2015-week3

Print history for class to see.

    wget https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz
    tar -xvzf velvet_1.2.10.tgz

[![tar](https://monsterbashseq.files.wordpress.com/2015/08/tar.png?w=660){.alignnone
.size-large .wp-image-1022 width="660"
height="212"}](http://forums.xkcd.com/viewtopic.php?f=7&t=100061)

    cd velvet_1.2.10/
    make 'MAXKMERLENGTH=127'

"If you couldn't figure out if it did anything, re-run the commands."

Stickies up and down. (Software Carpentry has a teaching method with
colored post-it notes. Ours are pink and blue.
http://software-carpentry.org/workshops/operations.html)  
[![history\_velvet\_installation](https://monsterbashseq.files.wordpress.com/2015/08/history_velvet_installation.png){.alignnone
.size-full .wp-image-1023 width="496"
height="528"}](https://monsterbashseq.files.wordpress.com/2015/08/history_velvet_installation.png)

(Do not put spaces in PATH!!!)

Velvet installed. One hour to get here.

Now we need data.

    mkdir velvet
    cd velvet
    mkdir data
    cd data
    wget https://www.dropbox.com/s/kopguhd9z2ffbf6/MiSeq_Ecoli_MG1655_50x_R1.fastq && wget https://www.dropbox.com/s/i99h7dnaq61hrrc/MiSeq_Ecoli_MG1655_50x_R2.fastq

Questions to ask students (not doing here):

-   Are reads in the same order?
-   What does /1 and /2 mean?

        cd
        mkdir assembly
        cd assembly

    We're going to run the assembly and record results in a spreadsheet.
    We will each pick a kmer size. Here is the spreadsheet link to
    pick/assign ourselves a kmer:

    https://docs.google.com/spreadsheets/d/1MejHg68VCicqs-8saAr267BN6sKoaK2LbiP-P7mLitI/edit\#gid=0

    I picked 99.

    Why do kmers need be odd numbers? Can't be even numbers unless self
    complementary kmers. Need figure. Titus: In theory simplifies, but
    doesn't actually matter. Will: Palendromic kmers.

    Build command for velvet. Explain each parameter.

        velveth k99 99 -short -separate -fastq   
       /home/ubuntu/velvet/data/MiSeq_Ecoli_MG1655_50x_R1.fastq \ /home/ubuntu/velvet/data/MiSeq_Ecoli_MG1655_50x_R2.fastq

    Put in own numbers. These are the flags we will use. See manual for
    other options:  
   https://www.ebi.ac.uk/\~zerbino/velvet/Manual.pdf  
   http://genome.cshlp.org/content/18/5/821.full  
   (Note, this software is no longer in development. We are using this
    for teaching purposes.)

    'k99' is name of folder  
   99 is parameter kmer size  
   -short (not sanger)  
   -separate (not interleaved)  
   -fastq (not fasta)  
   full path of files, including pwd (remind students to use tab
    complete)

    This will create a directory in the current working directory called
    'k99'. Then run the velvetg command:

        velvetg k99/

    Program will run, there will be some output stored in /k99/Log.
    Results:

        Final graph has 583 nodes and n50 of 28687, max 100861, total 4564264, using 0/1546558 reads

    Nodes are \# nodes in the graph. N50 = greater than 50% of reads
    are &gt;X length. Put numbers in spreadsheet.

    Then, pick another number for k and run assembly again. I picked 45.

        velveth k45 45 -short -separate -fastq \ /home/ubuntu/velvet/data/MiSeq_Ecoli_MG1655_50x_R1.fastq \ /home/ubuntu/velvet/data/MiSeq_Ecoli_MG1655_50x_R2.fastq 
        velvetg k45

    Results:

        Final graph has 9427 nodes and n50 of 2363, max 12216, total 4727570, using 0/1546558 reads

    <p>
    This is a really cool learning experience to take part in a class of
    people all assembling data then populating table with results to
    make an x-y graph of N50 vs. k! Optimal kmer size for these data can
    be determined:

[![N50\_K\_graph](https://monsterbashseq.files.wordpress.com/2015/08/n50_k_graph.png?w=660){.alignnone
.size-large .wp-image-1024 width="660"
height="328"}](https://monsterbashseq.files.wordpress.com/2015/08/n50_k_graph.png)

Doesn't mean that at k81 all contigs are correct. Just an indication of
lengths. But, good approximation. That is what we will use.

Quiz:

Find neighbor and discuss answer. Multiple choice question. Discuss
which is correct and why. Link to Google form to enter answer. Then we
discuss distribution of answers. Go back, discuss if we want to change
our opinion based on what the class is thinking. Then vote again. Then
look at what class thinks.

https://docs.google.com/forms/d/1KxKRpSvrZ1UzV\_Ye7AUbtl3uaoSDQA0ndgk7PIVaGvk/viewform

https://www.flickr.com/photos/lpcohen/20885356611/in/photostream/

We voted 4.  Length of reads are 150. We know that error drops out as
the read gets longer.

[![length](https://monsterbashseq.files.wordpress.com/2015/08/length.png?w=660){.alignnone
.size-large .wp-image-1025 width="660"
height="120"}](https://monsterbashseq.files.wordpress.com/2015/08/length.png)

This is what the class thought:

https://www.flickr.com/photos/lpcohen/20690303388/

2 min re-discussion, time on phone - rings. Class &gt;80% still thinks
\#3 is correct.

Explanation: Higher kmer sizes, lose overlaps.

One sequence with ATTCG at end. Another sequence has same at beginning.
Share stretch of kmers. Need long kmers to resolve repeats.

Titus: Does this change when there are more data? More errors?

Errors lead to more wrong kmers. Don't have enough coverage to correct.
Therefore \#3 is correct. Not effective. If you have, e.g. 300x coverage
with 150b reads, pushes kmer higher because excessive data some of which
can be overlapped. Lower coverage, lower kmer size.

If you had perfect reads, you could have longer k. Errors are reducing
effect of coverage.

Reading to do:

Zhang et al. 2014:
http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0101271  
Chikhi and Medvedev: http://arxiv.org/abs/1304.5665  
http://cristal.univ-lille.fr/\~chikhi/pdf/2013-july-20-hitseq.pdf

    ubuntu@ip-172-31-49-141:~/velvet/assembly/k81$ column -t stats.txt | less -S

Lesson in 'less'!! This will allow you to scroll during less using the
right arrow. How do you page 55 lines forward?

    55f

55 lines back?

    55b

Stats on all nodes. Length. Coverage.

[![assembly\_stats](https://monsterbashseq.files.wordpress.com/2015/08/assembly_stats.png?w=660){.alignnone
.size-large .wp-image-1026 width="660"
height="185"}](https://monsterbashseq.files.wordpress.com/2015/08/assembly_stats.png)

Flipped kmer coverage distribution:  
[![stats](https://monsterbashseq.files.wordpress.com/2015/08/stats.png?w=660){.alignnone
.size-large .wp-image-1027 width="660"
height="517"}](https://monsterbashseq.files.wordpress.com/2015/08/stats.png)

Two and a half hours to get here.

Then, we can make modifications and tell velvet we only want kmers above
certain size. Run velvetg again (no need to run velveth again):

    velvetg k81 -exp_cov 18 -cov_cutoff 4

Results:

    Final graph has 393 nodes and n50 of 59759, max 156412, total 4564976, using 1409228/1546558 reads

[![exp\_cov](https://monsterbashseq.files.wordpress.com/2015/08/exp_cov.png?w=660){.alignnone
.size-large .wp-image-1028 width="660"
height="445"}](https://monsterbashseq.files.wordpress.com/2015/08/exp_cov.png)

If we did this practically, use Spades. Megahit with prokaryotic. Celera
assembler good luck. This assembles with different kmer sizes and merges
assemblies. Try with half the read-leangth.

    velvetg k81 -exp_cov auto -cov_cutoff auto

Results:

    Final graph has 361 nodes and n50 of 59759, max 156412, total 4562066, using 1408871/1546558 reads

[![auto](https://monsterbashseq.files.wordpress.com/2015/08/auto.png?w=660){.alignnone
.size-large .wp-image-1029 width="660"
height="504"}](https://monsterbashseq.files.wordpress.com/2015/08/auto.png)

In a course, you can have a discussion with students about:

-   Assembly quality
-   We didn't use pairing information. We have paired reads, but we just
    told velvet 'reads'. If we had, this gives the assembler more
    information, could potentially lead to better assemblies.
-   Map to reference if there is one available. Cortex will allow
    reference based assembly.
-   sequencing strategy for assembly application

