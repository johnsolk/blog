Title: Plotting Data in R
Date: 2013-10-13 09:34
Author: monsterbashseq
Category: Coursera, R
Slug: plotting-data-in-r
Status: published

Base vs. Lattice graphics, examples from "Computing for Data Analysis"
Week 3 lectures by Dr. Roger Peng (Johns Hopkins/Coursera) and R
datasets:

https://www.coursera.org/course/compdata

**Base Graphing**

Base parameter documentation, use this:

    >?par

Using base graphics **plot()**, add a title (**main=""**) and axis
labels (**xlab=""**, **ylab=""**) like this:

    >plot(x,y,main="Eruptions of Old faithful",xlab="eruption time(x)",ylab="waiting time (min)")

[![R\_testgraph](http://monsterbashseq.files.wordpress.com/2013/10/r_testgraph.jpeg){.alignnone
.size-full .wp-image-348 width="535"
height="394"}](http://monsterbashseq.files.wordpress.com/2013/10/r_testgraph.jpeg)  
\[1\]
http://stat.ethz.ch/R-manual/R-devel/library/graphics/html/text.html  
\[2\]
http://www.dummies.com/how-to/content/how-to-add-titles-and-axis-labels-to-a-plot-in-r.html  
\[3\] http://stackoverflow.com/questions/3453695/adding-text-to-a-plot  
\[4\]
http://stackoverflow.com/questions/12121060/adding-text-to-a-plot-axes-without-removing-existing-axes-labels-in-r

You can also use separate title("") and text(x,y,"") where the x,y
coordinates will specify where on the graph the text will be displayed.

[![Screenshot from 2013-10-13
10:47:29](http://monsterbashseq.files.wordpress.com/2013/10/screenshot-from-2013-10-13-104729.png){.alignnone
.size-full .wp-image-358 width="287"
height="187"}](http://monsterbashseq.files.wordpress.com/2013/10/screenshot-from-2013-10-13-104729.png)

[![Rplot\_scatterplotexample\_ablinedefault](http://monsterbashseq.files.wordpress.com/2013/10/rplot_scatterplotexample_ablinedefault.jpeg){.alignnone
.size-full .wp-image-359 width="535"
height="394"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_scatterplotexample_ablinedefault.jpeg)

    >abline(fit,lwd=3,col="blue")

[![Rplot\_abline\_lwd3\_colblue](http://monsterbashseq.files.wordpress.com/2013/10/rplot_abline_lwd3_colblue.jpeg){.alignnone
.size-full .wp-image-361 width="535"
height="394"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_abline_lwd3_colblue.jpeg)

Fit more than one plot in a graphic with this:

    > par(mar=c(2,2,1,1))
    > par(mfrow=c(2,2))
    > plot(x,y)
    > plot(x,z)
    > plot(z,x)
    > plot(y,x)

[![Rplot\_mfrow2\_2](http://monsterbashseq.files.wordpress.com/2013/10/rplot_mfrow2_2.jpeg){.alignnone
.size-full .wp-image-365 width="535"
height="394"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_mfrow2_2.jpeg)

Subset data, then use **points()** function to sequentially add each
subset to the plot and differentiate between the two with different
colors, or symbols, etc.

    > par(mfrow=c(1,2))
    > x<-rnorm(100)
    > y<-x+rnorm(100)
    > g<-gl(2,50,labels=c("Male","Female"))
    > str(g)
     Factor w/ 2 levels "Male","Female": 1 1 1 1 1 1 1 1 1 1 ...
    > plot(x,y)
    > plot(x,y,type="n")
    > points(x[g=="Male"],y[g=="Male"],col="green")
    > points(x[g=="Female"],y[g=="Female"],col="blue")

[![Rplot\_points](http://monsterbashseq.files.wordpress.com/2013/10/rplot_points.jpeg){.alignnone
.size-full .wp-image-368 width="535"
height="394"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_points.jpeg)

Labels need to be added and the margins with **par(mar=c(a,b,c,d))**
need to be adjusted so the plotting graphics are sized more
appropriately. But, you get the idea.

See an example of **pch** point options available in the base graphics
plotting function **plot()**:

    >example(points)

[![pch\_plotsymbols](http://monsterbashseq.files.wordpress.com/2013/10/pch_plotsymbols.jpeg){.alignnone
.size-full .wp-image-355 width="535"
height="394"}](http://monsterbashseq.files.wordpress.com/2013/10/pch_plotsymbols.jpeg)

**Lattice Graphing**

The main advantage is in specifying conditional variables after the |
allowing you to visualize relationships with a lattice of variables. You
will sometimes end up writing separate functions embedded within the
function calls so that one long function call will produce one graphic.
Whereas base graphing consists of multiple single line function calls to
set up and edit the graphic. Lattice Graphics documentation:

    > package ? lattice

Insert text here.

    > library(lattice)
    > library(nlme)
    > xyplot(distance~age|Subject,data=Orthodont, type="b")

[![Rplot\_latticeOrthodont\_typeb](http://monsterbashseq.files.wordpress.com/2013/10/rplot_latticeorthodont_typeb.jpeg){.alignnone
.size-full .wp-image-372 width="508"
height="415"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_latticeorthodont_typeb.jpeg)

    > data(environmental)
    > ?environmental
    > head(environmental)
      ozone radiation temperature wind
    1    41       190          67  7.4
    2    36       118          72  8.0
    3    12       149          74 12.6
    4    18       313          62 11.5
    5    23       299          65  8.6
    6    19        99          59 13.8
    > xyplot(ozone~radiation,data=environmental)

In the last **xyplot()** function call, the **data=environmental**
argument after the **,** tells the function which data structure to go
to look up the variables **ozone** and **radiation**.  
[![Rplot\_lattice\_environmentalscatter](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmentalscatter.jpeg){.alignnone
.size-full .wp-image-373 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmentalscatter.jpeg)

    > temp.cut<-equal.count(environmental$temperature,4)
    > xyplot(ozone~radiation|temp.cut,data=environmental)

[![Rplot\_lattice\_environmental\_temp.cut](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_temp-cut.jpeg){.alignnone
.size-full .wp-image-376 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_temp-cut.jpeg)

    > xyplot(ozone~radiation|temp.cut,data=environmental, layout=c(1,4),as.table=TRUE)

[![Rplot\_lattice\_environmental\_tempcut\_layout1\_4](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_layout1_4.jpeg){.alignnone
.size-full .wp-image-377 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_layout1_4.jpeg)

    xyplot(ozone~radiation|temp.cut,data=environmental,as.table=TRUE, pch=20
           panel=function(x,y,...){
                 panel.xyplot(x,y,...)
                 fit<-lm(y~x)
                 panel.abline(fit,lwd=2)     
           })

[![Rplot\_lattice\_environmental\_tempcut\_regressionlinefunction](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_regressionlinefunction1.jpeg){.alignnone
.size-full .wp-image-380 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_regressionlinefunction1.jpeg)

    xyplot(ozone~radiation|temp.cut,data=environmental,as.table=TRUE, pch=20,
           panel=function(x,y,...){
                 panel.xyplot(x,y,...)
                 panel.loess(x,y)
           }, xlab="Solar Radiation",ylab="Ozone (ppb)",
           main="Ozone vs. Solar Radiation")

[![Rplot\_lattice\_environmental\_tempcut\_loessregression\_axislabels](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_loessregression_axislabels.jpeg){.alignnone
.size-full .wp-image-382 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_loessregression_axislabels.jpeg)

    > wind.cut<-equal.count(environmental$wind,4)
    > xyplot(ozone~radiation|temp.cut*wind.cut,data=environmental,as.table=TRUE, pch=20,
           panel=function(x,y,...){
                 panel.xyplot(x,y,...)
                 panel.loess(x,y)
           }, xlab="Solar Radiation",ylab="Ozone (ppb)",
           main="Ozone vs. Solar Radiation")

[![Rplot\_lattice\_environmental\_tempcut\_windcut\_loessregression\_axislabels](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_windcut_loessregression_axislabels.jpeg){.alignnone
.size-full .wp-image-384 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_lattice_environmental_tempcut_windcut_loessregression_axislabels.jpeg)

    > splom(~environmental)

[![Rplot\_splom](http://monsterbashseq.files.wordpress.com/2013/10/rplot_splom.jpeg){.alignnone
.size-full .wp-image-386 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_splom.jpeg)

More references on plotting in R:

-   http://www.sr.bham.ac.uk/\~ajrs/R/r-gallery.html
-   http://www.cyclismo.org/tutorial/R/plotting.html
-   http://cran.r-project.org/doc/contrib/usingR.pdf
-   http://people.su.se/\~lundh/reproduce/introduction\_plot.pdf
-   https://www.stat.auckland.ac.nz/\~ihaka/120/Notes/ch03.pdf
-   http://www.stat.berkeley.edu/\~statcur/WorkshopBC/Presentations/Graphics/graphics.pdf
-   http://gettinggeneticsdone.blogspot.com/2009/09/comparison-of-plots-using-stata-r-base.html
-   http://www.dummies.com/how-to/content/base-grid-and-lattice-graphics-in-r.html
-   http://astrostatistics.psu.edu/su07/R/html/lattice/html/Lattice.html
-   http://www.r-project.org/conferences/DSC-2001/Proceedings/Murrell.pdf

