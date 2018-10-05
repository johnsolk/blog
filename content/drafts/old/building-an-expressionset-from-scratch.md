Title: Building An ExpressionSet From Scratch
Date: 2013-10-16 12:57
Author: monsterbashseq
Category: Bioconductor, Microarray, R
Slug: building-an-expressionset-from-scratch
Status: published

http://www.bioconductor.org/packages/2.13/bioc/vignettes/Biobase/inst/doc/ExpressionSetIntroduction.pdf

http://www.bioconductor.org/help/course-materials/2006/biocintro\_oct/labs/ExpressionSet/ExpressionSetIntro-lab.pdf

1.Make sure raw microarray data are in a matrix of the appropriate
dimensions.

    > class(sponge_data) 
    [1] "data.frame"
    > matrix_sponge_data<-as.matrix(sponge_data)
    > class(matrix_sponge_data)
    [1] "matrix"
    > dim(matrix_sponge_data)
    [1] 15744    77
    > colnames(matrix_sponge_data)
     [1] "initial_blockdata.RefNumber" "initial_blockdata.ID"       
     [3] "initial_blockdata.Name"      "initial_blockdata.Row"      
     [5] "initial_blockdata.Column"    "Block 1 Chip 1"             
     [7] "Block 2 Chip 1"              "Block 3 Chip 1"             
     [9] "Block 4 Chip 1"              "Block 5 Chip 1"             
    [11] "Block 6 Chip 1"              "Block 7 Chip 1"             
    [13] "Block 8 Chip 1"              "Block 1 Chip 2"             
    [15] "Block 2 Chip 2"              "Block 3 Chip 2"             
    [17] "Block 4 Chip 2"              "Block 5 Chip 2"             
    [19] "Block 6 Chip 2"              "Block 7 Chip 2"             
    [21] "Block 8 Chip 2"              "Block 1 Chip 3"             
    [23] "Block 2 Chip 3"              "Block 3 Chip 3"             
    [25] "Block 4 Chip 3"              "Block 5 Chip 3"             
    [27] "Block 6 Chip 3"              "Block 7 Chip 3"             
    [29] "Block 8 Chip 3"              "Block 1 Chip 4"             
    [31] "Block 2 Chip 4"              "Block 3 Chip 4"             
    [33] "Block 4 Chip 4"              "Block 5 Chip 4"             
    [35] "Block 6 Chip 4"              "Block 7 Chip 4"             
    [37] "Block 8 Chip 4"              "Block 1 Chip 5"             
    [39] "Block 2 Chip 5"              "Block 3 Chip 5"             
    [41] "Block 4 Chip 5"              "Block 5 Chip 5"             
    [43] "Block 6 Chip 5"              "Block 7 Chip 5"             
    [45] "Block 8 Chip 5"              "Block 1 Chip 6"             
    [47] "Block 2 Chip 6"              "Block 3 Chip 6"             
    [49] "Block 4 Chip 6"              "Block 5 Chip 6"             
    [51] "Block 6 Chip 6"              "Block 7 Chip 6"             
    [53] "Block 8 Chip 6"              "Block 1 Chip 7"             
    [55] "Block 2 Chip 7"              "Block 3 Chip 7"             
    [57] "Block 4 Chip 7"              "Block 5 Chip 7"             
    [59] "Block 6 Chip 7"              "Block 7 Chip 7"             
    [61] "Block 8 Chip 7"              "Block 1 Chip 8"             
    [63] "Block 2 Chip 8"              "Block 3 Chip 8"             
    [65] "Block 4 Chip 8"              "Block 5 Chip 8"             
    [67] "Block 6 Chip 8"              "Block 7 Chip 8"             
    [69] "Block 8 Chip 8"              "Block 1 Chip 9"             
    [71] "Block 2 Chip 9"              "Block 3 Chip 9"             
    [73] "Block 4 Chip 9"              "Block 5 Chip 9"             
    [75] "Block 6 Chip 9"              "Block 7 Chip 9"             
    [77] "Block 8 Chip 9"

2\. Make a minimal ExpressionSet, just to check:

    > minimalSet<-ExpressionSet(assayData=matrix_sponge_data)
    > head(minimalSet)
    ExpressionSet (storageMode: lockedEnvironment)
    assayData: 1 features, 77 samples 
      element names: exprs 
    protocolData: none
    phenoData: none
    featureData: none
    experimentData: use 'experimentData(object)'
    Annotation:

3\. Load Phenotype Data, which summarizes the information about the
samples, experimental treatments, covariates, etc.

    > samples<-read.csv("targets_experiment_sample_info.csv",header=TRUE,check.names=FALSE)
    > head(samples)
      Chip Number                   File Name Hyb Date Tank Treatment Colony
    1           1 253295110067_2012-08-01.txt 8/1/2012   C3        UC      P
    2           1 253295110067_2012-08-01.txt 8/1/2012   B2        UD      P
    3           1 253295110067_2012-08-01.txt 8/1/2012   B2        UD      O
    4           1 253295110067_2012-08-01.txt 8/1/2012   D3        OD     BL
    5           1 253295110067_2012-08-01.txt 8/1/2012   D1        OD      O
    6           1 253295110067_2012-08-01.txt 8/1/2012   C3        UC      O
      Raceway Block
    1       B     1
    2       A     2
    3       A     3
    4       A     4
    5       B     5
    6       B     6
    > class(samples)
    [1] "data.frame"
    > samples_matrix<-as.matrix(samples)
    > all(rownames(samples_matrix)==colnames(matrix_sponge_data))
    [1] TRUE

4\. Load Annotation file:

    > annotation<-read.csv("FeatAnnotFile_SEE_10-18-12.csv",header=TRUE,check.name=FALSE)
    > class(annotation)
    [1] "data.frame"
    > annotation_matrix<-as.matrix(annotation)
    > class(annotation_matrix)
    [1] "matrix"
    > all(rownames(annotation_matrix)==rownames(matrix_sponge_data))
    [1] TRUE

5\. Experiment Description:

    > experimentData<-new("MIAME",name="Sara Edge, Lisa Cohen",
                                  lab="Marine Genomics, HBOI",
                                  contact="lcohen49@hboi.fau.edu",
                                  title="Sponge Oil Dispersant Exposure Experiment",
                                  abstract="ExpressionSet for Sponge Microarray Data",
                                  other=list(notes="Created from GenePix *.gal files"))

6\. Assemble ExpressionSet:

    > sponge_ExpressionSet<-new("ExpressionSet",exprs=sponge_data,phenoData=samples_matrix,experimentData=experimentData,annotation=annotation_matrix)
    Error: ExpressionSet 'phenoData' is class 'matrix' but should be or extend 'AnnotatedDataFrame'

But, I got the error in red above.
