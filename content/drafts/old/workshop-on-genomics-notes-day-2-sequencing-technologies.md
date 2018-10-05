Title: Workshop on Genomics (Notes, Day 2) - Sequencing Technologies
Date: 2014-01-14 08:07
Author: monsterbashseq
Category: Bioinformatics, Genomics Workshop, Sequencing
Slug: workshop-on-genomics-notes-day-2-sequencing-technologies
Status: published

http://www.flickr.com/photos/lpcohen/11945854246/in/photostream  
Dr. Konrad Paszkiewicz, University of Exeter

Lecture slides:
http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2014/01/Cesky-Krumlov-Lecture-1-ver6.pdf

From Sanger -&gt; human genome -&gt; 2nd gen -&gt; 3rd gen -&gt;
Nanopore (not yet released)

Recommended videos on Sanger sequencing:  
http://youtu.be/91294ZAG2hg  
http://youtu.be/bEFLBf5WEtc

Illumina - Least expensive and most commonly used

Advantages:  
- short run times  
- straight-forward sample prep  
- open source software

Disadvantages:  
- short reads  
- pooling samples  
- sequence clusters on flow cell

Each cycle uses -&gt; 1.) blocking, 2.) enzyme, 3.) fluorophore

\* Paired-end sequencing is analyzed based on lane proximities, bridge
amplification, each dot represents cluster, lane calling

Each cycle looks at color and position of dots:

[![Screenshot from 2014-01-14
23:04:28](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230428.png?w=300){.alignnone
.size-medium .wp-image-737 width="300"
height="210"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230428.png)

Oversimplification of adding bases at each cycle: dye-labeled bases are
added, then block, then block is washed away, laser excitation, the next
cycle starts:

[![Screenshot from 2014-01-14
23:08:09](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230809.png?w=300){.alignnone
.size-medium .wp-image-738 width="300"
height="236"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230809.png)
[![Screenshot from 2014-01-14
23:08:38](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230838.png?w=300){.alignnone
.size-medium .wp-image-739 width="300"
height="254"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230838.png)

The resulting image of the flow cell, at each cycle, looks like this:

[![Screenshot from 2014-01-14
23:09:24](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230924.png?w=300){.alignnone
.size-medium .wp-image-740 width="300"
height="198"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230924.png)
[![Screenshot from 2014-01-14
23:09:52](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230952.png?w=300){.alignnone
.size-medium .wp-image-741 width="300"
height="153"}](http://monsterbashseq.files.wordpress.com/2014/01/screenshot-from-2014-01-14-230952.png)

Algorithms take into consideration emission wavelengths at each cycle at
each spot, and the reads are constructed from these. Each cycle looks at
color and position of the dots.

36-150 nucleotides per read, 300 Gb data per run

Quality scores decrease as run progresses, error rate of enzyme
increases

2 sets of amplifications - before (library prep, enough sample), during
(to get enough signal)

Issues:  
- cluster merging ([Krueger et al.
2011](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0016607))  
- inverted repeats and GGC motif

454 Sequencing: longer read lengths, bead-based adapters at end of bead,
pyrosequencing, phased out by Roche in 2012

SOliD: abandoned by Life Technologies in favor of Ion Torrent recently

Benchtop Sequencing:

Ion Torrent: no optics, pH sensor detects nucleotide by release of H+
(different for each base), no incorporation or termination, 400 bp
reads, 2 hr runtime, various chip types

Ion Proton: 200 bp reads, single end, PGM vs. Proton

Useful benchtop technology review paper, Loman et al. (2012):
http://www.nature.com/nbt/journal/v30/n5/full/nbt.2198.html

3rd gen: single molecule sequencing - Pac Bio only one on market at the
moment (RSII)  
- Zero Mode wave (ZMW) guide on an SMRT flow cell (looks like a
microarray with fixed position  
- camera detection  
- library prep required  
- 100,000-150,000 per run, few hours, \$500/run  
- 300-500Mb  
- distribution of read lengths  
- good for detecting epigenetic changes  
- error rates, but algorithms to correct,  
- look at materials on PacBio github:
https://github.com/PacificBiosciences/Bioinformatics-Training/wiki  
- Cicular consensus sequencing can be used

Nanopore = "very small hole"  
- measures current changes as polymer passes through hole  
- exonuclease to chop DNA  
- cyclodextrin to measure charge across membrane

Strand sequencing, MinIon:  
- 512 pore chip  
- 100 Mb-1 Gb per run  
- disposable after 6 hr run  
- 4% error rate in trials  
- requires library prep - introduces loops for feeding to Nanopore  
- more for detection  
- error profiles can be handled with different pore types with
complimentary error  
- cost is high

Illumina still least expensive of all technologies.

\*\*\*Take-home message: Technology is becoming easier to acquire
massive amounts of data. Bottleneck is now always at bioinformatics
level.
