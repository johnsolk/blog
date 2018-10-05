Title: gene set enrichment analysis (GSEA)
Date: 2014-07-10 14:38
Author: monsterbashseq
Category: Bioinformatics, Data Analyses
Slug: gene-set-enrichment-analysis-gsea
Status: published

What is a gene set enrichment analysis? What is a reasonable enrichment
score? With the genes in common between the two groups from yesterday's
venn diagram, I want to see what functions they correspond to. There are
many ways to assign functions to genes. One way is with gene ontology
terms, which are standardized terms for the functions of genes. When
working with model species, e.g. mouse or fly or human, standardized
terms are fairly easy to acquire. I plugged them into
[DAVID](http://david.abcc.ncifcrf.gov/tools.jsp) bioinformatics database
and got some output, including this chart:

[![DAVID\_output](https://monsterbashseq.files.wordpress.com/2014/07/david_output.png?w=640){.alignnone
.size-large .wp-image-854 width="640"
height="448"}](https://monsterbashseq.files.wordpress.com/2014/07/david_output.png)

The highest enrichment scores with several pathways listed (signal
peptides, glycoproteins, respond to wounding, etc.) have an enrichment
scores around 5-6. Are these high scores or low?

What do enrichment scores mean?

According to this
[paper](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1239896/pdf/pnas-0506580102.pdf),
an enrichment score represents the degree to which a set of genes
is overrepresented at the top or bottom of the total list submitted. The
program ranks the genes somehow. I don't understand the ranking
process. The score is calculated by walking down the list. When a gene
in the set of interest is encountered, a running-sum statistic is
increased. If a gene not in the set is encountered, the running-sum
statistic is decreased. The running sum is based on
the [Kolmogorov–Smirnov test](http://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test).
The magnitude of the incremental increasing or decreasing depends on a
correlation of the gene with the phenotype. The enrichment score is the
maximum deviation from zero encountered during the random walk (see
figure 1B from the paper below).

[![GSEA\_score](https://monsterbashseq.files.wordpress.com/2014/07/gsea_score.png?w=640){.alignnone
.size-large .wp-image-857 width="640"
height="352"}](https://monsterbashseq.files.wordpress.com/2014/07/gsea_score.png)

Given that the list only had 87 genes, given that 39 of them have some
correlation with signaling peptides, it is probably safe to say that the
genes in common between these two treatment groups are involved with
cell signaling (intra or intercellular).
