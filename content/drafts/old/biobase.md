Title: Biobase
Date: 2013-10-16 12:39
Author: monsterbashseq
Category: Bioconductor, R
Slug: biobase
Status: published

    > source("http://bioconductor.org/biocLite.R")
    Bioconductor version 2.13 (BiocInstaller 1.12.0), ?biocLite for help

    > biocLite("Biobase")
    BioC_mirror: http://bioconductor.org
    Using Bioconductor version 2.13 (BiocInstaller 1.12.0), R version 3.0.2.
    Installing package(s) 'Biobase'
    trying URL 'http://bioconductor.org/packages/2.13/bioc/bin/windows/contrib/3.0/Biobase_2.22.0.zip'
    Content type 'application/zip' length 2335919 bytes (2.2 Mb)
    opened URL
    downloaded 2.2 Mb

    package ‘Biobase’ successfully unpacked and MD5 sums checked

    The downloaded binary packages are in
        C:\Documents and Settings\lcohen49\Local Settings\Temp\RtmpkLNtBy\downloaded_packages
    > library(Biobase)
    Loading required package: BiocGenerics
    Loading required package: parallel

    Attaching package: ‘BiocGenerics’

    The following objects are masked from ‘package:parallel’:

        clusterApply, clusterApplyLB, clusterCall, clusterEvalQ,
        clusterExport, clusterMap, parApply, parCapply, parLapply,
        parLapplyLB, parRapply, parSapply, parSapplyLB

    The following object is masked from ‘package:limma’:

        plotMA

    The following object is masked from ‘package:stats’:

        xtabs

    The following objects are masked from ‘package:base’:

        anyDuplicated, append, as.data.frame, as.vector, cbind, colnames,
        duplicated, eval, evalq, Filter, Find, get, intersect, is.unsorted,
        lapply, Map, mapply, match, mget, order, paste, pmax, pmax.int,
        pmin, pmin.int, Position, rank, rbind, Reduce, rep.int, rownames,
        sapply, setdiff, sort, table, tapply, union, unique, unlist

    Welcome to Bioconductor

        Vignettes contain introductory material; view with
        'browseVignettes()'. To cite Bioconductor, see
        'citation("Biobase")', and for packages 'citation("pkgname")'.
