Title: R Classes: factor vs. character
Date: 2015-04-09 16:53
Author: monsterbashseq
Category: Bioinformatics, R
Slug: r-classes-factor-vs-character
Status: published

How to subset a data frame with only gene names in common with another
list? Turned out, problem was the class of one list was a 'factor' and
the other was a 'character'.

Solution:

` > qPCR<-read.csv("file1.csv") > Affy_DE_list<-read.csv("file2.csv") > class(qPCR) [1] "data.frame" > class(Affy_DE_list) [1] "data.frame" > colnames(qPCR)<-c("qPCR.ID","mRNA.Accession","Gene.Symbol","Gene.Name","Info") > a<-qPCR$mRNA.Accession > length(a) [1] 95 > class(a) [1] "factor" > a<-as.character(a) > head(a) [1] "NM_000042" "NM_198098" "NM_130851" "NM_000579" "NM_001773" "NM_000733" > b<-Affy_DE_list$mRNA.Accession > length(b) [1] 29158 > class(b) [1] "factor" > b<-as.character(b) > b<-gsub(" ", "",b) > head(b) [1] "NM_018476" "NM_003151" "NM_021800" "EU250749" "NM_001144757" "NM_003283" > x<-intersect(a,b) > length(x) [1] 55 > m<-qPCR$Gene.Symbol > length(m) [1] 95 > class(m) [1] "factor" > m<-gsub(" ", "",as.character(m)) > head(m) [1] "APOH" "AQP1" "BMP4" "CCR5" "CD34" "CD3E" > n<-Affy_DE_list$Gene.Symbol > length(n) [1] 29158 > class(n) [1] "factor" > n<-gsub(" ", "",as.character(n)) > head(n) [1] "BEX1" "STAT4" "DNAJC12" "LINC00862" "SCG5" "TNNT1" > y<-intersect(m,n) > length(y) [1] 86 > class(y) [1] "character" > source('~/Documents/scripts/overLapper.R') > setlist OLlist counts vennPlot(counts=counts) > ### This is the final way to subset a data frame by character list! > overlap_PCRlist <-filtered[gsub(" ", "",as.character(filtered$Gene.Symbol)) %in% y,] > dim(overlap_PCRlist) [1] 87 19`

Tried doing it the other way, making y a factor, and this did not work.

Made this venn diagram to show overlap between lists:

![venn](https://monsterbashseq.files.wordpress.com/2015/04/venn.png?w=300){.alignnone
.size-medium .wp-image-935 width="300" height="169"}
