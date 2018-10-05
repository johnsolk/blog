Title: Workshop on Genomics (Notes, Day 2) - Advanced UNIX
Date: 2014-01-14 09:51
Author: monsterbashseq
Category: Genomics Workshop, Linux
Slug: workshop-on-genomics-notes-day-2-advanced-unix
Status: published

UNIX tutorial instructions: http://evomics.org/learning/unix-tutorial/  
Exercises, part 2:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2014/01/2014\_genomics\_IntroUnixPart2.pdf

Common UNIX commands:
http://mally.stanford.edu/\~sr/computing/basic-unix.html

Homework assignment 1:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2014/01/2014\_genomics\_unix\_hw\_1.pdf  
Homework 2:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2014/01/2014\_genomics\_unix\_hw\_2.pdf

Yesterday, take tab-separated file, manipulate data in columns, filter
by value  
Take gene-pop file, manipulate with shell program sed

Today:  
1. Review of pipes  
2. Regular Expressions  
3. sed  
4. edit fastq file headers  
5. Shell loops  
6. Shell scripts

Yesterday, pipes:

    cat seqs.fa | grep '^ACGT' output

Only things that meet conditions of grep will make it through to output.

Today, Regular Expressions - finding patters in text  
![](http://imgs.xkcd.com/comics/perl_problems.png){.alignnone
width="548" height="205"}  
Simplest, '.'  
Character class, match anything one or more of the letters: \[ACGT\]  
One or more of the numbers 0-9: \[0-9\]+  
Find someone's first and last name (lower case): \[a-z\]+ \[a-z\]+  
Phone number: \[0-9\]{3}\\-\[0-9\]{3}\\-\[0-9\]{4}  
\\makes literal hyphen  
Find America date format before the 10th, e.g. June 3, 1978: \[a-zA-Z\]+
\[0-9\], \[0-9\]{4}

Command-line tricks:  
Ctrl-a beginning of line  
Ctrl-e end of line  
Ctrl-d delete in place  
Ctrl-v tab (literal tab)

[![Screenshot from 2014-01-14
16:03:25](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-160325.png){.alignnone
.size-full .wp-image-728 width="640"
height="493"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-160325.png)

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ cp /unix_data/record.tsv.gz record.tsv.gz
    ubuntu@domU-12-31-39-0B-68-22:~/shell$ gunzip record.tsv.gz

To highlight first and last name:

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ grep -E "[a-z]+ [a-z]+" record.tsv
    341341  julian catchen  541-485-5128    June 3, 1978
    1243    rodger voelker 541-234-4732     January 12, 1981 
    99999   andy berglund  541-498-9999     August 03, 2000
    37916   william cresko (541) 234-4522       Mar 7, 1977
    222 john letaw  123-455-7834    September 1996

To highlight phone numbers:

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ grep -E "[0-9]{3}\-[0-9]{3}\-[0-9]{4}" record.tsv
    341341  julian catchen  541-485-5128    June 3, 1978
    1243    rodger voelker 541-234-4732     January 12, 1981 
    99999   andy berglund  541-498-9999     August 03, 2000
    222 john letaw  123-455-7834    September 1996

To match capital and lowercase words, character class order does not
matter:

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ grep -E "[A-Za-z]+" record.tsv

sed, a stream editor, ctd.

    s/pattern/replace/

Search and replace:

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ cat record.tsv |sed -E 's/[a-z]+ [a-z]+/foo/'
    341341  foo 541-485-5128    June 3, 1978
    1243    foo 541-234-4732        January 12, 1981 
    99999   foo  541-498-9999       August 03, 2000
    37916   foo (541) 234-4522      Mar 7, 1977
    222 foo 123-455-7834    September 1996

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ cat record.tsv |sed -E 's/[a-z]+) [a-z]+/\1/'
    sed: -e expression #1, char 20: Unmatched ) or \)
    ubuntu@domU-12-31-39-0B-68-22:~/shell$ cat record.tsv |sed -E 's/([a-z]+) [a-z]+/\1/'
    341341  julian  541-485-5128    June 3, 1978
    1243    rodger 541-234-4732     January 12, 1981 
    99999   andy  541-498-9999      August 03, 2000
    37916   william (541) 234-4522      Mar 7, 1977
    222 john    123-455-7834    September 1996

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ cat record.tsv |sed -E 's/[0-9]+//'
        julian catchen  541-485-5128    June 3, 1978
        rodger voelker 541-234-4732     January 12, 1981 
        andy berglund  541-498-9999     August 03, 2000
        william cresko (541) 234-4522       Mar 7, 1977
        john letaw  123-455-7834    September 1996

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ cat record.tsv |sed -E 's/[0-9]+//g'
        julian catchen  --  June , 
        rodger voelker --       January ,  
        andy berglund  --       August , 
        william cresko () -     Mar , 
        john letaw  --  September 

    ubuntu@domU-12-31-39-0B-68-22:~/shell$ cat record.tsv |sed -E 's/[0-9]+         //'
    341341  julian catchen  541-485-5128    June 3, 1978
    1243    rodger voelker 541-234-January 12, 1981 
    99999   andy berglund  541-498-August 03, 2000
    37916   william cresko (541) 234-Mar 7, 1977
    222 john letaw  123-455-7834    September 1996

Use sed to rename series of many files.

Use this to pipe files into pipe one line at a time:

    ls -1

    ls -1 |sed -E 's/^(fish_[0-9]+\.tags)\.tags)\.tsv/mv \1\.tsv \1.loc/'
