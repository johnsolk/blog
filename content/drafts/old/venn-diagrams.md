Title: Venn Diagrams
Date: 2014-07-09 22:29
Author: monsterbashseq
Category: Bioconductor, Bioinformatics, R
Slug: venn-diagrams
Status: published

Today's adventures in Venn Diagrams. Seems like a simple task, right?
Two (or more) circles with numbers in the middle. I want to use this
visualization graphic to show the number of genes differentially
expressed between 2 sets of groups.

Fold-change differences in gene expression were calculated between 2
groups, relative to the control.

The question: How many genes are expressed differently between one set
of groups vs. the other set of groups? What are the genes they are
expressing in common?

Since these are three groups, two of which are being compared to a
control, it is helpful to know what genes are expressed in common
between the two treatments and which are different. This way, the
researchers can narrow in on what those same or different genes are
doing, then target treatment, therapy, or possibly use a suite of these
as biomarkers for diagnosis.

I'm using R. This is a topic for another post about how much I dislike
R.

Venn diagrams are a bit arbitrary, but they can give you a ballpark
idea. This is just a methodical process of filtering. The cutoff for
what is "differentially expressed" is a bit arbitrary and depends on the
results. What is a reasonable cutoff? We're aiming for significant, so a
p or alpha value of 0.05 is usually used to indicate that 95% of the
differences seen can be explained from biological significance, rather
than by chance. We also have a q value, which is an adjusted p value and
more stringent. (The [mathematical details of these particular
tests](http://training.bioinformatics.ucdavis.edu/docs/2012/05/RNA/_downloads/the-statistics-of-rna-seq.pdf)
are also for another day's post.) The q value is more stringent, and
since we have tens of thousands of genes, using q&lt;0.25 will narrow
our results down to lists with hundreds of "significantly" different
genes, making the task of identifying the functions of these genes
(rather than tens or hundreds of thousands) more manageable. Since we
assign an arbitrary cutoff of significance, some groups end up having
slightly different numbers of significantly different genes compared to
the control, so a Venn diagram approach to displaying these differences
is a bit arbitrary, but narrowing down hundreds from hundreds of
thousands will give an idea that there are differences identify genes to
investigate further.

It would be more interesting if we had more comparisons to make, but we
are only making 2 today. The first challenge to making graphics in R, or
doing anything in R really, is getting your data in the right format.
There are data.frames, matrices, tables, vectors, etc. Column names have
to match up between matrices being compared, otherwise you are comparing
the wrong values. There is a general graphic package in R called
'[gplots](http://cran.r-project.org/web/packages/gplots/gplots.pdf)'.
This will give you all kinds of good graphing tools, such as histograms,
heatmaps, plots, and venn diagrams. This was the most logical choice to
look up when setting out to make a venn diagram. In doing an internet
search, there seem to be quite a few venn diagram packages, introducing
color, ease of coding, and other features. At first I was hung up on
wanting color. After realizing how complicated this is, I became less
interested in this feature. The [limma
Bioconductor](http://www.bioconductor.org/packages/release/bioc/vignettes/limma/inst/doc/usersguide.pdf)
package also has a function for the venn diagram. Also, no color. These
are the basic steps. The venn diagram is just counts, so the basic idea
is you have to create an array with 0 or 1 for each gene for each
comparison to indicate whether the gene is present or absent in that
group.

1.  Use the 'union' function in R to get a list of all unique genes
    shared between the groups.
2.  Make a list of all 0 the length of the union list for each group.
3.  Match the differentially-expressed gene list with the list of all 0
    in \#2 and set the matches=1. (This will give you a list of 0 and 1,
    depending on whether the gene was present or not.) Do this for all
    groups.
4.  cbind the groups together
5.  Venn diagram of counts.

gplots:
[![second\_venn](https://monsterbashseq.files.wordpress.com/2014/07/second_venn.png?w=640){.alignnone
.size-large .wp-image-841 width="640"
height="477"}](https://monsterbashseq.files.wordpress.com/2014/07/second_venn.png)limma:
![redo\_limma\_venn](https://monsterbashseq.files.wordpress.com/2014/07/redo_limma_venn.png?w=640){.alignnone
.size-large .wp-image-840 width="640" height="471"} Thankfully, the
results are the same (which obviously they should be because I'm giving
the same data structure to each function). Here is my code:

    # with help from:
    # https://insilicodb.com/compare-deg-signatures/
    # http://cran.r-project.org/web/packages/colorfulVennPlot/colorfulVennPlot.pdf
    library(limma)
    library(gplots)
    raw_ApoE_WT<-read.csv("sig_genes_WT_ApoE.csv",sep=",")
    raw_DKO_WT<-read.csv("sig_genes_WT_DKO.csv",sep=",")
    gene.ApoE_WT<-raw_ApoE_WT$gene
    gene.DKO_WT<-raw_DKO_WT$gene
    gene_union<-union(gene.ApoE_WT,gene.DKO_WT)
    ApoE_WT<-array(0,dim=c(length(gene_union)))
    DKO_WT<-array(0,dim=c(length(gene_union)))
    ApoE_WT[match(gene.ApoE_WT,gene_union)]=1
    DKO_WT[match(gene.DKO_WT,gene_union)]=1
    #limma package vennDiagram
    venncounts_all<-cbind(ApoE_WT,DKO_WT)
    venncounts=vennCounts(venncounts_all)
    vennDiagram(venncounts)
    # gplots venn
    combined<-cbind(ApoE_WT,DKO_WT)
    combined_data.frame<-as.data.frame(combined)
    venn(combined_data.frame)

My colleague was disappointed that I couldn't get colorful venn
diagrams, so this will be a project for another day when I have more
time to spend on this. The two packages that seem promising are
venneuler and colorfulVennPlot. Here are some helpful references for
then:

http://cran.r-project.org/web/packages/colorfulVennPlot/colorfulVennPlot.pdf  
http://www.inside-r.org/packages/cran/colorfulVennPlot/docs/plotVenn3d  
http://stackoverflow.com/questions/1428946/venn-diagrams-with-r  
https://github.com/drpowell/vennt  
https://www.biostars.org/p/102393/  
https://insilicodb.com/compare-deg-signatures/  
http://www.inside-r.org/packages/cran/colorfulVennPlot/docs/plotVenn  
http://stackoverflow.com/questions/9121956/legend-venn-diagram-in-venneuler  
http://stackoverflow.com/questions/8713994/venn-diagram-in-r-proportional-and-color-shading-possible-semi-transparency-sup  
http://stackoverflow.com/questions/8153594/venn-diagram-from-list-of-clusters-and-co-occuring-factors  
https://www.biostars.org/p/70963/  
http://www.ats.ucla.edu/stat/r/faq/venn.htm  
http://www.biomedcentral.com/1471-2105/12/35  
http://stackoverflow.com/questions/12803390/venndiagram-internal-labels
