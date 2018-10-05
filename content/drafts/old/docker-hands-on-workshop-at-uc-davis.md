Title: Docker hands-on workshop at UC Davis
Date: 2015-11-09 11:29
Author: monsterbashseq
Category: Bioinformatics, workshops
Slug: docker-hands-on-workshop-at-uc-davis
Status: published

[Dr. C. Titus Brown](http://ivory.idyll.org/lab/), [Docker hands-on
workshop at UC
Davis](http://dib-training.readthedocs.org/en/pub/2015-11-09-docker.html)

[Lots of workshops available at
UCD](http://dib-training.readthedocs.org/en/pub/), open to everyone and
free! (sign up, as max capacity is 40) Entry and intermediate levels
available. [Data Science Initiative](http://datascience.ucdavis.edu/) is
a hub for data science on campus with space available for workshops in
the library at UC Davis, which is where we are located today! All
materials are CC0, feel free to re-package and use for your own purposes
and workshops.

Check out training organizations, [Data
Carpentry](http://www.datacarpentry.org/) and [Software
Carpentry](https://software-carpentry.org/) programming software
development and data science, short two-day local workshops available
internationally, beginner to intermediate skills.

Also available: [Michael Barton](http://www.bioinformaticszen.com/) from
[DOE-](http://jgi.doe.gov/automating-selection-process-genome-assembler/)[JGI](http://jgi.doe.gov/automating-selection-process-genome-assembler/)
lead on [bioboxes](http://bioboxes.org/) and
[nucleotid.es](http://nucleotid.es/)

=========

Materials for today:

https://github.com/ngs-docs/2015-nov-docker

Intro:

https://github.com/ngs-docs/2015-nov-docker/blob/master/docker-intro.rst

Launch EC2 m3.xlarge instance (15 GB RAM, 4 cores and 2x40 SSD, renting
around \$0.12/hr), install stuff. Log out, log back in.

[Docker](https://www.docker.com/) containers are lightweight, can grow
and shrink in ways VMs cannot. Access-level sandbox. Philosophy of
community-level and light-weight is appealing in the sense that it's
accessible.

[![docker](https://monsterbashseq.files.wordpress.com/2015/11/docker.png?w=300){.alignnone
.size-medium .wp-image-1461 width="300"
height="173"}](https://www.docker.com/)  
Need host environment. Docker runs natively on linux os. We'll use AWS
to install Docker. Almost all workshops available through [dib
lab](http://dib-training.readthedocs.org/en/pub/) are via AWS, minimizes
problems dealing with local hardware. Instructions
[here](http://angus.readthedocs.org/en/2015/amazon).

Ubuntu 14.04 LTS, downstream of Debian, Long-term Support (LTS) for 5
years (until 2019). So, all materials here should be stable until then.

Get it all working first by copy-pasting commands directly from
tutorial. (You'll learn less this passive way, but then make sure to go
back later and change things up to see what happens. This will increase
understanding.)

Main idea is that you need to download and run Docker as root.
(Exceptionally bad idea to do, in general! We're assuming we can trust
Docker at this point, but usually we encourage to be more skeptical of
downloading things from websites and running as root.) Need root
privileges. (Some HPC systems will not grant users root privaleges.
Docker cannot be run in this case.) Nice thing about AWS is if you screw
something up, running as root, we're deleting the instance anyway. Get
docker running, prompt will change (this is bash prompt inside Docker
container, mostly isolated from host operating system):

[![rundocker](https://monsterbashseq.files.wordpress.com/2015/11/rundocker.png?w=300){.alignnone
.size-medium .wp-image-1462 width="300"
height="26"}](https://monsterbashseq.files.wordpress.com/2015/11/rundocker.png)

Host accommodates many Docker containers, which each have their own file
systems. Uses host hardware. Dependent on the size of the machine. If
you have Mac/Windows configured with Linux VM, then the Docker will be
dependent on the hardware designated for the VM. [Docker
Machine](https://docs.docker.com/machine/) allows a backend memory
allocation. Everything you did in the Docker, when you exit, Docker is
deleted. It's accessible again only if you know what your'e looking
for. New fresh Docker container starts each time. If you want to spin up
Docker containers all running web server, Docker is awesome for that.
For bioinformatics workflows, not main customer base for Docker, this is
not well worked out, much less supported with little infrastructure
existing. Titus' idea is to scale out, move computing to data rather
than move data to computing. With Docker containers, can spinning up
software processing &gt;1 TB datasets (don't use shared file systems),
using many EBS volumes, many EC2 instances. You could feasibly install
and run individual software programs in separate Docker containers, e.g.
trimmomatic (java) and megahit (assembly) which might have
incompatibilities and periodic updates.

[![docker](https://monsterbashseq.files.wordpress.com/2015/11/docker1.png?w=300){.alignnone
.size-medium .wp-image-1463 width="300"
height="96"}](https://monsterbashseq.files.wordpress.com/2015/11/docker1.png)

https://twitter.com/ctitusbrown/status/663791278560141312

Get data and put on host, not on Docker (since you want to run the
Docker on the data. Bring the computing to the data, rather than the
other way around). Then, run the docker container, run the assembly
program command from within the container, exit. And the resulting data
from the assembly after it's finished are on the host!!!! SUPER COOL!!!!
:)

[![megahit\_docker](https://monsterbashseq.files.wordpress.com/2015/11/megahit_docker.png?w=300){.alignnone
.size-medium .wp-image-1464 width="300"
height="247"}](https://monsterbashseq.files.wordpress.com/2015/11/megahit_docker.png)

Actually, you can run this all piped into one command, without having to
run the docker command separately from the program command.

    docker run -v /home/ubuntu/data:/mydata   
      -it megahit_ctr   
   sh -c '/home/megahit/megahit --12 /mydata/*.pe.fq.gz
                         -r /mydata/*.se.fq.gz
                         -o /mydata/ecoli -t 4'

Or, you can write a bash shell script (see tutorial), then run the
script.

Create Dockerfile, which can be version controlled. When encoding the
commands in a Dockerfile, each RUN command is a layer of the Dockerfile.
Try to include as many commands in one RUN command as possible, to
create less layers. None of this has to be repeated, once the Dockerfile
has been created and pushed to the [Docker
hub](https://hub.docker.com/) (`docker login`,
`docker build -t titus/megahit .`, and `docker push titus/megahit)`. All
you have to do is get the Dockerfile, install Dockerfile, know where
your data are, and run!!!

Do challenge exercises:

https://github.com/ngs-docs/2015-nov-docker/blob/master/challenge-exercises.rst
