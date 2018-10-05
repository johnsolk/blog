Title: iPlant - Advanced workshop
Date: 2015-09-23 12:10
Author: monsterbashseq
Category: Linux, workshops
Slug: iplant-advanced-workshop
Status: published

"API for scalable science" - [Matt
Vaughn](https://www.tacc.utexas.edu/about/directory/matthew-vaughn),
[John Fonner](https://www.tacc.utexas.edu/about/directory/john-fonner)

https://pods.iplantcollaborative.org/wiki/display/Events/2015+09+21+iPlant+Workshops+at+UC+Davis

https://github.com/iPlantCollaborativeOpenSource/Advanced\_iPlant

slides:

https://docs.google.com/presentation/d/1RioNnjvL2qyRPQHSQ2-MG04m\_LwNzf9gGqHwsSpCguM/edit?usp=sharing

Install [Docker](http://docs.docker.com/mac/started/) (I'm running OSX.
See other instructions for Linux and Windows, although there were
challenges with Windows users in the workshop). Docker is solution to
binaries and configurations, etc. specific to hardware. Cool because
hardware goes out of date, need to move software to keep working. VM -
one way to backup and move software and storage - are snapshot of entire
operating system, big and heavy. Literally booting a computer. With
docker containers, all containers share kernel. Disk images layered.
(Provisionally based on Linux.) Coupled with services that allow
publishing images in layers. If wanting to automate server production,
can have orchestrated by Docker. Pull down base image, apache
installation. Platform as service, versionable. Integration between hub
and github and other public source control services. It is the recipe
for building a web server. Useful for sharing code and workflows between
people with different versions of software. Want Docker to follow recipe
so software worries can be solved behind the scenes, allowing people to
focus on using the software.

[![docker\_hellpworld](https://monsterbashseq.files.wordpress.com/2015/09/docker_hellpworld.png?w=300){.alignnone
.size-medium .wp-image-1234 width="300"
height="265"}](https://monsterbashseq.files.wordpress.com/2015/09/docker_hellpworld.png)

[iPlant](http://www.iplantcollaborative.org/ci/atmosphere) with [Agave
platform](http://preview.agaveapi.co/about/), moving to Docker. (Can
only be done on system you own. So, iPlant sysadmin will run this from
backend, but not users.) Integrates storage and computing into unified
environment and access all same way on web server available to public.

Idea is that "*Scientists, with a  few exceptions, are not trained
programmers*." "*Science is no longer done in a sandbox*." Meaning that
large interdisciplinary research needed to answer one question. Data not
all living in one place. Docker allows for programability. Security
issues, Docker will need to run user namespace  to allow users to run
custom Docker images.

[Interactive
Tour](https://github.com/iPlantCollaborativeOpenSource/Advanced_iPlant/blob/master/TOUR.rst)

Launch [Agave CLI](https://hub.docker.com/r/agaveapi/agave-cli/)
container:

[![Screen Shot 2015-09-22 at 4.47.47
PM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-22-at-4-47-47-pm.png?w=300){.alignnone
.size-medium .wp-image-1235 width="300"
height="114"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-22-at-4-47-47-pm.png)

Get authorization tokens with iPlant login account.

Storage systems avail, including ncbi - can edit to point to specific
directory location:

[![Screen Shot 2015-09-23 at 11.44.04
AM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-44-04-am.png?w=300){.alignnone
.size-medium .wp-image-1236 width="300"
height="184"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-44-04-am.png)

Look through api tools, e.g. files-list

[![Screen Shot 2015-09-23 at 11.59.57
AM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-59-57-am.png?w=300){.alignnone
.size-medium .wp-image-1238 width="300"
height="16"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-59-57-am.png)

did not work for ncbi:

[![Screen Shot 2015-09-23 at 11.57.41
AM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-57-41-am.png?w=300){.alignnone
.size-medium .wp-image-1237 width="300"
height="32"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-57-41-am.png)

Use this for advanced system management:

http://preview.agaveapi.co/documentation/tutorials/system-management-tutorial/

[![Screen Shot 2015-09-23 at 11.59.57
AM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-59-57-am.png?w=300){.alignnone
.size-medium .wp-image-1238 width="300"
height="16"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-11-59-57-am.png)

and list all iplant training files:

[![Screen Shot 2015-09-23 at 12.01.29
PM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-01-29-pm.png?w=300){.alignnone
.size-medium .wp-image-1239 width="300"
height="260"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-01-29-pm.png)

Make file and upload:

[![Screen Shot 2015-09-23 at 12.02.47
PM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-02-47-pm.png?w=300){.alignnone
.size-medium .wp-image-1240 width="300"
height="51"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-02-47-pm.png)

Permission bug with files creation and getting:

[![Screen Shot 2015-09-23 at 12.08.55
PM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-08-55-pm.png?w=300){.alignnone
.size-medium .wp-image-1241 width="300"
height="23"}](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-08-55-pm.png)

**Apps**, here are some: account-toolname-system-version-versionnum

![Screen Shot 2015-09-23 at 12.12.23
PM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-12-23-pm.png?w=181){.alignnone
.size-medium .wp-image-1243 width="181" height="300"}

Can do jobs template (see [tutorial under
'Jobs'](https://github.com/iPlantCollaborativeOpenSource/Advanced_iPlant/blob/master/TOUR.rst)).

Can search for name and get list of results:

![Screen Shot 2015-09-23 at 12.16.56
PM](https://monsterbashseq.files.wordpress.com/2015/09/screen-shot-2015-09-23-at-12-16-56-pm.png?w=300){.alignnone
.size-medium .wp-image-1244 width="300" height="72"}
