Title: Reading single-channel microarray data
Date: 2013-05-09 18:07
Author: monsterbashseq
Category: limma, R
Tags: BioConductor
Slug: r-targets-file
Status: published

The first step in working with microarray data, in general, is to gather
and format all of your data files. In most cases, this can be a tedious
task. In R, the first step is to import your data.

1\. Create a Microsoft Excel spreadsheet with the names of all raw data
files in the experiment. In this particular experiment with sponge
samples, we had 9 chips (8 samples per chip). Assign each chip/slide its
own unique number 1-*x* (where *x* is the total number of chips in the
experiment). These raw intensity data files can be .gpr or .txt files
exported from Gene Pix Pro image processing software. Gene Pix Pro
creates and reads .tiff files from the microarray laser scanner (ours is
an Axon 4200). We use single-channel microarrays (Cy3). This is what the
Excel file will look like:

[![targets](http://monsterbashseq.files.wordpress.com/2013/05/targets.jpg?w=640){.alignnone
.size-large .wp-image-4 width="640"
height="546"}](http://monsterbashseq.files.wordpress.com/2013/05/targets.jpg)

2\. Save As Type Text (tab delimited) (\*.txt) with the filename
"targets.txt" (or whatever you want to name your file).

3\. In the Linux Terminal, start R.

flcellogrl@purplebanyan:\~\$R

4\. Use the following R commands to import the **linear models for
microarray data (limma)** library, see which working directory you're
in, if you're not in the one you want to be in, change the working
director to let the R environment know where to look for your files, and
then read the "targets.txt" file.

&gt;library(limma)  
&gt;getwd()  
\[1\] "/home/flcellogrl"  
&gt;setwd("/home/flcellogrl/R/sponge")  
&gt;getwd()  
\[1\] "/home/flcellogrl/R/sponge"  
&gt;targets&lt;-readTargets("targets.txt")  
&gt;targets  
Slide.Number                   File.Name  
1            1 253295110067\_2012-08-01.txt  
2            2 253295110050\_2012-07-25.txt  
3            3 253295110075\_2012-09-20.txt  
4            4 253295110077\_2012-09-13.txt  
5            5 253295110079\_2012-09-06.txt  
6            6 253295110065\_2012-08-09.txt  
7            7 253295110035\_2012-08-23.txt  
8            8 253295110062\_2012-08-16.txt  
9            9 253295110059\_2012-08-30.txt

This targets file, now that it has been read by the R environment, can
be used to further process the raw intensity data.

**References**  
\[1\]
http://www.bioconductor.org/packages/release/bioc/vignettes/limma/inst/doc/usersguide.pdf  
\[2\]
http://matticklab.com/index.php?title=Single\_channel\_analysis\_of\_Agilent\_microarray\_data\_with\_Limma  
\[3\] http://frink.nuigalway.ie/\~pat/2007-02-19\_130\_0532.gpr
