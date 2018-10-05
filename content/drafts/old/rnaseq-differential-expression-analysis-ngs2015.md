Title: RNAseq differential expression analysis - NGS2015
Date: 2015-08-26 12:11
Author: monsterbashseq
Category: Bioinformatics, Genomics Workshop
Slug: rnaseq-differential-expression-analysis-ngs2015
Status: published

Dr. Meeta Mistry, [Harvard School of Public Health, Bioinformatics
Core](http://cbmi.catalyst.harvard.edu/cores/cat/core.html?core_id=121&uri_id=0000012e-58be-17bc-55da-381e80000000&category_id=10&navMode=cat)

See awesome workflows available from facility:

https://bcbio-nextgen.readthedocs.org/en/latest/

HSPH Bioinformatics Core offers regular short courses, Introduction to
RNA-Seq, ChIP-seq, Unix and R courses as well as in-depth NGS courses,
Software and Data Carpentry, version control, downstream analyses in R.
Selected only one individual. Emphasis with getting people to
come discuss before starting a sequencing experiment.

Really awesome slides and presentation discussion of intricacies of
RNAseq workflow, highlighting Poisson distribution vs. negative binomial
distribution.

https://www.flickr.com/photos/lpcohen/20901869925/

**Tutorial**

Summary: Use different tools. Understand underlying assumptions and math
associated with each model. Compare. Have robust design and number of
samples. Validate your results with additional experimentation, e.g.
[Nanostring](http://www.nanostring.com/applications/technology)or qPCR
(old).

https://github.com/mistrm82/msu\_ngs2015/blob/master/hands-on.Rmd

Libraries installed before the tutorial:

    source("https://bioconductor.org/biocLite.R")
    biocLite("BiocStyle")
    source("https://bioconductor.org/biocLite.R")
    biocLite("BiocStyle")
    biocLite(limma)
    biocLite('edgeR')
    biocLite("DESeq2")
    library(limma)
    library('edgeR')
    library('DESeq2')

Then get data from repo:

    mkdir RNAseq_workflow
    cd RNAseq_workflow
    git clone https://github.com/mistrm82/msu_ngs2015.git
    cd msu_ngs2015

Open RStudio, navigate to the directory where you cloned the repo where
the .RData file is, then set working directory. Can be done with command
or from menu in RStudio.

    setwd("~/RNAseq_workflow/msu_ngs2015")

[![set\_working\_directory](https://monsterbashseq.files.wordpress.com/2015/08/set_working_directory.png?w=300){.alignnone
.size-medium .wp-image-1049 width="300"
height="129"}](https://monsterbashseq.files.wordpress.com/2015/08/set_working_directory.png)

Then, load the data into the RStudio environment:

    load("~/RNAseq_workflow/msu_ngs2015/bottomly_eset.RData")

Loading complicated ExpressionSet .eset object. A clunky process of
getting data into this structure, so we just load a saved .RData object
here. Instructions for getting your raw count data into this object can
be found in the DESeq2 vignette. Also, use library(BioBase) and
?ExpressionSet.

    eset <- bottomly.2reps

[![eset](https://monsterbashseq.files.wordpress.com/2015/08/eset.png?w=300){.alignnone
.size-medium .wp-image-1056 width="300"
height="172"}](https://monsterbashseq.files.wordpress.com/2015/08/eset.png)

Then, we can make calculations:

    eset <- bottomly.2reps
    cpm.mat <- log(cpm(exprs(eset)))
    mean.vec <- apply(cpm.mat, 1, mean)
    sdvec <- apply(cpm.mat, 1, sd)
    plot(mean.vec, sdvec, pch=".", main="2 replicates", ylab="sd", xlab="Average logCPM")

Heteroscedacity, 2 replicates:  
[![heteroscedacity](https://monsterbashseq.files.wordpress.com/2015/08/heteroscedacity.png?w=300){.alignnone
.size-medium .wp-image-1050 width="300"
height="209"}](https://monsterbashseq.files.wordpress.com/2015/08/heteroscedacity.png)

5 replicates:

    eset <- bottomly.5reps
    cpm.mat <- log(cpm(exprs(eset)))
    mean.vec <- apply(cpm.mat, 1, mean)
    sdvec <- apply(cpm.mat, 1, sd)
    plot(mean.vec, sdvec, pch=".", main="5 replicates", ylab="sd", xlab="Average logCPM")

[![heterscedacity\_5replicates](https://monsterbashseq.files.wordpress.com/2015/08/heterscedacity_5replicates.png?w=300){.alignnone
.size-medium .wp-image-1051 width="300"
height="209"}](https://monsterbashseq.files.wordpress.com/2015/08/heterscedacity_5replicates.png)

10 replicates:

    eset <- bottomly.eset
    cpm.mat <- log(cpm(exprs(eset)))
    mean.vec <- apply(cpm.mat, 1, mean)
    sdvec <- apply(cpm.mat, 1, sd)
    plot(mean.vec, sdvec, pch=".", main="10 replicates", ylab="sd", xlab="Average logCPM")

[![heteroscedacity\_10replicates](https://monsterbashseq.files.wordpress.com/2015/08/heteroscedacity_10replicates.png?w=300){.alignnone
.size-medium .wp-image-1052 width="300"
height="209"}](https://monsterbashseq.files.wordpress.com/2015/08/heteroscedacity_10replicates.png)

Each point represents a gene/transcript. Discussion of what is being
shown in these plots? On the x axis is log of mean CPM for each
gene/transcript across all replicates. On the y axis is standard
deviation of the log mean values. The variance shrinks across genes as
the number of replicates (from 2 to 10) are increased. Here is a good
reference with a nicely designed experiment showing what happens when
you increase number of replicates to 48:

http://arxiv.org/pdf/1505.00588.pdf

Dispersion is a parameter that estimates variability within negative
binomial distribution. Analagous for variance for normal distribution.
Because never sampling randomly, dispersion does not penalize
differences from mean. Why does the trend look the way it does? Why does
it trend asymptotically? Lower end lacks statistical power towards low
end.

Mathematical property of taking log of counts, fractions are not
equidistant. See Bioconductor vignette:

https://www.bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.pdf

Dispersion estimate is built-in to the DESeq model.

2 replicates, overestimated for lower replicates, lowering true
differential expression:  
[![dispersion\_2replicates](https://monsterbashseq.files.wordpress.com/2015/08/dispersion_2replicates.png?w=300){.alignnone
.size-medium .wp-image-1053 width="300"
height="206"}](https://monsterbashseq.files.wordpress.com/2015/08/dispersion_2replicates.png)  
5 replicates:  
[![dispersion\_5replicates](https://monsterbashseq.files.wordpress.com/2015/08/dispersion_5replicates.png?w=300){.alignnone
.size-medium .wp-image-1054 width="300"
height="206"}](https://monsterbashseq.files.wordpress.com/2015/08/dispersion_5replicates.png)  
10 replicates:  
[![dispersion\_10replicates](https://monsterbashseq.files.wordpress.com/2015/08/dispersion_10replicates.png?w=300){.alignnone
.size-medium .wp-image-1055 width="300"
height="206"}](https://monsterbashseq.files.wordpress.com/2015/08/dispersion_10replicates.png)  
Decreasing dispersion will result in more false positives. Shrinkage is
greater below the line than above.

Interesting discussion including point that people running these
analyses are sometimes blindly running packages and describing in
methods, e.g. "DESeq2 was run with default parameters with version y".
These packages have been designed to be easily run, code is not
difficult and can be run without any understanding the assumptions and
models running behind the scenes. Instead, really understand what is
going on and try a few packages. Look into the data objects and look at
these dispersion estimates. In methods, include something like "I used
DESeq version x and EdgeR version y. Results were similar using MDS."
Show overlaps between packages. Which genes cluster together? Confidence
from multiple approaches and discussion demonstrating understanding for
why genes were chosen based on confidence in where they lie within
the mathematical models underlying the packages used.

edgeR

[![edgeR\_2replicates](https://monsterbashseq.files.wordpress.com/2015/08/edger_2replicates.png?w=300){.alignnone
.size-medium .wp-image-1059 width="300"
height="164"}](https://monsterbashseq.files.wordpress.com/2015/08/edger_2replicates.png)

[![edgeR\_5replicates](https://monsterbashseq.files.wordpress.com/2015/08/edger_5replicates.png?w=300){.alignnone
.size-medium .wp-image-1060 width="300"
height="164"}](https://monsterbashseq.files.wordpress.com/2015/08/edger_5replicates.png)

[![edgeR\_10replicates](https://monsterbashseq.files.wordpress.com/2015/08/edger_10replicates.png?w=300){.alignnone
.size-medium .wp-image-1061 width="300"
height="164"}](https://monsterbashseq.files.wordpress.com/2015/08/edger_10replicates.png)

voom

2 replicates

[![voom\_replicates\_2replicates](https://monsterbashseq.files.wordpress.com/2015/08/voom_replicates_2replicates.png?w=300){.alignnone
.size-medium .wp-image-1062 width="300"
height="164"}](https://monsterbashseq.files.wordpress.com/2015/08/voom_replicates_2replicates.png)

5 replicates

[![voom\_5replicates](https://monsterbashseq.files.wordpress.com/2015/08/voom_5replicates.png?w=300){.alignnone
.size-medium .wp-image-1063 width="300"
height="164"}](https://monsterbashseq.files.wordpress.com/2015/08/voom_5replicates.png)

10 replicates

[![voom\_10replicates](https://monsterbashseq.files.wordpress.com/2015/08/voom_10replicates.png?w=300){.alignnone
.size-medium .wp-image-1064 width="300"
height="164"}](https://monsterbashseq.files.wordpress.com/2015/08/voom_10replicates.png)

**Comparisons between methods:**

See the [tutorial for
code](https://github.com/mistrm82/msu_ngs2015/blob/master/hands-on.Rmd),
here is overlap between edgeR, voom and DESeq2 with p.threshold=0.05 and
10 replicates:

[![overlap\_genes\_voom\_edgeR\_DEseq](https://monsterbashseq.files.wordpress.com/2015/08/overlap_genes_voom_edger_deseq.png?w=300){.alignnone
.size-medium .wp-image-1057 width="300"
height="281"}](https://monsterbashseq.files.wordpress.com/2015/08/overlap_genes_voom_edger_deseq.png)

Here is output with same comparisons, same threshold, with 2 replicates:

[![overlap\_2replicates](https://monsterbashseq.files.wordpress.com/2015/08/overlap_2replicates.png?w=300){.alignnone
.size-medium .wp-image-1058 width="300"
height="281"}](https://monsterbashseq.files.wordpress.com/2015/08/overlap_2replicates.png)

From NGS2015 week 1, Dr. Ian Dworkin identified for the class options
for tools for RNAseq to choose from:

https://www.flickr.com/photos/lpcohen/20725950392/

If someone has a small number of replicates, beware of the caveats of
these particular software tools and the impact on final results. DESeq2,
voom, and EdgeR can handle lower replicate numbers. But, confidence in
results will be low. The number of replicates is, of course, based on
funding constraints. 48 replicates might be too much. But, 5 or 6 is
optimal suggested number. By increasing number of replicates, increasing
certainty for each individual gene. Tools will work better because they
are based on this underlying assumption. More reliable distribution,
better answers.
