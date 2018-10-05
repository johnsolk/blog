Title: Bioboxes Demo at UC Davis
Date: 2015-11-09 14:47
Author: monsterbashseq
Category: Bioinformatics, workshops
Slug: bioboxes-demo-at-uc-davis
Status: published

[Michael Barton](http://www.bioinformaticszen.com/),
[JGI](http://jgi.doe.gov/) sequencing QA/QC group

https://www.flickr.com/photos/lpcohen/22487127088/

-   DNA sequencing
-   Evaluating scientific software
-   [Bioboxes](http://bioboxes.org/),
    [nucleotid.es](http://nucleotid.es/)

https://www.flickr.com/photos/lpcohen/22284282293/

Suggests reading [Malcom
McLean](https://en.wikipedia.org/wiki/Malcom_McLean) ([[The
Box](http://press.princeton.edu/titles/9383.html)]{style="text-decoration:underline;"}),
who implemented idea for standardized cargo containers. All you have to
do is load standard container from factory, fit onto truck, cargo ships,
and trains. Then unload. Created containerized globalization. Similar
concept to standardized containers for software, biobox:

Biobox f:fastq-&gt; assembly

Categorize Docker containers by their inputs and outputs, reads -&gt;
assembler -&gt; output assembly, pass data

Problem is really social, need suggestions for improvements from
community. Most agree that standards benefit everyone involved. We're
members of the community. Example that we all have a collection of
adapters for peripheral hardware, e.g. display and printers, keyboards,
etc. At some point, it's good to have standard adapters, e.g. USB (not
going to mention Mac thunder port)

Pass parameters to biobox, e.g. insert size

Develop a machine to make machines (tools to make tools), simliar to
software tools - standardized way to develop

Testing! Examples of tests to see whether they pass: Invalid format,
missing vresion numer, invalid version number, issing arguments, unknown
additional field, create contigs file, given valid input files, metadata
mounted

`pip install --user biobox_cli`

`biobox run`

`short_read_assembler \ bioboxes/velvet \ --input reads.fq.gz \ --output contigs.fa`

Tutorial, run through neat examples:

http://bioboxes.org/docs/how-to-install/

http://bioboxes.org/docs/example-biobox-use/

How to make a biobox? See workshop hackpad:

https://hackpad.com/Notes-from-the-Docker-hands-on-Nov-9-10-2015-olJpjzy4jCj

Demo repository:

https://github.com/bioboxes/identity
