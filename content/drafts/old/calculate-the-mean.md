Title: Calculate the mean
Date: 2013-09-27 21:13
Author: monsterbashseq
Category: Coursera, R
Slug: calculate-the-mean
Status: published

> What is the mean of the Ozone column in this dataset? Exclude missing
> values (coded as NA) from this calculation.

There is no information in the Coursera lecture notes on how to
calculate the mean from a column of data. I Google search for "R
calculate mean exclude missing values":

Some helpful links and info:

\[1\] http://www.statmethods.net/input/missingdata.html

Excluding Missing Values from Analyses
--------------------------------------

Arithmetic functions on missing values yield missing values.

`x <- c(1,2,NA,3) mean(x) # returns NA mean(x, na.rm=TRUE) # returns 2 `

The function **complete.cases()** returns a logical vector indicating
which cases are complete.

`# list rows of data that have missing values mydata[!complete.cases(mydata),]`

The function **na.omit()** returns the object with listwise deletion of
missing values.

`# create new dataset without missing data newdata <- na.omit(mydata) `

\[2\] https://stat.ethz.ch/pipermail/r-help/2007-November/146886.html

The following series of commands end up working:

[![ProgrammingQuizW1\_data\_mean\_subsetcolumn\_attempt](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_mean_subsetcolumn_attempt.jpg){.alignnone
.size-full .wp-image-258 width="562"
height="180"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_mean_subsetcolumn_attempt.jpg)

[![ProgrammingQuizW1\_data\_missingvalues\_attempt](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_attempt2.jpg){.alignnone
.size-full .wp-image-263 width="135"
height="460"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_attempt2.jpg)

This produced an integer matrix of 153 values, which includes missing
values.

Then,

[![ProgrammingQuizW1\_data\_missingvalues\_attempt2](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_attempt22.jpg){.alignnone
.size-full .wp-image-265 width="562"
height="146"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_attempt22.jpg)

This puts the data back into another format. An attempt to take the mean
of the column results in an error (below). So, I put them back into a
matrix with another u&lt;-cbind(u) command.

[![ProgrammingQuizW1\_data\_missingvalues\_colmeans](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_colmeans.jpg){.alignnone
.size-full .wp-image-266 width="518"
height="586"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_colmeans.jpg)

The result is this, which is the correct answer for the quiz:

[![ProgrammingQuizW1\_data\_missingvalues\_works\_sortof](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_works_sortof2.jpg){.alignnone
.size-full .wp-image-268 width="121"
height="53"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_missingvalues_works_sortof2.jpg)
