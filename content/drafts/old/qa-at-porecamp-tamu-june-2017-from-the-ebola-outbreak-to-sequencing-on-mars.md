Title: Q&A at Porecamp TAMU, June 2017: From the Ebola Outbreak to Sequencing on Mars
Date: 2018-02-01 11:41
Author: monsterbashseq
Category: biotech, workshops
Slug: qa-at-porecamp-tamu-june-2017-from-the-ebola-outbreak-to-sequencing-on-mars
Status: published

https://twitter.com/monsterbashseq/status/871794185866625024

As part of my PhD project at UC Davis with [Dr. C. Titus
Brown](http://ivory.idyll.org/lab/) and [Dr. Andrew
Whitehead](https://whiteheadresearch.wordpress.com/), I am assessing the
feasibility of using [Oxford Nanopore Technologies (ONT)
MinION](https://nanoporetech.com/products/minion) device to generate
long reads of DNA sequencing data for *de novo *genome assemblies of
[several species of freshwater *Fundulidae*
killifish](http://onlinelibrary.wiley.com/store/10.1111/j.1558-5646.2010.00957.x/asset/j.1558-5646.2010.00957.x.pdf;jsessionid=1329DEEDADBB8146DB0DD64C6FE11E52.f02t02?v=1&t=jd3ujrnj&s=f224e7931e610848265eb2b5fff75e1dd51c4e6d&systemMessage=Please+be+advised+that+we+experienced+an+unexpected+issue+that+occurred+on+Saturday+and+Sunday+January+20th+and+21st+that+caused+the+site+to+be+down+for+an+extended+period+of+time+and+affected+the+ability+of+users+to+access+content+on+Wiley+Online+Library.+This+issue+has+now+been+fully+resolved.++We+apologize+for+any+inconvenience+this+may+have+caused+and+are+working+to+ensure+that+we+can+alert+you+immediately+of+any+unplanned+periods+of+downtime+or+disruption+in+the+future.).
The final assemblies for each freshwater species will be used to compare
genomic regions to their sister marine species, *[Fundulus
heteroclitus](https://academic.oup.com/gbe/article/9/3/659/2992614)*.

The MinION is a portable (plugs into the USB port of a laptop!),
real-time sequencing technology that can [potentially yield reads
&gt;100 kb](https://twitter.com/mattloose/status/954147458778587136)
([distributed read lengths &gt;10
kb](https://twitter.com/mattloose/status/956937752557379584)). This is
so super cool! Below is our MinION device chugging along last week with
data from *Fundulus nottii*.

![39716498871\_a757d55f89\_b](https://monsterbashseq.files.wordpress.com/2018/01/39716498871_a757d55f89_b-e1517451140171.jpg){.alignnone
.size-full .wp-image-4963 width="1022" height="566"}

From June 5-9, 2017, I attended [Porecamp USA at Texas
A&M](http://www.txgen.tamu.edu/porecamp_usa/), hosted by the [TAMU
Agrilife sequencing facility](http://www.txgen.tamu.edu/), to get
organized instruction and hands-on experience with the MinION. This was
great for several reasons. Since ONT is a relatively new sequencing
technology, [troubleshooting efforts have been
challenging](https://monsterbashseq.wordpress.com/2016/08/13/adventures-with-ont-minion-at-mbls-microbial-diversity-course/).
Updates to the platform occur rapidly. Attending Porecamp allowed me the
opportunity to meet experts in person as well as other researchers who
are also excited about this new technology. Twitter and email are great
for asking questions, but there is no substitute to asking someone a
question or having a discussion in person. Making connections and being
part of the community of MinION users was an invaluable part of the
Porecamp experience. I felt lucky to attend Porecamp, took an
overwhelming amount of notes and wanted to share here so others can
hopefully benefit. This will likely be just one in a series of blogposts
to come!

The first night, there was a very informative Q&A session with the panel
of instructors for the workshop, who are leading experts in the field:
[Nick Loman](http://lab.loman.net/), [Josh
Quick](https://twitter.com/Scalene), [Matt
Loose](https://www.nottingham.ac.uk/life-sciences/people/matt.loose), [John
Tyson](http://snutchlab.msl.ubc.ca/labmembers/), and [Mick
Watson](http://www.roslin.ed.ac.uk/mick-watson/).

https://twitter.com/ThatLionLady/status/871884381090181124

Below is a transcript from my notes. Any mis-interpretation or
misinformation is error on my part. Please let me know!

***Q: For species with small body sizes or low yields, how feasible are
whole genome assemblies from multiple individuals using reads from only
ONT and/or ONT and other platforms?***

***A:*** Same for any genome assembly. What you want for a reference
genome assembly is to get a [haploid genome
assembly](https://uswest.ensembl.org/Help/Faq?id=216) from tons of DNA.
There are some diploid assembly tools, which try to separate out
haplotypes, but to be honest they're not very good. As soon as you put
multiple individuals into a pool for sequencing, you get a worse
assembly because all the structural variation is unique to each
individual and the assembly graph kind of falls apart where they don't
agree with one another. But it's perfectly possible, people have been
doing it for years with nematode worms and all sorts of other stuff.
Heterozygosity is a massive problem for all genome assemblies all the
way back to when we were doing them with Sanger. If you can develop some
kind of cell lines and generate buckets of DNA, that's often a good way
to go.

***Q: How much time should one allow for ordering flowcells? (Backstory:
Ordering to delivery has taken from 1 week to 1 month and has been
difficult to plan for fresh DNA extractions, library prep and sequencing
library and it's been challenging.)***

***A:*** I think that's quite an interesting question actually. We're a
bit biased because we're in the UK. And I don't know what effect being
in the UK has on flowcell supply. In 2014 we all got involved in
Nanopore sequencing and it would be fair to say that there have been
periods of time when flowcell supply has been restrictive, but now it
seems to be very robust and very reliable. We do have [Michael]{.il}
Micorescu from ONT here to help answer these questions at another time.

***Q: What would you say is the shelf life of a flowcell?***

***A:*** The shelf life of a flowcell now, 8 weeks is absolutely fine.
We've got flowcells that have been sitting in the fridge for longer than
that and I'm still looking forward to using them. So, there's no
problem. 8 weeks is fine. It used to be that you wanted to use them as
soon as they arrived, but that's not the case now. They're pretty
stable.

Since they're more stable than they were initially, and I think the
flowcells are much more consistent and more reliable than they have ever
been, I think. You need to get the temperature right, they can't be
frozen.

I can confirm from a postdoc who did received flowcells and put them in
the -80 degC and that doesn't work. We did call Nanopore and they asked
what had happened. It was quite an interesting response was, we don't
know what will happen, can you try running them anyway. The answer is
they don't work. So, don't put them at -80.

***Q: What level of sequencing coverage is necessary to correct for
sequencing error?***

***A:*** The short answer is we don't really have a good answer for that
question. It depends on a number of factors, including are you doing 1D
or 1D\^2 and what is the context GC homopolymeric content of your
gene-level region of interest. I'd say as a rule of thumb, it is
diminishing returns as you get above 100x coverage. You'll probably got
most of the benefit from consensus calling quite early on, probably
around 25x. We found that when we get systematic assessments in the
Ebola project, actually 25x of 2D and 50x of 1D was sufficient to get us
the correct genotype. If you got to 100X you might get a little bit
more, but what's notable is you don't really get the perfect consensus
at any point because of residual homopolymeric problems. And that's an
open problem with the platform. So it's not worth it to go to thousands
of x coverage, it just makes everything slower an doesn't really improve
anything.

It's also important to use the signal. We'll talk about that later \[in
the workshop\] when we talk about bioinformatics, the importance of
using the signal, not just the basecalls. The signal is where there's
extra information that can be utilized to get a really good result. And
that's often not used. Typically, in Illumina sequencing, you don't go
back to the signal. But it's important in Nanopore that you do look at
the signal information.

***Q: Are there batch effects from one flowcell to another. How wary
should we be of combining data from multiple flowcells?***

***A:*** Within a single flowcell type, we're on R9.5 at the moment, I
don't think there are any issues with combining data across flowcells.
If you take exactly the same library and split it across 2 different
flowcells it will perform equivalently. In fact, we did a really nice
experiment just last week showing that and looking at the read length
distributions and they're identical across 2 flowcells. You might get
slightly different yield. And we'll talk a lot about the nitty gritty of
this on the running days, the number of pores you have available for
sequencing. It can get complicated if you are starting to merge data
from different flowcell types. So, that's always worth remembering which
flowcell you're looking at.

There is potentially a benefit from doing that? Didn't Jared \[Simpson\]
once say he could get good results combining R9 and R7.3. But they will
have slightly different error profiles, though. Different pore types
have slightly different error profiles.

I think there's another point about that we often don't have the same
starting DNA from different samples in an experiment, if you try to do a
controlled experiment. With the high input requirements, it makes it
quite tempting to go and do another extraction. Just bear in mind that
those are going to be technical replicates, or biological replicates.
They can also be completely different conditions depending on if you
gone back and regrown organisms. So, you could be called out if you're
trying to do a bunch of different experiments and combine them
toegether, especially for something like transcription.

***Q: What is the minimum DNA requirement for the Tagmentation
protocol?***

***A:*** According to the protocol, it is 400 ng for R9.5. If you want
to target very long reads, input would be 2 or 3 or 4 ug. (laughter) A
very broad minimum range.

***Q: What are the factors that contribute to how much data one flowcell
can yield.***

***A:*** Ultimately it comes down to the quality of the DNA you put in,
in terms of the number of the ability to generate enough active ends
with the motor to bind to the flow cell. In some senses, need to keep
the pores fed so you need to keep the concentration high enough so
enough sequence goes through the pore and when it's finished it needs to
bind to another fragment. So you want to keep that process as efficient
as possible so you maximize the usage of the pores as well. Every
flowcell you have will have a different number of pores. Although they
are very consistent in terms of the activity of what's there. The
difference is that the more pores you have, the more sequence you're
going to get, because there's more active processing.

I think it's fair to say there's a fair amount of variability. You can
have a library that looks good and has run well before and sometimes it
will be disappointing and sometimes it will be incredible. Some
flowcells just don't seem to ever give up and will be extreme outliers.
And I think it's fair to say that no one really understands why that is.
You can see some runs on the MinION now out to 10, 15, possibly even 17
Gb. But that's not typical. Typical for us would be more like 5 Gb. It's
not particularly well understood why, otherwise they would make it
consistent in the manufacturing.

***Q: How are the newest chemistries solving error issues?***

***A:*** One of the biggest improvements recently wasn't the chemistry
but the software engineering with the recent version of albacore
basecalling, which solves a lot of the homopolymer errors. So, it's not
just the chemistry. The R9 flowcells have been wonderful in terms of
quality, but the biggest improvement has been the software.

To say something about the pore or the shape of the pore. I think the
understanding is that the different pores have different reading edge
shapes. And that reading edge makes some context easier to read and in
some contexts more difficult to read. The net effect of that when they
moved from the R7 pore, which no one knows exactly what the biological
molecule was, but the R9 we do (the [csgG
protein](http://www.uniprot.org/uniprot/P0AEA2) from *E. coli*). That
was a very clear improvement from one pore to the other and it certainly
improved the ability to solve high GC, which was something that the R7
pore struggled with. And that had to do with the shape of the aperture
and the effect that has on the electrical current signal. And we'll talk
about that a bit more.

But I think too that the software improvements are just as relevant to
getting better results at the moment. Moving from quite simple models of
signal using Hidden Markov Models to the start of using neural networks,
recurrent neural networks and deep learning approaches which can use
much more long range context, that can understand, for example, the
effect of what sequence is in the motor protein quite far upstream of
the pore, say 20 bases upstream, what effect that sequence has on things
like movement time and downstream bases that are actually in the pore.
Seems like factoring in that conditionality gives a lot of improvements.

I think it's quite exciting that the improvements have been driven by
bioinformatics actually. Makes me think that someone can come along and
make it even better going forward. In fact, I think, for example, Oxford
Nanopore is usually quite closed in their software releases until
recently, but in the last few days have open sourced their based caller,
[scrappie](https://github.com/nanoporetech/scrappie) for the first time,
so that is quite exciting. That means that the community can have a go
at trying to improve on their current best. And I think that part of the
reason why they've done that is to encourage the community to get those
last percent or so of residual error sorted out.

***Q: How can I get a PromethION?***

***A:*** I'd quite like to know the answer to that myself. The simple
answer is you pay some money to Oxford Nanopore and they send you one.
But I guess that's not the answer that was requested. I think they hand
build them to a certain rate. They're not being rolled out as fast as
they could be because there are still some improvements in flowcell
chemistry that need to be sorted out before they're ready for prime
time.

And they're constantly improving the compute as well. I think people
underestimate how big of a machine the PromethION is, actually. If it
delivers 8 Gb from 48 flowcells, you think managing the data from one
MinION is bad. Wait until you start playing with a PromethION. They're
coming. They're out there. But the infrastructure needs to be setup.

Large-scale sequencing facilities are looking to use the PromethION.
There is the idea that if you get accuracy up to a certain level with
the long reads, you can move away from re-sequencing the human genome to
more *de novo* and large-scale structural variant analysis on the human
genome on the Nanopore platform, but there needs to be a cost benefit
before people would consider switching routinely.

***Q: Can you multiplex RNA on the MinION?***

***A:*** On the direct RNA protocol you can't with barcodes. The cDNA
protocol you could. What you can do surprisingly well is multiplex
samples without barcodes, particularly if they're sufficiently distinct.
We do that with bacterial genomes, like *Staph*, *Strep*, *Pseudomonas*,
although you could barcode. But just throw them all in together and save
yourself a little lab time, because they will assembly out as long as
the read length is sufficiently long, probably 10kb is more than
adequate. They'll just fall out.

Long amplicon cDNA, can do that as well. As long as they're different.
Goal is targeted sequencing, can just mix them in there.

You could also make your own barcodes.

***Q: What would be your recommendation for a lab that is considering
switching from Illumina to ONT sequencing?***

***A:*** I don't think they're equivalent. I'd think you'd want to keep
both so you can have a broader range of applications. They're
complimentary technology. Particularly the wgs, you want the long reads
to get all the structural variation to get the assembly in the first
place, but it's still useful to have Illumina to polish out the errors.
For RNAseq, you can get full-length cDNA with the long reads, but there
probably aren't enough reads to be truly quantitative and do counting so
you're going to need Illumina to do that. I wouldn't recommend doing 16S
anyway.

If the question was would you recommend switching from PacBio to
Nanopore, then yes. For smaller genome, like *C. elegans* genomes that
are \~100Mb with structural variations in them, we can span those now.
We have the benefit of being able to detect those now. You can use
Illumina data to polish those out. It's not like you have to have one or
the other. The cost is getting so cheap that it's silly not to use it to
improve. One can do very well with one or the other. But why not
combine? Which is what we're doing at the moment.

It's worth knowing that there's a lot of unused Illumina capacity in the
world. There are people who have HiSeqX that are not on full, and loads
more people are going to buy NovaSeqs, which won't be full. So, you
don't have to run your own Illumina. Just buy the data from any number
of service providers that will give it to you rather cheaply.

***Q: Can we link SmidgeION to cloud computing to compute real-time
basecalling from mobile devices? How would this revolutionize genomics
in the field?***

https://twitter.com/snkravitz/status/871842789906153473

***A:*** My understanding for the intention of the SmidgeION is that you
won't be basecalling in the cloud, you'll be basecalling on the phone.
Which is really quite cool. So, it would be local, hand-held. Bear in
mind that the SmidgeION is the smaller through-put device. So, I don't
think that you'll need to use the cloud for basecalling. It's worth
saying that cloud basecalling is gone. It used to be that you would send
your reads into the Amazon cloud. They'd be base-called there, and you
would get your called data back. That's gone. It's now all local
basecalling anyways.

In terms of how that will revolutionize genomics, it's a subject we're
very passionate about, which is really pathogen detection and diagnosis
in the field. The key thing for the SmidgeION is not that it's
necessarily on a mobile device, but that the cost of the flowcell should
be much, much lower than the current [cost of the
flowcells](https://store.nanoporetech.com/flowcells.html) (individually,
\$900/flowcell to get 2-10 Gbases). And that's really critical for
diagnostics. A \$500 diagnostic is too much for many applications.
(flowcells are \$500 each if you buy bulk packs of 48 for \$24,000,
\$475 for a pack of 300 for \$142,500). A \$20 diagnostic, if you can
get discovery of a whole bunch of different pathogens in one assay, and
typing and antibiotic resistance information, quickly, for things like
TB, HIV, Malaria, Ebola. All of those are going to be incredible
applications that you can have in the field. It will be a change to
diagnostics. Right now diagnostics is pretty much focused on targeted,
small numbers of pathogens that you assay at a time for things that you
expect to find. So, replace that with an open-ended diagnostic where you
can discover things that you might not expect to find. The classic
example for us from work that we've done is during the West African
Ebola epidemic, that wasn't recognized as Ebola for a good 2-3 months
after the first case, and that was because Ebola had never been seen in
that part of Africa before. You don't want to test for everything you
can imagine it could be. You want to get a definitive diagnosis quickly.
That means you can put the right measures in to stop small outbreaks
from becoming larger-scale outbreaks and eventually epidemics. So,
that's what we think is going to be the really exciting thing about an
even more portable sequencing diagnostic. But you could also imaging
similar things for human genetics as well. Some peopel think that people
will bring sequencing home for personal sequencing, like your fitbit,
you'll have your personal transcriptome measuring device. Whether that's
going to happen is going to be interesting. (It'll happen in my house.
But that's just because I really like sequencing.)

I think the MinION has already revolutionized genomics. Then with the
SmidgeION, it's only incremental on top of that.

***Q: Is the platform appropriate for potentially fragmented or degraded
DNA, particularly things like ancient DNA?***

***A:*** I think it's going to depend on if you can generate a piece of
DNA. You're not going to get really long pieces. But it's like any
system, if you can amplify, then you can generate sequence. You're not
necessarily going to get long pieces. The MinION can sequence your
pieces, you just won't get the benefit of long reads, which happens to
be the main benefit of the platform at the moment. [Justin O'Grady has
this protocol where he extracts DNA from
sputum](https://www.sciencedirect.com/science/article/pii/S221255311630228X)
and he uses the rapid PCR kit and regularly does that. I think the idea
of looking at ancient DNA on the MinION would be very exciting in the
sense that contamination would be the major issue. As well as DNA
damage. You have to remember with MinION and Nanopore, you are
sequencing the native molecule. So, we're actually looking at the
molecule itself, not a secondary copy of it \[like you are with the
Illumina platform and sequencing-by-synthesis technology\]. So, you are
able to look at what is the damage that's there. What are the changes
that happen over time to the DNA molecule. That's going to be really
exciting.

We think it's going to be huge in the direct RNA sequencing. We think
it's going to be the major draws. We've seen this in the little bit we
have done so far. There are certainly modifications you can spot just on
the fact that it throws the basecaller off compared to what the
reference sequence should be. So, you can have a reference sequence from
the exact same sample and you don't see base changes, but the basecaller
from the MinION is showing a change. That may be indicative of some
direct RNA modification to hte base that's going on there. It's a power
in being able to actually see what is there. Being able to interpret
that requires the ability to train and recognize those different
chemistries but I think that will come with time for sure.

We were just down at [ASM the last few days in New
Orleans](https://www.asm.org/index.php/asm-events/post-meeting-materials),
hearing [Astronaut Dr. Kate
Rubins](https://www.youtube.com/watch?v=Mnvy4LyO5EI) on [sequencing on
the
ISS](https://www.asm.org/index.php/general-science-blog/item/6444-the-first-person-to-sequence-dna-in-space-molecular-biologist-and-nasa-astronaut-kate-rubins).
The idea was that NASA wanted to get a sequencing capacity sorted out
for the first trips to Mars with the idea that if there are similar
macromolecules to biological ones, something like a Nanopore sequencer
would be the correct way of assaying them. A little bit science fiction,
but sequencing in space on something like the ISS would have been
regarded as science fiction just 3 or 4 years ago. And it's happened.
So, maybe we should keep an open mind about the opportunity for
sequencing alien life on Mars.

![DBp-7TBUIAAfjf\_](https://monsterbashseq.files.wordpress.com/2018/01/dbp-7tbuiaafjf_-e1517449051603.jpg){.alignnone
.size-full .wp-image-4962 width="1159" height="737"}

(Slide from Matt Loose)