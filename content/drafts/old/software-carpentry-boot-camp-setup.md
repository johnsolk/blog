Title: Software Carpentry Boot Camp, setup
Date: 2013-11-13 20:15
Author: monsterbashseq
Category: Linux, Python, software, Software Carpentry, Ubuntu
Slug: software-carpentry-boot-camp-setup
Status: published

[Setup instructions](http://wltrimbl.github.io/2013-11-14-woodshole/)
for the [Software Carpentry Boot
Camp](http://software-carpentry.org/bootcamps/2013-11-14-whoi/index.html)
at [Woods Hole Oceanographic
Institution](http://www.nefsc.noaa.gov/nefsc/woodshole/) from 14-15 Nov.
I'm really looking forward to this Boot Camp and setting up something
similar at HBOI.

I already have the Linux command terminal, a text editor, and Python
IDLE. The workshop will be using Python version 2.7. While I use Python
IDLE version 3.3, I'm unsure of whether this will be ok. I've heard this
before, that people still use Python version 2 for things, and I don't
understand why. I will have to ask tomorrow. Python version 3.3 is the
latest. There are syntax differences between the two versions, *e.g.*
print foo vs. print(foo).

I did have to [install
git](https://www.digitalocean.com/community/articles/how-to-install-git-on-ubuntu-12-04). 
I'm a little fuzzy on the concept of git, which I'm looking forward to
learning more about tomorrow. This fuzziness is even despite [my own
github account](https://github.com/ljcohen). Github is, coincidentally,
the subject of a [blog post this week on Molecular
Ecologist](http://www.molecularecologist.com/2013/11/using-github-with-r-and-rstudio/).

    flcellogrl@flcellogrl:~$ sudo apt-get install git-core
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following packages were automatically installed and are no longer required:
      libcurl3-nss libnspr4-dev libnss3-dev libssl-dev libssl-doc
      linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic
      linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
    Use 'apt-get autoremove' to remove them.
    The following extra packages will be installed:
      git git-man liberror-perl
    Suggested packages:
      git-daemon-run git-daemon-sysvinit git-doc git-el git-arch git-cvs git-svn
      git-email git-gui gitk gitweb
    The following NEW packages will be installed:
      git git-core git-man liberror-perl
    0 upgraded, 4 newly installed, 0 to remove and 12 not upgraded.
    Need to get 7,417 kB of archives.
    After this operation, 17.3 MB of additional disk space will be used.
    Do you want to continue [Y/n]? y
    Get:1 http://us.archive.ubuntu.com/ubuntu/ raring/main liberror-perl all 0.17-1 [23.8 kB]
    Get:2 http://us.archive.ubuntu.com/ubuntu/ raring/main git-man all 1:1.8.1.2-1 [653 kB]
    Get:3 http://us.archive.ubuntu.com/ubuntu/ raring/main git i386 1:1.8.1.2-1 [6,739 kB]
    Get:4 http://us.archive.ubuntu.com/ubuntu/ raring/main git-core all 1:1.8.1.2-1 [1,392 B]
    Fetched 7,417 kB in 5min 13s (23.7 kB/s)                                       
    Selecting previously unselected package liberror-perl.
    (Reading database ... 438507 files and directories currently installed.)
    Unpacking liberror-perl (from .../liberror-perl_0.17-1_all.deb) ...
    Selecting previously unselected package git-man.
    Unpacking git-man (from .../git-man_1%3a1.8.1.2-1_all.deb) ...
    Selecting previously unselected package git.
    Unpacking git (from .../git_1%3a1.8.1.2-1_i386.deb) ...
    Selecting previously unselected package git-core.
    Unpacking git-core (from .../git-core_1%3a1.8.1.2-1_all.deb) ...
    Processing triggers for man-db ...
    Setting up liberror-perl (0.17-1) ...
    Setting up git-man (1:1.8.1.2-1) ...
    Setting up git (1:1.8.1.2-1) ...
    Setting up git-core (1:1.8.1.2-1) ...

As a side note, I think that the [Software
Carpentry](http://software-carpentry.org/index.html) concept and
[team](http://software-carpentry.org/team.html) are incredibly  cool.
This is a non-profit organization comprised of a multidisciplinary team
of instructors (University professors, graduate students, software
professionals) who are involved with software at various levels. The aim
is to train post-graduate scientists in computing skills to get us to
where we need to be: programming and using advanced computing tools in
our research to help with big data needs. I would love to be a part of
this as an instructor someday, if I can ever get my skills to a level
where they should be!

I was reading their
[blog](http://software-carpentry.org/blog/index.html), and some of their
developers posted an interesting report from a project they're working
on with [PLOS Computational Biology](http://www.ploscompbiol.org/) and
partners at Mozilla looking into [code published in scientific
literature](http://mozillascience.org/code-review-for-science-what-we-learned/).
