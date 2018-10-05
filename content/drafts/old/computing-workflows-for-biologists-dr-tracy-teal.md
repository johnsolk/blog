Title: Computing Workflows for Biologists - Dr. Tracy Teal
Date: 2016-07-31 15:33
Author: monsterbashseq
Category: Data Analyses, reproducibility, science, talks, workshops
Slug: computing-workflows-for-biologists-dr-tracy-teal
Status: published

I'm so excited to be visiting the
[Microbial Diversity Course](http://www.mbl.edu/microbialdiversity/) at
the [Marine Biological Lab](http://www.mbl.edu/) in Woods Hole,
Massachusetts right now. Really enjoying talking to students and faculty
working on projects related to microbial communities, aspects of
microbial metabolism, microbial genomics, transcriptomics. I'm here with
our
[lab](http://ivory.idyll.org/lab/)'s [MinION](https://www.nanoporetech.com/products-services/minion-mki)
to sequence genomes from cultured microorganisms isolated by students
during the course. (More about this in a future blog post!)

View of Eel Pond from MBL St.

https://www.flickr.com/photos/lpcohen/28584334686/

Each day of the
[course](https://twitter.com/hashtag/micdiv2016?src=hash&lang=en), there
are lectures in the morning on a variety of interesting topics relevant
to microbial diversity. For those not familiar, this field is rapidly
accumulating and analyzing large collections of data. For example,
see [Raza
and Luheshi (2016)](http://mgen.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.000046).

[Dr. Tracy Teal](https://twitter.com/tracykteal?lang=en), Executive
Director of [Data Carpentry](http://www.datacarpentry.org/) gave us an
inspiring talk this morning on data analysis, reproducibility and
sharing.

https://www.flickr.com/photos/lpcohen/28552189241/in/dateposted-friend/

Read her paper, which summarizes these topics:

[Shade and Teal. 2015. Computing Workflows for Biologists: A Roadmap.
PLoS
Biology. doi:10.1371/journal.pbio.1002303](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002303)

She raises a number of interesting points and gives good advice relevant
to the [growing amount of data in
biology](http://www.nature.com/nature/journal/v498/n7453/full/498255a.html), so
wanted to write them down to share here.

Dr. Teal opens with the question: "*How many people use computers for
your work?*" Everyone in the room raised their hand.

**We all use our computers for some aspect of our research.**

The reasons for using good practices for data management and computer
usage are not just for the greater good, but for ***you***. And your
sanity. We all appreciate how much data even one project can generate.
This is not going to change in the future. There is an upward trend of
data production over time. Thinking about this and planning now will
help the future you. Even if you rely on others for the bulk of the data
analysis.

"*How many of you work with other people?*" Everyone works in a team in
a lab and sometimes with outside collaborators. There is generally a
need to communicate with others about data analyses so that someone else
besides you can understand what you did. Paper reviewers and readers
should be able to understand. But first, there are the people in your
lab. This is called the "*leaving science forever*" test, where you ask
yourself whether what you are doing could be followed by someone else if
you were to suddenly leave. Have you ever taken over a project from
someone where you found files, samples and notebooks were not
descriptive enough for you to just pick up from where they left off?
Don't wait until this happens. The more transparent and vigilant you are
about this on a regular basis, the happier you will be in the future.

**What knowledge and elements are necessary for these good practices?**

**Metadata:**

1.  How were data generated?
2.  Where are raw data located? (e.g. HPLC files, \*.txt files, \*.fastq
    sequence files, microarray \*.cel files, etc)
3.  What were the data cleaning steps? (e.g. formatting steps between
    raw data and doing something interesting with software. This is
    actually a HUGE part of data analysis pipelines and can be &gt;80%
    of your work. If you can automate these steps, the better off you
    will be in the future.)
4.  Steps of the data analysis: exact parameters used, software versions
5.  Final plots and charts: This is the least important. If you keep
    track of the other steps, you should be able to recreate the exact
    plots very easily.

**Let's talk about data.**

Keep raw data files raw. Make copies of raw files before you start to
work with the data. Post these files somewhere public, in a place where
they will not be deleted. Why not make them public? If you don't want to
do that, put them in a safe lockbox, but where someone else can access
them if needed.

How many people have a data management plan? If a lab has a policy where
data have to be placed, besides someone's personal hard-drive, the
information will have a greater chance of surviving past the time when
people leave the lab.

**Let's talk about spreadsheets.**

*Have you ever done something in an Excel spreadsheet that made you
sad?* We all have. Single columns get resorted rather than whole sheet.
Autocorrecting spelling will change gene names. Dates get messed up. MS
Excel makes these formatting mistakes. Google sheets makes the same
formatting mistakes.

http://www.datacarpentry.org/spreadsheet-ecology-lesson/

**Train yourself to think like a computer.**

There are rules for using Excel. This may seem silly, but following
these rules will actually save you and collaborators much time. People
know spreadsheets. Many biologists use spreadsheets in a way that is
time-consuming in the long-run, e.g. laying out information to be read
for humans, with color-coding and notes.

Follow these simple rules:

-   Put each variable into a separate column
-   Do not use color to convey information. Add a "calibrated" column
    and a one- or two-word code associated, e.g. YES or NO, EXTRACTED or
    NOT, etc.
-   Do not use Excel data files to write out long metadata notes about
    your file. This is best to be saved in another README file.
-   Leave raw data raw. If you're going to transform data or perform a
    calculation, create a new file or a separate column(s)
-   Break data down into the finest scale resolution to give you the
    most options. Don't combine multiple types of information into one
    column, e.g. Species-Sex, Month-Year. One simple trick to avoid the
    annoying auto-formatting of dates in Excel: use three separate
    columns for month, date, year. This will allow you to look at date
    ranges, e.g. only fall, easily pull out years, or 15th of every
    month. Gives more flexibility!
-   Export your .xls into a .csv to avoid errors in downstream analyses

If you need more motivation for why it's a good idea train yourself to
follow these Excel rules, this is a great list of all the common errors
that spreadsheets can make:

http://www.datacarpentry.org/2015-05-29-great-plains/spreadsheet-ecology/02-common-mistakes.html

**Proceeding with analysis:**

Good data organization is the foundation for any project. Without this,
none of the actual meaningful aspects of the project will be easy or
efficient and data analyses will drag on and on.

1.  What is your motivation, overarching goal of analysis? To test
    hypotheses? Exploratory?
2.  Adopt automation techniques to reduce errors, which are iterative
    patterns that don't rely on human input
3.  Reproducibiltiy checkpoints
4.  Taking good notes
5.  Sharing responsibility, team approach

**Motivation**

Hopefully your experimental design was set up to motivate different
strategies, hypothesis-testing vs. exploratory. Write out each step of
the workflow by hand. Just asking yourself, "What am I going to do now?"
can help to guide a workflow.

**Reproducibility checkpoints, scrutinizing integrity of analyses:**

Modularize your workflow and set up checkpoints at certain points to
make sure you have what you expect. Does it actually work? Is the
outcome is consistent? (some programs have stochastic element) Do the
results make biological sense?

Examples of negative consequences for having problems with code and
research that is not reproducible:

fMRI results:

http://www.economist.com/news/science-and-technology/21702166-two-studies-one-neuroscience-and-one-palaeoclimatology-cast-doubt

Clinical genetics:

http://www.theatlantic.com/science/archive/2015/12/why-human-genetics-research-is-full-of-costly-mistakes/420693/

Unfortunately, there are probably many other examples... (I'm interested
in these, so please feel free to comment and share.)

Reproducibility and data management plans are now score-able in [grant
reviews](http://grants.nih.gov/reproducibility/index.htm) and [peer
review](https://gigascience.biomedcentral.com/articles/10.1186/s13742-015-0071-8). This
is starting to be valued more in the research community.

This is difficult. No one is perfect. You get to decide what your values
are. We have opportunities to set norms in our communities for what we
see.

**Take good notes**

Include this information:

-   Software version
-   Description of what software is doing/goal
-   What are the default options?
-   Brief notes on deviation  from default options
-   Workflows: Include a progression using different software (e.g.
    PANDAseq -&gt; QIIME --&gt; R). See Figure 1 from [Shade and
    Teal (2015)](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002303).
-   *ALL* formatting steps required to move between tools. (Write a
    tutorial for others. [This is a good
    example.](https://github.com/ttimbers/SKAT_NGS-2015/blob/master/NGS_GWAS_via_SKAT.md))
    Avoid manually formatting data. Ideally, a script will be written
    and made available to automatically re-format data.
-   Anything else that will help you remember what you did
-   Most important person to explain your process to is ***you*** in 6
    months. Unfortunately, you from 6 months ago will not answer email.
    If you need to re-do something, you need to remember what you did.

When writing a paper, go through your workflow again. Start from the
beginning and make sure you can do again what you thought you did. Make
sure you can reproduce. We rarely have the opportunity to do this with
lab work because it's too expensive. But we can do this with
computational analyses!

These things take time. It's easy to fling data everywhere. Being
organized takes time and is less easy. Value this.

**Shared responsibility**

Shared responsibility enhances reproducible workflows. Holding each
other accountable for high-quality results, confidence in results
promotes a strong sense of collaboration. Some general advice:

1.  Shared storage and workspace can facility access to all group data.
    Within a lab group, it is VERY common to have different computers
    (each lab member usually has one, for example). Institutional shared
    drives are maintained by administrators and occasionally need to be
    deleted to preserve space.
2.  No one is perfect.Not backing files up, or knowing where files or
    code are, are common mistakes. It happens. It's easy to throw hands
    up in the air and complain or shame each others' work habits related
    to all topics we're discussing here. [Shame is less
    productive](http://www.myscizzle.com/blog/rethinking-academic-culture/)
    than learning from mistakes, growing and discussing as a group. Use
    these opportunities to productively grow together. Few people have
    malicious intent. We're all people. Work together to make
    productive, positive changes.
3.  Talk to data librarians at institutions. (Advocate for starting such
    a position is this person does not exist.)
4.  Share data. [Dr. C. Titus Brown](http://ivory.idyll.org/blog/)
    advocates for publishing all pieces of data publicly on
    [figshare](https://figshare.com/). Half of peoples' problems with
    data stem from the desire to keep data private until publishing.
    This is usually &gt;3 yrs from time of collection. Then you can't
    find it. Or you spend too much time trying to make it "perfect".
    Publish the data as soon as you collect it. Then you can go back and
    improve data annotations. When you do a "data dump", your name will
    be associated with those data. Chances of people being malicious,
    wanting to steal your data are almost unheard of. (If you have
    examples, would be interesting to hear.) There is almost never a
    reason NOT to publish data as soon as it's collected. Publishing
    data as soon as it is collected is a great way to advertise what you
    are doing so others can collaborate or not go down the same avenue
    if unproductive.
5.  Join data working groups
6.  Using version control repositories for code and data analyses
    ([github](https://github.com/ljcohen))
7.  Set expectations for 'reproducibility checkpoints' with team
    "hackathons" or open-computer group meetings dedicated to analysis
8.  Lab paper reviews focused on data reproducibility
9.  Look for help/support outside the lab, e.g. bioinformatics or user
    group office hours, [Stack Overflow](http://stackoverflow.com/),
    [BioStars](https://www.biostars.org/). You are not alone. Few people
    are alone in wanting to learn things. We never can know
    everything, so talk to people.

Bioinformatics resources:

https://github.com/mblmicdiv/course2016/blob/master/bioinfo-resources.md

If you see a typo or problem with tutorials, please let people know. :)

Here is an exercise to try!

https://github.com/datacarpentry/2015-08-24-ISU/blob/gh-pages/lessons/00-intro-to-data-tidy.md

View of Eel Pond from Water St.

https://www.flickr.com/photos/lpcohen/28562219695/
