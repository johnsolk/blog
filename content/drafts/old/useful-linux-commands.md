Title: Useful Linux commands
Date: 2015-03-12 17:31
Author: monsterbashseq
Category: bash, Linux
Slug: useful-linux-commands
Status: published

Decompress a gzipped tar file:  
` tar -xzvf file.tar.gz`  
Or just a tar file:  
` tar -xvf file.tar`  
Install program:  
` tar -xzvf rsem-1.2.8.tar.gz cd rsem-1.2.8 make cd EBSeq make echo 'export PATH=$PATH:/root/rsem-1.2.8' >> ~/.bashrc source ~/.bashrc`  
Screen command, when you want to break your ssh connection but still
want process to run and see output later. Use Ctrl-A-D to detach
screen.  
` screen screen -r screen -r 11074.pts-25.phoenix2`  
Find latest 10 subdirectories by date:  
` find /ifs/data/sequence/Illumina/production/ -maxdepth 1 -type d -mtime -10 | sed -e 's/.*\///' | sort`
