Title: WHOI Software Carpentry notes, Day 1 - afternoon
Date: 2013-11-14 14:54
Author: monsterbashseq
Category: Python, software, Software Carpentry
Slug: whoi-software-carpentry-notes-day-1-afternoon
Status: published

Python

Canopy?

    sudo apt-get install ipython

    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ sudo apt-get install ipython
    [sudo] password for flcellogrl: 
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following packages were automatically installed and are no longer required:
      libcurl3-nss libnspr4-dev libnss3-dev libssl-dev libssl-doc linux-headers-3.8.0-19
      linux-headers-3.8.0-19-generic linux-image-3.8.0-19-generic
      linux-image-extra-3.8.0-19-generic
    Use 'apt-get autoremove' to remove them.
    The following extra packages will be installed:
      python-configobj python-decorator python-simplegeneric
    Suggested packages:
      ipython-doc ipython-notebook ipython-qtconsole python-matplotlib python-zmq
    The following NEW packages will be installed:
      ipython python-configobj python-decorator python-simplegeneric
    0 upgraded, 4 newly installed, 0 to remove and 15 not upgraded.
    Need to get 932 kB of archives.
    After this operation, 4,623 kB of additional disk space will be used.
    Do you want to continue [Y/n]? y
    Get:1 http://us.archive.ubuntu.com/ubuntu/ raring/main python-configobj all 4.7.2+ds-4 [234 kB]
    Get:2 http://us.archive.ubuntu.com/ubuntu/ raring/main python-decorator all 3.3.3-1 [19.9 kB]
    Get:3 http://us.archive.ubuntu.com/ubuntu/ raring/universe python-simplegeneric all 0.8.1-1 [11.5 kB]
    Get:4 http://us.archive.ubuntu.com/ubuntu/ raring/universe ipython all 0.13.2-1 [667 kB]
    Fetched 932 kB in 1s (858 kB/s)  
    Selecting previously unselected package python-configobj.
    (Reading database ... 439323 files and directories currently installed.)
    Unpacking python-configobj (from .../python-configobj_4.7.2+ds-4_all.deb) ...
    Selecting previously unselected package python-decorator.
    Unpacking python-decorator (from .../python-decorator_3.3.3-1_all.deb) ...
    Selecting previously unselected package python-simplegeneric.
    Unpacking python-simplegeneric (from .../python-simplegeneric_0.8.1-1_all.deb) ...
    Selecting previously unselected package ipython.
    Unpacking ipython (from .../ipython_0.13.2-1_all.deb) ...
    Processing triggers for doc-base ...
    Processing 1 added doc-base file...
    Registering documents with scrollkeeper...
    Processing triggers for bamfdaemon ...
    Rebuilding /usr/share/applications/bamf-2.index...
    Processing triggers for desktop-file-utils ...
    Processing triggers for gnome-menus ...
    Processing triggers for hicolor-icon-theme ...
    Processing triggers for man-db ...
    Setting up python-configobj (4.7.2+ds-4) ...
    Setting up python-decorator (3.3.3-1) ...
    Setting up python-simplegeneric (0.8.1-1) ...
    Setting up ipython (0.13.2-1) ...
    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ ipython
    Python 2.7.4 (default, Sep 26 2013, 03:20:56) 
    Type "copyright", "credits" or "license" for more information.

    IPython 0.13.2 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: quit()

    sudo apt-get install python-notebook

    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-python$ sudo apt-get install ipython-notebook
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following packages were automatically installed and are no longer required:
      libcurl3-nss libnspr4-dev libnss3-dev libssl-dev libssl-doc linux-headers-3.8.0-19
      linux-headers-3.8.0-19-generic linux-image-3.8.0-19-generic
      linux-image-extra-3.8.0-19-generic
    Use 'apt-get autoremove' to remove them.
    The following extra packages will be installed:
      fonts-mathjax ipython-notebook-common libjs-mathjax libpgm-5.1-0 libzmq1 python-tornado
      python-zmq
    Suggested packages:
      fonts-mathjax-extras libjs-mathjax-doc
    The following NEW packages will be installed:
      fonts-mathjax ipython-notebook ipython-notebook-common libjs-mathjax libpgm-5.1-0 libzmq1
      python-tornado python-zmq
    0 upgraded, 8 newly installed, 0 to remove and 15 not upgraded.
    Need to get 2,990 kB of archives.
    After this operation, 16.6 MB of additional disk space will be used.
    Do you want to continue [Y/n]? y
    Get:1 http://us.archive.ubuntu.com/ubuntu/ raring/universe fonts-mathjax all 2.1+20121028-1 [958 kB]
    Get:2 http://us.archive.ubuntu.com/ubuntu/ raring/universe libpgm-5.1-0 i386 5.1.118-1~dfsg-0.1ubuntu1 [182 kB]
    Get:3 http://us.archive.ubuntu.com/ubuntu/ raring/universe libzmq1 i386 2.2.0+dfsg-2ubuntu1 [106 kB]
    Get:4 http://us.archive.ubuntu.com/ubuntu/ raring/universe libjs-mathjax all 2.1+20121028-1 [887 kB]
    Get:5 http://us.archive.ubuntu.com/ubuntu/ raring/universe ipython-notebook-common all 0.13.2-1 [360 kB]
    Get:6 http://us.archive.ubuntu.com/ubuntu/ raring/main python-tornado all 2.4.1-1 [255 kB]
    Get:7 http://us.archive.ubuntu.com/ubuntu/ raring/universe python-zmq i386 2.2.0.1-1 [217 kB]
    Get:8 http://us.archive.ubuntu.com/ubuntu/ raring/universe ipython-notebook all 0.13.2-1 [25.0 kB]
    Fetched 2,990 kB in 4s (649 kB/s)           
    Selecting previously unselected package fonts-mathjax.
    (Reading database ... 440060 files and directories currently installed.)
    Unpacking fonts-mathjax (from .../fonts-mathjax_2.1+20121028-1_all.deb) ...
    Selecting previously unselected package libpgm-5.1-0:i386.
    Unpacking libpgm-5.1-0:i386 (from .../libpgm-5.1-0_5.1.118-1~dfsg-0.1ubuntu1_i386.deb) ...
    Selecting previously unselected package libzmq1:i386.
    Unpacking libzmq1:i386 (from .../libzmq1_2.2.0+dfsg-2ubuntu1_i386.deb) ...
    Selecting previously unselected package libjs-mathjax.
    Unpacking libjs-mathjax (from .../libjs-mathjax_2.1+20121028-1_all.deb) ...
    Selecting previously unselected package ipython-notebook-common.
    Unpacking ipython-notebook-common (from .../ipython-notebook-common_0.13.2-1_all.deb) ...
    Selecting previously unselected package python-tornado.
    Unpacking python-tornado (from .../python-tornado_2.4.1-1_all.deb) ...
    Selecting previously unselected package python-zmq.
    Unpacking python-zmq (from .../python-zmq_2.2.0.1-1_i386.deb) ...
    Selecting previously unselected package ipython-notebook.
    Unpacking ipython-notebook (from .../ipython-notebook_0.13.2-1_all.deb) ...
    Processing triggers for fontconfig ...
    Setting up fonts-mathjax (2.1+20121028-1) ...
    Setting up libpgm-5.1-0:i386 (5.1.118-1~dfsg-0.1ubuntu1) ...
    Setting up libzmq1:i386 (2.2.0+dfsg-2ubuntu1) ...
    Setting up libjs-mathjax (2.1+20121028-1) ...
    Setting up ipython-notebook-common (0.13.2-1) ...
    Setting up python-tornado (2.4.1-1) ...
    Setting up python-zmq (2.2.0.1-1) ...
    Setting up ipython-notebook (0.13.2-1) ...
    Processing triggers for libc-bin ...
    ldconfig deferred processing now taking place
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-python$ ipython notebook variables.ipynb
    [NotebookApp] Using existing profile dir: u'/home/flcellogrl/.config/ipython/profile_default'
    [NotebookApp] Serving notebooks from /home/flcellogrl/2013-11-14-woodshole/lessons/thw-python
    [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8888/
    [NotebookApp] Use Control-C to stop this server and shut down all kernels.

    (process:6034): GLib-CRITICAL **: g_slice_set_config: assertion `sys_page_size == 0' failed
    ^CShutdown Notebook Server (y/[n])? y
    [NotebookApp] Shutdown confirmed
    [NotebookApp] Shutting down kernels
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-python$ ls
    data-structures  functions-and-modules  obj-orientation  vars-types
    flow-control     functions-modules      strings-io
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-python$ cd vars-types
    flcellogrl@flcellogrl:~/2013-11-14-woodshole/lessons/thw-python/vars-types$ ipython notebook variables.ipynb
    [NotebookApp] Using existing profile dir: u'/home/flcellogrl/.config/ipython/profile_default'
    [NotebookApp] Serving notebooks from /home/flcellogrl/2013-11-14-woodshole/lessons/thw-python/vars-types
    [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8888/
    [NotebookApp] Use Control-C to stop this server and shut down all kernels.

    (process:6116): GLib-CRITICAL **: g_slice_set_config: assertion `sys_page_size == 0' failed
    [NotebookApp] Using system MathJax
    [NotebookApp] Kernel started: 679ff4f0-49e3-4400-a2b2-ea9cba39ec45
    [IPKernelApp] To connect another client to this kernel, use:
    [IPKernelApp] --existing kernel-679ff4f0-49e3-4400-a2b2-ea9cba39ec45.json
    [NotebookApp] Connecting to: tcp://127.0.0.1:57053
    [NotebookApp] Connecting to: tcp://127.0.0.1:59491
    [NotebookApp] Connecting to: tcp://127.0.0.1:55042

Running lecture from IP\[y\]:Notebook from shell

http://www.flickr.com/photos/lpcohen/10876121684/

Working from Python 3.3.1 Shell (IDLE).

Shift-Enter will run the code displayed.

Half-open slicing: http://c2.com/cgi/wiki?ZeroAndOneBasedIndexes

Python's [half-open, 0-based index
notation](http://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html):

http://www.flickr.com/photos/lpcohen/10868749926/in/photostream/

Defect:

    a = [1, 2]
    b = a
    a.append(10)
    print(a)
    print(b)

The output is this:

    [1, 2, 10]
    [1, 2, 10]

To get an actual copy, do this:

    a = [1, 2]
    b = list(a)
    a.append(10)
    print(a)
    print(b)

Output:

    [1, 2, 10]
    [1, 2]

Covered:  
Data Types: float, integer, string  
Data Structures: list, tuple, dictionary

Appending dictionaries and lists

\#aside: What is working directory for Python IDLE?

    #Exercise 5:
    #Need to figure out how to specify where file is located
    #what is python's working directory?
    #http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    print("Path at terminal when executing this file")
    print(os.getcwd() + "\n")
    print("This file path, relative to os.getcwd()")
    print(__file__ + "\n")
    print("This file full path (following symlinks)")
    full_path = os.path.realpath(__file__)
    print(full_path + "\n")
    print("This file directory and name")
    path, file = os.path.split(full_path)
    print(path + ' --> ' + file + "\n")
    print("This file directory only")
    print(os.path.dirname(full_path))

    #fh=open("data.dat")
    #for line in fh:
    #    print(line.strip())

Flow Control  
Comparisons

    42 < 24 or True and 'wow' != 'mom'

Please use parentheses to separate logic statements. Python knows what
it's doing, you don't necessarily know the order.

    (42 < 24 or True) and 'wow' != 'mom'

Python knows nothing about sports:

    "Red Sox" > "Yankees"

    False

If statements, multiple elifs, only one else:

    x = 5
    if x < 0:
        print("x is negative")
    elif x == 0:
        print("x is zero")
    elif x<5:
        print("x is small")
    else:
        print("x is positive")

For any x, determine whether x is odd or even:

    if x%2==0:
        print("x is even.")
    else:
        print("x is odd.")

Or:

    x=2.1
    if x%2==0:
        print("x is even.")
    elif x%2 ==1:
        print("x is odd.")
    else:
        print("Are you sure you have an integer?")

Let's get loopy.

while loops are less common, probably because of their ability to shunt
out, undesireably  
for loops more common, list of examples:

Useful tool: dir(foo), will give you a list of functions available for
that type.

in Python notebook:, type foo.(then hit tab key,) a list of functions
will appear in a dropdown menu

Learn Python notebook. This will help you show off your Python code and
document it.

\#calculate factorial of 7  
\#product of all positive integers up to and including 7

    n=7
    fact=1
    for i in range(n):
        fact=fact*(i+1)
        print(i,fact,fact+1)
    print(fact)

Reading and writing files.  
Figure out working directory, where files are located, etc.

wakari: https://www.wakari.io/
