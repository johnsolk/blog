Title: Subsetting Data
Date: 2013-09-26 13:20
Author: monsterbashseq
Category: Coursera, R
Slug: subsetting-data
Status: published

In addition to what I tried yesterday, I tried these today, with no
luck:

[![ProgrammingQuizW1\_data\_csvfile\_last2rows\_error2](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_error2.jpg?w=640){.alignnone
.size-large .wp-image-223 width="640"
height="320"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_error2.jpg)

Then, finally, this worked!

[![ProgrammingQuizW1\_data\_csvfile\_last2rows\_WORKS](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_works1.jpg){.alignnone
.size-full .wp-image-233 width="505"
height="153"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_works1.jpg)

A combination of \[1\] and the lecture notes on subsetting lists and
matrices, with syntax:  

    > x<-list(foo=1:4,bar=0.6,baz="hello")
    > x[c(1,3)]
    $foo
    [1] 1 2 3 4

    $baz
    [1] "hello"

    > x[[c(1,3)]]
    [1] 3

\[1\]
http://stackoverflow.com/questions/13817174/how-can-i-extract-non-consecutive-rows-from-a-data-set-in-r?rq=1

This also seems to work:

[![ProgrammingQuizW1\_data\_subset](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_subset.jpg?w=300){.alignnone
.size-medium .wp-image-251 width="300"
height="132"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_subset.jpg)
