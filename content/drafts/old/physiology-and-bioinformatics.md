Title: Physiology and Bioinformatics
Date: 2015-10-31 12:51
Author: monsterbashseq
Category: Bioinformatics, Grad School, physiology
Slug: physiology-and-bioinformatics
Status: published

Physiologists strive to understand how and why things work in living
tissues. I've been trying to think about physiology in the context of my
research interests in genomics and bioinformatics in nonmodel species.
We don't discuss this at all in my physiology courses, but I can't help
thinking about sequencing data that I work with and how I've seen these
gene names and pathways show up on functional annotations lists that
I've delivered to people. Are they accurate annotations? We all struggle
to understand the data. (Incidentally, this is one of the many reasons
why I chose a physiology grad program rather than a bioinformatics- or
genomics-focused grad program. I think it's really important and want to
understand the details of how and why living tissues work.)

These data are generated from preserved tissues, giving us a snapshot of
processes in time. To understand genomic and transcriptomic (and
proteomic and metabolomic) data, I think it is necessary to understand
the biochemical processes that are going on, being encoded for by these
data.

One of my favorite physiologists is [August
Krogh](http://www.nobelprize.org/nobel_prizes/medicine/laureates/1920/krogh-bio.html),
founder of comparative physiology. He defined the concept of an animal
model as one that enables us to study any question we want to ask:

![](http://www.nobelprize.org/nobel_prizes/medicine/laureates/1920/krogh.jpg){.alignleft}

> **"For such a large number of problems, there will be some animal of
> choice, or a few such animals, on which it can be most conveniently
> studied."**

In genomics, the concept of model organisms is slightly different. A
model organism is [one that is extensively
studied](https://en.wikipedia.org/wiki/Model_organism). In contrast,
nonmodel species are organisms with genomes that are not well
characterized. In this [new era of
biology](http://www.nature.com/ng/journal/v34/n4/full/ng0803-345.html),
utilizing [Krogh's
principle](https://en.wikipedia.org/wiki/Krogh%27s_principle), we can
apply what we know about some organisms in the context of evolutionary
relationship and conserved functions to others for which we know less to
bridge the gap between genotype and phenotype.

Why is this important? We are accumulating more and more genomic-scale
nucleic acid sequencing information from millions of species (nonmodel
species) for a variety of reasons, e.g. organismal health, environmental
health and management, species conservation. High-throughput automated
methods of data collection are at our disposal. It’s all really
exciting. Just looking at eukaryotes (prokaryotes an even larger
group!):

[![pie\_chart\_NCBI\_predicted\_species\_labeled](https://monsterbashseq.files.wordpress.com/2015/10/pie_chart_ncbi_predicted_species_labeled.png?w=265){.size-medium
.wp-image-1374 .alignleft width="265"
height="300"}](https://monsterbashseq.files.wordpress.com/2015/10/pie_chart_ncbi_predicted_species_labeled.png)

**There are an estimated 8.74 million eukaryotic species on Earth (outer
circle, data from [Mora et al.
2011](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001127)),
of which 316,235 species are currently represented in the** [**NCBI
nucleotide
database**](http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=statistics&uncultured=hide&unspecified=hide)
**(inner circle, data accessed May 23, 2015). The majority, 88% (7.7
million) is predicted to be metazoan, of which we have nucleic acid
sequences for approximately 2%. Data accessed from NCBI are numbers of
species regardless of number of nucleotide records present. There are
currently**
[**150,279,335**](http://www.ncbi.nlm.nih.gov/nuccore/?term=txid2759%5BOrganism:exp%5D)
**eukaryotic nucleotide records in NCBI (May 23, 2015).**

The majority of metazoans will likely be insects.

Wilson EO. 1987. [The Little Things That Run the World (The Importance
and Conservation of
Invertebrates)](http://www.esf.edu/efb/gibbs/efb413/little_things.pdf).
*Conservation Biology*. 1(4): 344-346.

The problem is, sequences are just code. Once we obtain all this code,
what does it mean? Annotations have to be assigned.

Most of what we know about molecular mechanisms of cellular processes is
based on experimental evidence. How can we reliably connect experimental
evidence with sequence annotations in an automated high-throughput way
for data from nonmodel organisms? Mouse and human systems are relatively
well-studied on an experimental level. But for new organisms whose
physiology we know relatively little about, how reliable is it to
annotate a new genome with protein function data from distantly-related
species? There are often small changes in protein's primary structure
from one species to another. For example, connexins (below):

![2015-10-31\_05-58-32\_22666604631\_o](https://monsterbashseq.files.wordpress.com/2015/11/2015-10-31_05-58-32_22666604631_o.jpg?w=148){.size-medium
.wp-image-1381 .alignleft width="148" height="300"}How distant is too
distant? Even if there is complimentary proteomic data to the nucleic
acid data from the same species, [it will not always match
up](http://www.sciencedirect.com/science/article/pii/S0968000414002023).
When is it acceptable to use experimental evidence from
distantly-related species to predict function at another species level?

**I want to understand more about the evolutionary relationships
among all of the protein and nucleic acid sequencing** **data.**

I need to understand more about position scoring matrices to identify
sensitive protein homologies between data sets. Hidden Markov
model-based software [HMMER](http://hmmer.janelia.org/) (Eddy 2011) and
existing hand-curated protein databases such as
[PROSITE](http://prosite.expasy.org/) (Sigrist et al. 2012), Pfam A and
B (Finn et al. 2014) and
[ProDom](http://prodom.prabi.fr/prodom/current/html/home.php) (Servant
et al. 2002). Also,
[phastCons](http://genome.ucsc.edu/goldenPath/help/phastCons.html):

Siepel A and Haussler D (2005). [Phylogenetic hidden Markov
models](http://compgen.cshl.edu/~acs/phylohmm.pdf). In R. Nielsen, ed.,
*Statistical Methods in Molecular Evolution*, pp. 325-351, Springer, New
York.

Siepel, A., Bejerano, G., Pedersen, J.S., Hinrichs, A., Hou, M.,
Rosenbloom, K., Clawson, H., Spieth, J., Hillier, L.W., Richards, S.,
Weinstock, G.M., Wilson, R. K., Gibbs, R.A., Kent, W.J., Miller, W., and
Haussler, D. [Evolutionarily conserved elements in vertebrate, insect,
worm, and yeast
genomes](http://www.genome.org/cgi/doi/10.1101/gr.3715005). *Genome
Res.* **15**, 1034-1050 (2005).

And then of course understand more about proteins themselves. For
nonmodel species annotations, there seems to be a disconnect between:
1.) experimental evidence for molecular structures and functions and 2.)
the sequences that encode for these.

With the extreme contrast between my research interests in
bioinformatics and my physiology core courses at UC Davis, I've found it
necessary to remind myself of why I'm motivated to study the fundamental
basics of physiology.
