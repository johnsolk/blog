Title: Programming Quiz 1 - Week 1
Date: 2013-09-25 16:58
Author: monsterbashseq
Category: R
Slug: programming-quiz-1-week-1
Status: published

[Computing for Data
Analysis](https://class.coursera.org/compdata-003/class)

Quiz 1 Steps:

1.  Download "hw1\_data.zip" from course website.
2.  Extract files, "hw1\_data.csv". I opened this file in MS Excel, to
    visualize the data.  
   [![ProgrammingQuizW1\_data](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data.jpg?w=240){.alignnone
    .size-medium .wp-image-203 width="240"
    height="300"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data.jpg)
3.  There are 154 rows and 6 columns of data, with 1 header row with
    names: "Ozone", "Solar", "Wind.R", "Temp", "Month", "Day". Note that
    there are some missing values "NA" in the first two columns. Data in
    columns 1,2,3,4,5 all seem to be integers. In column 3, there are
    decimals, the data are numeric.
4.  I'm attempting to save this file as "hw1\_data.txt" to see if it
    will be easier to work with in R. "Save As", "Other Formats", "Save
    as type:" selected "Unicode Text (\*.txt)"
5.  With this line:

`   data <- read.table("hw1_data.txt")`

The following occurred:

[![R\_1\_nofile](http://monsterbashseq.files.wordpress.com/2013/09/r_1_nofile.jpg?w=300){.alignnone
.size-medium .wp-image-206 width="300"
height="230"}](http://monsterbashseq.files.wordpress.com/2013/09/r_1_nofile.jpg)

Probably need to set working directory in R to point towards my files.

6\. In RStudio, there is a menu option under "Session", "Set Working
Directory", "To Files Panes Location" (if you have the files section
pointed to where your working files are) or you can "Choose Directory"
to specify another location.

[![Screenshot from 2013-09-25
20:27:29](http://monsterbashseq.files.wordpress.com/2013/09/screenshot-from-2013-09-25-202729.jpg?w=640){.alignnone
.size-large .wp-image-217 width="640"
height="458"}](http://monsterbashseq.files.wordpress.com/2013/09/screenshot-from-2013-09-25-202729.jpg)

Using this menu option automatically generates this code on the command
line:

`setwd("~/Dropbox/CS/R/Coursera - Computing for Data Analysis (Sept 2013)")`

This menu option-driven code generation ability, and also having
different panes open within the RStudio GUI has a MATLAB, and also SAS,
feel to it.

7\. Now, with this line:

`   data <- read.table("hw1_data.txt")`

The following occurred:

`Error in type.convert(data[[i]], as.is = as.is[i], dec = dec, na.strings = character(0L)) : invalid multibyte string at '<ff><fe>O'`

To me, this suggests there is something wrong with the file. Maybe I
shouldn't have exported the original "hw1\_data.csv" we were given to a
.txt file? The only instructions we were given about this file were:

> ### Data
>
> The zip file containing the data for this assignment can be downloaded
> here:
>
> -   [hw1\_data.zip
>     \[1.4K\]](http://spark-public.s3.amazonaws.com/compdata/data/hw1_data.zip)
>
> For this assignment you will need to unzip this file in your working
> directory.

I need to find more information about data file formats in R and how to
read them.

7\. Here are some links:

\[1\] <http://cran.r-project.org/doc/manuals/r-release/R-data.html>

\[2\] <http://www.cyclismo.org/tutorial/R/input.html>

\[3\] <http://www.r-tutor.com/r-introduction/data-frame/data-import>

8\. It looks like, from
\[[2](http://www.cyclismo.org/tutorial/R/input.html)\], that this
command can be used to open a .csv file:

**`data<- read.csv(file="hw1_data.csv", head=TRUE)`**

And, SUCCESS! A line appears in the upper right corner of the screen
under the "Data" section that there are "153 obs. of 6 variables".

[![ProgrammingQuizW1\_data\_csvfile\_success](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_success.jpg?w=640){.alignnone
.size-large .wp-image-208 width="640"
height="390"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_success.jpg)

Yay! Now, I can begin answering the questions about the data.

9\. First, I have to print the data to the console and answer some
questions about the way they appear:

`print(data)`

Then, I have to only print the last 2 rows. I don't know how to do this
yet, so I type this to look at the documentation:

`?read.csv`

This is the format for `read.csv`:

`read.csv(file, header = TRUE, sep = ",", quote = "\"", dec = ".", fill = TRUE, comment.char = "", ...)`

I think that this might help:

> **row.names**  
> a vector of row names. This can be a vector giving the actual row
> names, or a single number giving the column of the table which
> contains the row names, or character string giving the name of the
> table column containing the row names.
>
> If there is a header and the first row contains one fewer field than
> the number of columns, the first column in the input is used for the
> row names. Otherwise if row.names is missing, the rows are numbered.
>
> Using row.names = NULL forces row numbering. Missing or NULL row.names
> generate row names that are considered to be ‘automatic’ (and not
> preserved by as.matrix).

Therefore, I try this:

[![ProgrammingQuizW1\_data\_csvfile\_last2rows\_error](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_error.jpg?w=640){.alignnone
.size-large .wp-image-211 width="640"
height="158"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_error.jpg)

No luck. How about this?  
[![ProgrammingQuizW1\_data\_csvfile\_last2rows\_columnheadersdifferent](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_columnheadersdifferent.jpg?w=640){.alignnone
.size-large .wp-image-212 width="640"
height="133"}](http://monsterbashseq.files.wordpress.com/2013/09/programmingquizw1_data_csvfile_last2rows_columnheadersdifferent.jpg)  
These are the data in last two rows, but now they are rows 1 and 2 and
the column headers are different.

What about a subset?

`data<- subset(data,row>151)`

Output:

`Error in row > 151 : comparison (6) is possible only for atomic and list types`

Ok. Now I'm really not sure what to do. At this point, I miss Python and
am wondering why I'm learning R? I'm distracted and start
Google-searching "microarray data python" and come up with several
interesting pages that I would like to revist later:

\[4\]
<http://stackoverflow.com/questions/2293143/python-script-for-robust-multi-array-average-on-microarray-data>  
\[5\] <http://www.ncbi.nlm.nih.gov/pubmed/20970526>  
\[6\] <https://sites.google.com/site/plaisier/python-examples-1>

I agree with
\[[4](http://stackoverflow.com/questions/2293143/python-script-for-robust-multi-array-average-on-microarray-data)\],
in that the vast majority of microarray data packages have already been
written for R, so it makes sense to learn R. RPy seems intriguing,
though, so I will explore this later.

Back to R. I think the answer is in a subset, but I can't figure this
out just yet. I want to take a subset of the data. The rows are counted
by R with an integer. I need there to be a vector of row numbers -
somehow - then my data subset will skip rows&lt;152. I don't know how to
tell R this yet.
