Title: Reading Microarray Data
Date: 2013-10-10 16:52
Author: monsterbashseq
Category: Bioconductor, limma, R
Slug: reading-microarray-data
Status: published

Given an Agilent microarray, scanned intensity data converted with
GenePix to \*.gpr, I want to write automated R functions that will:  
1. read only F532-BG column in each .gpr file in a directory  
2. separate rows of data by block

    chip1<-readGAL("08.23.2012_253295110035.gpr",path=NULL,header=TRUE,sep="\t",quote="\"",skip=NULL,as.is=TRUE)
    > names(chip1)
     [1] "Block"                "Column"               "Row"                 
     [4] "Name"                 "ID"                   "X"                   
     [7] "Y"                    "Dia."                 "F532.Median"         
    [10] "F532.Mean"            "F532.SD"              "F532.CV"             
    [13] "B532"                 "B532.Median"          "B532.Mean"           
    [16] "B532.SD"              "B532.CV"              "X....B532.1SD"       
    [19] "X....B532.2SD"        "F532...Sat."          "F.Pixels"            
    [22] "B.Pixels"             "Circularity"          "F532.Median...B532"  
    [25] "F532.Mean...B532"     "F532.Total.Intensity" "SNR.532"             
    [28] "Flags"                "Normalize"            "Autoflag"            
    [31] "RefNumber"            "ControlType"          "GeneName"            
    [34] "TopHit"               "Description" 
    > good<-chip1$F532.Median...B532

References  
\[1\]
http://www.bioconductor.org/packages/2.12/bioc/vignettes/limma/inst/doc/usersguide.pdf
