Title: Reproducible Research Using Rmarkdown - NGS2015 Week 3
Date: 2015-08-25 19:28
Author: monsterbashseq
Category: Genomics Workshop, github, R, reproducibility, workshops
Slug: reproducible-research-using-rmarkdown-ngs2015-week-3
Status: published

Tutorial by Marian Schmidt, PhD candidate at the University of Michigan
and Software Carpentry instructor.

Fun presentation! Have used [knitR and Rmarkdown for analysis script
files
before](http://ljcohen.github.io/analyses/Blanco/DESeq2_Blanco_invivo_June2015.html),
but I didn't even know that github could be accessed through the RStudio
interface. Appreciated spending time on these tasks discussing how to
automate, generate report, and documenting workflow.

However, I couldn't actually get my RStudio to connect to my github
account. (See bottom explanation and screenshot with errors.) Any help
or suggestions for how to proceed with this would be greatly
appreciated! Google results didn't come up with much, but probably
missing something. Otherwise, could make and push .Rmd files to github
via commandline, great.

**Tutorial**

Marian's Link, great *Key Resources* listed on the page, go look!

http://rpubs.com/marschmi/105639

How is everyone feeling? [Who is Amy
Cuddy?](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0CCkQtwIwAWoVChMI2ayk5o3FxwIVS-KACh3DAwzV&url=http%3A%2F%2Fwww.ted.com%2Ftalks%2Famy_cuddy_your_body_language_shapes_who_you_are%3Flanguage%3Den&ei=t9TcVZn1DsvEgwTDh7CoDQ&usg=AFQjCNHlD-yrscyq-C1cAvc8Jjr8tCbv_g&sig2=2Zsq9uFhr9aCmFLm57Yg4Q)
Do a power pose!

https://www.flickr.com/photos/lpcohen/20693806009/

What do you need to reproduce Figure?  
- data  
- metadata  
- programs and parameters  
- error bars  
- explanation of methods  
- pipeline workflow  
- explanations for legend (what does "a" and "ab" mean, e.g.)  
- versions of software and packages used

Producing a figure removes the figure from the scientific code used to
generate the figure. Unless you have someone looking at your code, using
it to produce similar figures. Let's keep figures and code connected.

Suggestion for hackathons with people using similar code to put in
different datasets, test, everyone is thinking about the code, using the
code, and making sure it is robust.

Write code for yourself in 6 months, so that you will like yourself. :)

Post your code online! (Yes, you really need to do this...)

Cannot automate tasks or make science reproducible with .xls
spreadsheets with notes and color coding. We've all seen this from
colleagues. It's OK to suggest to people you see doing this that there
is a better way. Discussion for how to do this with a positive angle.
For example: "Your data are cool. There is an easy way that requires R
or Python to automate what you are doing. I am happy to help if you are
interested." If someone closer to you personally, like a labmate, shame
and humor can be used. :)

Use pre-existing libraries and packages when possible. Groups of people
testing these functions, then goes out into 'Rsphere'.

Where are your files? If you wanted to go to a project, and look at the
most current results you are working on. Where are they? Could you send
a link to collaborators?

Last fall, conference to discuss how to make science more reproducible.
Suggested this file structure:

https://github.com/Reproducible-Science-Curriculum/rr-init

Computing notebooks should be as ubiquitous and thorough as wet lab
notebooks. This is SO important. Document all of these things for every
single project at all steps:

-   Document your methods and workflows
-   Document the origin of all data in your project directory
-   Document when and how you downloaded the data
-   Record data version info
-   Record software version info with session\_info()

You can use an Rmarkdown file to do this. Using inline code to make
creation of tables much easier if the data change. Write pdf() and
images. Relative paths instead of absolute paths. Use seed.seed() for
randomizations. Parts of my workflow to change:

<ul>
<ul>
-   session\_info
-   absolute paths
-   saving figures with pdf() instead of by hand
-   write code as though I'm sharing it
-   comment moreIn github, make repository.

</ul>
</ul>
Install:

    install.packages("knitr")
    install.packages("rmarkdown")
    library("knitr")
    library("rmarkdown")

**Here's where the problem started:**

From RStudio, must go to Preferences and specify Git executable. You
should then be able to connect your github repository to your RStudio
and push changes directly from the RStudio GUI. Unfortunately, I got
derailed and my RStudio showed this error message,

![git\_error](https://monsterbashseq.files.wordpress.com/2015/08/git_error.png?w=300){.alignnone
.size-medium .wp-image-1037 width="300" height="213"}

     
    ProductName:    Mac OS X
    ProductVersion: 10.9.5
    BuildVersion:   13F34

Even though my git is installed and functional on the commandline, path
to git executable input to RStudio will not work and keeps indicating
that git is not detected on the system path. I even deleted RStudio,
downloaded the lastest version (since mine was old). It still could not
detect git in system path. What to do?

[![git\_exe](https://monsterbashseq.files.wordpress.com/2015/08/git_exe3.png?w=300){.alignnone
.size-medium .wp-image-1038 width="300"
height="281"}](https://monsterbashseq.files.wordpress.com/2015/08/git_exe3.png)

Here is my git and path:

[![which\_git](https://monsterbashseq.files.wordpress.com/2015/08/which_git.png?w=300){.alignnone
.size-medium .wp-image-1040 width="300"
height="26"}](https://monsterbashseq.files.wordpress.com/2015/08/which_git.png)

[![path](https://monsterbashseq.files.wordpress.com/2015/08/path.png?w=300){.alignnone
.size-medium .wp-image-1039 width="300"
height="28"}](https://monsterbashseq.files.wordpress.com/2015/08/path.png)

Had lots of help trying to figure this out during the tutorial and could
proceed just not with GUI. Something weird is going on.

From the commandline, can push files to github repo so really not a big
deal. Here is some of the output from the practice script we did as a
class, yay .Rmd works!

http://ljcohen.github.io/NGS\_Reproducibility/MultivariateAnalysesusingRmarkdown.html

https://github.com/ljcohen/NGS\_Reproducibility/blob/gh-pages/MultivariateAnalysesusingRmarkdown.html

(This .html file is viewable from the web from the NGS\_Reproducibility
repo by adding "gh-pages" branch in this repo,then accessing via
ljcohen.github.io server name.)

Suggestion for educator to look up and read publications on Peer
Instruction: Dr. Eric Mazur, Physics Instructor at Harvard:
http://mazur.harvard.edu/education/educationmenu.php
