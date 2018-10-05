Title: MMETSP re-assemblies
Date: 2016-09-13 14:56
Author: monsterbashseq
Category: Bioinformatics, cluster, Data Analyses, MMETSP, reproducibility, science
Slug: mmetsp-re-assemblies
Status: published

\*\*\* Update (9/27/2016): 719 assemblies now available at the links
below. All FINISHED!!!

\*\*\* Update (9/22/2016): 715 assemblies now available at the links
below.

I have \*almost\* finished re-assembling *de novo* transcriptomes from
the Marine Microbial Eukaryotic Transcriptome Sequencing Project
([Keeling et al.
2014](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889)).
This is an effort that I have been working on over the past year as
a PhD student in [Titus Brown's
lab](http://ivory.idyll.org/lab/index.html) at UC Davis. The lab has
developed the Eel pond [khmer
protocol](https://khmer-protocols.readthedocs.io/en/ctb/mrnaseq/) for
assembling RNAseq data *de novo* from any species. I adapted and
automated this protocol for Illumina PEx50 data from the MMETSP.

Here are 659 assemblies:

[Figshare](https://figshare.com/articles/Marine_Microbial_Eukaryotic_Transcriptome_Sequencing_Project_re-assemblies/3840153/3)

We're not completely finished yet, but in the meantime we wanted to make
these available in case they are useful to you. If you do use, (per
academic protocol) please cite us:

Cohen, Lisa; Alexander, Harriet; Brown, C. Titus (2016): Marine
Microbial Eukaryotic Transcriptome Sequencing Project, re-assemblies.
figshare. [https://dx.doi.org/10.6084/m9.figshare.3840153.v3](https://figshare.com/articles/Marine_Microbial_Eukaryotic_Transcriptome_Sequencing_Project_re-assemblies/3840153/3){.citation-link}

Let us know if you have any questions or difficulties. As a caveat: we
aren't guaranteeing that these assemblies are better than the [NCGR
assemblies](ftp://ftp.imicrobe.us/projects/104/). They are different as
a whole. Here is some [quality
information](https://github.com/ljcohen/MMETSP/blob/master/notebooks/MMETSP_Trinity_transrate_busco_scores.ipynb) and
spreadsheets to look up your specific MMETSP ID of interest:

[BUSCO
scores](https://github.com/ljcohen/MMETSP/blob/master/assembly_evaluation_data/busco_scores_MMETSP.csv)

[Transrate
scores](https://github.com/ljcohen/MMETSP/blob/master/assembly_evaluation_data/transrate_scores.csv)

**Automated Scripts**

https://github.com/ljcohen/MMETSP

I'm still working on makings these scripts more accessible and useful
for people. Thanks especially to the [DIB lab code review
session](https://github.com/ljcohen/MMETSP/issues/5), I will be working
on these over the next month. Stay tuned!

The pipeline (flowchart below
created with [draw.io](https://drive.google.com/a/ucdavis.edu/file/d/0BwVev-vusUH1ZXh2ekRsVjFZSkU/view?usp=sharing))
is as follows: 1.) getata.py, 2.) trim\_qc.py, 3.) diginorm\_mmetsp, 4.)
assembly.py. All of the Python scripts are controlled by the
[SraRunInfo.csv](https://github.com/ljcohen/MMETSP/blob/master/SraRunInfo.csv)
metadata spreadsheet downloaded from NCBI that contains the url and
sample ID information.

![mmetsp\_pipeline](https://monsterbashseq.files.wordpress.com/2016/09/mmetsp_pipeline1.png){.alignnone
.size-full .wp-image-4260 width="723" height="283"}

This pipeline could be used with SraRunInfo.csv obtained for any
collection of samples on [NCBI](http://www.ncbi.nlm.nih.gov/sra):

![ncbi\_sraruninfo](https://monsterbashseq.files.wordpress.com/2016/09/ncbi_sraruninfo3.png){.alignnone
.size-full .wp-image-4546 width="1500" height="681"}

**Is there value in re-assembling what has already been done?**

The [NCGR already performed assemblies with their pipeline in
2014](https://github.com/ncgr/rbpa) when these data were sequenced
([more information about their
pipeline](http://marinemicroeukaryotes.org/home/faq)). Why are we
interested in doing it again?

Software and best practices for RNAseq *de novo* transcriptome assembly
are changing rapidly, even since 2014. We found
[preliminary evidence](https://monsterbashseq.wordpress.com/2016/04/07/marine-microbes-what-to-do-with-all-the-data/)
that our assemblies are different than NCGR. Taking a look at some
[quality metrics for 589 new
assemblies](https://github.com/ljcohen/MMETSP/blob/master/notebooks/MMETSP_Trinity_transrate_busco_scores.ipynb),
here are the proportion of contigs from our new
[DIB](http://ivory.idyll.org/lab/) assemblies aligning with assemblies
from NCGR as reference
([left](https://github.com/ljcohen/MMETSP/blob/master/assembly_evaluation_data/transrate_reference_scores_cds.csv)),
compared to the reverse where the NCGR assemblies are aligned to our new
DIB assemblies
([right](https://github.com/ljcohen/MMETSP/blob/master/assembly_evaluation_data/transrate_reverse_scores_cds.csv)).

[![dib\_v\_ncgr](https://monsterbashseq.files.wordpress.com/2016/09/dib_v_ncgr.png){.alignnone
.wp-image-4342 width="313"
height="220"}![ncgr\_v\_dib](https://monsterbashseq.files.wordpress.com/2016/09/ncgr_v_dib.png){.alignnone
.wp-image-4341 width="290"
height="210"}](https://github.com/ljcohen/MMETSP/blob/master/notebooks/MMETSP_Trinity_transrate_busco_scores.ipynb)

This confirms our preliminary evidence that we have assembled nearly
everything the NCGR did, plus extra. Still not sure what the extra stuff
is, if it's useful.

There are some samples that have performed well (shown below [BUSCO
scores](http://busco.ezlab.org/) - left - and [transrate
scores](http://hibberdlab.com/transrate/metrics.html) - right), while
others that have not.

[![busco](https://monsterbashseq.files.wordpress.com/2016/09/busco.png){.alignnone
.wp-image-4400 width="305"
height="208"}![transrate](https://monsterbashseq.files.wordpress.com/2016/09/transrate.png){.alignnone
.wp-image-4401 width="310"
height="215"}](https://github.com/ljcohen/MMETSP/blob/master/notebooks/MMETSP_Trinity_transrate_busco_scores.ipynb)

The effects of one pipeline vs another - which software programs are
used and decisions made during the pipeline are not well understood. Are
there biological consequences, i.e. are there more protein coding
regions detected, between pipelines? Ours may or may not be better, but
they're different so we're exploring how and why.

If our results are different for these assemblies, chances are high that
results from other people's assemblies are dependent on the methods they
are using to do their assemblies. Every month, there are \~a dozen
publications announcing a new *de novo* transcriptome of a eukaryotic
species. Just in 2016, there have
been 743 [publications](https://scholar.google.com/scholar?q=%22de+novo+transcriptome+assembly%22&btnG=&hl=en&as_sdt=0%2C5&as_ylo=2016) (as
of 9/13/2016) on "de novo transcriptome assembly". When new software
programs are developed, updated versions are released, decisions are
made about which software programs and what pipeline/workflow to use.
What are the effects of these decisions on the results being produced by
the scientific community?

This is the first time - as far as we are aware - that anyone has looked
carefully at a mass of assemblies like this from a diversity of
organisms. This is a really great data set for a number of reasons: 1) a
diversity of species, 2) library prep and sequencing was all done by the
same facility. This is such a large number of samples that we can apply
a statistical analysis to examine the distribution of evaluation
metrics, e.g. transrate scores, BUSCO scores, proportion of contigs
aligning to the reference, etc.

We're really excited to be working with these data! And very grateful
that these samples have been collected for this project and that the raw
data and assemblies done by NCGR are available to the public!

**Scripts for this project were developed on different systems:  
**

-   Cluster: [MSU HPCC](https://icer.msu.edu/)
-   Cloud: [AWS](https://aws.amazon.com/)
-   Cloud: [NSF-XSEDE
    Jetstream](https://www.xsede.org/jump-on-jetstream) (TG-BIO160028:
    "[Startup allocation request for the storage, exploration, and
    analysis of the Marine Microbial Eukaryotic Transcriptome Sequencing
    Project](https://www.xsede.org/web/staff/allocations-by-institution?p_p_id=allocationsbyinstitution_WAR_allocationqueriesportlet_INSTANCE_qfS0&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=2&_allocationsbyinstitution_WAR_allocationqueriesportlet_INSTANCE_qfS0_caller=link&_allocationsbyinstitution_WAR_allocationqueriesportlet_INSTANCE_qfS0_institutionId=101&_allocationsbyinstitution_WAR_allocationqueriesportlet_INSTANCE_qfS0_queryType=active&_allocationsbyinstitution_WAR_allocationqueriesportlet_INSTANCE_qfS0_institutionName=University+of+California%2C%20Davis)")

https://twitter.com/monsterbashseq/status/755223283486699520

**The mystery of the extra samples:**

This is more of an issue related to managing data from a project with
this number of samples rather than a scientific problem. But it required
some forensic files investigation. The number of samples in the SRA
Bioproject is different than the number of samples on imicrobe. There
are 678 samples approved by the
[MMETSP](http://marinemicroeukaryotes.org/project_organisms):

![mmetsp\_approved](https://monsterbashseq.files.wordpress.com/2016/09/mmetsp_approved.png){.alignnone
.wp-image-4148 width="241" height="153"}

Whereas there are 719 Experiments in the
[SRA](http://www.ncbi.nlm.nih.gov/bioproject/PRJNA231566/):

![mmetsp\_sra\_ncbi](https://monsterbashseq.files.wordpress.com/2016/09/mmetsp_sra_ncbi.png){.alignnone
.wp-image-4151 width="473" height="267"}

![mmetsp\_id\_venn](https://monsterbashseq.files.wordpress.com/2016/09/mmetsp_id_venn.png){.alignnone
.wp-image-4175 width="392" height="251"}

> OLlist\$Venn\_List\$NCBI  
> \[1\] "MMETSP0132\_2" "MMETSP0196" "MMETSP0398" "MMETSP0451\_2"
> "MMETSP0922" "MMETSP0924"  
> &gt; OLlist\$Venn\_List\$imicrobe  
> \[1\] "MMETSP0132\_2C" "MMETSP0196C" "MMETSP0398C" "MMETSP0419\_2"
> "MMETSP0451\_2C"  
> \[6\] "MMETSP0922C" "MMETSP0924C"

It turns out that these "extras" on either side of the venn diagram were
just ID with the letter "C" on the end.

For some reason, MMETSP0419\_2 (Tetraselmis sp. GSL018) has its own
BioProject
accession: [PRJNA245816](http://www.ncbi.nlm.nih.gov/bioproject/245816){.RegularLink}.
So, [PRJNA248394](http://www.ncbi.nlm.nih.gov/bioproject/248394){.RegularLink}
has 718 samples. Total, there are 719 MMETSP samples in the SRA:
[PRJNA231566](http://www.ncbi.nlm.nih.gov/bioproject/PRJNA231566/). In
the SraRunInfo.csv, the "SampleName" column for the extra sample
(SRR1264963) says "Tetraselmis sp. GSL018" rather than MMETSP0419\_2.

The next thing to figure out was that there are more IDs in SRA than in
imicrobe because some MMETSP ID have multiple, separate Run ID in SRA:

    > length(unique(MMETSP_id_NCBI))
    [1] 677
    > length(unique(ncbi$Run))
    [1] 718
    > length(unique(MMETSP_id_imicrobe))
    [1] 678

These are the samples that have multiple MMETSP ID in SRA:

![sra\_duplicated\_mmetsp](https://monsterbashseq.files.wordpress.com/2016/09/sra_duplicated_mmetsp1.png){.alignnone
.size-full .wp-image-4537 width="1374" height="397"}

Samples were assembled individually by each SRR id.

**Naming files is hard.**

It took me &gt;a day, plus some time thinking about this problem
beforehand, to sort out what to name these assembly files for sharing.
There are 2 useful ID for each sample: MMTESP id (MMETSPXXXX) and
NCBI-SRA id (SRRXXXXXXX). Since files were downloaded from NCBI and I'm
assembling samples individually, it made sense to organize by unique SRA
id since there can be multiple MMETSP for some SRR. IDs are not
recognizeable by humans reading them, though. So, in naming these files
I wanted to include scientific names (Genus\_species\_strain) as well as
the ids:

***Genus\_species\_strain\_SRR\_MMETSP.Trinity.fasta***

Upon further examination, it turns out that some of the Genus and
species names were different between the metadata from the
[SRA](http://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=231566)
and [imicrobe](http://data.imicrobe.us/project/view/104). For example:

    Different imicrobe: Nitzschia_punctata SRA: Tryblionella_compressa
    Different imicrobe: Chrysochromulina_polylepis SRA: Prymnesium_polylepis
    Different imicrobe: Crustomastix_stigmata SRA: Crustomastix_stigmatica
    Different imicrobe: Chrysochromulina_polylepis SRA: Prymnesium_polylepis
    Different imicrobe: Compsopogon_coeruleus SRA: Compsopogon_caeruleus
    Different imicrobe: Lingulodinium_polyedra SRA: Lingulodinium_polyedrum

There were &gt;100 of these differences. Some were spelling errors, but
others, like the *Lingulodinium polyedra* vs. *Lingulodinium polyedrum*
or *Copsopogon coeruleus* vs. *Compsopogon caeruleus *examples above, I
wasn't sure if this was a spelling preference or an actual difference.
The scientific naming in the SRA is linked to the NCBI taxonomy
convention, but it could be possible that the names assigned by experts
in this field (thus making their way into the metadata hosted by
[imicrobe](http://imicrobe.us/)) are further ahead in its naming than
NCBI. So, in these cases, I included both SRA and imicrobe names.

***Genus\_species(SRA)\_strain\_SRR\_MMETSP\_alt\_Genus\_species(imicrobe).Trinity.fasta***

It was also necessary to clean the metadata to remove special, illegal
characters like ")(%\\/?'. Some of the assembly file names now have
multiple "\_" and "-" because characters had to be stripped out.
[OpenRefine](http://openrefine.org/) is a fantastic program to
automatically do this task. Anyone can freely use it. Those who manage
projects with metadata input by a consortium of people individually
entering data by hand should especially use OpenRefine! It will even
cluster similar spellings and help to catch data entry typos! [Data
Carpentry has a fantastic lesson to walk you through using
OpenRefine.](http://www.datacarpentry.org/OpenRefine-ecology-lesson/00-getting-started.html) Use
it. It will make your life easier.

**Uploading files**

It turns out that version-controlling file storage and sharing for
hundreds of files is not straight-forward yet. We explored figshare,
Box, Dropbox, S3, ftp server hosting, and/or institutional server
storage. For reasons, we chose figshare (for one .zip file) and Box
cloud storage for individual files. As we get the last of the
assemblies, we'll move files and update the links at the top of this
blog post.

**Downloading files**

We chose to use the NCBI version of these files. [ENA
numbers](http://www.ebi.ac.uk/ena) were not as easy as SRA to locate a
metadata spreadsheet with a predictable url address for each sample. The
imicrobe project hosts these files, but the files do not follow a
predictable pattern to facilitate downloading all of the data. So, we
downloaded the fastq from NCBI.

When we wanted to compare our assemblies to NCGR assemblies, [Luiz
Irber](http://www.luizirber.org/) wrote this
wonderful [script](https://github.com/ljcohen/MMETSP/blob/master/imicrobe/download_mmetsp_transcriptomes.sh)
for downloading the [NCGR assemblies for all of the
samples](https://github.com/ljcohen/MMETSP/blob/master/imicrobe/download.txt) from
the [imicrobe ftp
server](ftp://ftp.imicrobe.us/projects/104/transcriptomes/).

    #!/bin/bash

    # from Luiz Irber
    # sudo apt-get install parallel

    seq -w 000 147 | parallel -t -j 5 "wget --spider -r \  
   ftp://ftp.imicrobe.us/projects/104/transcriptomes/MMETSP{} 2>&1 \  
   | grep --line-buffered -o -E 'ftp\:\/\/.*\.cds\.fa\.gz' > urls{}.txt"
    cat urls* | sort -u > download.txt
    cat download.txt | parallel -j 30 -t "wget -c {}"

**Loose ends:**

Most assembles are done. Some aren't.

![finished\_trinity](https://monsterbashseq.files.wordpress.com/2016/09/finished_trinity1.png){.alignnone
.size-full .wp-image-4557 width="1500" height="600"}

**To-Do:**

-   Complete the remaining 59 assemblies. Assess what happened to these
    59 samples.
-   Assess which samples are performing poorly according to evaluation
    metrics.
-   Look at Transrate output to help answer, "What is the extra stuff?"
-   Make scripts more accessible.
-   Partition a set of samples for benchmarking additional software.
    (With [bioboxes](http://bioboxes.org/)?)
-   Update [khmer
    protocols](https://khmer-protocols.readthedocs.org/en/ctb/mrnaseq/).

**Acknowledgements**

Special thanks to Moore Foundation for funding, [Titus
Brown](http://ivory.idyll.org/blog/), [Harriet
Alexander](http://halexand.github.io/) and everyone in the [DIB
lab](http://ivory.idyll.org/lab/members.html) for guidance and
information. Thanks also to [Matt MacManes](http://genomebio.org/)'
suggestions and [helpful tutorial and installation
instructions](http://angus.readthedocs.io/en/2016/MacManes_Trinity.html) and
[Torsten Seeman](http://tseemann.github.io/)'s and [Rob
Patro](http://www.robpatro.com/redesign/)'s helpful assistance at
[NGS2016](http://angus.readthedocs.io/en/2016/) with asking questions
and getting BUSCO and Transrate running.
