Title: How to install linux software without root privileges
Date: 2016-01-24 23:51
Author: monsterbashseq
Category: cluster, High Performance Computing, Linux, software
Slug: how-to-install-linux-software-without-root-privileges
Status: published

HPC cluster users rarely have root privileges for installing new
software. Default location for installation is usually /usr/bin/, but
our user directories are usually located somewhere else like
/home/ljcohen/ or /mnt/home/ljcohen/. So, what are you supposed to do
when you need to use a new software package? You can contact your
cluster sysamins to have them install the package cluster-wide. In
general, it's a good idea to be in contact with them. (Usually they're
nice, helpful, and like to hear from their users to learn more about how
you're using the cluster.) But, sometimes you just want to try something
out to see if it's useful. Here is how.

I wanted to install [samstat](http://samstat.sourceforge.net/). (btw, I
don't mean to single out samstat. This is just what I happened to be
trying out today. And it was a relatively easy fix!)

The first step is to download the installation file by grabbing the
latest version available through the [software's
website](http://sourceforge.net/projects/samstat/):

<http://downloads.sourceforge.net/project/samstat/samstat-1.5.1.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fsamstat%2F&ts=1453702634&use_mirror=iweb>

But, notice how this web address is longer than it needs to be. This is
because sourceforge.net puts on the extra stuff at the end you don't
need.  You could first download this file to your local harddrive then
transfer the file onto your cluster account. But, the easiest thing is
the wget command and download the file directly into your linux cluster
environment.

Right-click on the "Direct Link", select "Copy Link Address" from the
menu, then manually delete everything after the filename:

![samstat\_download](https://monsterbashseq.files.wordpress.com/2016/01/samstat_download.png){.alignnone
.size-full .wp-image-1974 width="1280" height="223"}

Create and keep a directory where you will download and install all of
your local software. I keep software in .local. Navigate to that
directory and download the file. Use this command:

    wget http://downloads.sourceforge.net/project/samstat/samstat-1.5.1.tar.gz

If you follow the [installation
instructions](http://samstat.sourceforge.net/#install) exactly, you will
get a few errors:

![tar\_err](https://monsterbashseq.files.wordpress.com/2016/01/tar_err.png){.alignnone
.size-full .wp-image-2023 width="1228" height="123"}

![make\_clean](https://monsterbashseq.files.wordpress.com/2016/01/make_clean1.png){.alignnone
.size-full .wp-image-2028 width="770" height="65"}

By looking at the README file, there are slightly different instructions
compared to the website:

![samstat](https://monsterbashseq.files.wordpress.com/2016/01/samstat.png){.alignnone
.size-full .wp-image-1985 width="1234" height="507"}

After decompressing the .tar.gz file, the next command ./configure
results in "self tests run under valgrind" not passing:

![configure](https://monsterbashseq.files.wordpress.com/2016/01/configure.png){.alignnone
.size-full .wp-image-2038 width="452" height="1125"}

I decided to keep going and see what would happen. Running the next
command 'make' appears fine:

![make](https://monsterbashseq.files.wordpress.com/2016/01/make.png){.alignnone
.size-full .wp-image-2042 width="1500" height="783"}

Even 'make check' passes all the tests:

![make\_check](https://monsterbashseq.files.wordpress.com/2016/01/make_check.png){.alignnone
.size-full .wp-image-2047 width="1049" height="1125"}

The executable file 'samstat' is in the appropriate directory. It
appears everything is fine:

![src](https://monsterbashseq.files.wordpress.com/2016/01/src.png){.alignnone
.size-full .wp-image-2051 width="971" height="1105"}

However, the final command 'make install' has a problem:

![makeinstall](https://monsterbashseq.files.wordpress.com/2016/01/makeinstall.png){.alignnone
.size-full .wp-image-2055 width="1500" height="591"}

There is a problem creating a file in /usr/local/bin/samstat with
"Permission denied". This directory does not belong to me, and I don't
have privileges to write there.

From experience, I know that I need to tell the installation process
where to install files so it does not try in the default location.

But how do I know this?

When faced with errors, knowing what to use as a Google search string
can be a challenge. When I used the exact error "cannot create regular
file", [the results were not very
helpful](https://www.google.com/search?q=cannot+create+regular+file).
(at least for me)

This is what I used: ["make install without root
privileges"](https://www.google.com/search?q=make+install+without+root+privileges).

[The most helpful page for me was a post on the Biostars
forum](https://www.biostars.org/p/104605/).

To undo the failed installation attempt, all you have to do is delete
the directory with rm -rf. But remember to keep the compressed tar file!

![rm](https://monsterbashseq.files.wordpress.com/2016/01/rm.png){.alignnone
.size-full .wp-image-2069 width="1320" height="799"}

Then start over. Finally, I managed to get it right! Here are the
working commands I used:

    tar -zxvf samstat-1.5.1.tar.gz
    cd samstat-1.5.1/
    ./configure --prefix=/home/ljcohen/.local
    make
    make check
    make install

And it works!

![samstat\_working](https://monsterbashseq.files.wordpress.com/2016/01/samstat_working.png){.alignnone
.size-full .wp-image-2014 width="1106" height="261"}

Don't forget to add this working directory to your \$PATH.

 

When you get something to work, it feels good. :) While all of your
commands are saved in your history. Don't forget to keep a log of what
you've done and how to fix it so that your future self can remember when
this happens again.

[![future\_self](https://monsterbashseq.files.wordpress.com/2016/01/future_self.png){.alignnone
.size-full .wp-image-2113 width="280"
height="462"}](https://xkcd.com/1421/)
