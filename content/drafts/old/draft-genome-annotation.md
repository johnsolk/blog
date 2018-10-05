Title: Draft Genome Annotation
Date: 2015-03-14 15:49
Author: monsterbashseq
Category: Bioinformatics
Slug: draft-genome-annotation
Status: published

Annotating a draft *de novo* genome assembly of a
previously-uncharacterized species with gene function information is a
challenging problem. Having the genome sequence is not
biologically-important until you know what the sequence does, in terms
of what proteins are expressed/translated.
Genome-&gt;transcriptome-&gt;protein sequence information is collected
experimentally and must be integrated. Some pipelines include using
annotated genomes and transcriptomes, proteomes from closely-related
species. There is not one clear set of methods, and multiple pipeline
tools are available. A question is, which is the best to use? Right now,
we should try multiple methods and see which combination of results make
the most sense.

http://www.nature.com/nrg/journal/v13/n5/full/nrg3174.html

1\. CEGMA (Core Eukaryotic Genes Mapping Approach), which takes a set of
458 proteins found to be highly conserved among Eukaryotes.  
http://korflab.ucdavis.edu/datasets/cegma/

2\. EuGene, a software with gene prediction modeling that promises
integration with RNAseq or EST data, not straightfoward to learn how to
use. Parameters are not easy to follow and require integration with
plugins.

http://eugene.toulouse.inra.fr/  
https://mulcyber.toulouse.inra.fr/docman/view.php/10/1567/EuGeneDoc.pdf

3\. The PASA pipeline is another method to try:  
https://github.com/PASApipeline/PASApipeline/blob/master/docs/index.asciidoc\#A\_RNASeq  
http://wfleabase.org/release1/PASA\_gene\_annotation.html  
http://rice.plantbiology.msu.edu/training/Haas\_PASA2.pdf

4\. MAKER:  
http://www.yandell-lab.org/software/maker.html
