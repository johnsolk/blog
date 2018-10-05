Title: Pathway Analysis for RNAseq Data - NGS2015
Date: 2015-08-26 16:19
Author: monsterbashseq
Category: Bioinformatics, Genomics Workshop
Slug: pathway-analysis-for-rnaseq-data-ngs2015
Status: published

Presentation by Dr. Asela Wijeratne, Ohio State University at [Molecular
and Celluar Imaging Center](http://oardc.osu.edu/mcic/). Research
interests in co-expression networks during pathogen attack in
agricultural plant species to identify regulatory genes.

Today: Different approaches for pathway analysis, statistical
approaches, example using GAGE, challenges for pathway analysis, gene
set enrichment analysis.

Pathways: metabolic (e.g. Krebs), gene regulatory, signal transduction,
etc.  
https://www.genome.gov/27530687

https://www.flickr.com/photos/lpcohen/20715535748/

Why do we do pathway analysis? What are activated, deactivated under
certain conditions, how mutations affect? Functional descriptions of
genes. Measure molecular responses somehow. Connect to statistical test,
network reconstruction. Set of functions.

How do we get functional annotations? Gene ontology terms grouped by
functional terms. GO, KEGG, BioCarta databases, transcription targets
(tools) Great for model organisms but not great for nonmodel. Each term
describes. Directed acyclic graph (DAG) du Plessis L et al. Brief
Bioinform. 2001 to construct database of terms that represent functions
for purposes and connectivity. Controlled by GO consortium with
vocabulary for these terms. Examples annotation is given with evidence.
Experimental evidence codes, computational analysis, author statement,
curator statement, automatically-assigned evidence codes inferred from
electronic annotation (be careful), obsolete evidence codes.

This is what I think is really interesting:

**Just because you have a functional annotation, doesn't mean it is
real!** Model systems have these annotations. **Newly assembled
transcriptomes and genomes have inferred annotations.** Problems: KEGG
pathways, not flexible to nonmodel species. User working with species
with metabolic pathways different than species already in databases
cannot re-draw. Evidence codes can be automatically-assigned.

For purposes of learning today, assume you are working with a model
system, e.g. human or mouse. Which categories are the most common in
databases you are using?

After RNAseq analysis, I have the gene list. Now what? Over or
under-represented GO terms? Discuss.

https://www.flickr.com/photos/lpcohen/20877471646/

Problem of small size. How to decide what is over- or under-represented?
For example, hypergeometric test: 100/500 genes involved in cell cycle.
25/500 involved in cell cycle. Is cell cycle enriched? Use r function
phyper(25,500,4500,100,lower.tail=FALSE) = 3.9e-06 Correct for multiple
hypothesis testing: probability of saying something is being
differentially expressed when it is not. Bonferroni (Google
'Bonferroni), more stringent and (FDR)
[Benjamini-Hochberg](http://www.jstor.org/stable/2346101?seq=1#page_scan_tab_contents)
method can be used, although FDR is less stringent. Rank list of GO
categories by P-values. Then adjust (multiply) by total number of
categories/rank to get FDR.

Functional Class Scoring (FCS) assumes coordinated changes in related
set of genes can have signifiant effect. No threshold. Analysis define
the "gene set" Enrichment is for an entire set. GSEA, for model
species. http://www.broadinstitute.org/gsea/index.jsp

We will use the [GAGE](http://www.biomedcentral.com/1471-2105/10/161)
package to see how it works.

http://www.bioconductor.org/packages/release/bioc/vignettes/gage/inst/doc/gage.pdf

Flexible, generally applicable to nonmodel species. Separate gene sets
into two categories, two different entities. For example, curated gene
set and pathway information, e.g. KEGG and combine. Can use for
microarray and RNAseq. 1-on-1 comparison, e.g. Control 1 to Exp 1,
Control 1 to Exp 2, etc. Summarize and meta-test, correct for FDR. Fold
change for each comparison and get global mean, also get global mean for
entire set. Limitations of FCS: treats pathways independently, etc.

Pathway Topology (PT) based approaches: provides additional information
such as gene interactions, how they interact, location of the
interaction.

Example tools, packages used in R: SPIA, NetGSA, ScorePAGE

Discuss challenges: hard to compare different methods. Lacking benchmark
datasets to put in all packages to see how they do. Inability to model
dynamic responses, e.g. time-series. Inability to model effects of
external stimuli. Main challenge, however is incomplete knowledge base
for annotations. Often no annotations for all transcripts. Or inaccurate
annotations. More GO annotations are inferred electronic annotations.
Missing conditions, cell-specific information. Divergence in genes,
still associated with pathway. Not known whether still performs same
function. Khatri et al. 2012 paper, 10 years of challenges:

http://www.ploscompbiol.org/article/fetchObject.action?uri=info:doi/10.1371/journal.pcbi.1002375&representation=PDF

**Tutorial**

Install packages, see notes on Etherpad:

https://etherpad.mozilla.org/ngs2015-week3

    library(limma)
    library('edgeR')
    library('DESeq2')
    library('Biobase')
    library(gplots)
    library('pathview')
    library('gage')

Here are Asela's tutorial instructions:  
https://github.com/ajwije/150826\_pathway\_analysis  
https://github.com/ajwije/150826\_pathway\_analysis/blob/master/Tutorial\_150827.Rmd

From commandline:

    mkdir pathway_analysis
    cd pathway_analysis/
    git clone https://github.com/ajwije/150826_pathway_analysis.git
    150826_pathway_analysis/

In RSTudio, set working directory, download dataset and import from
current directory:

    setwd("~/Documents/ngs2015/pathway_analysis/150826_pathway_analysis")
    rnaseq_URL <- "https://github.com/vsbuffalo/rna-seq-example/raw/master/results/raw-counts.txt"
    download.file(rnaseq_URL, destfile = "rnaseq_data.txt")
    rnaseq_data 

[![rnaseq\_data](https://monsterbashseq.files.wordpress.com/2015/08/rnaseq_data.png?w=300){.alignnone
.size-medium .wp-image-1068 width="300"
height="116"}](https://monsterbashseq.files.wordpress.com/2015/08/rnaseq_data.png)

Find short code for oraganism. Here it is:

    korg[species, 1, drop = F]

If you need to find code for another organism, go here:

http://rest.kegg.jp/list/organism

If your organism is not on the list of &gt;3,000 species, do KEGG
ortholog mapping. (instructions to follow)

Gene identifiers from kegg:

[![kegg\_pathways\_genes](https://monsterbashseq.files.wordpress.com/2015/08/kegg_pathways_genes.png?w=300){.alignnone
.size-medium .wp-image-1069 width="300"
height="181"}](https://monsterbashseq.files.wordpress.com/2015/08/kegg_pathways_genes.png)

There are two ways to use GAGE:  
1. Native: normalization/variance stabilization &gt;&gt; GAGE  
2. Combine: EdgeR &gt;&gt; GAGE

We will do "Native".

1\. Remove zero counts:

[![removing\_zero\_counts](https://monsterbashseq.files.wordpress.com/2015/08/removing_zero_counts.png?w=300){.alignnone
.size-medium .wp-image-1070 width="300"
height="123"}](https://monsterbashseq.files.wordpress.com/2015/08/removing_zero_counts.png)

2\. Normalization library counts

[![norm\_counts](https://monsterbashseq.files.wordpress.com/2015/08/norm_counts.png?w=300){.alignnone
.size-medium .wp-image-1071 width="300"
height="70"}](https://monsterbashseq.files.wordpress.com/2015/08/norm_counts.png)

3\. Variance stabilization transformation, 8 is added from KEGG manual,
to avoid -inf during log

plot MDS and MA plot to see processed data variances. Here is MDS plot,
MA plot would not work for me.

    limma::plotMDS(norm_counts)

[![variance\_Stabilize](https://monsterbashseq.files.wordpress.com/2015/08/variance_stabilize.png?w=300){.alignnone
.size-medium .wp-image-1072 width="300"
height="57"}](https://monsterbashseq.files.wordpress.com/2015/08/variance_stabilize.png)

4\. Define reference and experiment samples  
5. Enrichment analysis  
6. Some outputs,

[![outputs](https://monsterbashseq.files.wordpress.com/2015/08/outputs.png?w=300){.alignnone
.size-medium .wp-image-1073 width="300"
height="102"}](https://monsterbashseq.files.wordpress.com/2015/08/outputs.png)

Quickly went through edgeR to combine with GAGE:

1\. Make the study design  
2. Create DGElist object  
3. Remove lowly expressed genes  
4. Normalize the data  
5. multidimentional scaling plot  
6. Estimate the dispersion  
7. Differential gene expression  
8. Making the data suitable for pathway analysis  
9. GAGE analysis

Overrepresentation analysis with GAGE should include all normalized
genes, not just the differentially expressed ones. GAGE determines
pathways that are significant. Individual genes that are differentially
expressed come from the edgeR (or DESeq2, limma, etc. packages)

Visualization is Key:

From last command in tutorial, here are genes differentially expressed
in DNA replication pathway. The pathway was determined by GAGE. There
are 2 genes differentially expressed (identified by edgeR) in this
pathway. This gives biological meaning to the differential gene
expression analysis. Not only were the genes differentially expressed,
but this pathway was significantly enriched.

[![ath03030.DNA\_replication](https://monsterbashseq.files.wordpress.com/2015/08/ath03030-dna_replication.png?w=288){.alignnone
.size-medium .wp-image-1074 width="288"
height="300"}](https://monsterbashseq.files.wordpress.com/2015/08/ath03030-dna_replication.png)
