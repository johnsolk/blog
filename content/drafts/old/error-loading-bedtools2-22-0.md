Title: Error loading bedtools/2.22.0
Date: 2015-04-14 12:08
Author: monsterbashseq
Category: bash, Bioinformatics, Python
Slug: error-loading-bedtools2-22-0
Status: published

By default, gcc/4.4 is loaded in my cluster environment. This happened
when running bedtools:

` gcc/4.7.0(5):ERROR:150: Module 'gcc/4.7.0' conflicts with the currently loaded module(s) 'gcc/4.4' gcc/4.7.0(5):ERROR:102: Tcl command execution failed: conflict gcc/4.4`

bedtools/2.22.0(6):ERROR:151: Module 'bedtools/2.22.0' depends on one of
the module(s) 'gcc/4.7.0'  
bedtools/2.22.0(6):ERROR:102: Tcl command execution failed: prereq
gcc/4.7.0  
</code>

To fix, first module unload gcc/4.4 then module load gcc/4.7.0.

Edited my cluster.py custom module 'qsub\_sge\_file' function, which I
use for all of my commandline bioinformatics pipelines to create a
standard bash shell script and qsub submit as job to Sun Grid Engine, to
include a line checking if 'bedtools' is being loaded:

` module_load=['gcc/4.7.0','samtools','bedtools'] if any('bedtools' in s for s in module_load):      sge_file.write('module unload gcc/4.4\n')`

Then, module load gcc/4.7.0.

` module_list=[] for module in module_name_list:     module_load="module load "+module     module_list.append(module_load)`
