Title: Extracting biological features from 'big data' with ADAGE - Dr. Casey Greene
Date: 2015-10-12 11:51
Author: monsterbashseq
Category: talks
Slug: extracting-biological-features-from-big-data-with-adage-dr-casey-greene
Status: published

[Dr. Casey Greene, University of
Pennsylvania](http://www.greenelab.com/research) - talk at UC Davis,
October 12, 2015

Twitter, to be
used! [@GreeneScientist](https://twitter.com/GreeneScientist)

Started with example that [Carrots are routine fun part of every
day!](https://hbr.org/2015/10/the-ceo-of-bolthouse-farms-on-making-carrots-cool) Just
like bioinformatics and genomics. Aim to scale up data universe from lab
-&gt; publicly-available -&gt; compendium. Big data universe right now
includes all the data collected, really big for humans available now
\~1.3 million public assays. Can we use?

https://www.flickr.com/photos/lpcohen/21926855508/in/dateposted-public/

Analysis methods are accessible, available, affordable. Sustainable for
compendium of human data  and also nonmodel systems.

Worlds fastest introduction to machine learning. Classes of algorithms.
What patterns normally exist? Unsupervised algorithm vs. supervised
giving system some knowledge. With new data, what else looks like it?
What new features can you extract that I care about?

Example with tissue-specific expression from cell lineages. Physically
too connected to each other. COmputationlly, wanted to subtract out what
not interested in. Started with large data sets, small set of genes
curated from literature that interested. Machine learning approach. List
of genes specifically expressed for cell lineage.

**Support vector machines** (not a scary method, despite
name!): Expression of features in sample 1, low expression of same
features in sample 2 and other features high in both. Place line in
manner to maximally separate data from different animals, support
vectors will create buffered area + and - surrounding the line.

*In silico* predictions, now that I know where proteins are expressed,
what other information can we learn?

Functional interaction standard, genes work together during specific
processes. Assumption that functioning together in tissues. Structure
algorithm to use this and make predictions from this assumption. Draw
gold standard of things you think will work together by overlaying
tissue on process network. Judge every publicly-available by how much it
tells you about that tissues. Generate network for every tissue and do
things like understand how genes are connected to each other, disease
states, GWAS.

Take a look at [Greene et al. *Nature Genetics*,
2015.](http://www.nature.com/ng/journal/v47/n6/abs/ng.3259.html)

GWAS example: Cases vs. Controls, Manhattan plot for every SNP in
genome. Low statistical strength because of low-frequency mutations.
Don't observe enough to draw strong inference, possibly small effects.
Noisy data. Build prediction, then better mapping to annotated disease
genes. For example, Kidney NetWAS of hypertension. Also, lupus Type 2
Diabetes, etc. (Irene's paper just accepted)

Discovery is the point. "[Research is to see what everyone else has
seen, to think what nobody else has thought." -Albert
Szent-Györgyi](http://szegedmed.hu/pdf/Conference_summary.pdf)

Should be using unsupervised algorithms from a discovery standpoint. If
you showed 16,000 computers 10 million images from youtube, what would
they see?

https://www.flickr.com/photos/lpcohen/21926777930/in/dateposted-public/

Cats. [Le et al.
2012](http://static.googleusercontent.com/media/research.google.com/en//archive/unsupervised_icml2012.pdf)
Unsupervised discovery for Google.

Analysis with Denoising Autoencoders of Gene Expression
([ADAGE](https://github.com/greenelab/adage)), preprint:

[Jie Tan, John H Hammond, Deborah A Hogan, Casey S Greene. 2015. ADAGE
analysis of publicly available gene expression data collections
illuminates Pseudomonas aeruginosa-host interactions. doi:
http://dx.doi.org/10.1101/030650](http://biorxiv.org/content/early/2015/11/05/030650)

Judge algorithm for how well it removes noise.

Gene Expression -&gt; add random noise -&gt; corrupted expression -&gt;
extract features -&gt; interpret -&gt; biological meaning, e.g. growth
rate, strain, oxygen, then reconstruct Gene Expression.

[Tan et al. Pac Symp Biocomput.
2015:132-43.](http://www.ncbi.nlm.nih.gov/pubmed/25592575)

Corroborating evidence from [LeCun Bengio and Hund Nature
2015](http://www.nature.com/nature/journal/v521/n7553/full/nature14539.html) 
that unsupervised learning has something going for it.

Generate meaningful hyptheses...produce useful networks.

ADAGE identifies strain differences. Genome Hybridization, PA01 vs.
PA14. Activity value of one node, low to high activitiy. If I care about
strains, things that don't hyb will look different. Algorithm can
differentiate. Confirmation that model is pulling out biological
properties.

ADAGE-based pathway analysis of transcriptomic changes, e.g. regulators
of nitrogen metabolism. Gives us smaller universe to think about,
looking at processes as a whole. Lets us get beyond curated pathway
database, e.g. KEGG. **This is really, really, really cool.** (example
that you will only get 1 gene if you relied on curated KEGG database,
relative to network discovery from ADAGE)

Pan-Cancer Analysis with tissue biopsies.

PILGRM is for biologists: [Greene and Tryoanskaya Nucleic Acids
Research. 2011](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3125802/)

[Wong et al. Nucleic Acids Res.
2012](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3394282/)

Tribe, Zelaya and Green, *In prep*

Sign up on webpage to get info on web servers:

http://www.greenelab.com/webservers/
