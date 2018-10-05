Title: How many transcripts?
Date: 2015-02-20 17:30
Author: monsterbashseq
Category: Bioinformatics
Slug: how-many-transcripts-do-organisms-have
Status: published

How many transcripts are there in common model species reference
annotation files?

`[17:21] cohenl06@phoenix1 ~ $ cut -f9 /local/data/iGenomes/Mus_musculus/UCSC/mm9/Annotation/Genes/genes.gtf | cut -d ";" -f1 | sort | uniq | wc -l 23366 [17:21] cohenl06@phoenix1 ~ $ cut -f9 /local/data/iGenomes/Homo_sapiens/UCSC/hg19/Annotation/Genes/genes.gtf | cut -d ";" -f1 | sort | uniq | wc -l 23368 [17:22] cohenl06@phoenix1 ~ $ cut -f9 /local/data/iGenomes/Drosophila_melanogaster/UCSC/dm3/Annotation/Genes/genes.gtf | cut -d ";" -f1 | sort | uniq | wc -l 15340 [17:22] cohenl06@phoenix1 ~ $ cut -f9 /local/data/iGenomes/Caenorhabditis_elegans/UCSC/ce10/Annotation/Genes/genes.gtf | cut -d ";" -f1 | sort | uniq | wc -l 40076 [17:22] cohenl06@phoenix1 ~ $ cut -f9 /ifs/home/cohenl06/data/reference/sacCer3_annot.gtf | cut -d ";" -f1 | sort | uniq | wc -l 6692 [17:22] cohenl06@phoenix1 ~ $ cut -f9 /local/data/iGenomes/Arabidopsis_thaliana/NCBI/TAIR10/Annotation/Genes/genes.gtf | cut -d ";" -f1 | sort | uniq | wc -l 26995`
