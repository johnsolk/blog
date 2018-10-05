Title: ScrapeR installation on Ubuntu
Date: 2013-10-16 21:00
Author: monsterbashseq
Category: R, Ubuntu
Slug: scraper-installation-on-ubuntu
Status: published

The 'scrapeR' package in R will remove html, xml tags from text.  
http://cran.r-project.org/web/packages/scrapeR/scrapeR.pdf  
http://files.meetup.com/1625815/crug\_scraper\_05-01-2013.pdf

I wanted to use this to parse out information for my Week 4 Programming
Assignment. However, I ran into this problem:

    >installation of package ‘scrapeR’ had non-zero exit status

http://stackoverflow.com/questions/7765429/unable-to-install-r-package-in-ubuntu-11-04  
http://stackoverflow.com/questions/5560139/install-r-package-xml-in-debian-ubuntu

In the Terminal:

    flcellogrl@flcellogrl:~$ sudo apt-get update
    [sudo] password for flcellogrl: 
    Get:1 http://security.ubuntu.com raring-security Release.gpg [933 B]
    Hit http://cran.cnr.Berkeley.edu raring/ Release.gpg                           
    Get:2 http://security.ubuntu.com raring-security Release [40.8 kB]             
    Hit http://cran.cnr.Berkeley.edu raring/ Release                               
    Get:3 http://security.ubuntu.com raring-security/main Sources [46.9 kB]        
    Hit http://cran.cnr.Berkeley.edu raring/ Packages                              
    Get:4 http://security.ubuntu.com raring-security/restricted Sources [14 B]     
    Get:5 http://security.ubuntu.com raring-security/universe Sources [9,271 B]    
    Get:6 http://security.ubuntu.com raring-security/multiverse Sources [2,266 B]  
    Get:7 http://security.ubuntu.com raring-security/main i386 Packages [121 kB]   
    Get:8 http://security.ubuntu.com raring-security/restricted i386 Packages [14 B]
    Get:9 http://security.ubuntu.com raring-security/universe i386 Packages [39.0 kB]
    Get:10 http://security.ubuntu.com raring-security/multiverse i386 Packages [3,864 B]
    Hit http://security.ubuntu.com raring-security/main Translation-en             
    Hit http://security.ubuntu.com raring-security/multiverse Translation-en       
    Ign http://cran.cnr.Berkeley.edu raring/ Translation-en_US                     
    Hit http://security.ubuntu.com raring-security/restricted Translation-en       
    Ign http://cran.cnr.Berkeley.edu raring/ Translation-en                        
    Hit http://security.ubuntu.com raring-security/universe Translation-en         
    Ign http://security.ubuntu.com raring-security/main Translation-en_US          
    Hit http://us.archive.ubuntu.com raring Release.gpg                            
    Get:11 http://us.archive.ubuntu.com raring-updates Release.gpg [933 B]      
    Ign http://security.ubuntu.com raring-security/multiverse Translation-en_US    
    Get:12 http://extras.ubuntu.com raring Release.gpg [72 B]             
    Hit http://us.archive.ubuntu.com raring-backports Release.gpg         
    Hit http://us.archive.ubuntu.com raring Release 
    Ign http://security.ubuntu.com raring-security/restricted Translation-en_US    
    Hit http://extras.ubuntu.com raring Release                                    
    Get:13 http://us.archive.ubuntu.com raring-updates Release [40.8 kB]   
    Ign http://security.ubuntu.com raring-security/universe Translation-en_US      
    Hit http://extras.ubuntu.com raring/main Sources          
    Hit http://us.archive.ubuntu.com raring-backports Release
    Hit http://us.archive.ubuntu.com raring/main Sources                           
    Hit http://extras.ubuntu.com raring/main i386 Packages                         
    Hit http://us.archive.ubuntu.com raring/restricted Sources                     
    Hit http://us.archive.ubuntu.com raring/universe Sources                       
    Hit http://us.archive.ubuntu.com raring/multiverse Sources                     
    Hit http://us.archive.ubuntu.com raring/main i386 Packages                     
    Hit http://us.archive.ubuntu.com raring/restricted i386 Packages               
    Hit http://us.archive.ubuntu.com raring/universe i386 Packages                 
    Hit http://us.archive.ubuntu.com raring/multiverse i386 Packages               
    Hit http://us.archive.ubuntu.com raring/main Translation-en                    
    Hit http://us.archive.ubuntu.com raring/multiverse Translation-en              
    Hit http://us.archive.ubuntu.com raring/restricted Translation-en              
    Hit http://us.archive.ubuntu.com raring/universe Translation-en                
    Get:14 http://us.archive.ubuntu.com raring-updates/main Sources [75.5 kB]      
    Ign http://extras.ubuntu.com raring/main Translation-en_US                     
    Ign http://extras.ubuntu.com raring/main Translation-en                        
    Get:15 http://us.archive.ubuntu.com raring-updates/restricted Sources [14 B]   
    Get:16 http://us.archive.ubuntu.com raring-updates/universe Sources [73.1 kB]  
    Get:17 http://us.archive.ubuntu.com raring-updates/multiverse Sources [2,266 B]
    Get:18 http://us.archive.ubuntu.com raring-updates/main i386 Packages [191 kB] 
    Get:19 http://us.archive.ubuntu.com raring-updates/restricted i386 Packages [14 B]
    Get:20 http://us.archive.ubuntu.com raring-updates/universe i386 Packages [151 kB]
    Get:21 http://us.archive.ubuntu.com raring-updates/multiverse i386 Packages [3,864 B]
    Hit http://us.archive.ubuntu.com raring-updates/main Translation-en            
    Hit http://us.archive.ubuntu.com raring-updates/multiverse Translation-en      
    Hit http://us.archive.ubuntu.com raring-updates/restricted Translation-en      
    Hit http://us.archive.ubuntu.com raring-updates/universe Translation-en        
    Hit http://us.archive.ubuntu.com raring-backports/main Sources                 
    Hit http://us.archive.ubuntu.com raring-backports/restricted Sources           
    Hit http://us.archive.ubuntu.com raring-backports/universe Sources             
    Hit http://us.archive.ubuntu.com raring-backports/multiverse Sources           
    Hit http://us.archive.ubuntu.com raring-backports/main i386 Packages           
    Hit http://us.archive.ubuntu.com raring-backports/restricted i386 Packages     
    Hit http://us.archive.ubuntu.com raring-backports/universe i386 Packages       
    Hit http://us.archive.ubuntu.com raring-backports/multiverse i386 Packages     
    Hit http://us.archive.ubuntu.com raring-backports/main Translation-en          
    Hit http://us.archive.ubuntu.com raring-backports/multiverse Translation-en    
    Hit http://us.archive.ubuntu.com raring-backports/restricted Translation-en    
    Hit http://us.archive.ubuntu.com raring-backports/universe Translation-en      
    Ign http://us.archive.ubuntu.com raring/main Translation-en_US                 
    Ign http://us.archive.ubuntu.com raring/multiverse Translation-en_US           
    Ign http://us.archive.ubuntu.com raring/restricted Translation-en_US           
    Ign http://us.archive.ubuntu.com raring/universe Translation-en_US             
    Ign http://us.archive.ubuntu.com raring-updates/main Translation-en_US         
    Ign http://us.archive.ubuntu.com raring-updates/multiverse Translation-en_US   
    Ign http://us.archive.ubuntu.com raring-updates/restricted Translation-en_US   
    Ign http://us.archive.ubuntu.com raring-updates/universe Translation-en_US     
    Ign http://us.archive.ubuntu.com raring-backports/main Translation-en_US       
    Ign http://us.archive.ubuntu.com raring-backports/multiverse Translation-en_US 
    Ign http://us.archive.ubuntu.com raring-backports/restricted Translation-en_US 
    Ign http://us.archive.ubuntu.com raring-backports/universe Translation-en_US   
    Fetched 802 kB in 15s (53.2 kB/s)                                              
    Reading package lists... Done
    flcellogrl@flcellogrl:~$ sudo apt-get install libxml2-dev
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following packages were automatically installed and are no longer required:
      linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic
      linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
    Use 'apt-get autoremove' to remove them.
    The following NEW packages will be installed:
      libxml2-dev
    0 upgraded, 1 newly installed, 0 to remove and 9 not upgraded.
    Need to get 853 kB of archives.
    After this operation, 2,472 kB of additional disk space will be used.
    Get:1 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libxml2-dev i386 2.9.0+dfsg1-4ubuntu4.3 [853 kB]
    Fetched 853 kB in 1s (771 kB/s)      
    Selecting previously unselected package libxml2-dev:i386.
    (Reading database ... 239212 files and directories currently installed.)
    Unpacking libxml2-dev:i386 (from .../libxml2-dev_2.9.0+dfsg1-4ubuntu4.3_i386.deb) ...
    Processing triggers for man-db ...
    Setting up libxml2-dev:i386 (2.9.0+dfsg1-4ubuntu4.3) ...

I still got the same Warning message in R.

In R, this worked:

    > install.packages("XML")
    Installing package into ‘/home/flcellogrl/R/i686-pc-linux-gnu-library/3.0’
    (as ‘lib’ is unspecified)
    trying URL 'http://cran.rstudio.com/src/contrib/XML_3.98-1.1.tar.gz'
    Content type 'application/x-gzip' length 1582216 bytes (1.5 Mb)
    opened URL
    ==================================================
    downloaded 1.5 Mb

    * installing *source* package ‘XML’ ...
    ** package ‘XML’ successfully unpacked and MD5 sums checked
    checking for gcc... gcc
    checking for C compiler default output file name... 
    rm: cannot remove 'a.out.dSYM': Is a directory
    a.out
    checking whether the C compiler works... yes
    checking whether we are cross compiling... no
    checking for suffix of executables... 
    checking for suffix of object files... o
    checking whether we are using the GNU C compiler... yes
    checking whether gcc accepts -g... yes
    checking for gcc option to accept ISO C89... none needed
    checking how to run the C preprocessor... gcc -E
    checking for sed... /bin/sed
    checking for pkg-config... /usr/bin/pkg-config
    checking for xml2-config... /usr/bin/xml2-config
    USE_XML2 = yes
    SED_EXTENDED_ARG: -E
    Minor 9, Patch 0 for 2.9.0
    Located parser file -I/usr/include/libxml2/parser.h
    Checking for 1.8:  -I/usr/include/libxml2
    Using libxml2.*
    checking for gzopen in -lz... yes
    checking for xmlParseFile in -lxml2... yes
    checking for xmlHashSize in -lxml2... yes
    Using built-in xmlHashSize
    Checking DTD parsing (presence of externalSubset)...
    checking for xmlHashSize in -lxml2... yes
    Found xmlHashSize
    checking for xmlOutputBufferCreateBuffer in -lxml2... yes
    have xmlOutputBufferCreateBuffer()
    checking for xmlDocDumpFormatMemoryEnc in -lxml2... yes
    checking libxml/xmlversion.h usability... yes
    checking libxml/xmlversion.h presence... yes
    checking for libxml/xmlversion.h... yes
    Expat:  FALSE
    Checking for return type of xmlHashScan element routine.
    No return value for xmlHashScan
    xmlNs has a context field
    Checking for cetype_t enumeration
    No cetype_t enumeration defined in R headers.
    checking for xmlsec1-config... no
    nodegc default 
    xml-debug default 
    Version has XML_WITH_ZLIB
    Version has xmlHasFeature()

    ****************************************
    Configuration information:

    Libxml settings

    libxml include directory: -I/usr/include/libxml2
    libxml library directory: -lxml2 -lz  -lxml2
    libxml 2:                 -DLIBXML2=1

    Compilation flags:         -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 
    Link flags:               -lxml2 -lz  -lxml2

    ****************************************
    configure: creating ./config.status
    config.status: creating src/Makevars
    config.status: creating R/supports.R
    config.status: creating inst/scripts/RSXML.csh
    config.status: creating inst/scripts/RSXML.bsh
    ** libs
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c DocParse.c -o DocParse.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c EventParse.c -o EventParse.o
    EventParse.c: In function ‘RS_XML_textHandler’:
    EventParse.c:419:37: warning: cast from pointer to integer of different size [-Wpointer-to-int-cast]
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c ExpatParse.c -o ExpatParse.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c HTMLParse.c -o HTMLParse.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c NodeGC.c -o NodeGC.o
    NodeGC.c: In function ‘initDocRefCounter’:
    NodeGC.c:178:12: warning: assignment makes integer from pointer without a cast [enabled by default]
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c RSDTD.c -o RSDTD.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c RUtils.c -o RUtils.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c Rcatalog.c -o Rcatalog.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c Utils.c -o Utils.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c XMLEventParse.c -o XMLEventParse.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c XMLHashTree.c -o XMLHashTree.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c XMLTree.c -o XMLTree.o
    XMLTree.c: In function ‘R_createXMLNodeRef’:
    XMLTree.c:1103:9: warning: assignment makes integer from pointer without a cast [enabled by default]
    XMLTree.c: In function ‘R_xmlSearchNs’:
    XMLTree.c:1695:39: warning: comparison of distinct pointer types lacks a cast [enabled by default]
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c fixNS.c -o fixNS.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c libxmlFeatures.c -o libxmlFeatures.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c schema.c -o schema.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c xmlsecurity.c -o xmlsecurity.o
    gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1  -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1  -I. -DLIBXML2=1     -fpic  -O2 -pipe -g  -c xpath.c -o xpath.o
    gcc -std=gnu99 -shared -o XML.so DocParse.o EventParse.o ExpatParse.o HTMLParse.o NodeGC.o RSDTD.o RUtils.o Rcatalog.o Utils.o XMLEventParse.o XMLHashTree.o XMLTree.o fixNS.o libxmlFeatures.o schema.o xmlsecurity.o xpath.o -lxml2 -lz -lxml2 -L/usr/lib/R/lib -lR
    installing to /home/flcellogrl/R/i686-pc-linux-gnu-library/3.0/XML/libs
    ** R
    ** inst
    ** preparing package for lazy loading
    Creating a generic function for ‘source’ from package ‘base’ in package ‘XML’
    in method for ‘xmlAttrsToDataFrame’ with signature ‘"AsIs"’: no definition for class “AsIs”
    in method for ‘readKeyValueDB’ with signature ‘"AsIs"’: no definition for class “AsIs”
    in method for ‘readSolrDoc’ with signature ‘"AsIs"’: no definition for class “AsIs”
    ** help
    *** installing help indices
    ** building package indices
    ** testing if installed package can be loaded
    * DONE (XML)

    The downloaded source packages are in
        ‘/tmp/RtmpNXrL9u/downloaded_packages’
    > install.packages("scrapeR", dependencies=TRUE)
    Installing package into ‘/home/flcellogrl/R/i686-pc-linux-gnu-library/3.0’
    (as ‘lib’ is unspecified)
    trying URL 'http://cran.rstudio.com/src/contrib/scrapeR_0.1.6.tar.gz'
    Content type 'application/x-gzip' length 6754 bytes
    opened URL
    ==================================================
    downloaded 6754 bytes

    * installing *source* package ‘scrapeR’ ...
    ** R
    ** inst
    ** preparing package for lazy loading
    ** help
    *** installing help indices
    ** building package indices
    ** testing if installed package can be loaded
    * DONE (scrapeR)

    The downloaded source packages are in
        ‘/tmp/RtmpNXrL9u/downloaded_packages’
    > library(ScrapeR)
    Error in library(ScrapeR) : there is no package called ‘ScrapeR’
    > library(scrapeR)
    Loading required package: XML
    Loading required package: RCurl
    Loading required package: bitops