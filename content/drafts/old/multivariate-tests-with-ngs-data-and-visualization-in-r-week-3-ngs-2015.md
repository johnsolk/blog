Title: Multivariate Tests with NGS Data and Visualization in R - Week 3 NGS 2015
Date: 2015-08-25 12:08
Author: monsterbashseq
Category: Genomics Workshop
Slug: multivariate-tests-with-ngs-data-and-visualization-in-r-week-3-ngs-2015
Status: published

[Dr. Ryan Williams](http://ryanjw.github.io/), postdoc at Iowa State
leads tutorial on R visualizations with multivariate statistical
approaches for RNAseq data. Traditionally, multivariate stats approaches
used for community ecology.

https://www.flickr.com/photos/lpcohen/20881761561/

Following are my patchy notes from the tutorial. Please feel free to
comment and correct!

The tutorial, part 1:

https://github.com/ngs-docs/angus/blob/2015/week3/visualizations/multivariate-tests/tests.md

Using [RStudio](https://www.rstudio.com/), load dataset from URL.

> <div id="magicdomid67" class="ace-line">
>
> [\# Possible solution for ubuntu RCurl]{.author-g-bknu96h89iod9lno}
>
> </div>
>
> <div id="magicdomid79" class="ace-line">
>
> [\# In the terminal:]{.author-g-bknu96h89iod9lno}
>
> </div>
>
> <div id="magicdomid81" class="ace-line">
>
>     sudo apt-get install libcurl4-openssl-dev
>
> </div>

Head of data, transcript ID from htseq-count:

[![head\_fly\_htseq\_data](https://monsterbashseq.files.wordpress.com/2015/08/head_fly_htseq_data.png?w=660){.alignnone
.size-large .wp-image-1010 width="660"
height="232"}](https://monsterbashseq.files.wordpress.com/2015/08/head_fly_htseq_data.png)

> A major assumption of MANOVA is that variables within each treatment
> level come from a multivariate normal distribution.

What's the difference between a multivariate normal distribution and
just a normal distribution? [Generalization of one-dimensional
(univariate) normal distribution to higher
dimensions.](https://en.wikipedia.org/wiki/Multivariate_normal_distribution) Setup
linear model first for univariate data, then set nested functions
together.

https://stat.ethz.ch/R-manual/R-devel/library/stats/html/summary.manova.html

Look at dataset transcript counts. Lots of zeros. If we ran the model,
it might crash and give errors because of all these zeros. Let's look at
one transcript.

    # just insert one of the transcripts,
    # color by fly type "fly"
    # set alpha to 0.5
    ggplot(dataset)+geom_density(aes(x=FBgn0000022,fill=fly,alpha=0.5))

[![single\_transcript\_densityplot\_histogram\_smoothed\_by\_fly](https://monsterbashseq.files.wordpress.com/2015/08/single_transcript_densityplot_histogram_smoothed_by_fly1.png?w=660){.alignnone
.size-large .wp-image-1007 width="660"
height="474"}](https://monsterbashseq.files.wordpress.com/2015/08/single_transcript_densityplot_histogram_smoothed_by_fly1.png)

Data are not normally distributed. Y axis is proportion of data. The
above graphic looks different with the same data if you look at it with
histogram function:

    ggplot(dataset)+geom_histogram(aes(x=FBgn0000022,fill=fly,alpha=0.5))

[![histogram](https://monsterbashseq.files.wordpress.com/2015/08/histogram.png){.alignnone
.size-full .wp-image-1008 width="618"
height="509"}](https://monsterbashseq.files.wordpress.com/2015/08/histogram.png)

Bins of counts for this particular transcript. Change to another
transcript:

    ggplot(dataset)+geom_histogram(aes(x=FBgn0000056,fill=fly,alpha=0.5),binwidth=100)

[![different\_transcript](https://monsterbashseq.files.wordpress.com/2015/08/different_transcript.png?w=660){.alignnone
.size-large .wp-image-1009 width="660"
height="504"}](https://monsterbashseq.files.wordpress.com/2015/08/different_transcript.png)

See info on ggplot graphics in References section below. First, add data
to ggplot function. Then add 'aes' layers. The 'aes' means *aesthetic*
which adds features to the graphic.

Run a MANOVA demonstrating [Wilk's
lambda](https://en.wikipedia.org/wiki/Wilks%27s_lambda_distribution) test,
multivariate generalization of F-distribution.

Permanova, permutations of F stastistic.
[?adonis](http://127.0.0.1:26220/library/vegan/html/adonis.html) Think
of data like cloud, shuffles data around, gets p values, asks how often
data are close within distance of alpha.

Challenge:

    adonis(decostand(dataset[,-c(1:3)],method="pa")~dataset$fly*dataset$type,method="jaccard")

Tutorial, part 2:

https://github.com/ngs-docs/angus/blob/2015/week3/visualizations/multivariate-viz/visualizations.md

Samples are unlabeled, can we figure out what groups they belong to
based on similarity?

Difference between MDS and PCA: With your cloud of data, rotate on axis
- orthogonal axis 2nd, look at 3rd, 4th, 5th, etc. PCA looks at all
coordinates possible. MDS collapses to smaller, user-defined dimensions,
e.g. k=3 or k=2. Can play with this to see how stress statistical values
can be minimized.

Here is MDS:

    ggplot(sc)+geom_point(aes(x=NMDS1,y=NMDS2,colour=info,shape=type),size=3)

[![mds](https://monsterbashseq.files.wordpress.com/2015/08/mds1.png?w=660){.alignnone
.size-large .wp-image-1012 width="660"
height="433"}](https://monsterbashseq.files.wordpress.com/2015/08/mds1.png)  
Here is PCA:

    pca<-capscale(dataset[,-c(1:4)]~1)
    pca
    eigs<-eigenvals(pca)
    eigs/sum(eigs)
    eigenvals(pca)
    sum(eigs)
    sc<-data.frame(scores(pca)$sites,dataset[,1:4])
    ggplot(sc)+geom_point(aes(x=MDS1,y=MDS2,colour=info,shape=type))+labs(x="PC1 (75.9% of variation explained)",y="PC2 (5.8% of variation explained)")

[  
![PCA](https://monsterbashseq.files.wordpress.com/2015/08/pca.png?w=660){.alignnone
.size-large .wp-image-1014 width="660"
height="433"}](https://monsterbashseq.files.wordpress.com/2015/08/pca.png)

This is how you get the first 2 eigenvalues for PC1 and PC2:

[![values\_PC1\_PC2](https://monsterbashseq.files.wordpress.com/2015/08/values_pc1_pc2.png){.alignnone
.size-full .wp-image-1013 width="308"
height="109"}](https://monsterbashseq.files.wordpress.com/2015/08/values_pc1_pc2.png)

PCoA:

    pcoa<-capscale(decostand(dataset[,-c(1:4)],"total")~dataset$fly,distance="bray")
    scores(pcoa)$centroids
    ggplot(sc)+geom_point(aes(x=MDS1,y=MDS2,colour=info,shape=type))+labs(x="MDS1 (33.0% of variation explained)",y="MDS1 (8.2% of variation explained)")+annotate("text",x=c(-.157,-.077,.17),y=c(-.004,.670,.156),label=c("HYB","ORE","SAM"))

Hardcoded coordinates of text of group names from pcoa\$centroids:

[![centroids](https://monsterbashseq.files.wordpress.com/2015/08/centroids.png?w=660){.alignnone
.size-large .wp-image-1016 width="660"
height="176"}](https://monsterbashseq.files.wordpress.com/2015/08/centroids.png)

[![PCoA](https://monsterbashseq.files.wordpress.com/2015/08/pcoa.png?w=660){.alignnone
.size-large .wp-image-1015 width="660"
height="433"}](https://monsterbashseq.files.wordpress.com/2015/08/pcoa.png)

Discussion:

*What parts of data are responsible for underlying differences?* How to
see how screwed up data are? If we only look at certain genes in NGS
data example, how does that change variation? Can use this data? Which
treatments interested in? Pairing tests appropriately with
visualizations. Adonis package can rank based on 'simper' within adonis
or 'anosim' or 'envfit' package to give explanatory components to see
what is contributing to your PCA. Try 'taxdist' or 'unifrac', to look at
taxonomic distances to add in weighting variables. See what happens when
you chop off, reduce. Same pattern? Now we have these clusters. Can we
figure out why our data is noisy, useless or useful?

**References**

[Grammar of
graphics](http://vita.had.co.nz/papers/layered-grammar.pdf) by author of
ggplot

[R cookbook with
examples](http://www.r-bloggers.com/r-cookbook-with-examples/)

[Stephen Turner's (UVA) advanced
visualization](http://bioconnector.org/workshops/lessons/r/r-viz/)

https://en.wikipedia.org/wiki/Jaccard\_index
