Title: Error in validObject(.Object)
Date: 2013-10-17 13:25
Author: monsterbashseq
Category: Bioconductor, Microarray, R
Slug: error-in-validobject-object
Status: published

Biobase's  "ExpressionSet" package:

    sponge_ExpressionSet<-new("ExpressionSet",exprs=sponge_data,phenoData=pd,experimentData=experimentData,featureData=an)
    Error in validObject(.Object) : 
      invalid class “ExpressionSet” object: 1: featureNames differ between assayData and featureData
    invalid class “ExpressionSet” object: 2: sampleNames differ between assayData and phenoData

It is looking for the same data in all sets to match. I need to figure
out how it wants featureNames and sampleNames to be specified, row
headers? a column of data?

http://stackoverflow.com/questions/7363991/expressionset-phenodata

http://grokbase.com/t/r/bioconductor/12c6e2j6ba/bioc-oligo-package

http://www.hsph.harvard.edu/carey/lect3dstr.pdf
