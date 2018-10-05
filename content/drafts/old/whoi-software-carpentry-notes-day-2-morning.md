Title: WHOI Software Carpentry notes, Day 2 – morning
Date: 2013-11-15 12:14
Author: monsterbashseq
Category: github, software, Software Carpentry, Ubuntu
Slug: whoi-software-carpentry-notes-day-2-morning
Status: published

https://etherpad.mozilla.org/swc-whoi-2013

Distributed version control systems, e.g. git, bzr, hg, dcvs

No master controller. All copies are equivalently complete and
functional.

Yesterday, we ran:

    git clone http://github.com/wltrimbl/2013-11-14-woodshole

Changes were made last night. Today, we need to update.

In terminal, we type:

    flcellogrl@flcellogrl:~$ cd 2013-11-14-woodshole/
    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ git pull origin gh-pages
    remote: Counting objects: 47, done.
    remote: Compressing objects: 100% (26/26), done.
    remote: Total 39 (delta 23), reused 29 (delta 13)
    Unpacking objects: 100% (39/39), done.
    From http://github.com/wltrimbl/2013-11-14-woodshole
     * branch            gh-pages   -> FETCH_HEAD
    Updating 8836b0d..9960092
    Fast-forward
     lessons/index.html                                 |  34 +-
     .../matplotlib_and_basemaps.ipynb                  | 578 +++++++++++++++++++++
     lessons/thw-git/local.md                           |  15 +-
     lessons/thw-numpy/numpy.ipynb                      | 506 +++++-------------
     lessons/thw-testing-gc/Readme.md                   | 450 ++++++++++++++++
     lessons/thw-testing-gc/calculate_gc.py             |   5 +
     lessons/thw-testing-gc/mean.py                     |   9 +
     lessons/thw-testing-gc/test_calculate_gc.py        |  35 ++
     lessons/thw-testing-gc/test_mean.py                |  26 +
     lessons/thw-testing-gc/test_prod.jpg               | Bin 0 -> 44369 bytes
     lessons/thw-testing-gc/test_transcribe.py          |   4 +
     lessons/thw-testing-gc/transcribe.py               |  18 +
     12 files changed, 1269 insertions(+), 411 deletions(-)
     create mode 100644 lessons/misc-python-for-geosciences/matplotlib_and_basemaps.ipynb
     create mode 100644 lessons/thw-testing-gc/Readme.md
     create mode 100644 lessons/thw-testing-gc/calculate_gc.py
     create mode 100644 lessons/thw-testing-gc/mean.py
     create mode 100644 lessons/thw-testing-gc/test_calculate_gc.py
     create mode 100644 lessons/thw-testing-gc/test_mean.py
     create mode 100644 lessons/thw-testing-gc/test_prod.jpg
     create mode 100644 lessons/thw-testing-gc/test_transcribe.py
     create mode 100644 lessons/thw-testing-gc/transcribe.py

Keep track of who is making changes:

    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ git config --global user.name "Lisa Cohen"
    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ git config user.email "lisa.johnson.cohen@gmail.com"

    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ git config --global user.name "Lisa Cohen"
    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ git config user.email "lisa.johnson.cohen@gmail.com"

Start repository:

    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ cd
    flcellogrl@flcellogrl:~$ mkdir good_science
    flcellogrl@flcellogrl:~$ cd good_science
    flcellogrl@flcellogrl:~/good_science$ git init
    Initialized empty Git repository in /home/flcellogrl/good_science/.git/

    flcellogrl@flcellogrl:~/2013-11-14-woodshole$ cd
    flcellogrl@flcellogrl:~$ mkdir good_science
    flcellogrl@flcellogrl:~$ cd good_science
    flcellogrl@flcellogrl:~/good_science$ git init
    Initialized empty Git repository in /home/flcellogrl/good_science/.git/

    flcellogrl@flcellogrl:~/good_science/.git$ ls
    branches  config  description  HEAD  hooks  info  objects  refs
    flcellogrl@flcellogrl:~/good_science/.git$ ls info
    exclude
    flcellogrl@flcellogrl:~/good_science/.git$ cat exclude
    cat: exclude: No such file or directory
    flcellogrl@flcellogrl:~/good_science/.git$ cat info/exclude
    # git ls-files --others --exclude-from=.git/info/exclude
    # Lines that start with '#' are comments.
    # For a project mostly in C, the following would be a good set of
    # exclude patterns (uncomment them if you want to use them):
    # *.[oa]
    # *~

\[history\]  
\^  
|  
type: git commit  
|  
\[stage\]  
\^  
|  
type: git add  
|  
\[working directory\]

[![basic-usage.svg](http://monsterbashseq.files.wordpress.com/2013/11/basic-usage-svg.png?w=300){.alignnone
.size-medium .wp-image-601 width="300"
height="128"}](http://marklodato.github.io/visual-git-guide/index-en.html)  
Create file "readme"

    nano readme.rst &

List possible git commands.

    git help

    flcellogrl@flcellogrl:~/good_science$ git commit -m "This is my first commit"

    *** Please tell me who you are.

    Run

      git config --global user.email "you@example.com"
      git config --global user.name "Your Name"

    to set your account's default identity.
    Omit --global to set the identity only in this repository.

    fatal: unable to auto-detect email address (got 'flcellogrl@flcellogrl.(none)')
    flcellogrl@flcellogrl:~/good_science$ git config --global user.name "Lisa Cohen"flcellogrl@flcellogrl:~/good_science$ git config user.email "lisa.johnson.cohen@gmail.com"
    flcellogrl@flcellogrl:~/good_science$ git config --global user.email "lisa.johnson.cohen@gmail.com"

Write good commit messages. You're probably writing these for yourself
(and possibly collaborators) to remember what and why you did these
things, later.

vim:  
:q! to quit without saving  
http://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor

Git: Undo a bad change:

    flcellogrl@flcellogrl:~/good_science/.git$ cd ..
    flcellogrl@flcellogrl:~/good_science$ ls
    flcellogrl@flcellogrl:~/good_science$ nano readme.rst 7
    flcellogrl@flcellogrl:~/good_science$ nano readme.rst &
    [1] 14169
    flcellogrl@flcellogrl:~/good_science$ git add readme.rst
    fatal: pathspec 'readme.rst' did not match any files

    [1]+  Stopped                 nano readme.rst
    flcellogrl@flcellogrl:~/good_science$ git status
    # On branch master
    #
    # Initial commit
    #
    nothing to commit (create/copy files and use "git add" to track)
    flcellogrl@flcellogrl:~/good_science$ nano
    flcellogrl@flcellogrl:~/good_science$ ls
    description
    flcellogrl@flcellogrl:~/good_science$ git add description
    flcellogrl@flcellogrl:~/good_science$ git status
    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    #   (use "git rm --cached ..." to unstage)
    #
    #   new file:   description
    #
    flcellogrl@flcellogrl:~/good_science$ git help
    usage: git [--version] [--exec-path[=]] [--html-path] [--man-path] [--info-path]
               [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
               [--git-dir=] [--work-tree=] [--namespace=]
               [-c name=value] [--help]
                []

    The most commonly used git commands are:
       add        Add file contents to the index
       bisect     Find by binary search the change that introduced a bug
       branch     List, create, or delete branches
       checkout   Checkout a branch or paths to the working tree
       clone      Clone a repository into a new directory
       commit     Record changes to the repository
       diff       Show changes between commits, commit and working tree, etc
       fetch      Download objects and refs from another repository
       grep       Print lines matching a pattern
       init       Create an empty git repository or reinitialize an existing one
       log        Show commit logs
       merge      Join two or more development histories together
       mv         Move or rename a file, a directory, or a symlink
       pull       Fetch from and merge with another repository or a local branch
       push       Update remote refs along with associated objects
       rebase     Forward-port local commits to the updated upstream head
       reset      Reset current HEAD to the specified state
       rm         Remove files from the working tree and from the index
       show       Show various types of objects
       status     Show the working tree status
       tag        Create, list, delete or verify a tag object signed with GPG

    See 'git help ' for more information on a specific command.
    flcellogrl@flcellogrl:~/good_science$ git commit -m "This is my first commit"

    *** Please tell me who you are.

    Run

      git config --global user.email "you@example.com"
      git config --global user.name "Your Name"

    to set your account's default identity.
    Omit --global to set the identity only in this repository.

    fatal: unable to auto-detect email address (got 'flcellogrl@flcellogrl.(none)')
    flcellogrl@flcellogrl:~/good_science$ git config --global user.name "Lisa Cohen"flcellogrl@flcellogrl:~/good_science$ git config user.email "lisa.johnson.cohen@gmail.com"
    flcellogrl@flcellogrl:~/good_science$ git config --global user.email "lisa.johnson.cohen@gmail.com"
    flcellogrl@flcellogrl:~/good_science$ nano descriptoin
    flcellogrl@flcellogrl:~/good_science$ ls
    description
    flcellogrl@flcellogrl:~/good_science$ nano description
    flcellogrl@flcellogrl:~/good_science$ ls
    description
    flcellogrl@flcellogrl:~/good_science$ git commit descrition
    error: pathspec 'descrition' did not match any file(s) known to git.
    flcellogrl@flcellogrl:~/good_science$ git commit description
    Aborting commit due to empty commit message.
    flcellogrl@flcellogrl:~/good_science$ git commit -m "This is another commit"
    [master (root-commit) b0992fb] This is another commit
     1 file changed, 1 insertion(+)
     create mode 100644 description
    flcellogrl@flcellogrl:~/good_science$ git status
    # On branch master
    # Changes not staged for commit:
    #   (use "git add ..." to update what will be committed)
    #   (use "git checkout -- ..." to discard changes in working directory)
    #
    #   modified:   description
    #
    no changes added to commit (use "git add" and/or "git commit -a")
    flcellogrl@flcellogrl:~/good_science$ git add description
    flcellogrl@flcellogrl:~/good_science$ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD ..." to unstage)
    #
    #   modified:   description
    #
    flcellogrl@flcellogrl:~/good_science$ git commit -m "Added phrase change to description."
    [master 752b47e] Added phrase change to description.
     1 file changed, 1 insertion(+), 1 deletion(-)
    flcellogrl@flcellogrl:~/good_science$ git log
    commit 752b47e16d7645e641300bcbabf440e7b2963a87
    Author: Lisa Cohen 
    Date:   Fri Nov 15 09:56:47 2013 -0500

        Added phrase change to description.

    commit b0992fb1e8669a2ec01fddd32cad33e7b1598fc4
    Author: Lisa Cohen 
    Date:   Fri Nov 15 09:55:46 2013 -0500

        This is another commit
    flcellogrl@flcellogrl:~/good_science$ nano description
    flcellogrl@flcellogrl:~/good_science$ git add description
    flcellogrl@flcellogrl:~/good_science$ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD ..." to unstage)
    #
    #   modified:   description
    #
    flcellogrl@flcellogrl:~/good_science$ git diff
    flcellogrl@flcellogrl:~/good_science$ cat description
    Yay! This is a change.

    This change is no good.
    flcellogrl@flcellogrl:~/good_science$ git commit -m "This change is no good."
    [master 76f4e3a] This change is no good.
     1 file changed, 2 insertions(+)
    flcellogrl@flcellogrl:~/good_science$ git log --oneline
    76f4e3a This change is no good.
    752b47e Added phrase change to description.
    b0992fb This is another commit
    flcellogrl@flcellogrl:~/good_science$ git checkout 752b47e description
    flcellogrl@flcellogrl:~/good_science$ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD ..." to unstage)
    #
    #   modified:   description
    #
    flcellogrl@flcellogrl:~/good_science$ git add description
    flcellogrl@flcellogrl:~/good_science$ git commit -m "Undid the bad change."
    [master 67c8be5] Undid the bad change.
     1 file changed, 2 deletions(-)
    flcellogrl@flcellogrl:~/good_science$ git log --oneline
    67c8be5 Undid the bad change.
    76f4e3a This change is no good.
    752b47e Added phrase change to description.
    b0992fb This is another commit
    flcellogrl@flcellogrl:~/good_science$ echo Hello >one.txt
    flcellogrl@flcellogrl:~/good_science$ echo This is a test >two.txt
    flcellogrl@flcellogrl:~/good_science$ echo Hi.
    Hi.
    flcellogrl@flcellogrl:~/good_science$ ls -l
    total 12
    -rw-rw-r-- 1 flcellogrl flcellogrl 23 Nov 15 09:59 description
    -rw-rw-r-- 1 flcellogrl flcellogrl  6 Nov 15 10:03 one.txt
    -rw-rw-r-- 1 flcellogrl flcellogrl 15 Nov 15 10:03 two.txt
    flcellogrl@flcellogrl:~/good_science$ git add *.txt
    flcellogrl@flcellogrl:~/good_science$ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD ..." to unstage)
    #
    #   new file:   one.txt
    #   new file:   two.txt
    #
    flcellogrl@flcellogrl:~/good_science$ git commit -m "Added two small text files"
    [master 6996e83] Added two small text files
     2 files changed, 2 insertions(+)
     create mode 100644 one.txt
     create mode 100644 two.txt
    flcellogrl@flcellogrl:~/good_science$ git log --one
    fatal: unrecognized argument: --one
    flcellogrl@flcellogrl:~/good_science$ git log --oneline
    6996e83 Added two small text files
    67c8be5 Undid the bad change.
    76f4e3a This change is no good.
    752b47e Added phrase change to description.
    b0992fb This is another commit

Undoing a commit?

How do you list files in the git branch?

Creating and merging branches.

Resolving conflicting file versions.

Good for collecting students' homework assignments. "Your code has to be
posted to this repository by a certain date/time."

Forking, cloning

    git remote add upstream http://github.com/wltrimbl/testrepo-2013-11-14-woodshole.git

    flcellogrl@flcellogrl:~/testrepo-2013-11-14-woodshole$ git remote -v
    origin  https://github.com/ljcohen/testrepo-2013-11-14-woodshole/ (fetch)
    origin  https://github.com/ljcohen/testrepo-2013-11-14-woodshole/ (push)
    upstream    http://github.com/wltrimbl/testrepo-2013-11-14-woodshole.git (fetch)
    upstream    http://github.com/wltrimbl/testrepo-2013-11-14-woodshole.git (push)

Green compare and review button.  
Must press green "Push request" button.
