Title: aRgh
Date: 2015-03-18 12:21
Author: monsterbashseq
Category: limma, Microarray, R
Slug: argh
Status: published

Getting data into the right format is a frustration I have with R:  
``  > arrayQualityMetrics(expressionset = eset,outdir = "ArrayQualityMetrics",intgroup = c("sample_type_2.0"),do.logtransform=TRUE) The directory 'ArrayQualityMetrics' has been created. Error in `[.data.frame`(x, order(x, na.last = na.last, decreasing = decreasing)) : undefined columns selected ``

I've run into this problem before and manage to forget from time to
time. From this post
(http://stackoverflow.com/questions/21178236/r-quantile-of-a-data-frame-is-giving-me-undefined-columns-selected),
remembered that data cannot be a data frame class, instead a matrix
class. I still don't understand the difference between matrix and data
frame in R. Sometimes certain functions complain if data are in one
class vs. another so you just have to figure out which is best for what
you're doing and convert between the two when necessary.

Switch from data frame to matrix and back again with:

` x<-as.matrix(y) y<-as.data.frame(x)`  
For the [Bioconductor,
limma](http://master.bioconductor.org/packages/release/bioc/html/limma.html)
package with the ExpressionSet container, the featureData (annotations)
and phenoData (sample info) objects must be data frames, while the
assayData "exprs" must be a matrix.
