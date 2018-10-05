Title: GitHub, Pull Requests, and ReadTheDocs - NGS2015
Date: 2015-08-28 10:57
Author: monsterbashseq
Category: Genomics Workshop
Slug: github-pull-requests-and-readthedocs-ngs2015
Status: published

"We're good enough and deserve github."

https://www.flickr.com/photos/lpcohen/20330046134/

[Dr. C. Titus Brown](http://ivory.idyll.org/lab/) shares methods for
using [readthedocs](https://readthedocs.org/), which he uses for classes
including [NGS2015](http://angus.readthedocs.org/en/2015/week3.html), as
well as github and forking pull requests.
[Sphinx](http://sphinx-doc.org/) is Python based, readthedocs is
web-based method for putting stuff in Sphinx. Learning goals at top of
lesson pages. We're going to go through steps on the web all together.
Screenshots become out of data too quickly.

http://angus.readthedocs.org/en/2015/week3/CTB\_github\_editing.html

Readthedocs will take some version controlled project from somewhere
(github or bitbucket) and format it for you. GitHub webhook activated.
Readthedocs will sync and automatically rebuild.

[![readthedocs](https://monsterbashseq.files.wordpress.com/2015/08/readthedocs.png?w=300){.alignnone
.size-medium .wp-image-1139 width="300"
height="200"}](https://monsterbashseq.files.wordpress.com/2015/08/readthedocs.png)

This is  my version of the readthedocs:

http://angus-ljcohen.readthedocs.org/en/stable/

Edit in github, this will update:

http://angus.readthedocs.org/en/2015/week3/merge-demo.html

Forking one repository with groups of people.

https://www.flickr.com/photos/lpcohen/20764676629/in/dateposted-public/

Titus makes changes in file. Pull in changes made in central repository.
My repo is behind:

[![behind\_repo](https://monsterbashseq.files.wordpress.com/2015/08/behind_repo.png?w=300){.alignnone
.size-medium .wp-image-1140 width="300"
height="162"}](https://monsterbashseq.files.wordpress.com/2015/08/behind_repo.png)

Pull requests: One of top useful things Titus has learned! Goal is to
keep track of changes, see progression.

Merge pull request, now all chnages updated. Click on "compare", if
there are any changes they will be highlighted. Once they are merged,
there will not be any more changes. Sometimes you need to switch head
fork to base fork accounts. Branches are very useful for years of
courses, versions of software, etc.

[![compare\_across\_forks](https://monsterbashseq.files.wordpress.com/2015/08/compare_across_forks.png?w=300){.alignnone
.size-medium .wp-image-1141 width="300"
height="127"}](https://monsterbashseq.files.wordpress.com/2015/08/compare_across_forks.png)

Leigh: What are best practices with group of pull requests? What is one
or some people are making tons, tons of changes? Should we pull? Master
branch. You can ignore until ready to be merged. They will tell you when
they want pull request, but they will have to reconcile with the one
true. Person who is making changes has to deal with everyone else's
changes so everyone else doesn't get behind. Software lines of code so
"bombs" do not mess up everyone else's code.

**The one true branch.**

https://www.flickr.com/photos/lpcohen/20329357194/in/dateposted-public/

Amanda: Where do people who have write access to the one true master
branch? Does she work in own fork? Those people can make their own fork
then merge and conflict reconcile with one true. There are 2 commits,
one to merge pull (fetch) from original, second to put change in.

Now, we make changes to files. Add names to attendees list:

https://github.com/ljcohen/angus/blob/2015/week3.rst

Now compare.

[![compare\_changes](https://monsterbashseq.files.wordpress.com/2015/08/compare_changes.png?w=300){.alignnone
.size-medium .wp-image-1142 width="300"
height="174"}](https://monsterbashseq.files.wordpress.com/2015/08/compare_changes.png)

[![commit\_code](https://monsterbashseq.files.wordpress.com/2015/08/commit_code.png?w=300){.alignnone
.size-medium .wp-image-1143 width="300"
height="73"}](https://monsterbashseq.files.wordpress.com/2015/08/commit_code.png)

Can search for commits, issues, and pull requests associated with this
code.

Merge conflicts  occur when computer can't resolve.

Win!

[![git\_commit](https://monsterbashseq.files.wordpress.com/2015/08/git_commit1.png?w=300){.alignnone
.size-medium .wp-image-1151 width="300"
height="171"}](https://xkcd.com/1296/)
