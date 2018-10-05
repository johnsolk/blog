Title: Missing Values
Date: 2013-09-26 14:14
Author: monsterbashseq
Category: Coursera, R
Slug: missing-values
Status: published

> How many missing values are in the Ozone column of this data frame?

I want to calculate the number of missing values in a column without
having to count them by hand. I'm not sure how to subset only one column
of data.

I try this:

[![ProgrammingQuizW1\_data\_missingvalues\_completecases](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_completecases.jpg?w=640){.alignnone
.size-large .wp-image-231 width="640"
height="225"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_completecases.jpg)

It gives me 153 values. This is the number of rows in the data matrix.
But, I'm not sure which columns are represented here.

I try this:

[![ProgrammingQuizW1\_data\_missingvalues\_attempt](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_attempt1.jpg?w=300){.alignnone
.size-medium .wp-image-253 width="300"
height="171"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_attempt1.jpg)

And while it seems to print all rows of just the first column and
displays the number of missing values, I would have to count them by
hand. I want to code a counter to do this for me. There is no mention in
the Coursera lecture notes about how to count the number of occurrences.
I try a Google search for "R count number of missing values in column"
and this was helpful:

\[1\] http://forums.psy.ed.ac.uk/R/P01582/essential-10/

I try this and it seems to work:

[![ProgrammingQuizW1\_data\_missingvalues\_works\_sortof](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_works_sortof.jpg){.alignnone
.size-full .wp-image-249 width="264"
height="111"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_works_sortof.jpg)

The closest multiple choice option on the quiz is 43. I select this, but
get the answer wrong.

> **Question Explanation**
>
> The \`is.na' function can be used to test for missing values.

I've already used this, but clearly in the wrong way. So. Let's try
again.

[![ProgrammingQuizW1\_data\_subset4](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_subset4.jpg){.alignnone
.size-full .wp-image-285 width="559"
height="179"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_subset4.jpg)

[![ProgrammingQuizW1\_data\_subset4\_answer](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_subset4_answer.jpg){.alignnone
.size-full .wp-image-286 width="210"
height="53"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_subset4_answer.jpg)

This is the correct answer.
