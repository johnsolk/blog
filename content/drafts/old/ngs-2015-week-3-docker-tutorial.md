Title: NGS 2015 Week 3 - Docker Tutorial
Date: 2015-08-24 16:45
Author: monsterbashseq
Category: Bioinformatics, Computational Biology, Genomics Workshop, Linux
Slug: ngs-2015-week-3-docker-tutorial
Status: published

Here at MSU's [W.K. Kellogg Biological Station](http://www.kbs.msu.edu/)
for the 3rd week of NGS 2015 workshop by [Dr. C. Titus
Brown](http://ivory.idyll.org/blog/) from UC Davis and a wealth of
[superstar
instructors](https://twitter.com/ctitusbrown/status/636228826201235457).
This week is intended for advanced bioinformatics users and alum of the
course to 1.) be a practice audience for new lessons and 2.) push our
bioinformatics toolkits to a new level.

https://www.flickr.com/photos/lpcohen/20250815668/

All tutorials are publicly available on this site:

http://angus.readthedocs.org/en/2015/week3.html

Super excited to be here to learn some new bioinformatics techniques and
also learn how these expert instructors explain complex instructions to
newbies like me. :)

Here is schedule from the first 2 weeks of beginning level:  
http://angus.readthedocs.org/en/2015/

-----------

Today's tutorial is on [Docker](https://www.docker.com/)! I have been
interested in this for several months now, from interest in *de
novo *transcriptome and genome assembly benchmarking with this site:

http://nucleotid.es/

and Titus Brown's blog posts:

http://ivory.idyll.org/blog/tag/benchmarking.html

http://ivory.idyll.org/blog/2015-docker-and-replicating-papers.html

**Here is the tutorial:**

https://github.com/ngs-docs/angus/blob/2015/week3/CTB\_docker.rst

https://www.flickr.com/photos/lpcohen/20859065351/

Docker is an alternative to virtual machines, since 2013 has been
popular. Solves some problems including software installation and
versions. Does it solve problems for research and training? Commands in
tutorial should work, just need to undestand concepts.

Let's say you want to install a new software package to use. What do you
do? Problem of spend 3 days installing stuff. Everything breaks when you
update one thing for one software or for another reason. Standard
problem with teaching students, who show up with different OS and
hardware. Can start virtual machine simulation of another computer to
run inside. But limited, cannot run bigger computer and then have
different GUI to deal with. Instead, Docker is isolated lightweight
containers. Can run several as processes, only take up as much memory as
they need, can run from different OS, isolated. Problems solved with
tech work with databases, web servers, etc. We are interested in Docker
because scientific computing can benefit from reproducibility.
Publications can provide Docker containers including software and data
to send to people with instructions and allow other people to make
things happen, build on, etc. This promotes collaboration. Can send
analyses and data and software to people, don't require everyone to have
the same hardware.

Super Cool.

Steps:

1.  Launch EC2 instance. (Cloud cheaper option than buying new hardware.
    Rent what you use, don't pay when you don't need it. Amazon images
    are larger than local computer hardware.) Today's tutorial will use
    7 GB of memory. This is sometimes more than peoples' computers, so
    we use an Amazon (AWS) EC2
    image. http://angus.readthedocs.org/en/2015/amazon/index.html
2.  Get Docker, run as root user. You are now running a container within
    AWS EC2 instance.
3.  Update and install stuff on docker container. Porosity is user
    defined. Can get out to internet by default. No way for network to
    get into container, unless configured.
4.  Save docker image by typing 'hostname'. Keep this host code.
5.  Save image by commit command with hostname:  
   ![docker\_login\_logout](https://monsterbashseq.files.wordpress.com/2015/08/docker_login_logout1.png?w=660){.alignnone
    .size-large .wp-image-1000 width="660" height="115"}
6.  Add containers and run as needed.
7.  If you want to use data from outside container, mount data as
    symlink, mirrored data:

        docker run -v /home/ubuntu/data:/data   
          -it megahit

8.  Log back in to docker image, then your data will be there: ls /data
9.  Now you can run the megahit assembly software you installed on the
    docker image with the data you
    mounted.[![docker\_data\_mount](https://monsterbashseq.files.wordpress.com/2015/08/docker_data_mount.png?w=660){.alignnone
    .size-large .wp-image-1001 width="660"
    height="309"}](https://monsterbashseq.files.wordpress.com/2015/08/docker_data_mount.png)
10. Now, output data from megahit assembly will be saved (because
    of symlink) on EC2 instance at

        /home/ubuntu/data

    <p>
    [![megahit\_output](https://monsterbashseq.files.wordpress.com/2015/08/megahit_output.png?w=660){.alignnone
    .size-large .wp-image-1002 width="660"
    height="179"}](https://monsterbashseq.files.wordpress.com/2015/08/megahit_output.png)

11. Now you can write a script to both install, download, and run the
    software.

Note, docker is a security vulnerability hole between image and host
computer files. Some HPC systems will not let you run Docker because of
this.

Docker runs in a similar way to github with an account:
https://hub.docker.com/  
If you want to pull a public Dockerfile, just install docker. It will
find script.  
https://hub.docker.com/r/titus/megahit/

Sensible defaults. All you need is Dockerfile to make new docker image.
Install docker, also need script to run. Docker image will run with
local hardware. (Floating point numbers on different systems could lead
to slightly different results.)

https://www.flickr.com/photos/lpcohen/20852912655/

Do challenge exercises.

**Super cool new commandline tricks**:

    cat < do-assemble.sh
    #! /bin/bash
    rm -fr /data/ecoli
    /home/megahit/megahit --12 /data/*.pe.fq.gz   
                        -r /data/*.se.fq.gz    
                        -o /data/ecoli -t 4
    EOF

    Ctrl-R

when typing commands, e.g. 'docker' will search history and show you
last command with 'docker', again will show previous, etc.

Critical evaluations of Docker:

http://txt.fliglio.com/2015/07/containers-and-cfg-mgmt/

http://www.boycottdocker.org/
