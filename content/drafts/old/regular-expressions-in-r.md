Title: Regular Expressions in R
Date: 2013-10-16 21:58
Author: monsterbashseq
Category: R
Slug: regular-expressions-in-r
Status: published

http://stackoverflow.com/questions/10294284/remove-all-special-characters-from-a-string-in-r

http://stackoverflow.com/questions/6240026/regular-expressions-in-r-to-erase-all-characters-after-the-first-space

Removing special characters in R:

    new_homicides<-gsub("<[^>]+>","",homicides)
