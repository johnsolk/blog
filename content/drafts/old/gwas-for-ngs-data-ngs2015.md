Title: GWAS for NGS data - NGS2015
Date: 2015-08-26 22:29
Author: monsterbashseq
Category: Genomics Workshop
Slug: gwas-for-ngs-data-ngs2015
Status: published

Dr. Tiffany Timbers, [postdoc at Simon Fraser
University](http://tiffanytimbers.com/). Became interested in automating
and programming from Multiworm tracker, automated image analyses for
worm behavioral studies.

https://www.flickr.com/photos/lpcohen/20917921421/

Today we will use a dataset from 2,007 individuals, 700,000 variants,
20,000 genes potentially contain disruptive alleles.

GWAS vs. SNP microarrays. Differences and similarities? Example of
question typically asked with GWAS analyses, "Do I rescue the mutant by
knocking out a region with significant SNP activity?"

Really cool website, facilitating classroom discussion with student
input-typed answers:  
Code: F321E8CC  
https://b.socrative.com/student/\#take-quiz/q/1

Power analyses to consider with GWAS from NGS vs. microarray, difficult
to estimate effect sizes. Work needs to be done on how to do a power
analysis for this type of study. Haplotype matrix, not a lot of good
data available to generate this in non-human populations. Have to come
up with own methods for determining robust design. Positives of GWAS for
NGS data include being able to call rare variants. Take region with
groupings, gene level rather than on variant-level. What are you doing
with intergenic data? Very new type of analysis. How important is this?
When severe mutations are of interest in isolated population vs. natural
population. Indels vs. copy number variants.

Sequence kernel association test (SKAT): linear model  
disease/phenotype = alpha + (alpha1)covariants (e.g. age, sex) +
(beta)variantsets ( e.g. genes) + epsilon

SKAT R package documentation:  
https://cran.r-project.org/web/packages/SKAT/SKAT.pdf

SKAT paper, Wu et al. Am. J. Hum. Genet. 2011:  
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3135811/pdf/main.pdf

**Tutorial**

(Proceed with amazing, well-worked out install instructions. All the
code instructions for this whole tutorial are great - solid and work.
Really appreciate having location instructions at beginning of each code
block. :)  
https://github.com/ttimbers/SKAT\_NGS-2015/blob/master/Setup-for-gwas-on-EC2.md

https://github.com/ttimbers/SKAT\_NGS-2015/blob/master/NGS\_GWAS\_via\_SKAT.md

Tiffany: "Ignore all warnings, say 'yes' to everything, and it will
work." If it doesn't work, kill the machine, start over. Computers are
fun. Tweeting lots of quotes, \#ngs2015. :) Future for Docker. Tiffany:
dplyr is worth it. Titus: R did something better than Python. See Jenny
Bryan, stat545:

https://stat545-ubc.github.io/bit001\_dplyr-cheatsheet.html

Let's look at data. There are some .vcf files, there are a lot. Here are
the first 5. we need to put them all together into a massive .vcf file
to look at whole population. We're only going to look at chromosome 4
because it makes the data more manageable for this tutorial.

Here is .vcf format:

[![first5vcffiles](https://monsterbashseq.files.wordpress.com/2015/08/first5vcffiles.png?w=300){.alignnone
.size-medium .wp-image-1078 width="300"
height="67"}](https://monsterbashseq.files.wordpress.com/2015/08/first5vcffiles.png)

[![vcf](https://monsterbashseq.files.wordpress.com/2015/08/vcf.png?w=300){.alignnone
.size-medium .wp-image-1079 width="300"
height="90"}](https://monsterbashseq.files.wordpress.com/2015/08/vcf.png)

[![vcf\_info](https://monsterbashseq.files.wordpress.com/2015/08/vcf_info.png?w=300){.alignnone
.size-medium .wp-image-1080 width="300"
height="46"}](https://monsterbashseq.files.wordpress.com/2015/08/vcf_info.png)

We will use vcf-merge, takes a minute:

    vcf-merge data/*.vcf.gz | bgzip -c > MMP_vcf-merge.vcf.gz

Here is the merged file, 1.3 M:

[![merged\_vcf](https://monsterbashseq.files.wordpress.com/2015/08/merged_vcf.png?w=300){.alignnone
.size-medium .wp-image-1081 width="300"
height="19"}](https://monsterbashseq.files.wordpress.com/2015/08/merged_vcf.png)

VCF-tools is silly and puts "." in output. We need "0/0" to move on.
Tiffany figured out this awk command to use to change that.

[![awk](https://monsterbashseq.files.wordpress.com/2015/08/awk.png?w=300){.alignnone
.size-medium .wp-image-1082 width="300"
height="44"}](https://monsterbashseq.files.wordpress.com/2015/08/awk.png)

This worked and is amazing:

[![awk\_works](https://monsterbashseq.files.wordpress.com/2015/08/awk_works.png?w=300){.alignnone
.size-medium .wp-image-1083 width="300"
height="44"}](https://monsterbashseq.files.wordpress.com/2015/08/awk_works.png)

Enthusiasm from class at 8:45pm.

No best practices in field right now. Decisions that follow are
investigator-specific. We're going to only look at coding regions.
Throwing out everything, e.g. silent mutations, intergenic regions, etc.
With clunky but amazing grep command:

[![grep\_cds](https://monsterbashseq.files.wordpress.com/2015/08/grep_cds1.png?w=300){.alignnone
.size-medium .wp-image-1085 width="300"
height="61"}](https://monsterbashseq.files.wordpress.com/2015/08/grep_cds1.png)

Get data in R:  
[![r\_table](https://monsterbashseq.files.wordpress.com/2015/08/r_table.png?w=300){.alignnone
.size-medium .wp-image-1087 width="300"
height="121"}](https://monsterbashseq.files.wordpress.com/2015/08/r_table.png)

Overheard: Don't have to understand everything as long as the desired
output comes out.

Create pheno\_file and fam\_file:

[![pheno\_file](https://monsterbashseq.files.wordpress.com/2015/08/pheno_file.png?w=300){.alignnone
.size-medium .wp-image-1088 width="300"
height="110"}](https://monsterbashseq.files.wordpress.com/2015/08/pheno_file.png)

Join and drop files, rename colnames:  
[![phenotypes](https://monsterbashseq.files.wordpress.com/2015/08/phenotypes.png?w=300){.alignnone
.size-medium .wp-image-1089 width="300"
height="160"}](https://monsterbashseq.files.wordpress.com/2015/08/phenotypes.png)

Now association analysis, gene by gene. The more SNPs you have, the
longer it takes. Lex: Suggestion Jones et al. 2012 stickleback sliding
window approach.

Set seed to 100, so p values are reproducible. Run SKAT.SSD.ALL, but we
won't do that. Open saved data file with output, as this takes too long
to perform during class. Compares with null model.

Apply multiple testing correction with library(fdrtool). Sort. Cutoff.

R is [cromulent](https://en.wikipedia.org/wiki/Lisa_the_Iconoclast).

SNPs:

[![SNPs](https://monsterbashseq.files.wordpress.com/2015/08/snps.png?w=300){.alignnone
.size-medium .wp-image-1090 width="300"
height="193"}](https://monsterbashseq.files.wordpress.com/2015/08/snps.png)

Shouldn't just take this information and run with it. Columns 4 and 5
(integers) indicate number of times this SNP ID occurs, some are 2 and 3
in entire dataset. You will have to figure out how many times you will
tolerate mutations to call it significant. Plot histogram, what are the
minor allele count. Could use cluster and pathway analyses, gene
adjacency to define SNP sets. Be careful with GO terms and pathway
analyses for SNP analyses. These are pitfalls. Really cool, new
software! But, more people need to be talking about this, developing
these tools further. And know how it works. Great opportunity with this
tutorial to review this workflow.

Frequency of allele counts for \# genes:

[![histo](https://monsterbashseq.files.wordpress.com/2015/08/histo.png?w=286){.alignnone
.size-medium .wp-image-1091 width="286"
height="300"}](https://monsterbashseq.files.wordpress.com/2015/08/histo.png)

This is where "p hacking" comes in to determine what is reasonable
variance to be in SNP set. No answer.

Throw SSID into R, throw away everything less than 5 variants to keep in
data set. From histogram above, all small allele counts (largest number
of genes) will be thrown away. Commence R joining plyr and dplyr
genes-to-include magic...and voila:

[![reduced\_SSID](https://monsterbashseq.files.wordpress.com/2015/08/reduced_ssid.png?w=300){.alignnone
.size-medium .wp-image-1092 width="300"
height="82"}](https://monsterbashseq.files.wordpress.com/2015/08/reduced_ssid.png)

Null model for SKAT doesn't change. Run, this takes a long time so we
will open reduced data output file. Now SKAT reduced results look more
reasonable to use for further interpretation.

[![reduced\_SKAT](https://monsterbashseq.files.wordpress.com/2015/08/reduced_skat.png?w=300){.alignnone
.size-medium .wp-image-1093 width="300"
height="193"}](https://monsterbashseq.files.wordpress.com/2015/08/reduced_skat.png)
