Title: Longest Common Substring Problem
Date: 2013-09-25 12:12
Author: monsterbashseq
Category: Bioinformatics, Python
Slug: longest-common-substring-problem
Status: published

To find a [shared motif between a collection of nucleic acid
sequences](http://rosalind.info/problems/lcsm/), skills for solving the
[longest common substring
problem](http://en.wikipedia.org/wiki/Longest_common_substring_problem)
are needed.

Suffix Trees, Dynamic Programming:

http://www.cs.cmu.edu/\~ckingsf/bioinfo-lectures/suffixtrees.pdf

http://en.wikibooks.org/wiki/Algorithm\_Implementation/Strings/Longest\_common\_substring\#Python

    function LCSubstr(S[1..m], T[1..n])
        L := array(1..m, 1..n)
        z := 0
        ret := {}
        for i := 1..m
            for j := 1..n
                if S[i] == T[j]
                    if i == 1 or j == 1
                        L[i,j] := 1
                    else
                        L[i,j] := L[i-1,j-1] + 1
                    if L[i,j] > z
                        z := L[i,j]
                        ret := {S[i-z+1..i]}
                    elif L[i,j] == z
                        ret := ret ∪ {S[i-z+1..i]}
                else L[i,j]=0;
        return ret
