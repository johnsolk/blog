Title: UC Davis Docker workshop, live-coding
Date: 2015-11-10 11:53
Author: monsterbashseq
Category: workshops
Slug: uc-davis-docker-workshop-live-coding
Status: published

For the second day of the UC Davis [Docker
workshop](http://dib-training.readthedocs.org/en/pub/2015-11-09-docker.html),
[Dr. Titus Brown](http://ivory.idyll.org/blog/) initiates a "teach-me"
session on how to make a Docker container. He will live-code and we will
tell him what to write. The idea is to package software he knows well,
e.g. [khmer](https://github.com/dib-lab/khmer) into a Docker container,
run the Dockerfile successfully, and upload to [Docker
hub](https://hub.docker.com/u/diblab/).

This really highlights the beauty of Docker. One of the most
time-consuming aspects of open-source software is installing and getting
it to work. There are many dependencies and sometimes version updates
with dependencies can conflict with dependencies of other software.
Docker containers install dependencies in [one fell
swoop](https://en.wiktionary.org/wiki/one_fell_swoop) and run the
software in isolation from other software with separate dependencies.

[Hackpad](https://hackpad.com/Notes-from-the-Docker-hands-on-Nov-9-10-2015-olJpjzy4jCj)

Titus' github [repo](https://github.com/ctb/2015-docker-building)

Start EC2 instance, m3.xlarge, [install and run
Docker](https://github.com/ngs-docs/2015-nov-docker/blob/master/docker-intro.rst) (don't
forget to log out then log back in again)

While editing `Dockerfile`, have two windows with the same instance
open: 1.) Docker is running, 2.) instance shell to figure stuff out

Tricky part is figuring out what dependencies are required for install,
can use `ENV PACKAGES` and `ENV VERSION`. Fill in `{PACKAGES}` and
`{VERSION}`, see if they work, then will have completed `Dockerfile` for
running.

Then, write script `build_test.sh` to run with set of test data to see
if Dockerfile works.

`git clone https://github.com/ctb/2015-docker-building.git cd 2015-docker-building/khmer/ bash run_test.sh`

Works, so cool!!

[![khmer\_docker](https://monsterbashseq.files.wordpress.com/2015/11/khmer_docker.png?w=300){.alignnone
.size-medium .wp-image-1478 width="300"
height="294"}](https://monsterbashseq.files.wordpress.com/2015/11/khmer_docker.png)

Now, Figure out how to upload to Docker hub.

http://docs.docker.com/engine/userguide/dockerrepos/

`docker tag diblab/khmer:2.0 diblab/khmer:latest`

Puts the image here:

https://hub.docker.com/r/diblab/khmer/

Now, anyone can run:

`docker pull diblab/khmer`

Yay!

This took 1.5 hrs.

Also, [salmon](https://github.com/COMBINE-lab/salmon) and [dammit](https://github.com/camillescott/dammit).

dammit has database files, which are big-ish (\~GB): options for these:

1.  include db files in image (BAD because image is big and not shared
    between containers)
2.  download each time (BAD because slow and not shared between
    containers, goal with large dataset is that we want to share between
    containers)
3.  **\*\*\* want to do this \*\*\* create data volume within Docker, an
    image that is just detachable, configured disk space, download files
    once and then share forever (downside is accessible only in docker
    files system)**
4.  local disk (a. download, b. mount each time, BAD because local file
    system is required, not independent and sometimes doesn't work)

