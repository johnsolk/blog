Title: Downloading masses of files, useful ftp commands
Date: 2016-02-02 11:25
Author: monsterbashseq
Category: Linux
Slug: downloading-masses-of-files-useful-ftp-commands
Status: published

You have finished a sequencing project and now your sequencing facility
is sending you lots of files! You're eager to see your results. Your
facility sends you a link with files displayed on a website. Now what
are you supposed to do?

First, log in to your hpc server (AWS or HPC cluster) where you will
work with the files.

Depending on the type of server where your files have been made
available (ftp or http), try these commands:

If **ftp** server, with user and password required:

    wget -r --user XXX --password XXX ftp://1234.5678.10

You can also log in to the ftp server, navigate and change directories,
then **mget** to [copy multiple files from the remote server to your
local server](https://www.cs.colostate.edu/helpdocs/ftp.html).
(Although, this will sometimes take longer than wget for some reason.)
(The -P 2121 is optional, leave it out if you don't know the port.)

``` {.p1}
ncftp -u XXX -p XXX -P 2121 server.server.edu
cd /path/to/files
ls
mget *
```

If **http** or **https** server, with user and password. The  -r is
recursive, -l1 is only level 1, and --no-parent means no files up.
(These stop wget from automatically downloading files linking files
being downloaded, which can happen with websites.)

    wget -r -l1 --no-parent --user=user --password=password http://server.server.edu/path/to/files/

With no user or password required:

    wget -r -l1 --no-parent --no-check-certificate https://server.server.edu/path/to/files

Most facilities are friendly and will help you download your files. In
some cases, they will provide temporary **ssh** access, but other times
not. It depends on the facility. If you don't know the name of the
**ftp** or **http** server, or the directory where the files are
located, write to them and ask.

[Thanks to Luiz Irber and Dragos Scarlet for the help and motivation for
working through this problem. :)]{.s1}
