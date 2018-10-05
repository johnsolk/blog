Title: Differential expression and dosage compensation in RNAseq - NGS2015
Date: 2015-08-27 15:47
Author: monsterbashseq
Category: Genomics Workshop
Slug: differential-expression-and-dosage-compensation-in-rnaseq-ngs2015
Status: published

[Dr. Chris Hamm, University of Kansas](http://butterflyology.net/), side
effects of sexual reproduction in Lepidoptera!

https://www.flickr.com/photos/lpcohen/20920007072/in/dateposted-public/

Explanation of ESA, species status dependent \# of self-sustaining
populations, Mitchell's satyr butterfly endangered. Suggests [Butterfly
People](http://www.amazon.com/Butterfly-People-American-Encounter-Beauty/dp/1400076927).

[K-means cluster](https://en.wikipedia.org/wiki/K-means_clustering)
plots, each vertical bar individual. Michigan different than other
populations.

Diversification of Lepidoptera, Mutanen et al. 2010:

https://www.flickr.com/photos/lpcohen/20307587874/

Evolution of sex chromosomes: female heterogamety, "chocoblock full of
transposable elements" Sex chromosomes present gene dosage problem, no
matter how many chromosomes you have, you still have the same gene
expression. Females mammals inactivate extra X chromosome. Drosophila
males double expression to deal with balance.

[**Tutorial**]{style="color:#000000;"}

https://angus.readthedocs.org/en/2015/\_static/SLDC-code.html  
https://github.com/ngs-docs/angus/blob/2015/week3/SLDC/SLDC-code.Rmd

**Simulated Data**

[![plot\_Code](https://monsterbashseq.files.wordpress.com/2015/08/plot_code.png?w=300){.alignnone
.size-medium .wp-image-1124 width="300"
height="190"}](https://monsterbashseq.files.wordpress.com/2015/08/ma.png)

[![MA](https://monsterbashseq.files.wordpress.com/2015/08/ma.png?w=300){.alignnone
.size-medium .wp-image-1123 width="300"
height="224"}](https://monsterbashseq.files.wordpress.com/2015/08/ma.png)

**Practice Data**

Bmori.dat &lt;- read.csv("Bmori-data.csv", header = TRUE)

[![4plots](https://monsterbashseq.files.wordpress.com/2015/08/4plots.png?w=300){.alignnone
.size-medium .wp-image-1126 width="300"
height="224"}](https://monsterbashseq.files.wordpress.com/2015/08/4plots.png)

**Plotting in R - Awesome Digression!**

Multiple plots on one space, add plots, text, arrows, whatever on top
with [base R](http://www.statmethods.net/advgraphs/layout.html).  
Reset with:

    par(mfrow=c(1,1))

[![RPKM](https://monsterbashseq.files.wordpress.com/2015/08/rpkm.png?w=300){.alignnone
.size-medium .wp-image-1127 width="300"
height="203"}](https://monsterbashseq.files.wordpress.com/2015/08/rpkm.png)

Looking at expression per chromosome:

[![expr](https://monsterbashseq.files.wordpress.com/2015/08/expr.png?w=300){.alignnone
.size-medium .wp-image-1130 width="300"
height="203"}](https://monsterbashseq.files.wordpress.com/2015/08/expr.png)

[![zchrom](https://monsterbashseq.files.wordpress.com/2015/08/zchrom.png?w=300){.alignnone
.size-medium .wp-image-1129 width="300"
height="203"}](https://monsterbashseq.files.wordpress.com/2015/08/zchrom.png)

**MA plots**

http://web.mit.edu/\~r/current/arch/i386\_linux26/lib/R/library/limma/html/plotma.html  
I posted a question on the Bioconductor listserv:

https://support.bioconductor.org/p/71562/  
http://nar.oxfordjournals.org/content/43/7/e47

limma::plotMA

[![weird\_MAplot](https://monsterbashseq.files.wordpress.com/2015/08/weird_maplot.png?w=300){.alignnone
.size-medium .wp-image-1125 width="300"
height="224"}](https://monsterbashseq.files.wordpress.com/2015/08/weird_maplot.png)

plot(log2(res1\_filtered\$baseMean), res1\_filtered\$log2FoldChange,
col=ifelse(res1\_filtered\$padj &lt; 0.25, "red","gray67"),main="In
vivo, ApoE vs. WT
(padj&lt;0.25)",xlim=c(1,20),ylim=c(-10,10),pch=20,cex=1)  
abline(h=c(-1 ,1), col="blue")

[![MAplot\_invivo\_DKOvWT\_June2015](https://monsterbashseq.files.wordpress.com/2015/08/maplot_invivo_dkovwt_june2015.png?w=300){.alignnone
.size-medium .wp-image-1128 width="300"
height="297"}](https://monsterbashseq.files.wordpress.com/2015/08/maplot_invivo_dkovwt_june2015.png)
