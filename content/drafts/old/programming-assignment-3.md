Title: Programming Assignment 3
Date: 2013-10-13 14:27
Author: monsterbashseq
Category: Coursera, R
Slug: programming-assignment-3
Status: published

Plotting outcome of hospital care data,

    > outcome <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
    > outcome[, 11] <- as.numeric(outcome[, 11])
    Warning message:
    NAs introduced by coercion 
    > hist(outcome[, 11],xlab="30-Day Death Rate",main="Heart Attack 30-day Death Rate")

[![Rplot\_hist\_outcome\_labels](http://monsterbashseq.files.wordpress.com/2013/10/rplot_hist_outcome_labels.jpeg){.alignnone
.size-full .wp-image-392 width="640"
height="387"}](http://monsterbashseq.files.wordpress.com/2013/10/rplot_hist_outcome_labels.jpeg)

Part 2

Note: Could not get this to work.

    > a<-as.numeric(outcome$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack)
    > b<-as.numeric(outcome$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure)
    > c<-as.numeric(outcome$Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia)
    > death_rate_range <- range(c(outcome[,17],outcome[,11],outcome[,23]), na.rm = TRUE)
    > 

On the forums, this is what someone suggested:

    > heart_attack=na.omit(outcome[,11])
    > heart_failure=na.omit(outcome[,17])
    > pneumonia=na.omit(outcome[,23])

Part 3

 

    > outcome<-read.csv("outcome-of-care-measures.csv",colClasses="character")
    > outcome[,11]<-as.numeric(outcome[,11])
    > x<-table(outcome$State)
    > sub_x<-subset(x,x>=20)
    > sub_x_names<-names(sub_x)
    > outcome2<-subset(outcome,outcome$State %in% sub_x_names)
