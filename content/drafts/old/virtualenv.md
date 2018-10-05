Title: virtualenv
Date: 2013-05-03 20:19
Author: monsterbashseq
Category: Python, Ubuntu, virtualenv
Slug: virtualenv
Status: published

Installing Python on Ubuntu.

Installing Biopython on Ubuntu.

Dealing with vcf and gatk modules to evntually use in a Python pipeline
script. The documentation for those are here:

<https://github.com/chapmanb/bcbio-nextgen>  
<https://github.com/jamescasbon/PyVCF>

Here are the Linux command lines to setup the Python virtualenv (virtual
environment) and install pip (python installation package):

    flcellogrl@purplebanyan:~$ sudo apt-get install python-pip python-dev build-essential 
    flcellogrl@purplebanyan:~$ sudo pip install --upgrade pip 
    flcellogrl@purplebanyan:~$ sudo pip install --upgrade virtualenv 

    then, use the virtualenv and pip to setup the virtual environment (bioinformatics) and install the packages you want:

`flcellogrl@purplebanyan:~$ virtualenv -p /usr/bin/python3 bioinformatics`

`flcellogrl@purplebanyan:~$ source bioinformatics/bin/activate `

\*\*\*note how the commandline changes\*\*\*

`(bioinformatics)flcellogrl@`</tt>`purplebanyan:~$ pip install pyvcf `

`(bioinformatics)flcellogrl@purplebanyan:~/bioinformatics$ python idle_bioinformatics.py`  
`(bioinformatics)flcellogrl@purplebanyan:~$ pip install --upgrade bcbio-nextgen`

Now you want to setup an IDLE use you can use the bioinformatics
virtualenv.

> You should be able to just do this:  
> flcellogrl@purplebanyan:\~\$ bioinformatics/idle\_bioinformatics.py

First mark it as executable, like this:

chmod u+x bioinformatics/idle\_bioinformatics.py

Now, the Python modules are all installed and ready to be used.

https://pypi.python.org/pypi/virtualenv
