Title: ExpressionSet success!!
Date: 2013-10-17 15:11
Author: monsterbashseq
Category: Bioconductor, Microarray, R
Slug: expressionset-success
Status: published

Behold, the ExpressionSet object:

    > sponge_ExpressionSet<-new("ExpressionSet",exprs=sponge_data,phenoData=pd,experimentData=experimentData,featureData=an)
    > sponge_ExpressionSet
    ExpressionSet (storageMode: lockedEnvironment)
    assayData: 15744 features, 72 samples 
      element names: exprs 
    protocolData: none
    phenoData
      sampleNames: 1_1 1_2 ... 9_8 (72 total)
      varLabels: Chip Number File Name ... Name (9 total)
      varMetadata: labelDescription
    featureData
      featureNames: 1 2 ... 15744 (15744 total)
      fvarLabels: Column Row ... X.1 (23 total)
      fvarMetadata: labelDescription
    experimentData: use 'experimentData(object)'
    Annotation:  
