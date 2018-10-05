Title: WHOI Software Carpentry notes, Day 1 - morning
Date: 2013-11-14 12:23
Author: monsterbashseq
Category: Linux, Python, software, Software Carpentry, Ubuntu
Slug: whoi-software-carpentry-notes-day-1
Status: published

    cd ; git clone http://github.com/wltrimbl/2013-11-14-woodshole

Copying workshop files.

    http://wltrimbl.github.io/2013-11-14-woodshole/
    http://wltrimbl.github.io/2013-11-14-woodshole/lessons/overview.html#%284%29

Scientists are teaching ourselves. Need to learn the tricks the right
way to save time later.  
Be fluent in multiple languages.  
Worth the effort. You will have tricks to use for years.  
Learn other peoples' libraries. Saves time the long run.  
If you find yourself copying and pasting a lot, that is an opportunity
to write a script.  
Commonly used blocks of code, e.g. opening files, etc. are best to put
into functions and use again.  
Group commonly-used functions into libraries.  
Share code with others.  
Writing less code, doing more things with fewer lines, is always a good
thing.  
Need good protocol for backing up data. You will make mistakes.  
Use version control for collaboration.  
Document.  
Every time you write a function, document, what is it for, file inputs,
so you don't hold yourself in contempt. Save every piece of code.
Annotation for versions of pieces of code.  
Aim for reproducibility.  
One of the most valuable things you can do in writing scientific code is
finding another person to read your code. This helps to eliminate
errors. A second pair of eyes will help uncover errors, e.g. reading in
wrong files, etc.  
http://wltrimbl.github.io/2013-11-14-woodshole/lessons/overview.html\#%2843%29  
Geeks recognize that scale of problem needs a function.  
Let the net do your debugging. Other people will notice your mistakes.
Share your code. Collaborate with your coding.

Invitation to Software Carpentry, sent out to potential instructors,
oceanographic community.  
Try to take high level lessons and show tools to solve our own problems.
how to make hard things easier. At the end of 2 days, some things should
go more efficiently.

Unix vs. Linux - historical, Linux open source after 1990s, based on
UNIX (copyright by AT&T/Bell)

Help each other to solve your problems. Help your neighbors.

Basic Commands  
http://wltrimbl.github.io/2013-11-14-woodshole/lessons/ref/shell.html  
cd in commands take you to home directory  
pwd: full path

linux commands take options, flags introduced with "-"  
man ls  
ls -l -t - r  
same as  
ls -lrt  
same as  
ls -l -reverse -t

first part of entry:  
d = directory  
- = file  
read, write, execute permission = rwx  
first set is user, then others

../  
(up one director, down another directory)

Shell is a programming language with variables, variables have \$in
front  
\$ echo \$0

name of shell program = bash

This will return what you are running.  
print command = echo

Different flavors of shells.

Shells sit atop kernels.

Kernel is always running on Linux machines.  
The shell is a different program that makes calls into program. Shell
decides prompts, reads commands. (insert video.) There are many
shells/Python/instances going on at the same time.  
Common kernel takes orders and shuffels and deals them out.

Artificial data. Half million people with cochlear implants.

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ ls
    alexander  bert  frank_richard  gerdal  jamesm  lawrence  thomas

Type in a partial command, then hit tab, it will auto fill-in files it
finds with that name, if it doesn't work, hit tab twice, and it will
list all files with that file beginning. Help with file-name
conventions.  
[![Screenshot from 2013-11-14
10:38:57](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-14-103857.png?w=300){.alignnone
.size-medium .wp-image-591 width="300"
height="189"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-14-103857.png)  
Find data with missing values.

ls -R

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ ls -R
    .:
    alexander  bert  frank_richard  gerdal  jamesm  lawrence  thomas

./alexander:  
data\_216.DATA  data\_297.DATA  data\_347.DATA  data\_415.DATA 
data\_473.DATA  data\_547.DATA  
data\_242.DATA  data\_305.DATA  data\_357.DATA  data\_420.DATA 
data\_498.DATA  data\_548.DATA  
data\_256.DATA  data\_306.DATA  data\_364.DATA  data\_421.DATA 
data\_502.DATA  data\_550.DATA  
data\_262.DATA  data\_309.DATA  data\_379.DATA  data\_427.DATA 
data\_516.DATA  data\_560.DATA  
data\_268.DATA  data\_318.DATA  data\_387.DATA  data\_434.DATA 
data\_527.DATA  
data\_277.DATA  data\_337.DATA  data\_389.DATA  data\_454.DATA 
data\_530.DATA  
data\_278.DATA  data\_339.DATA  data\_397.DATA  data\_462.DATA 
data\_536.DATA  
data\_288.DATA  data\_344.DATA  data\_402.DATA  data\_469.DATA 
data\_542.DATA  
data\_292.DATA  data\_346.DATA  data\_408.DATA  data\_471.DATA 
data\_546.DATA

./bert:  
audioresult-00215  audioresult-00304  audioresult-00359 
audioresult-00443  audioresult-00497  
audioresult-00222  audioresult-00317  audioresult-00372 
audioresult-00445  audioresult-00518  
audioresult-00223  audioresult-00319  audioresult-00377 
audioresult-00451  audioresult-00521  
audioresult-00235  audioresult-00320  audioresult-00380 
audioresult-00453  audioresult-00532  
audioresult-00239  audioresult-00321  audioresult-00384 
audioresult-00460  audioresult-00534  
audioresult-00246  audioresult-00330  audioresult-00386 
audioresult-00466  audioresult-00535  
audioresult-00265  audioresult-00332  audioresult-00393 
audioresult-00470  audioresult-00557  
audioresult-00267  audioresult-00350  audioresult-00412 
audioresult-00472  
audioresult-00270  audioresult-00353  audioresult-00416 
audioresult-00490  
audioresult-00286  audioresult-00355  audioresult-00422 
audioresult-00493

./frank\_richard:  
data\_212  data\_252  data\_285  data\_329  data\_398  data\_433 
data\_479  data\_507  data\_538  
data\_221  data\_254  data\_291  data\_366  data\_404  data\_436 
data\_491  data\_508  data\_540  
data\_224  data\_258  data\_295  data\_378  data\_405  data\_439 
data\_494  data\_512  data\_545  
data\_233  data\_259  data\_316  data\_381  data\_417  data\_444 
data\_500  data\_519  data\_555  
data\_237  data\_272  data\_323  data\_385  data\_428  data\_461 
data\_503  data\_533  NOTES  
data\_247  data\_273  data\_327  data\_388  data\_429  data\_477 
data\_504  data\_537

./gerdal:  
Data0211  Data0238  Data0269  Data0324  Data0370  Data0426  Data0495 
Data0541  Data0559  
Data0218  Data0240  Data0279  Data0331  Data0407  Data0446  Data0499 
Data0543  
Data0220  Data0243  Data0283  Data0338  Data0409  Data0458  Data0505 
Data0549  
Data0227  Data0245  Data0294  Data0342  Data0413  Data0459  Data0520 
Data0551  
Data0229  Data0250  Data0307  Data0356  Data0414  Data0468  Data0523 
Data0552  
Data0230  Data0257  Data0308  Data0365  Data0419  Data0486  Data0528 
Data0556  
Data0232  Data0263  Data0311  Data0367  Data0424  Data0487  Data0529 
Data0558

./jamesm:  
data\_217.txt  data\_261.txt  data\_312.txt  data\_375.txt 
data\_474.txt  data\_509.txt  
data\_219.txt  data\_264.txt  data\_325.txt  data\_383.txt 
data\_475.txt  data\_510.txt  
data\_226.txt  data\_266.txt  data\_326.txt  data\_394.txt 
data\_476.txt  data\_517.txt  
data\_228.txt  data\_280.txt  data\_343.txt  data\_395.txt 
data\_478.txt  data\_524.txt  
data\_231.txt  data\_282.txt  data\_360.txt  data\_401.txt 
data\_480.txt  data\_553.txt  
data\_236.txt  data\_290.txt  data\_368.txt  data\_418.txt 
data\_489.txt  NOTES  
data\_255.txt  data\_293.txt  data\_374.txt  data\_457.txt 
data\_496.txt

./lawrence:  
Data0214  Data0260  Data0300  Data0361  Data0392  Data0430  Data0449 
Data0492  Data0526  
Data0225  Data0271  Data0310  Data0362  Data0400  Data0437  Data0452 
Data0506  Data0531  
Data0234  Data0275  Data0313  Data0363  Data0403  Data0440  Data0455 
Data0511  Data0544  
Data0248  Data0276  Data0335  Data0371  Data0410  Data0441  Data0456 
Data0515  Data0554  
Data0251  Data0284  Data0345  Data0382  Data0411  Data0442  Data0463 
Data0522  
Data0253  Data0296  Data0352  Data0390  Data0423  Data0447  Data0483 
Data0525

./thomas:  
0213  0274  0298  0303  0328  0340  0351  0373  0399  0432  0450  0481 
0488  0539  
0241  0281  0299  0314  0333  0341  0354  0376  0406  0435  0464  0482 
0501  0561  
0244  0287  0301  0315  0334  0348  0358  0391  0425  0438  0465  0484 
0513  
0249  0289  0302  0322  0336  0349  0369  0396  0431  0448  0467  0485 
0514

What do we see from a visual inspection of these? All data files have
subject number. Some inconsistencies include Notes files, with no
numbers.

Can you give a list of only files that contain number 0 in name? Start
with directory jamesm:

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ ls jamesm/*0
    jamesm/data_280.txt  jamesm/data_360.txt  jamesm/data_480.txt  jamesm/data_510.txt
    jamesm/data_290.txt  jamesm/data_401.txt  jamesm/data_509.txt

The shell, before it prints, looks in directory and looks for patterns
with string of characters, number 0, then another string of characters.

Shell will fill out names into a command.

What the shell prints is equivalent to you typing a bunch of the
commands by hand.

ls will echo back.

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ ls -l jamesm/data_280.txt jamesm/data_290.txt
    -rw-rw-r-- 1 flcellogrl flcellogrl 150 Nov 14 09:11 jamesm/data_280.txt
    -rw-rw-r-- 1 flcellogrl flcellogrl 143 Nov 14 09:11 jamesm/data_290.txt

Let the computer do the work for you. They are great at remembering
stuff. We are crap at remembering stuff.

Use up arrows to remember commands. Use the computer to remember what
you did.

    history

It's like a lab notebook! It records everything you did.

    !559

Or

    history 10

Will bring back a command in the history. It will only store 500-600
lines. If you need to, you can change the number of lines it stores.

Ctrl-R and 'command' will reverse sesarch  
Ctrl-C will cancel current command.

How many files do we have? Which files have data, which are notes files?
Generate a list of data files, automatically?

    find . -

. will look at in home directories  
\* wild card  
'foo' protects string from the shell

This is different:

    find . -name Data*

Looks for files in current directory only. Interpolation. Wild card
expansion in quotes will have it print all files in other directories.

    |

Pipe. transferrs output to input of the next

Will make it fit in your screen. Will stop and give :  
Hit space bar. more forward. Gives another page. Chunks.  
Ctrl-B, back 1 page  
Ctrl-F, next 1 page  
q to get you back to command line.  
Enter will go line by line.

Ctrl-Z will halt it.  
Jobs will list stopped processes.

    fg %1

will bring it back

    kill %1

Will terminate process.

\*Aside: This is a good time to talk about the power of silent
processes. It's easy to remove files. Once they're gone from the kernel,
they're gone. It will be silent.

Moving on.

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ find . >filelist
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ head filelist
    .
    ./frank_richard
    ./frank_richard/data_444
    ./frank_richard/data_491
    ./frank_richard/data_538
    ./frank_richard/data_507
    ./frank_richard/data_237
    ./frank_richard/data_479
    ./frank_richard/data_316
    ./frank_richard/data_503
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ tail filelist
    ./alexander/data_389.DATA
    ./alexander/data_516.DATA
    ./alexander/data_364.DATA
    ./alexander/data_397.DATA
    ./alexander/data_357.DATA
    ./alexander/data_278.DATA
    ./alexander/data_530.DATA
    ./alexander/data_546.DATA
    ./alexander/data_547.DATA
    ./alexander/data_469.DATA
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ tail -n 4 filelist
    ./alexander/data_530.DATA
    ./alexander/data_546.DATA
    ./alexander/data_547.DATA
    ./alexander/data_469.DATA

Mechanize this. All files we're interested in have numbers. Pick out
patterns.

    grep

(global regular expression print)

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ find . >filelist
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ head filelist
    .
    ./frank_richard
    ./frank_richard/data_444
    ./frank_richard/data_491
    ./frank_richard/data_538
    ./frank_richard/data_507
    ./frank_richard/data_237
    ./frank_richard/data_479
    ./frank_richard/data_316
    ./frank_richard/data_503
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ tail filelist
    ./alexander/data_389.DATA
    ./alexander/data_516.DATA
    ./alexander/data_364.DATA
    ./alexander/data_397.DATA
    ./alexander/data_357.DATA
    ./alexander/data_278.DATA
    ./alexander/data_530.DATA
    ./alexander/data_546.DATA
    ./alexander/data_547.DATA
    ./alexander/data_469.DATA
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ tail -n 4 filelist
    ./alexander/data_530.DATA
    ./alexander/data_546.DATA
    ./alexander/data_547.DATA
    ./alexander/data_469.DATA

Print me every other line that doesn't contain 'NOTES':

    grep -v 'NOTES' filelist |less

Every file that with a name including these numbers:

    grep '[0123456789]' filelist

    grep '[0123456789]' filelist | less

    wc --htlp

Line, word, byte counts for each file.

Review:  
grep  
find

Let's say you wanted to do one command more than one time? Save command,
reuse. Editor.

Text editor: It is worth learning a cross-platform editor. This is very
important. Find one of these and use it.  
-[VIM](http://www.vim.org/)  
- Emacs  
- PyCharm: new Integrated Python IDE

Where to save shell script files, which directory? If you don't know
where your files are, and want to look everywhere for the files, start
with root directory:

    find / -name 2013-11-14-woodshole*

This will take a while because it's searching through your whole
computer.

Name shell scripts as .sh

(For now, I'm using gedit.)

If you're in Windows, you have directories with spaces.

    mkdir 'My Space'

Nice thing about tab completion, it will appropriately escape spaces or
Chinese characters or whatever.

    rmdir 'My Space'

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-shell/data$ grep 'Sex: N' $(cat filelist)
    grep: .: Is a directory
    grep: ./frank_richard: Is a directory
    ./frank_richard/data_491:Sex: N
    ./frank_richard/data_507:Sex: N
    ./frank_richard/data_479:Sex: N
    ./frank_richard/data_212:Sex: N
    ./frank_richard/data_247:Sex: N
    ./frank_richard/data_494:Sex: N
    ./frank_richard/data_504:Sex: N
    ./frank_richard/data_385:Sex: N
    ./frank_richard/data_508:Sex: N
    ./frank_richard/data_428:Sex: N
    ./frank_richard/data_545:Sex: N
    ./frank_richard/data_381:Sex: N
    ./frank_richard/data_224:Sex: N
    ./frank_richard/data_233:Sex: N
    ./frank_richard/data_221:Sex: N
    ./frank_richard/data_477:Sex: N
    ./frank_richard/data_519:Sex: N
    grep: ./bert: Is a directory
    ./bert/audioresult-00443:Sex: N
    ./bert/audioresult-00239:Sex: N
    ./bert/audioresult-00422:Sex: N
    ./bert/audioresult-00380:Sex: N
    ./bert/audioresult-00445:Sex: N
    ./bert/audioresult-00353:Sex: N
    ./bert/audioresult-00222:Sex: N
    ./bert/audioresult-00521:Sex: N
    ./bert/audioresult-00384:Sex: N
    ./bert/audioresult-00372:Sex: N
    ./bert/audioresult-00246:Sex: N
    ./bert/audioresult-00215:Sex: N
    ./bert/audioresult-00321:Sex: N
    ./bert/audioresult-00235:Sex: N
    ./bert/audioresult-00320:Sex: N
    ./bert/audioresult-00270:Sex: N
    grep: ./lawrence: Is a directory
    ./lawrence/Data0526:Sex: N
    ./lawrence/Data0363:Sex: N
    ./lawrence/Data0371:Sex: N
    ./lawrence/Data0492:Sex: N
    ./lawrence/Data0463:Sex: N
    ./lawrence/Data0234:Sex: N
    ./lawrence/Data0525:Sex: N
    ./lawrence/Data0310:Sex: N
    ./lawrence/Data0335:Sex: N
    ./lawrence/Data0390:Sex: N
    ./lawrence/Data0544:Sex: N
    ./lawrence/Data0251:Sex: N
    ./lawrence/Data0531:Sex: N
    ./lawrence/Data0276:Sex: N
    ./lawrence/Data0522:Sex: N
    ./lawrence/Data0225:Sex: N
    ./lawrence/Data0382:Sex: N
    ./lawrence/Data0362:Sex: N
    grep: ./jamesm: Is a directory
    ./jamesm/data_325.txt:Sex: N
    ./jamesm/data_475.txt:Sex: N
    ./jamesm/data_509.txt:Sex: N
    ./jamesm/data_264.txt:Sex: N
    ./jamesm/data_255.txt:Sex: N
    ./jamesm/data_236.txt:Sex: N
    ./jamesm/data_457.txt:Sex: N
    ./jamesm/data_231.txt:Sex: N
    ./jamesm/data_266.txt:Sex: N
    ./jamesm/data_480.txt:Sex: N
    ./jamesm/data_326.txt:Sex: N
    ./jamesm/data_476.txt:Sex: N
    ./jamesm/data_226.txt:Sex: N
    ./jamesm/data_217.txt:Sex: N
    ./jamesm/data_496.txt:Sex: N
    ./jamesm/data_383.txt:Sex: N
    grep: ./gerdal: Is a directory
    ./gerdal/Data0232:Sex: N
    ./gerdal/Data0279:Sex: N
    ./gerdal/Data0311:Sex: N
    ./gerdal/Data0549:Sex: N
    ./gerdal/Data0424:Sex: N
    ./gerdal/Data0220:Sex: N
    ./gerdal/Data0505:Sex: N
    ./gerdal/Data0218:Sex: N
    ./gerdal/Data0407:Sex: N
    ./gerdal/Data0458:Sex: N
    ./gerdal/Data0520:Sex: N
    ./gerdal/Data0338:Sex: N
    ./gerdal/Data0263:Sex: N
    ./gerdal/Data0528:Sex: N
    ./gerdal/Data0230:Sex: N
    ./gerdal/Data0523:Sex: N
    grep: ./thomas: Is a directory
    ./thomas/0328:Sex: N
    ./thomas/0333:Sex: N
    ./thomas/0334:Sex: N
    ./thomas/0373:Sex: N
    ./thomas/0369:Sex: N
    ./thomas/0432:Sex: N
    ./thomas/0464:Sex: N
    ./thomas/0287:Sex: N
    ./thomas/0213:Sex: N
    grep: ./alexander: Is a directory
    ./alexander/data_536.DATA:Sex: N
    ./alexander/data_427.DATA:Sex: N
    ./alexander/data_527.DATA:Sex: N
    ./alexander/data_402.DATA:Sex: N
    ./alexander/data_387.DATA:Sex: N
    ./alexander/data_548.DATA:Sex: N
    ./alexander/data_262.DATA:Sex: N
    ./alexander/data_216.DATA:Sex: N
    ./alexander/data_364.DATA:Sex: N
    ./alexander/data_357.DATA:Sex: N
    ./alexander/data_547.DATA:Sex: N
    ./alexander/data_469.DATA:Sex: N

To get grep to look inside the files, you need to feed them separately.

Two ways to use grep:  
1. grep ; looks for patterns, output  
2. grep Gives grep list of filenames. grep will go through each file,
makes a decision whether it meets criteria, then outputs something with
match.

&gt;

creates file

instead of \[0123456789\] just use \[0-9\]

&gt;&gt; appends instead of overwrites files
