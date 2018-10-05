Title: Beginnings of Metagenomics and the emerging tree of life - Dr. Norman Pace
Date: 2015-10-06 16:34
Author: monsterbashseq
Category: talks
Slug: beginnings-of-metagenomics-and-the-emerging-tree-of-life-dr-norman-pace
Status: published

https://www.flickr.com/photos/lpcohen/21817022598/in/dateposted-public/

\*\*\*Update, [Twitter
storify](https://storify.com/phylogenomics/norm-pace-talk-at-ucdavis)

I had the privilege today of attending a talk by [Dr. Norman
Pace](http://pacelab.colorado.edu/index.html) from UC-Boulder, who was
the first to investigate the structure/function of rRNA molecules in the
context of deep phylogeny. This opened the view of culture-independent
microbial studies.

Some notes:

UC Davis - Genome Center, 10/6/2015

http://microbe.net/2015/09/30/special-seminar-at-ucdavis-dr-norman-pace-on-metagenomics-and-the-tree-of-life/

[Dr. Jonathan Eisen](https://phylogenomics.wordpress.com/): transformed
his life, learned from Jennifer Doudna's course and per Colleen
Cavanaugh's instructions to read paper by Norman Pace.

*"Beginnings of Metagenomics and the emerging tree of life."*

[**Outline:**]{style="text-decoration:underline;"}  
**- historical context**  
**- emergence of modern microbial ecology, "metagenomics"**  
**- expansion of microbial diversity and the state of the big tree**  
**- alternatives of the Woese three-branched tree of life (correct?)**

Biology is not as simple as just saying prokaryotes and eukaryotes.

"Groping towards an objective describing of life's diversity": molecular
phylogeny  
(devil is in details)

1.  **align sequences** carefully so that orthologous residues are
    juxtaposed, common ancestry and function
2.  **count differences** between pairs of sequences = measureo f
    evolutionary distance that separates organisms
3.  **calculate map of relationships** = "tree" that most accurately
    fits all pairwise differences

Carl Woese studying data, early 1980s, 3 domain trees,  
Accumulated hand-curated oligonucleotide catalogues of 6mers and then
larger as homologues and orthologues. Published as table of "Association
coefficients (SAB)"

Broad general advice: *"Do what you can do to make your results
interpretable for a larger audience!"* Will drive home importance of
your work.

Archaebacteria, Eubacteria, Eukaryotes, Woese 1987

[Woese et al. 1990 Evolution PNAS Vol.
87](http://www.pnas.org/content/87/12/4576.full.pdf)

Some genes that are homologues underwent duplications before a common
ancestor.

Paralogs you can still recognize include: elongation factors EF-G and
EF-Tu, membrane ATP synthase subunits, tRNA

"blast hit doesn't mean much" the more unrelated you get

rooting the big tree, You are here: tree of life has three main
relatedness groups  
- origin in on the bacterial line of descent  
- chrloroplasts and mitochondria are bacterial origin  
- don't need to culture to identify

https://www.flickr.com/photos/lpcohen/21383719883/in/dateposted-public/

In 2001, term "metagenomics" was coined. Allows us to ask, *"What kinds
of organisms are there?"* and *"what kinds of genes are
there?"*. Requires reflection on sequence databases, then arrive at
community structure and functional results. At the end, can ask "What
kinds of genes does this community have?"

In the 80s, only had mixed natural samples and catalogue so had to
figure out how to characterize.

["Analysis of hydrothermal vent-associated symbionts by ribosomal RNA
sequences."](http://www.ncbi.nlm.nih.gov/pubmed/17741220)Science 224:
209 Stahl et al. 1984

["Characterization of a Yellowstone Hot Spring Microbial Community by 5S
rRNA sequences."](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC241732/)
Stahl et al. 1980s

Need a database, universal primers synthesized in house by hand (still
used!)

["Rapid determination of 16S ribosomal RNA sequences for phylogenotic
analyses."](http://www.pnas.org/content/82/20/6955.short) Lane et al.
1985

["Phylogenetic Stains: Ribosomal RNA-Based probes for the identification
of single cells."](http://www.ncbi.nlm.nih.gov/pubmed/2466341)Science
243: 1360-1989

sample-&gt;DNA-&gt;rDNA PCR library-&gt;clone-&gt;sequence (now NGS)

Pace studied a spectrum of environments, saturated brine
(cryptoendoliths), mines, open ocean, aerosols in NYC subway, soapscum

Worldwide, trend through time of cumulative number of sequences
&gt;700,000 environmental (in 2007), small percentage of cultured!

Expansion of bacterial tree, \~100 phyla, 30 cultured

Strains of pangenome of one species of bacteria, \~30% overlap

In the face of all the genomic variation, what does an environmental
rNRA sequence tell you?

Principle: representatives of a phylogenetic group are expected to have
properties common to the group

To validate, multiple environments, specific harvest, abundance is
validation of significance to the ecosystem

Concatenated gene sets for phylogeny == not a good idea, be careful. Can
use this, as with any method, as guideline for further analysis. (Later:
Has no problem with concatenated trees, as long as you're not too deep
in tree.)

Problems in resolving deep-branchig topology: representation,
uncertainty

Representation in databases: mostly pathogens, fecal, not much else
available to understand deep phylogeny

Pipelines, short reads - too short

Calculate amount of change, uncertainty deep in tree, inferred sequence
change vs. observed sequence change - apply metric Knuc =
-3/4ln(1-(4/3)D)

Alternatives to Woese 3D tree? Don't think so.

Eocyte hypothesis is stronger if you string genes together

While rRNA is highly conserved, some people argue that it's only 1500
charaters long so better to look at conservation and expand length of
sequences looking at. But, these are poorly aligned.

Different pictures of three-domain model emerged, e.g. eocyte

"Complex archaea that bridge the gap between prokaryotes and
eukaryotes." tree from concatenation of 29 genes

Big problems with concatenated protein genes: deep in the tree:  
- alignments (identification of orthologies)  
- unseen change (very big deal with long branches)  
- lateral transfer (e.g. 11/53 archaea proteins show evidence of lateral
transfer)  
- "heterotachy" (variable rates of change among sequences used in
analysis - a statistical killer)  
- did the LUCA (last universal common ancestor) state have stably
contiguous genomes?

Kubatko and Degnan. 2007. ["Inconsistency of phylogenetic estimates from
concatenated data under
coalescence."](http://www.ncbi.nlm.nih.gov/pubmed/17366134)

Beyond algorithms, look at properties of cells:

-   many properties of eukaryotes and archaea distinguish these lines
    from bacteria
-   Two properties are key: membrane chemistry and backbone
    stereochemistry are different: ether vs. ester lipids, opposite
    backbone stereoisomerism
-   So, if eukaryotes came out of crenarchaeota they had to remove one
    lipid metabolism and add-on another, highly unlikely

**[Need:]{style="text-decoration:underline;"} better ways of measuring
change - informatically - which will be more reliable with better
resolution to ensure we're arriving at the right answers. [One
example, ]{style="color:#000000;"}[PAM](https://en.wikipedia.org/wiki/Point_accepted_mutation)and
[BLOSUM](https://en.wikipedia.org/wiki/BLOSUM) protein alignment
matrices in models for deep phylogeny analysis**

Jonathan Eisen: Where do viruses fit?

Nance: Viruses at the time serving as vectors moving around genes,
recombination, if were to guess viruses, were around since the
beginning.

Amazing to attend this talk and hear from such a principal member of
this field.

https://www.flickr.com/photos/lpcohen/21817959689/in/dateposted-public/
