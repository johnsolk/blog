Title: iPlant - Intermediate workshop
Date: 2015-09-22 11:25
Author: monsterbashseq
Category: workshops
Slug: iplant-intermediate-workshop
Status: published

UCDavis, 9/22

http://dib-training.readthedocs.org/en/pub/2015-09-iplant.html  
https://pods.iplantcollaborative.org/wiki/display/Events/2015+09+21+iPlant+Workshops+at+UC+Davis  
https://etherpad.mozilla.org/iplant-ucdavis-sep2015

**[Harold Pimentel](https://pimentel.github.io/)**, PhD student in CS at
UC Berkeley

"Algorithms for RNAseq - from raw reads to differential expression
analysis"

[slides](https://pods.iplantcollaborative.org/wiki/download/attachments/21135454/2015_09_22%20Harold.pdf)

https://www.flickr.com/photos/lpcohen/21605321126/in/dateposted-public/

Not all reads are created equal! Number reads proportional to length of
transcript, normalize to correct for length bias

[![length\_norm](https://monsterbashseq.files.wordpress.com/2015/09/length_norm.png?w=300){.alignnone
.size-medium .wp-image-1224 width="300"
height="136"}](https://monsterbashseq.files.wordpress.com/2015/09/length_norm.png)

Very fast overview of RNAseq workflows. New RNAseq workflow faster.
Typically align reads (e.g. bowtie or splice-aware tophat). Genomic vs.
transcriptomic alignment? Genomic alignment is easier to visualize.
Tools are similar, similar results.

Pseudoalignment with [Kallisto](http://pachterlab.github.io/kallisto/).

**At the end of the day, what you care about is counting matches with
transcripts.** Can do analysis on laptop in &lt;10 min, similar accuracy
to existing methods.

[![tbg](https://monsterbashseq.files.wordpress.com/2015/09/tbg.png?w=300){.alignnone
.size-medium .wp-image-1225 width="300"
height="159"}](https://monsterbashseq.files.wordpress.com/2015/09/tbg.png)

Take *k-*mers of every single transcript, walk along path. Wherever they
differ, you create a new path. In dB graph, different splice sites
diverge along path of graph, sometimes they have same path but some
don't. Follow *k*-mers along graph, intersection of *k-*mers can give
upper bound on compatibility of prior kmers in path. First 3 *k*-mers
have exact same information, 2nd only have a few in common, same with
the next. Method always assumes

Performance speed &gt;500x faster than existing tools, comparable
accuracy.

Two schools of thought for RNAseq differential expression: transcript
abundance estimation vs. counts

[Issues with raw counts (Figure
1).](http://www.nature.com/nbt/journal/v31/n1/abs/nbt.2450.html) Counts
do not take into account length, not well posed: Isoform A (1000) vs.
Isoform B (500) vs. union of A and B (1500)

FPKM union &lt;= FPKM true

Sum of fractions vs. fractions of sums

How wrong is gene counting? Take a closer look at cuffdiff2 approach
([paper](http://www.nature.com/nbt/journal/v31/n1/abs/nbt.2450.html)).

Latent allocation problem. Maximum likelihood estimate number of reads
of one vs. num

[L. Pachter "Models for transcript quantification from RNA-Seq" arXiv,
2011](http://arxiv.org/abs/1104.3889). Review of models, all transcript
quantification methods boil down to inference algorithm. Then you have
abundance estimation output for sailfish, kallisto. For
example, proportionally assign A, fragment B which is compatible only
with red therefore unique mapping. Re-estimate maximum likelihood
estimate, iterate and prove likelihood and will be non-decreasing every
step every good as last step. Under some circumstances guaranteed local
maximum and under some global maximum.

Results are highly dependent on particular transcriptome, mapping step
parameters, and what is considered to be compatible. What if missing
annotation, get partial mapping with one complete mapping to another
isoform. Take this on case by case basis, not really a blanket statement
can be made about every scenario of analysis. A few papers have tried to
answer, but when you're missing 15-20% of transcriptome, depending on
what your'e missing ( what you're missing is probably not highly
expressed).

-   Simple *t*-test won't work because not normal distribution, negative
    binomial (NB2) (DESeq2, edgeR)
-   assume log(counts) = normal (sleuth, limma)

https://haroldpimentel.wordpress.com/2014/12/08/in-rna-seq-2-2-between-sample-normalization/

Between sample normalization, spike-ins are not to always be trusted
(from published studies). Naive vs. not-so naive normalization: TMM,
DESeq median count/geom. mean across samples.

Dealing with small sample sizes. Estimators have variance, this variance
is large in small samples, large variance on your variance! Prior
shrinking weights from weight towards some prior. eBayes estimator to
define what weights are going to be. Key principle. Increasing power by
pooling all information together. If only one estimate, not enough
information. Many estimates across many different genes, exploit this.

Multiple hypothesis testing problem. (Null true but rejected=type I
error) If we do this thousands of times, the number of false-positives
blows up, even if there isn't real discovery.

Sleuth has bootstrap, multinomial model to resample data and get new
transcript abundance estimates. Essentially, *in silico* technical
replicates. Take sample, bootstrap variance has high correlation. Assume
that noise is Poisson distributed, sometimes not true. Especially
transcript abundance estimated variance.

Try
[Snakemake](https://bitbucket.org/johanneskoester/snakemake/wiki/Home)
for creating reproducible workflows!

Conclusion:

1.  don't compare raw units without normalization
2.  every choice you make in a pipeline affects downstream
3.  RNAseq should be tool for guidance

(References on
[slides](https://pods.iplantcollaborative.org/wiki/download/attachments/21135454/2015_09_22%20Harold.pdf)
at end.)

Kallisto and sleuth walkthrough:
https://github.com/pimentel/bears\_iplant
