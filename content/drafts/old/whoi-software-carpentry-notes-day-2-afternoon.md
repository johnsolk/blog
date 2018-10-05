Title: WHOI Software Carpentry notes, Day 2 – afternoon
Date: 2013-11-15 13:55
Author: monsterbashseq
Category: Python, software, Software Carpentry
Slug: whoi-software-carpentry-notes-day-2-afternoon
Status: published

Theory: Typical programmer, regardless of language, will write the same
number of lines of code in their lifetime compared to any other
programmer.

Tab completion in the command line rocks. Worth the whole trip.

Calculate GC content.

    seq='ACGTACGTAGCTAGTAGCTACGTAGCTACGTA'
    g=seq.count('G')
    c=seq.count('C')
    a=seq.count('A')
    t=seq.count('T')
    gc=((g+c)/(a+t+g+c)*100)
    print('GC count is:',gc,'%')

Make functions:

    def gc_content(seq):
        seq=seq.upper()
        g=seq.count('G')
        c=seq.count('C')
        a=seq.count('A')
        t=seq.count('T')
        gc=((g+c)/(a+t+g+c)*100)
        return(gc)

Not good practice to do:

    from math import *

This is because you may be importing functions you're not aware of. If
you accidentally name one of your functions the same name, you will have
a conflict. Your namespace is polluted.  
http://stackoverflow.com/questions/1432480/any-way-to-clear-pythons-idle-window  
[![](http://imgs.xkcd.com/comics/the_general_problem.png){.alignnone
width="550" height="230"}](http://xkcd.com/974/)

THIS IS REALLY IMPORTANT. THIS WILL ALLOW YOU TO IMPORT YOUR FUNCTIONS.
Keep all functions in one working directory. Set pythonpath to working
directory so it can find your functions.  
In the terminal:

    flcellogrl@flcellogrl:~/good_science$ export PYTHONPATH=$(pwd)
    flcellogrl@flcellogrl:~/good_science$ echo $PYTHONPATH
    /home/flcellogrl/good_science

Runable script.  
In Python:

    def gc_content(seq):
        seq=seq.upper()
        g=seq.count('G')
        c=seq.count('C')
        a=seq.count('A')
        t=seq.count('T')
        gc=((g+c)/(a+t+g+c)*100)
        return(gc)

    def hello():
        print('Hello world.')

    if __name__=='__main__':
        print("Unimplemented")

Save in working directory.  
In Linux shell:

    flcellogrl@flcellogrl:~/good_science$ python cgc.py
    Unimplemented

Read shell on Linux shell command line.  
In Python:

    def gc_content(seq):
        seq=seq.upper()
        g=seq.count('G')
        c=seq.count('C')
        a=seq.count('A')
        t=seq.count('T')
        gc=((g+c)/(a+t+g+c)*100)
        return(gc)

    def hello():
        print('Hello world.')

    import sys
    if __name__=='__main__':
        print(sys.argv[1])

In Linux command line:

    flcellogrl@flcellogrl:~/good_science$ python cgc.py "Hello dolly"
    Hello dolly
    flcellogrl@flcellogrl:~/good_science$

Something useful:

    def gc_content(seq):
        seq=seq.upper()
        g=float(seq.count('G'))
        c=float(seq.count('C'))
        a=float(seq.count('A'))
        t=float(seq.count('T'))
        gc=(g+c)/(a+t+g+c)*100
        return(gc)

    import sys
    if __name__=='__main__':
        print(sys.argv[1])
        print(gc_content(sys.argv[1]))

In Linux shell:

    flcellogrl@flcellogrl:~/good_science$ python cgc.py ATGCGC
    ATGCGC
    66.6666666667
    flcellogrl@flcellogrl:~/good_science$

For comparable data types to data.frame in R, look more at [Python
pandas](http://pandas.pydata.org/) and [numpy](http://www.numpy.org/).

Things to consider for code, what to return when:

-   Mixed case: handled with string.upper()
-   Empty string: Return informative error?
-   No GC content:
-   No AT content
-   A letter of "n" or "N", meaning wildcard, flexible - could be
    A,T,C,or G: Return informative error
-   Protein sequence: Informative error.
-   non-DNA string: Informative error.
-   non-string argument: Informative error message
-   unprintable characters

<!-- -->

    from nose.tools import assert_equal, assert_almost_equal, assert_true,   
       assert_false, assert_raises, assert_is_instance

    from calculate_gc import calculate_gc

    def test_only_G_and_C():
        '''
        Sequence of only G's and C's has fraction 1.0
        '''
        fixture = 'GGCGCCGGC'
        result = calculate_gc(fixture)
        assert_equal(result, 1.0)

    def test_half():
        '''
        Sequence with half G and C has fraction 0.5
        '''
        fixture = 'ATGC'
        result = calculate_gc(fixture)
        assert_equal(result, 0.5)

    def test_lower_case():
        '''
        Sequence with lower case letters
        '''
        fixture = 'atgc'
        result = calculate_gc(fixture)
        assert_equal(result, 0.5)

    def test_not_DNA():
        '''
        Raise TypeError if not DNA
        '''
        fixture = 'qwerty'
        assert_raises(TypeError, calculate_gc, fixture)

From above:

    nose.tools

    nosetests

http://nose.readthedocs.org/en/latest/

[![test\_prod](http://monsterbashseq.files.wordpress.com/2013/11/test_prod1.jpg?w=300){.alignnone
.size-medium .wp-image-611 width="300"
height="300"}](http://monsterbashseq.files.wordpress.com/2013/11/test_prod1.jpg)

Debugging tools, didn't get to, Lesson on this (thw-python-debugging)
linked here:  
http://wltrimbl.github.io/2013-11-14-woodshole/lessons/

Pylint: http://www.pylint.org/

etherpad results from course:

    Welcome to MoPad!
    This pad text is synchronized as you type, so that everyone viewing this page sees the same text.  This allows you to collaborate seamlessly on documents!
    Please be cognizant of whether you are using a public pad or private/team pad, and take appropriate precautions with data you post here!

     Add your name in the box at the upper right -- then we can tell who's asking the question.
     And feel free to answer each other's questions!
     git clone https://github.com/wltrimbl/2013-11-14-woodshole.git

    If you want to install packages on the virtual machine (e.g. 'sudo apt-get install nedit') the password is "swc" 
    Lesson index:
    http://wltrimbl.github.io/2013-11-14-woodshole/lessons/
    Shell:
    Top-level website:
    http://wltrimbl.github.io/2013-11-14-woodshole
    (but this is probably how you got to the etherpad..)
    Shell cheat sheet:
    http://wltrimbl.github.io/2013-11-14-woodshole/lessons/ref/shell.html
    pwd   # show directory 
    cd  # cd with no arguments changes to $HOME directory
    cd ~       #   tilde  ~ is symbol for home directory
    cd ~/Desktop
    ls -ltr          #   long, sortbytime,  reverse  
    ls -l -t -r     # equivalent
    ls -lt --reverse  # equivalent
    man ls      # linux or mac
    ls --help    # windows/gitbash
    ls -l       # first column is fie/directory fie/directory permissions
        d   directory
        r    read
        w   write
        x   execute
        u   user
        g    your  group
        o    others
        rwx  *   ugo  = rwxrwxrwx
    cd
    cd 2013-11-17-woodshole
    cd lessons/thw-shell
    cd 2013    #   Typing  on an incomplete filename triggers tab-completion
                                # bash tries to guess what (long) filename you want to type.
                                # unless it's ambiguous
    or 
    cd ~/2013-11-17-woodshole/lessons/thw-shell
    cd data
    echo $0       # prints the location or name of the shell program that is currently running in bash
    echo Hello   
    echo $HOME
    echo $PATH
    cd ~/2013-11-17-woodshole/lessons/thw-shell/data
    ls
    cd alexander
    ls
    cat data_216.DATA
    cd ..
    ls bert
    cd bert
    ls aud    # double-tab gives a list of possibilities
    ls -R    # recursive  
    cat jamesm/NOTES      #    relative path
    cat /Users/wltrimbl/2013-11-17-woodshole/lessons/thw-shell/data/jamesm/NOTES  # absolute path
    TASK:
    find the files in the jamesm directory that contain the numeral 0 in their name
    ls jamesm/*0*          
           #    *   is the wildcard   -- it matches 0 or more characters, which can be anything
           #    *0*     matches anything with a 0 somewhere.  

        retrieves earlier commands entered at the bash prompt
    allows them to be repeated or modified.
    history
    !482     # invoke the 482nd command from the history .
    Control-R  : gives you a prompt to search previous commands
    Control-C :    put the command out of its sufferiing.  Aborts the current command.
    cd  ~/2013-11-17-woodshole/lessons/thw-shell/data
    find .  
    # spit out the relative paths of all of the files and directories in and beneath the current directory
    find . -name "Data*"
    echo Hi > Data000
    # creates a small file called Data000
    find . -name Data*
    expands to 
    find . -name Data000
    and only after doing the wildcard expansion is find invoked.
    find . | less
    #      |   is THE PIPE
    find . -name "Data*"  | less 
            #   shows the output of find one page at a time.
            #  within less, Control-B and Control-F go backward and forth
            #  within less,   q will escape and return you to the shell
    Control -C    :   Abort the current command  (never hear from it again)
    Control-Z    :    Suspend the current command and return you to the shell.  (command can be restarted)  
    Control-D  :    End of file character
    less ../dictionary.txt
    find .  | less
    find . > filelist
    #  creates a file called filelist with the contents of the output of find .
    tail filelist
    tail -n 4 filelist     # show the last four lines
    head filelist   
    grep NOTES filelist
    grep '[0123456789]' filelist
    grep '[0123456789]' filelist | wc
    # count the lines of the output of grep
    #  The power editors are vi  and emacs.  They do everything but are hard to learn.
    Notepad++   (windows)
    Sublime     (mac)
    TextWrangler (mac)
    Notepad or TextEdit as emergency backups..
    Use a text editor  to create a file with the contents 
    grep '[0123456789]' filelist  | wc 
    and save it (using the editor)  in the directory ~/2013-11-14-woodshole/lessons/thw-shell/data
    as the filename  
    count_data_files.sh
    mkdir "My Space"
    ls -F   
    # postpends directories with "/"
    # Coping with spaces in filenames  jargon:  "Escaping"  the space caracter
    rmdir My\ Space  
    rmdir "My Space"    
    ./count_data_files.sh
    # execute count_data_files
    ls -l count_data_files.sh
    chmod +x count_data_files.sh
    ls -l count_data_files.sh
    grep "Sex: N" $(cat filelist) 
    grep "Sex: N"  */*[1234567890]* 
    for thing in `ls`; do echo :::$thing:::; done
    for file in *;   do  head -n 2 $file | tail -n 1 ; done 
     ---------------------- PYTHON LESSONS ------------------------
    ~/2013-11-14-woodshole/lessons/thw-python/vars-types/variables.ipynb
    ~/2013-11-14-woodshole/lessons/thw-python/data-structures/data_structures.ipynb
    ~/2013-11-14-woodshole/lessons/thw-python/flow-control/python_flow_control.ipynb
    --------------------- Some things to do different next time in Woods Hole ---------------------
    - bigger room at another lab
    - or less people at NEFSC conf rm (also turn down thermostat!!)
    - knapkins
    - a better wireless and/or drop line arrangement
    - less coffee&pastry, more juice& fruit
    - end lectures earlier in the afternoon
    REMINDER:  Woods Hole Python Users Group meets every Tuesday a 11am in the Bigelow Bldg first floor conference room for about an hour to chat about Python and a few other related tools. All are welcome. Contact: james.manning@noaa.gov
    ----------------------------------------------------------------------------------------------------------------------
    DAY 2:
    Index: 
    http://wltrimbl.github.io/2013-11-14-woodshole/lessons/
    First lesson 
    http://wltrimbl.github.io/2013-11-14-woodshole/lessons/thw-git/local.html
    Basic motivation for version control:  http://www.phdcomics.com/comics/archive.php?comicid=1531
    github.com/wltrimbl/testrepo-2013-11-14-woodshole
    $ git remote add upstream http://github.com/wltrimbl/testrepo-2013-11-14-woodshole.git
    WRITING PYTHON FUNCTIONS
    2013-11-14-woodshole\lessons\thw-python\functions-modules
    You do not want 
    NONONO   2013-11-14-woodshole\lessons\thw-python\functions-and-modules NONONO
    Will you share your data?
    http://www.youtube.com/watch?v=N2zK3sAtr-4
    take your calculate_gc  funciton definition 
    and save it as calculate_gc.py     in   ~/good_science
    Navigate to ~/good_science in your shell
    cd ~/good_science
    Fire up
    python
    Inside of python   (after the >>>)
    from calculate_gc   import calculate_gc 
    calculate_gc("AGCTAGGAA")
    Q:  how can I add my own libraries / modules to somewhere where python will find them?
    A:  export PYTHONPATH=/path/to/modules
    echo $PATH
    mv calculate_gc.py dnautils.py    # renames calculate_gc.py
    python 
    import dnautils
    dir(dnautils)
    dnautils.calculate_gc("ATTTA")
    import dnautils
    dnautils.hello()
    create a file called cgc.py
    containing
    def calculate_gc(x): 
    ...
    and the two lines:
    if __name__ == '__main__':
        print "Unimplemented"
    And run it using:
    python cgc.py
    import sys
    if __name__ == '__main__':
        print sys.argv[1]
    python cgc.py  "Hello dolly"
    TESTING
    cp ~/2013-11-14-woodshole/lessons/thw-testing-gc/test_calculate_gc.py ~/good_science
    This copies  the file test_calculate_gc.py   to  good_science.
    Change from calculate_gc to from cgc   (or the name of your calculate_gc file)
    nosetests
    This is the post-bootcamp survey. Please, take the time to go through the survey we promise it's easier than the past two days have been.
    https://docs.google.com/forms/d/1IfuvX6jtpq-q41IW0nY1Sv2CIhFyJTHySkfpt6P2OCo/viewform
