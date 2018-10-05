Title: reduce pdf file size
Date: 2013-05-27 11:16
Author: monsterbashseq
Category: Linux, Ubuntu
Slug: reduce-pdf-file-size
Status: published

http://www.alfredklomp.com/programming/shrinkpdf/

flcellogrl@purplebanyan:\~\$ sudo apt-get install ghostscript  
\[sudo\] password for flcellogrl:  
Reading package lists... Done  
Building dependency tree  
Reading state information... Done  
ghostscript is already the newest version.  
ghostscript set to manually installed.  
The following packages were automatically installed and are no longer
required:  
guile-1.8-libs python-speechd liblouis2 python-brlapi python-louis  
gnome-games-data linux-headers-3.5.0-23 liblouis-data  
linux-headers-3.5.0-23-generic  
Use 'apt-get autoremove' to remove them.  
0 upgraded, 0 newly installed, 0 to remove and 9 not upgraded.  
flcellogrl@purplebanyan:\~\$ gs -sDEVICE=pdfwrite
-dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH
-sOutputFile=Lisacohen\_BS\_new.pdf
LisaCohen\_EckerdCollege\_BStranscript\_2002.pdf  
Error: /undefinedfilename in
(LisaCohen\_EckerdCollege\_BStranscript\_2002.pdf)  
Operand stack:

Execution stack:  
%interp\_exit   .runexec2   --nostringval--   --nostringval--  
--nostringval--   2   %stopped\_push   --nostringval--  
--nostringval--   --nostringval--   false   1   %stopped\_push  
Dictionary stack:  
--dict:1164/1684(ro)(G)--   --dict:0/20(G)--   --dict:77/200(L)--  
Current allocation mode is local  
Last OS error: 2  
GPL Ghostscript 9.05: Unrecoverable error, exit code 1  
flcellogrl@purplebanyan:\~\$ gs -sDEVICE=pdfwrite
-dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH
-sOutputFile=Lisacohen\_BS\_new.pdf
LisaCohen\_EckerdCollege\_BStranscript\_2002.pdf  
Error: /undefinedfilename in
(LisaCohen\_EckerdCollege\_BStranscript\_2002.pdf)  
Operand stack:

Execution stack:  
%interp\_exit   .runexec2   --nostringval--   --nostringval--  
--nostringval--   2   %stopped\_push   --nostringval--  
--nostringval--   --nostringval--   false   1   %stopped\_push  
Dictionary stack:  
--dict:1164/1684(ro)(G)--   --dict:0/20(G)--   --dict:77/200(L)--  
Current allocation mode is local  
Last OS error: 2  
GPL Ghostscript 9.05: Unrecoverable error, exit code 1  
flcellogrl@purplebanyan:\~\$ ls  
bioinformatics  Documents  Dropbox           Lisacohen\_BS\_new.pdf 
Pictures  R                       Templates   Videos  
Desktop         Downloads  examples.desktop  Music                
Public    temp Dropbox 5.27.2013  Ubuntu One  
flcellogrl@purplebanyan:\~\$ cd Dropbox  
flcellogrl@purplebanyan:\~/Dropbox\$ ls  
bahamas         Files with Lisa  Jobs                 Lisa and Ana   
misc    Public           St.Eve               to-do\_4.25.2013.txt\~  
Camera Uploads  Grad School      Kim and Lisa         Lisa and Peter 
Music   punta cana 2013  to-do\_4.13.2013.txt  Tursiops  
CS              HBOI             links\_4.24.2013.txt  MBEAB          
Photos  Sara and Lisa    to-do\_4.25.2013.txt  VBCO pics for website  
flcellogrl@purplebanyan:\~/Dropbox\$ cd Grad School  
bash: cd: Grad: No such file or directory  
flcellogrl@purplebanyan:\~/Dropbox\$ ls  
bahamas         Files with Lisa  Jobs                 Lisa and Ana   
misc    Public           St.Eve               to-do\_4.25.2013.txt\~  
Camera Uploads  Grad School      Kim and Lisa         Lisa and Peter 
Music   punta cana 2013  to-do\_4.13.2013.txt  Tursiops  
CS              HBOI             links\_4.24.2013.txt  MBEAB          
Photos  Sara and Lisa    to-do\_4.25.2013.txt  VBCO pics for website  
flcellogrl@purplebanyan:\~/Dropbox\$ cd Grad School  
bash: cd: Grad: No such file or directory  
flcellogrl@purplebanyan:\~/Dropbox\$ sh shrinkpdf.sh
LisaCohen\_EckerdCollege\_BStranscript\_2002.pdf  
sh: 0: Can't open shrinkpdf.sh  
flcellogrl@purplebanyan:\~/Dropbox\$ cd  
flcellogrl@purplebanyan:\~\$ cd Dropbox  
flcellogrl@purplebanyan:\~/Dropbox\$ cd "Grad School"  
flcellogrl@purplebanyan:\~/Dropbox/Grad School\$ ls  
advice.txt  Grad School 2006  links.txt                 My
application            schools.txt  
EMBL-EBI    GRE               M02\_Kellis\_Thesis\_03.pdf  Nature
2011\_PhD.pdf       short bio for HBOI website.txt  
FAU         Jackson Labs.txt  MiamiU-Ohio               programs to
apply to.txt  UF  
flcellogrl@purplebanyan:\~/Dropbox/Grad School\$ cd "My application"  
flcellogrl@purplebanyan:\~/Dropbox/Grad School/My application\$ sh
shrinkpdf.sh LisaCohen\_EckerdCollege\_BStranscript\_2002.pdf  
flcellogrl@purplebanyan:\~/Dropbox/Grad School/My application\$ sh
shrinkpdf.sh

 

You can change the resolution to adjust for desired file size. For some
reason, there is no difference between resolution of 90 and 99, but
there is between 90 and 100.

\#!/bin/sh

gs    -q -dNOPAUSE -dBATCH -dSAFER \\  
-sDEVICE=pdfwrite \\  
-dCompatibilityLevel=1.3 \\  
-dPDFSETTINGS=/screen \\  
-dEmbedAllFonts=true \\  
-dSubsetFonts=true \\  
-dColorImageDownsampleType=/Bicubic \\  
-dColorImageResolution=99 \\  
-dGrayImageDownsampleType=/Bicubic \\  
-dGrayImageResolution=99 \\  
-dMonoImageDownsampleType=/Bicubic \\  
-dMonoImageResolution=99 \\  
-sOutputFile=out.pdf \\  
\$1

 

 
