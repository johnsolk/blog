Title: Marine Microbes! What to do with all the data?
Date: 2016-04-07 10:30
Author: monsterbashseq
Category: Grad School, MMETSP, science
Slug: marine-microbes-what-to-do-with-all-the-data
Status: published

UPDATE: Check out Titus' blog post, [Bashing on monstrous sequencing
collections](http://ivory.idyll.org/blog/2016-mmetsp-a-first-look.html).

[Since Sept 2015, I've been a PhD student
in]{style="font-weight:400;"}[[C. Titus Brown’s
lab]{style="font-weight:400;"}](http://ivory.idyll.org/lab/index.html)[
at]{style="font-weight:400;"}[[UC
Davis]{style="font-weight:400;"}](http://mcip.ucdavis.edu/)[ working
with data from]{style="font-weight:400;"}[[Moore’s Marine Microbial
Eukaryotic Transcriptome Sequencing Project
(MMETSP)]{style="font-weight:400;"}](http://marinemicroeukaryotes.org/)[.
I would like to share some progress on that front from the past 6
months. Comments welcome!]{style="font-weight:400;"}

[MMETSP is a really unique and valuable data set consisting of 678
cultured samples with 306 species representing more than 40 phyla
(]{style="font-weight:400;"}[[Keeling et al
2014]{style="font-weight:400;"}](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889)[).
 It is public,]{style="font-weight:400;"}[[available on
NCBI]{style="font-weight:400;"}](http://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=231566)[.
The MMETSP data set consists entirely of cultured samples submitted by a
large consortium of PIs to the]{style="font-weight:400;"}[[same
sequencing
facility]{style="font-weight:400;"}](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889#s6)[.
All samples were PE 100 reads run on an Illumina HiSeq 2000 sequencing
instrument. A few samples were run on a
GAIIx.]{style="font-weight:400;"}

[For many species in this set, this is the only sequence data available
because reference genomes are not available. The figure below
from]{style="font-weight:400;"}[[Keeling et al.
2014]{style="font-weight:400;"}](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889)[
shows the diverse relationships between samples represented in the
MMETSP. The dashed lines indicate groups without reference genome
whereas the solid lines have references.]{style="font-weight:400;"}

[![10.1371-journal.pbio.1001889.g002](https://monsterbashseq.files.wordpress.com/2016/04/10-1371-journal-pbio-1001889-g002.png?w=2448){.wp-image-2436
.aligncenter width="450"
height="336"}](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889)

[Here are a few stars (]{style="font-weight:400;"}*[Micromonas
pusilla]{style="font-weight:400;"}*[ - left, *Thalassiosira
pseudonana*]{style="font-weight:400;"}*[ ]{style="font-weight:400;"}*[-
right):]{style="font-weight:400;"}

[![colored-2a](https://monsterbashseq.files.wordpress.com/2016/04/colored-2a.jpg){.alignnone
.wp-image-2675 width="263"
height="229"}](http://www.mbari.org/population-dynamics-of-phytoplankton/) [![thalassiosira-pseudonanana-n-kroger-tu-dresden](https://monsterbashseq.files.wordpress.com/2016/04/thalassiosira-pseudonanana-n-kroger-tu-dresden.jpg){.alignnone
.wp-image-2677 width="297"
height="173"}](http://www.washington.edu/news/2015/06/15/genetic-switch-lets-marine-diatoms-do-less-work-at-higher-co2/)

[It's worth emphasizing that this is - if not THE, one of the - largest
public, standardized RNAseq datasets available from a diversity of
species. Related to this cool dataset, I’m really grateful for a number
of things: a.) the MMETSP community who has taken the initiative to put
this sequencing dataset together, b.) the Moore Data Driven Discovery
program for funding, c.) to be working with a great PI who is willing
and able to focus efforts on these data, d.) being in a time when
working with a coordinated nucleic acid sequencing data set from such a
large number of species is even possible. ]{style="font-weight:400;"}

**Automated** ***De Novo*** **Transcriptome Assembly Pipeline**

[The]{style="font-weight:400;"}[[NCGR]{style="font-weight:400;"}](http://www.ncgr.org/)[
has already put together]{style="font-weight:400;"}[*[de
novo]{style="font-weight:400;"}*[transcriptome
assemblies]{style="font-weight:400;"}](ftp://ftp.imicrobe.us/projects/104/transcriptomes/)[
of all samples from this data set with]{style="font-weight:400;"}[[their
own pipeline]{style="font-weight:400;"}](https://github.com/ncgr/rbpa)[.
Part of the reason why we decided to make our own pipeline was that we
were curious to see if ours would be different. Also, because I’m a new
student, developing and automating this pipeline has been a great way
for me to learn about automating pipeline
scripts,]{style="font-weight:400;"}*[de
novo]{style="font-weight:400;"}*[ transcriptome assembly evaluation, and
the lab
diginorm]{style="font-weight:400;"}[[khmer]{style="font-weight:400;"}](http://khmer.readthedocs.org/en/latest/user/scripts.html)[
software. We’ve assembled just a subset of 56 samples so far, not the
entire data set yet. It turns out that our assemblies are different from
NCGR. (More on this at the bottom of this
post.)]{style="font-weight:400;"}

[All scripts and info that I've been working with are available
on]{style="font-weight:400;"}[[github]{style="font-weight:400;"}](https://github.com/dib-lab/MMETSP/blob/master/index.ipynb)[.
The pipeline is a modification of the first three steps of
the]{style="font-weight:400;"}[[Eel Pond mRNAseq
Protocol]{style="font-weight:400;"}](https://khmer-protocols.readthedocs.org/en/ctb/mrnaseq/)[
to run on an AWS instance. (I'm aware that these are not user-friendly
scripts right now, sorry. Working on that. My focus thus far has been on
getting these to be functional.)]{style="font-weight:400;"}

1.  [download raw reads
    from]{style="font-weight:400;"}[[NCBI]{style="font-weight:400;"}](http://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=231566)
2.  [[trim]{style="font-weight:400;"}](http://www.usadellab.org/cms/?page=trimmomatic)[
    raw reads,]{style="font-weight:400;"}[[check
    quality]{style="font-weight:400;"}](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
3.  [digital normalization
    with]{style="font-weight:400;"}[[khmer]{style="font-weight:400;"}](http://khmer.readthedocs.org/en/latest/user/scripts.html)
4.  *[de novo]{style="font-weight:400;"}*[transcriptome assembly
    with]{style="font-weight:400;"}[[Trinity]{style="font-weight:400;"}](https://github.com/trinityrnaseq/trinityrnaseq/wiki)
5.  [compare new assemblies to existing assemblies done
    by]{style="font-weight:400;"}[[NCGR]{style="font-weight:400;"}](https://github.com/ncgr/rbpa)

[The script]{style="font-weight:400;"}**getdata.py**[ takes a metadata
file downloaded from NCBI
(]{style="font-weight:400;"}[[SraRunInfo.csv]{style="font-weight:400;"}](https://github.com/ljcohen/MMETSP/blob/master/SraRunInfo.csv)[),
see screenshot below for how to obtain this
file:]{style="font-weight:400;"}

[![screenshot\_2015-10-041](https://monsterbashseq.files.wordpress.com/2016/04/screenshot_2015-10-041.png){.alignnone
.size-full .wp-image-2481 width="2252"
height="814"}](https://raw.githubusercontent.com/dib-lab/MMETSP/master/ScreenShot_2015-10-04.png)

[The metadata file contains info such
as]{style="font-weight:400;"}*[run]{style="font-weight:400;"}*[
(ID),]{style="font-weight:400;"}*[download\_path]{style="font-weight:400;"}*[,]{style="font-weight:400;"}*[ScientificName]{style="font-weight:400;"}*[,
and]{style="font-weight:400;"}*[SampleName]{style="font-weight:400;"}*[.
These are fed into a simple Python dictionary data structure, which
allows for looping and indexing to easily access and run individual
processes on these files in an automated and high-throughput way (subset
of the dictionary data structure shown
below):]{style="font-weight:400;"}

![dictionary](https://monsterbashseq.files.wordpress.com/2016/04/dictionary.png){.alignnone
.size-full .wp-image-2550 width="1500" height="779"}

[Each subsequent script
(]{style="font-weight:400;"}**trim\_qc.py**[,]{style="font-weight:400;"}**diginorm\_mmetsp.py**[,]{style="font-weight:400;"}**assembly.py**[,]{style="font-weight:400;"}**report.py**[,]{style="font-weight:400;"}**salmon.py**[)]{style="font-weight:400;"}
[uses this dictionary structure to loop through and run commands for
different software (trimmomatic, fastqc, khmer, Trinity, etc).
Assemblies were done separately for each sample, regardless of how they
were named. This way, we will be able to see how closely assemblies
cluster together or separately agnostic of scientific
naming.]{style="font-weight:400;"}

**Challenges**

[There have been several challenges so far in working with this public
data set.]{style="font-weight:400;"}

[It might seem simple in retrospect, but it actually took me a long time
to figure out how to grab the sequencing files, what to call them, and
how to connect names of samples and codes.
The]{style="font-weight:400;"}[[SraRunInfo.csv]{style="font-weight:400;"}](https://github.com/dib-lab/MMETSP/blob/master/SraRunInfo.csv)[
file available from NCBI helped us to translate SRA id to MMETSP id and
scientific names, but figuring this out required some poking around and
emailing people.]{style="font-weight:400;"}

[Second, for anyone in the future who is in charge of naming samples,
small deviations from naming convention, e.g. "\_" after the sample
name, can mess up automated scripts. For
example,]{style="font-weight:400;"}

    MMETSP0251_2
    MMETSP0229_2

[had to be split with the following lines of
code:]{style="font-weight:400;"}

    mmetsp=line_data[position_mmetsp]
    test_mmetsp=mmetsp.split("_")
    if len(test_mmetsp)>1:
        mmetsp_id=test_mmetsp[0]

Resulting in this:

    ['MMETSP0251', '2']
    ['MMETSP0229', '2']

[Then I grabbed the first entry of the list so that they looked like the
rest of the MMETSP id without the "\_". Not really a big deal, but it
created a separate problem that required some figuring out. My advice is
to pick one naming convention then name all of the files with the same
exact structure.]{style="font-weight:400;"}

Lastly, several of the records in the SraRunInfo.csv were not found on
the NCBI server, which required emailing with SRA.

![not\_found](https://monsterbashseq.files.wordpress.com/2016/04/not_found.png){.alignnone
.wp-image-2732 width="326" height="161"}

The people affiliated with SRA who responded were incredibly helpful and
restored the links.

**Assembly Comparisons**

[I used
the]{style="font-weight:400;"}[[transrate]{style="font-weight:400;"}](http://hibberdlab.com/transrate/)[
software
for]{style="font-weight:400;"}*[de-novo]{style="font-weight:400;"}*[
transcriptome assembly quality analysis to compare our assemblies with
the NCGR assemblies (\*.cds.fa.gz files). Below are frequency
distributions of proportions of reference contigs with Conditional
Reciprocal Best-hits Blast (CRBB), described
in]{style="font-weight:400;"}[[Aubry et al.
2014]{style="font-weight:400;"}](http://hit.http//journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1004365)[.
The left histogram below shows our
“]{style="font-weight:400;"}[[DIB]{style="font-weight:400;"}](http://ivory.idyll.org/lab/index.html)[”
contigs compared to NCGR. On the right are NCGR contigs compared to DIB
contigs. This means that we have assembled almost everything in their
assemblies plus some extra stuff!]{style="font-weight:400;"}

[![p\_ref\_CRBB\_dib\_v\_ncgr](https://monsterbashseq.files.wordpress.com/2016/04/p_ref_crbb_dib_v_ncgr1.png){.alignnone
.wp-image-2711 width="314"
height="230"}](https://github.com/ljcohen/MMETSP/blob/master/MMETSP_transrate.ipynb)[![p\_ref\_CRBB\_ncgr\_v\_dib](https://monsterbashseq.files.wordpress.com/2016/04/p_ref_crbb_ncgr_v_dib1.png){.alignnone
.wp-image-2713 width="313"
height="226"}](https://github.com/ljcohen/MMETSP/blob/master/MMETSP_reverse_transrate.ipynb)

[Here is the same metric shown in a different
way:]{style="font-weight:400;"}

[![p\_ref\_CRBB\_violin\_plots](https://monsterbashseq.files.wordpress.com/2016/04/p_ref_crbb_violin_plots1.png){.alignnone
.size-full .wp-image-2717 width="1500"
height="1005"}](http://rpubs.com/blahah/mmetsp_dib_vs_ncgr)

[We're not sure whether the extra stuff we’ve assembled is real, so we
plan to ground truth a few assemblies with a few reference genomes to
see.]{style="font-weight:400;"}

[For further exploration of these contig metrics, here are some static
notebooks:]{style="font-weight:400;"}

-   [[https://github.com/dib-lab/MMETSP/blob/master/MMETSP\_transrate.ipynb]{style="font-weight:400;"}](https://github.com/dib-lab/MMETSP/blob/master/MMETSP_transrate.ipynb)
-   [[https://github.com/dib-lab/MMETSP/blob/master/MMETSP\_reverse\_transrate.ipynb]{style="font-weight:400;"}](https://github.com/dib-lab/MMETSP/blob/master/MMETSP_reverse_transrate.ipynb)
-   [[http://rpubs.com/blahah/mmetsp\_dib\_vs\_ncgr]{style="font-weight:400;"}](http://rpubs.com/blahah/mmetsp_dib_vs_ncgr)

If you would like to explore these data yourself, here is an interactive
binder link that lets you run the actual graph production (thanks to
Titus for creating this link!):

[[http://mybinder.org/repo/dib-lab/MMETSP]{style="font-weight:400;"}](http://mybinder.org/repo/dib-lab/MMETSP)

**Outcomes**

[Based on these findings, several questions have come up
about]{style="font-weight:400;"}*[de
novo]{style="font-weight:400;"}*[transcriptome assemblies. Why are there
different results from different pipelines? Are these differences
significant? What can this tell us about
other]{style="font-weight:400;"}*[de novo]{style="font-weight:400;"}*[
transcriptome assemblies? Having distributions of quality metrics from
assemblies is a unique situation. Usually, assemblies are done by one
pipeline for just one species at a time, so means and standard
deviations are not available. There are increasingly more
new]{style="font-weight:400;"}*[de novo]{style="font-weight:400;"}*[
transcriptome assemblies being done and published by different groups
worldwide for
species]{style="font-weight:400;"}*[x]{style="font-weight:400;"}*[,]{style="font-weight:400;"}*[y]{style="font-weight:400;"}*[,]{style="font-weight:400;"}*[z.]{style="font-weight:400;"}*[
Yet, evaluations of the qualities of the assemblies are not
straight-forward. Is it worth developing approaches, a prioritized set
of metrics that will allow any]{style="font-weight:400;"}*[de
novo]{style="font-weight:400;"}*[ assembly to be evaluated in a standard
way? ]{style="font-weight:400;"}

[Moving forward, the plan is to:]{style="font-weight:400;"}

-   [keep working on this assembly evaluation
    problem,]{style="font-weight:400;"}
-   [assemble the rest of the samples in this data
    set,]{style="font-weight:400;"}
-   [make these data and pipeline scripts more user-friendly and
    available,]{style="font-weight:400;"}
-   [standardize annotations across species to enable meaningful
    cross-species analyses and comparisons.]{style="font-weight:400;"}

**Questions for the Community**

[What analyses would be useful to you?]{style="font-weight:400;"}

[What processed files are useful to you? (assembly fasta files, trimmed
reads, diginorm reads)]{style="font-weight:400;"}

[The idea is to make this data-intensive analysis process easier for the
consortium of PI who put these data together so that discoveries can be
proportional to the data collected. In doing so, we want to make sure
we're on the right track. If you're reading this and are interested in
using these data, we'd like to hear from you!]{style="font-weight:400;"}

[Special thanks to]{style="font-weight:400;"}[[C. Titus
Brown]{style="font-weight:400;"}](http://ivory.idyll.org/blog/)[,]{style="font-weight:400;"}[[Harriet
Alexander]{style="font-weight:400;"}](http://halexand.github.io/)[
and]{style="font-weight:400;"}[[Richard
Smith-Unna]{style="font-weight:400;"}](http://rik.smith-unna.com/)[ for
guidance, insightful comments, and plots!]{style="font-weight:400;"}

[Also, the cat:]{style="font-weight:400;"}

https://twitter.com/monsterbashseq/status/713202083009335297
