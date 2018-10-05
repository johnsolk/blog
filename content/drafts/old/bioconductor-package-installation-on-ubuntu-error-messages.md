Title: R/Bioconductor package installation on Ubuntu: Error messages
Date: 2013-10-18 10:38
Author: monsterbashseq
Category: Bioconductor, R, Ubuntu
Slug: bioconductor-package-installation-on-ubuntu-error-messages
Status: published

I fixed this issue by starting R as root user, then installing the
necessary packages. Apparently, this was a common rookie mistake using R
and Ubuntu/Linux that I luckily searched for and learned about. When
installing new R packages in Ubuntu, always start R as root user.

The Bioconductor package arrayQualityMetrics was successfully installed
with its dependent Cairo Library for graphics. Bioconductor still won't
update from 2.12 to 2.13 using the biocLite() function, but this
apparently didn't affect the installation of
biocLite("arrayQualityMetrics"). The following references were helpful:

http://grokbase.com/t/r/bioconductor/139dqv2ey0/bioc-installation-packages  
http://r.789695.n4.nabble.com/Cannot-Install-Cairo-Library-td891108.html

The following is the transcript showing how I fixed this issue:

    flcellogrl@flcellogrl:~$ sudo R
     [sudo] password for flcellogrl:
    R version 3.0.2 (2013-09-25) -- "Frisbee Sailing"
     Copyright (C) 2013 The R Foundation for Statistical Computing
     Platform: i686-pc-linux-gnu (32-bit)
    R is free software and comes with ABSOLUTELY NO WARRANTY.
     You are welcome to redistribute it under certain conditions.
     Type 'license()' or 'licence()' for distribution details.
    Natural language support but running in an English locale
    R is a collaborative project with many contributors.
     Type 'contributors()' for more information and
     'citation()' on how to cite R or R packages in publications.
    Type 'demo()' for some demos, 'help()' for on-line help, or
     'help.start()' for an HTML browser interface to help.
     Type 'q()' to quit R.
    > source("http://bioconductor.org/biocLite.R")
     Your Bioconductor is out-of-date, upgrade to version 2.13 by following
     instructions at http://bioconductor.org/install.
     Bioconductor version 2.12 (BiocInstaller 1.10.4), ?biocLite for help
     A newer version of Bioconductor is available for this version of R,
     ?BiocUpgrade for help
     > biocLite()
     BioC_mirror: http://bioconductor.org
     Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
     Old packages: 'XML', 'spatial'
     Update all/some/none? [a/s/n]: a
     trying URL 'http://cran.fhcrc.org/src/contrib/XML_3.98-1.1.tar.gz'
     Content type 'application/x-gzip' length 1582216 bytes (1.5 Mb)
     opened URL
     ==================================================
     downloaded 1.5 Mb
    * installing *source* package ‘XML’ ...
     ** package ‘XML’ successfully unpacked and MD5 sums checked
     checking for gcc... gcc
     checking for C compiler default output file name... rm: cannot remove 'a.out.dSYM': Is a directory
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
     Checking for 1.8: -I/usr/include/libxml2
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
     Expat: FALSE
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
     libxml library directory: -lxml2 -lz -lxml2
     libxml 2: -DLIBXML2=1
    Compilation flags: -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1
     Link flags: -lxml2 -lz -lxml2
    ****************************************
     configure: creating ./config.status
     config.status: creating src/Makevars
     config.status: creating R/supports.R
     config.status: creating inst/scripts/RSXML.csh
     config.status: creating inst/scripts/RSXML.bsh
     ** libs
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c DocParse.c -o DocParse.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c EventParse.c -o EventParse.o
     EventParse.c: In function ‘RS_XML_textHandler’:
     EventParse.c:419:37: warning: cast from pointer to integer of different size [-Wpointer-to-int-cast]
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c ExpatParse.c -o ExpatParse.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c HTMLParse.c -o HTMLParse.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c NodeGC.c -o NodeGC.o
     NodeGC.c: In function ‘initDocRefCounter’:
     NodeGC.c:178:12: warning: assignment makes integer from pointer without a cast [enabled by default]
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c RSDTD.c -o RSDTD.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c RUtils.c -o RUtils.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c Rcatalog.c -o Rcatalog.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c Utils.c -o Utils.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c XMLEventParse.c -o XMLEventParse.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c XMLHashTree.c -o XMLHashTree.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c XMLTree.c -o XMLTree.o
     XMLTree.c: In function ‘R_createXMLNodeRef’:
     XMLTree.c:1103:9: warning: assignment makes integer from pointer without a cast [enabled by default]
     XMLTree.c: In function ‘R_xmlSearchNs’:
     XMLTree.c:1695:39: warning: comparison of distinct pointer types lacks a cast [enabled by default]
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c fixNS.c -o fixNS.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c libxmlFeatures.c -o libxmlFeatures.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c schema.c -o schema.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c xmlsecurity.c -o xmlsecurity.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -DLIBXML -I/usr/include/libxml2 -DUSE_EXTERNAL_SUBSET=1 -DROOT_HAS_DTD_NODE=1 -DDUMP_WITH_ENCODING=1 -DUSE_XML_VERSION_H=1 -DXML_ELEMENT_ETYPE=1 -DXML_ATTRIBUTE_ATYPE=1 -DNO_XML_HASH_SCANNER_RETURN=1 -DLIBXML_NAMESPACE_HAS_CONTEXT=1 -DHAVE_XML_WITH_ZLIB=1 -DHAVE_XML_HAS_FEATURE=1 -DUSE_R=1 -D_R_=1 -DHAVE_VALIDITY=1 -DXML_REF_COUNT_NODES=1 -I. -DLIBXML2=1 -fpic -O2 -pipe -g -c xpath.c -o xpath.o
     gcc -std=gnu99 -shared -o XML.so DocParse.o EventParse.o ExpatParse.o HTMLParse.o NodeGC.o RSDTD.o RUtils.o Rcatalog.o Utils.o XMLEventParse.o XMLHashTree.o XMLTree.o fixNS.o libxmlFeatures.o schema.o xmlsecurity.o xpath.o -lxml2 -lz -lxml2 -L/usr/lib/R/lib -lR
     installing to /usr/lib/R/site-library/XML/libs
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
     ‘/tmp/RtmpvwT71f/downloaded_packages’
     trying URL 'http://cran.fhcrc.org/src/contrib/spatial_7.3-7.tar.gz'
     Content type 'application/x-gzip' length 44220 bytes (43 Kb)
     opened URL
     ==================================================
     downloaded 43 Kb
    * installing *source* package ‘spatial’ ...
     ** package ‘spatial’ successfully unpacked and MD5 sums checked
     ** libs
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -fpic -O2 -pipe -g -c init.c -o init.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -fpic -O2 -pipe -g -c krc.c -o krc.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -fpic -O2 -pipe -g -c pps.c -o pps.o
     gcc -std=gnu99 -shared -o spatial.so init.o krc.o pps.o -L/usr/lib/R/lib -lR
     installing to /usr/lib/R/library/spatial/libs
     ** R
     ** inst
     ** byte-compile and prepare package for lazy loading
     ** help
     *** installing help indices
     ** building package indices
     ** testing if installed package can be loaded
     * DONE (spatial)
    The downloaded source packages are in
     ‘/tmp/RtmpvwT71f/downloaded_packages’
     Updating HTML index of packages in '.Library'
     Making 'packages.html' ... done
     > biocLite("arrayQualityMetrics")
     BioC_mirror: http://bioconductor.org
     Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
     Installing package(s) 'arrayQualityMetrics'
     also installing the dependency ‘Cairo’
    trying URL 'http://cran.fhcrc.org/src/contrib/Cairo_1.5-2.tar.gz'
     Content type 'application/x-gzip' length 83972 bytes (82 Kb)
     opened URL
     ==================================================
     downloaded 82 Kb
    trying URL 'http://bioconductor.org/packages/2.12/bioc/src/contrib/arrayQualityMetrics_3.16.0.tar.gz'
     Content type 'application/x-gzip' length 573179 bytes (559 Kb)
     opened URL
     ==================================================
     downloaded 559 Kb
    * installing *source* package ‘Cairo’ ...
     ** package ‘Cairo’ successfully unpacked and MD5 sums checked
     checking for gcc... gcc -std=gnu99
     checking whether the C compiler works... yes
     checking for C compiler default output file name... a.out
     checking for suffix of executables...
     checking whether we are cross compiling... no
     checking for suffix of object files... o
     checking whether we are using the GNU C compiler... yes
     checking whether gcc -std=gnu99 accepts -g... yes
     checking for gcc -std=gnu99 option to accept ISO C89... none needed
     checking how to run the C preprocessor... gcc -std=gnu99 -E
     checking for grep that handles long lines and -e... /bin/grep
     checking for egrep... /bin/grep -E
     checking for ANSI C header files... yes
     checking for sys/wait.h that is POSIX.1 compatible... yes
     checking for sys/types.h... yes
     checking for sys/stat.h... yes
     checking for stdlib.h... yes
     checking for string.h... yes
     checking for memory.h... yes
     checking for strings.h... yes
     checking for inttypes.h... yes
     checking for stdint.h... yes
     checking for unistd.h... yes
     checking for string.h... (cached) yes
     checking sys/time.h usability... yes
     checking sys/time.h presence... yes
     checking for sys/time.h... yes
     checking for unistd.h... (cached) yes
     checking for an ANSI C-conforming const... yes
     checking for pkg-config... /usr/bin/pkg-config
     checking whether pkg-config knows about cairo... yes
     checking for configurable backends... cairo cairo-ft cairo-pdf cairo-png cairo-ps cairo-xlib cairo-xlib-xrender
     configure: CAIRO_CFLAGS=-I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12
     checking if R was compiled with the RConn patch... no
     checking cairo.h usability... yes
     checking cairo.h presence... yes
     checking for cairo.h... yes
     checking for PNG support in Cairo... yes
     checking for ATS font support in Cairo... no
     configure: CAIRO_LIBS=-lfreetype -lpng12 -lz -lXrender -lcairo -lXext -lX11
     checking for library containing deflate... none required
     checking whether Cairo programs can be compiled... yes
     checking whether cairo_image_surface_get_format is declared... no
     checking for FreeType support in cairo... yes
     checking whether FreeType needs additional flags... no
     checking wheter libjpeg works... yes
     checking wheter libtiff works... no
     configure: creating ./config.status
     config.status: creating src/Makevars
     config.status: creating src/cconfig.h
     ** libs
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairobem.c -o cairobem.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairogd.c -o cairogd.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairotalk.c -o cairotalk.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-backend.c -o img-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-jpeg.c -o img-jpeg.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-tiff.c -o img-tiff.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c pdf-backend.c -o pdf-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c ps-backend.c -o ps-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c svg-backend.c -o svg-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c w32-backend.c -o w32-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c xlib-backend.c -o xlib-backend.o
     xlib-backend.c:34:74: fatal error: X11/Intrinsic.h: No such file or directory
     compilation terminated.
     make: *** [xlib-backend.o] Error 1
     ERROR: compilation failed for package ‘Cairo’
     * removing ‘/home/flcellogrl/R/i686-pc-linux-gnu-library/3.0/Cairo’
     ERROR: dependency ‘Cairo’ is not available for package ‘arrayQualityMetrics’
     * removing ‘/home/flcellogrl/R/i686-pc-linux-gnu-library/3.0/arrayQualityMetrics’
    The downloaded source packages are in
     ‘/tmp/RtmpvwT71f/downloaded_packages’
     Warning messages:
     1: In install.packages(pkgs = pkgs, lib = lib, repos = repos, ...) :
     installation of package ‘Cairo’ had non-zero exit status
     2: In install.packages(pkgs = pkgs, lib = lib, repos = repos, ...) :
     installation of package ‘arrayQualityMetrics’ had non-zero exit status
     > q()
     Save workspace image? [y/n/c]: y
     flcellogrl@flcellogrl:~$ dpkg -S 'locate Intrinsic.h'
     dpkg-query: no path found matching pattern *locate Intrinsic.h*
     flcellogrl@flcellogrl:~$ sudo apt-get install libxt-dev
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     The following packages were automatically installed and are no longer required:
     libcurl3-nss libnspr4-dev libnss3-dev libssl-dev libssl-doc linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
     Use 'apt-get autoremove' to remove them.
     Suggested packages:
     libxt-doc
     The following NEW packages will be installed:
     libxt-dev
     0 upgraded, 1 newly installed, 0 to remove and 10 not upgraded.
     Need to get 472 kB of archives.
     After this operation, 1,053 kB of additional disk space will be used.
     Get:1 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libxt-dev i386 1:1.1.3-1ubuntu0.13.04.1 [472 kB]
     Fetched 472 kB in 4s (108 kB/s)
     Selecting previously unselected package libxt-dev:i386.
     (Reading database ... 243152 files and directories currently installed.)
     Unpacking libxt-dev:i386 (from .../libxt-dev_1%3a1.1.3-1ubuntu0.13.04.1_i386.deb) ...
     Processing triggers for man-db ...
     Setting up libxt-dev:i386 (1:1.1.3-1ubuntu0.13.04.1) ...
     flcellogrl@flcellogrl:~$ sudo R
    R version 3.0.2 (2013-09-25) -- "Frisbee Sailing"
     Copyright (C) 2013 The R Foundation for Statistical Computing
     Platform: i686-pc-linux-gnu (32-bit)
    R is free software and comes with ABSOLUTELY NO WARRANTY.
     You are welcome to redistribute it under certain conditions.
     Type 'license()' or 'licence()' for distribution details.
    Natural language support but running in an English locale
    R is a collaborative project with many contributors.
     Type 'contributors()' for more information and
     'citation()' on how to cite R or R packages in publications.
    Type 'demo()' for some demos, 'help()' for on-line help, or
     'help.start()' for an HTML browser interface to help.
     Type 'q()' to quit R.
    > biocLite("arrayQualityMetrics")
     Error: could not find function "biocLite"
     > source("http://bioconductor.org/biocLite.R")
     Your Bioconductor is out-of-date, upgrade to version 2.13 by following
     instructions at http://bioconductor.org/install.
     Bioconductor version 2.12 (BiocInstaller 1.10.4), ?biocLite for help
     A newer version of Bioconductor is available for this version of R,
     ?BiocUpgrade for help
     > biocLite()
     BioC_mirror: http://bioconductor.org
     Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
     > biocLite("arrayQualityMetrics")
     BioC_mirror: http://bioconductor.org
     Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
     Installing package(s) 'arrayQualityMetrics'
     also installing the dependency ‘Cairo’
    trying URL 'http://cran.fhcrc.org/src/contrib/Cairo_1.5-2.tar.gz'
     Content type 'application/x-gzip' length 83972 bytes (82 Kb)
     opened URL
     ==================================================
     downloaded 82 Kb
    trying URL 'http://bioconductor.org/packages/2.12/bioc/src/contrib/arrayQualityMetrics_3.16.0.tar.gz'
     Content type 'application/x-gzip' length 573179 bytes (559 Kb)
     opened URL
     ==================================================
     downloaded 559 Kb
    * installing *source* package ‘Cairo’ ...
     ** package ‘Cairo’ successfully unpacked and MD5 sums checked
     checking for gcc... gcc -std=gnu99
     checking whether the C compiler works... yes
     checking for C compiler default output file name... a.out
     checking for suffix of executables...
     checking whether we are cross compiling... no
     checking for suffix of object files... o
     checking whether we are using the GNU C compiler... yes
     checking whether gcc -std=gnu99 accepts -g... yes
     checking for gcc -std=gnu99 option to accept ISO C89... none needed
     checking how to run the C preprocessor... gcc -std=gnu99 -E
     checking for grep that handles long lines and -e... /bin/grep
     checking for egrep... /bin/grep -E
     checking for ANSI C header files... yes
     checking for sys/wait.h that is POSIX.1 compatible... yes
     checking for sys/types.h... yes
     checking for sys/stat.h... yes
     checking for stdlib.h... yes
     checking for string.h... yes
     checking for memory.h... yes
     checking for strings.h... yes
     checking for inttypes.h... yes
     checking for stdint.h... yes
     checking for unistd.h... yes
     checking for string.h... (cached) yes
     checking sys/time.h usability... yes
     checking sys/time.h presence... yes
     checking for sys/time.h... yes
     checking for unistd.h... (cached) yes
     checking for an ANSI C-conforming const... yes
     checking for pkg-config... /usr/bin/pkg-config
     checking whether pkg-config knows about cairo... yes
     checking for configurable backends... cairo cairo-ft cairo-pdf cairo-png cairo-ps cairo-xlib cairo-xlib-xrender
     configure: CAIRO_CFLAGS=-I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12
     checking if R was compiled with the RConn patch... no
     checking cairo.h usability... yes
     checking cairo.h presence... yes
     checking for cairo.h... yes
     checking for PNG support in Cairo... yes
     checking for ATS font support in Cairo... no
     configure: CAIRO_LIBS=-lfreetype -lpng12 -lz -lXrender -lcairo -lXext -lX11
     checking for library containing deflate... none required
     checking whether Cairo programs can be compiled... yes
     checking whether cairo_image_surface_get_format is declared... no
     checking for FreeType support in cairo... yes
     checking whether FreeType needs additional flags... no
     checking wheter libjpeg works... yes
     checking wheter libtiff works... no
     configure: creating ./config.status
     config.status: creating src/Makevars
     config.status: creating src/cconfig.h
     ** libs
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairobem.c -o cairobem.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairogd.c -o cairogd.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairotalk.c -o cairotalk.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-backend.c -o img-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-jpeg.c -o img-jpeg.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-tiff.c -o img-tiff.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c pdf-backend.c -o pdf-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c ps-backend.c -o ps-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c svg-backend.c -o svg-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c w32-backend.c -o w32-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c xlib-backend.c -o xlib-backend.o
     gcc -std=gnu99 -shared -o Cairo.so cairobem.o cairogd.o cairotalk.o img-backend.o img-jpeg.o img-tiff.o pdf-backend.o ps-backend.o svg-backend.o w32-backend.o xlib-backend.o -lfreetype -lpng12 -lz -lXrender -lcairo -lXext -lX11 -ljpeg -L/usr/lib/R/lib -lR
     installing to /home/flcellogrl/R/i686-pc-linux-gnu-library/3.0/Cairo/libs
     ** R
     ** preparing package for lazy loading
     ** help
     *** installing help indices
     ** building package indices
     ** testing if installed package can be loaded
     Warning: ignoring .First.lib() for package ‘Cairo’
     * DONE (Cairo)
     * installing *source* package ‘arrayQualityMetrics’ ...
     ** R
     ** inst
     ** preparing package for lazy loading
     Creating a generic function for ‘boxplot’ from package ‘graphics’ in package ‘affyPLM’
     Creating a generic function for ‘hist’ from package ‘graphics’ in package ‘affyPLM’
     ** help
     *** installing help indices
     ** building package indices
     ** installing vignettes
     ** testing if installed package can be loaded
     Creating a generic function for ‘boxplot’ from package ‘graphics’ in package ‘affyPLM’
     Creating a generic function for ‘hist’ from package ‘graphics’ in package ‘affyPLM’
     * DONE (arrayQualityMetrics)
    The downloaded source packages are in
     ‘/tmp/Rtmp6zTfiR/downloaded_packages’
     >

This was the original issue: I'm trying to install the R/Bioconductor
package arrayQualityMetrics on Ubuntu. I'm experiencing two problems: 1)
Bioconductor is not up-to-date (have 2.12 and 2.13 is the most recent)
and it is not allowing me to update, 2) arrayQualityMetrics will not
properly install:

    >source("http://bioconductor.org/biocLite.R")
    >biocLite()
    BioC_mirror: http://bioconductor.org
    Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
    Warning message:
    installed directory not writable, cannot update packages 'XML', 'spatial' 
    >biocLite("arrayQualityMetrics")
    ...
    ERROR: dependency ‘Cairo’ is not available for package ‘arrayQualityMetrics’
    * removing ‘/home/flcellogrl/R/i686-pc-linux-gnu-library/3.0/arrayQualityMetrics’

    The downloaded source packages are in
        ‘/tmp/Rtmp2QcQZd/downloaded_packages’
    Warning messages:
    1: In install.packages(pkgs = pkgs, lib = lib, repos = repos, ...) :
      installation of package ‘Cairo’ had non-zero exit status
    2: In install.packages(pkgs = pkgs, lib = lib, repos = repos, ...) :
      installation of package ‘arrayQualityMetrics’ had non-zero exit status
    3: installed directory not writable, cannot update packages 'XML', 'spatial'

This is a Ubuntu/Linux issue. I had this package working fine yesterday
from my Windows XP OS at work. But, at home, on Ubuntu version:

    flcellogrl@flcellogrl:~$ cat /proc/version
     Linux version 3.8.0-31-generic (buildd@aatxe) (gcc version 4.7.3 (Ubuntu/Linaro 4.7.3-1ubuntu1) ) #46-Ubuntu SMP Tue Sep 10 19:56:49 UTC 2013

Installed some things:

     flcellogrl@flcellogrl:~$ sudo apt-get install libcairo2-dev
     flcellogrl@flcellogrl:~$ sudo apt-get install xml2
     flcellogrl@flcellogrl:~$ sudo apt-get install libcurl3
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     libcurl3 is already the newest version.

See results below:

     flcellogrl@flcellogrl:~$ sudo apt-get install libcairo2-dev
     [sudo] password for flcellogrl:
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     The following packages were automatically installed and are no longer required:
     linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic
     linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
     Use 'apt-get autoremove' to remove them.
     The following extra packages will be installed:
     libcairo-script-interpreter2 libfontconfig1-dev libfreetype6-dev
     libglib2.0-dev libice-dev libpixman-1-dev libpthread-stubs0
     libpthread-stubs0-dev libsm-dev libx11-dev libx11-doc libxau-dev
     libxcb-render0-dev libxcb-shm0-dev libxcb1-dev libxdmcp-dev libxext-dev
     libxrender-dev x11proto-core-dev x11proto-input-dev x11proto-kb-dev
     x11proto-render-dev x11proto-xext-dev xorg-sgml-doctools xtrans-dev
     Suggested packages:
     libcairo2-doc libglib2.0-doc libice-doc libsm-doc libxcb-doc libxext-doc
     The following NEW packages will be installed:
     libcairo-script-interpreter2 libcairo2-dev libfontconfig1-dev
     libfreetype6-dev libglib2.0-dev libice-dev libpixman-1-dev libpthread-stubs0
     libpthread-stubs0-dev libsm-dev libx11-dev libx11-doc libxau-dev
     libxcb-render0-dev libxcb-shm0-dev libxcb1-dev libxdmcp-dev libxext-dev
     libxrender-dev x11proto-core-dev x11proto-input-dev x11proto-kb-dev
     x11proto-render-dev x11proto-xext-dev xorg-sgml-doctools xtrans-dev
     0 upgraded, 26 newly installed, 0 to remove and 10 not upgraded.
     Need to get 9,001 kB of archives.
     After this operation, 35.9 MB of additional disk space will be used.
     Do you want to continue [Y/n]? y
     Get:1 http://us.archive.ubuntu.com/ubuntu/ raring/main libcairo-script-interpreter2 i386 1.12.14-0ubuntu1 [64.9 kB]
     Get:2 http://us.archive.ubuntu.com/ubuntu/ raring/main libfreetype6-dev i386 2.4.11-0ubuntu1 [791 kB]
     Get:3 http://us.archive.ubuntu.com/ubuntu/ raring/main libfontconfig1-dev i386 2.10.2-0ubuntu2 [673 kB]
     Get:4 http://us.archive.ubuntu.com/ubuntu/ raring/main xorg-sgml-doctools all 1:1.10-1 [12.0 kB]
     Get:5 http://us.archive.ubuntu.com/ubuntu/ raring/main x11proto-core-dev all 7.0.23-1 [744 kB]
     Get:6 http://us.archive.ubuntu.com/ubuntu/ raring/main libxau-dev i386 1:1.0.7-1 [10.0 kB]
     Get:7 http://us.archive.ubuntu.com/ubuntu/ raring/main libxdmcp-dev i386 1:1.1.1-1 [26.8 kB]
     Get:8 http://us.archive.ubuntu.com/ubuntu/ raring/main x11proto-input-dev all 2.2.99.1-0ubuntu1 [139 kB]
     Get:9 http://us.archive.ubuntu.com/ubuntu/ raring/main x11proto-kb-dev all 1.0.6-2 [269 kB]
     Get:10 http://us.archive.ubuntu.com/ubuntu/ raring/main xtrans-dev all 1.2.7-1 [84.3 kB]
     Get:11 http://us.archive.ubuntu.com/ubuntu/ raring/main libpthread-stubs0 i386 0.3-3 [3,264 B]
     Get:12 http://us.archive.ubuntu.com/ubuntu/ raring/main libpthread-stubs0-dev i386 0.3-3 [2,860 B]
     Get:13 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libxcb1-dev i386 1.8.1-2ubuntu2.1 [81.2 kB]
     Get:14 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libx11-dev i386 2:1.5.0-1ubuntu1.1 [895 kB]
     Get:15 http://us.archive.ubuntu.com/ubuntu/ raring/main x11proto-render-dev all 2:0.11.1-2 [20.1 kB]
     Get:16 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libxrender-dev i386 1:0.9.7-1ubuntu0.13.04.1 [27.5 kB]
     Get:17 http://us.archive.ubuntu.com/ubuntu/ raring/main libice-dev i386 2:1.0.8-2 [52.3 kB]
     Get:18 http://us.archive.ubuntu.com/ubuntu/ raring/main libsm-dev i386 2:1.2.1-2 [17.6 kB]
     Get:19 http://us.archive.ubuntu.com/ubuntu/ raring/main libpixman-1-dev i386 0.28.2-0ubuntu1 [278 kB]
     Get:20 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libxcb-render0-dev i386 1.8.1-2ubuntu2.1 [21.1 kB]
     Get:21 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libxcb-shm0-dev i386 1.8.1-2ubuntu2.1 [6,866 B]
     Get:22 http://us.archive.ubuntu.com/ubuntu/ raring/main x11proto-xext-dev all 7.2.1-1 [265 kB]
     Get:23 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libxext-dev i386 2:1.3.1-2ubuntu0.13.04.1 [90.8 kB]
     Get:24 http://us.archive.ubuntu.com/ubuntu/ raring/main libglib2.0-dev i386 2.36.0-1ubuntu2 [1,227 kB]
     Get:25 http://us.archive.ubuntu.com/ubuntu/ raring/main libcairo2-dev i386 1.12.14-0ubuntu1 [749 kB]
     Get:26 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libx11-doc all 2:1.5.0-1ubuntu1.1 [2,448 kB]
     Fetched 9,001 kB in 15s (570 kB/s)
     Selecting previously unselected package libcairo-script-interpreter2:i386.
     (Reading database ... 239276 files and directories currently installed.)
     Unpacking libcairo-script-interpreter2:i386 (from .../libcairo-script-interpreter2_1.12.14-0ubuntu1_i386.deb) ...
     Selecting previously unselected package libfreetype6-dev.
     Unpacking libfreetype6-dev (from .../libfreetype6-dev_2.4.11-0ubuntu1_i386.deb) ...
     Selecting previously unselected package libfontconfig1-dev.
     Unpacking libfontconfig1-dev (from .../libfontconfig1-dev_2.10.2-0ubuntu2_i386.deb) ...
     Selecting previously unselected package xorg-sgml-doctools.
     Unpacking xorg-sgml-doctools (from .../xorg-sgml-doctools_1%3a1.10-1_all.deb) ...
     Selecting previously unselected package x11proto-core-dev.
     Unpacking x11proto-core-dev (from .../x11proto-core-dev_7.0.23-1_all.deb) ...
     Selecting previously unselected package libxau-dev:i386.
     Unpacking libxau-dev:i386 (from .../libxau-dev_1%3a1.0.7-1_i386.deb) ...
     Selecting previously unselected package libxdmcp-dev:i386.
     Unpacking libxdmcp-dev:i386 (from .../libxdmcp-dev_1%3a1.1.1-1_i386.deb) ...
     Selecting previously unselected package x11proto-input-dev.
     Unpacking x11proto-input-dev (from .../x11proto-input-dev_2.2.99.1-0ubuntu1_all.deb) ...
     Selecting previously unselected package x11proto-kb-dev.
     Unpacking x11proto-kb-dev (from .../x11proto-kb-dev_1.0.6-2_all.deb) ...
     Selecting previously unselected package xtrans-dev.
     Unpacking xtrans-dev (from .../xtrans-dev_1.2.7-1_all.deb) ...
     Selecting previously unselected package libpthread-stubs0:i386.
     Unpacking libpthread-stubs0:i386 (from .../libpthread-stubs0_0.3-3_i386.deb) ...
     Selecting previously unselected package libpthread-stubs0-dev:i386.
     Unpacking libpthread-stubs0-dev:i386 (from .../libpthread-stubs0-dev_0.3-3_i386.deb) ...
     Selecting previously unselected package libxcb1-dev:i386.
     Unpacking libxcb1-dev:i386 (from .../libxcb1-dev_1.8.1-2ubuntu2.1_i386.deb) ...
     Selecting previously unselected package libx11-dev:i386.
     Unpacking libx11-dev:i386 (from .../libx11-dev_2%3a1.5.0-1ubuntu1.1_i386.deb) ...
     Selecting previously unselected package x11proto-render-dev.
     Unpacking x11proto-render-dev (from .../x11proto-render-dev_2%3a0.11.1-2_all.deb) ...
     Selecting previously unselected package libxrender-dev:i386.
     Unpacking libxrender-dev:i386 (from .../libxrender-dev_1%3a0.9.7-1ubuntu0.13.04.1_i386.deb) ...
     Selecting previously unselected package libice-dev:i386.
     Unpacking libice-dev:i386 (from .../libice-dev_2%3a1.0.8-2_i386.deb) ...
     Selecting previously unselected package libsm-dev:i386.
     Unpacking libsm-dev:i386 (from .../libsm-dev_2%3a1.2.1-2_i386.deb) ...
     Selecting previously unselected package libpixman-1-dev.
     Unpacking libpixman-1-dev (from .../libpixman-1-dev_0.28.2-0ubuntu1_i386.deb) ...
     Selecting previously unselected package libxcb-render0-dev:i386.
     Unpacking libxcb-render0-dev:i386 (from .../libxcb-render0-dev_1.8.1-2ubuntu2.1_i386.deb) ...
     Selecting previously unselected package libxcb-shm0-dev:i386.
     Unpacking libxcb-shm0-dev:i386 (from .../libxcb-shm0-dev_1.8.1-2ubuntu2.1_i386.deb) ...
     Selecting previously unselected package x11proto-xext-dev.
     Unpacking x11proto-xext-dev (from .../x11proto-xext-dev_7.2.1-1_all.deb) ...
     Selecting previously unselected package libxext-dev:i386.
     Unpacking libxext-dev:i386 (from .../libxext-dev_2%3a1.3.1-2ubuntu0.13.04.1_i386.deb) ...
     Selecting previously unselected package libglib2.0-dev.
     Unpacking libglib2.0-dev (from .../libglib2.0-dev_2.36.0-1ubuntu2_i386.deb) ...
     Selecting previously unselected package libcairo2-dev.
     Unpacking libcairo2-dev (from .../libcairo2-dev_1.12.14-0ubuntu1_i386.deb) ...
     Selecting previously unselected package libx11-doc.
     Unpacking libx11-doc (from .../libx11-doc_2%3a1.5.0-1ubuntu1.1_all.deb) ...
     Processing triggers for doc-base ...
     Processing 2 added doc-base files...
     Registering documents with scrollkeeper...
     Processing triggers for man-db ...
     Processing triggers for libglib2.0-0:i386 ...
     Setting up libcairo-script-interpreter2:i386 (1.12.14-0ubuntu1) ...
     Setting up libfreetype6-dev (2.4.11-0ubuntu1) ...
     Setting up libfontconfig1-dev (2.10.2-0ubuntu2) ...
     Setting up xorg-sgml-doctools (1:1.10-1) ...
     Setting up x11proto-core-dev (7.0.23-1) ...
     Setting up libxau-dev:i386 (1:1.0.7-1) ...
     Setting up libxdmcp-dev:i386 (1:1.1.1-1) ...
     Setting up x11proto-input-dev (2.2.99.1-0ubuntu1) ...
     Setting up x11proto-kb-dev (1.0.6-2) ...
     Setting up xtrans-dev (1.2.7-1) ...
     Setting up libpthread-stubs0:i386 (0.3-3) ...
     Setting up libpthread-stubs0-dev:i386 (0.3-3) ...
     Setting up libxcb1-dev:i386 (1.8.1-2ubuntu2.1) ...
     Setting up libx11-dev:i386 (2:1.5.0-1ubuntu1.1) ...
     Setting up x11proto-render-dev (2:0.11.1-2) ...
     Setting up libxrender-dev:i386 (1:0.9.7-1ubuntu0.13.04.1) ...
     Setting up libice-dev:i386 (2:1.0.8-2) ...
     Setting up libsm-dev:i386 (2:1.2.1-2) ...
     Setting up libpixman-1-dev (0.28.2-0ubuntu1) ...
     Setting up libxcb-render0-dev:i386 (1.8.1-2ubuntu2.1) ...
     Setting up libxcb-shm0-dev:i386 (1.8.1-2ubuntu2.1) ...
     Setting up x11proto-xext-dev (7.2.1-1) ...
     Setting up libxext-dev:i386 (2:1.3.1-2ubuntu0.13.04.1) ...
     Setting up libglib2.0-dev (2.36.0-1ubuntu2) ...
     Setting up libcairo2-dev (1.12.14-0ubuntu1) ...
     Setting up libx11-doc (2:1.5.0-1ubuntu1.1) ...
     Processing triggers for libc-bin ...
     ldconfig deferred processing now taking place
     flcellogrl@flcellogrl:~$ sudo apt-get insgtall libxml2-dev libcurl-dev
     E: Invalid operation insgtall
     flcellogrl@flcellogrl:~$ sudo apt-get install libxml2-dev libcurl-dev
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     Package libcurl-dev is a virtual package provided by:
     libcurl4-openssl-dev 7.29.0-1ubuntu3.2
     libcurl4-nss-dev 7.29.0-1ubuntu3.2
     libcurl4-gnutls-dev 7.29.0-1ubuntu3.2
     You should explicitly select one to install.
    E: Package 'libcurl-dev' has no installation candidate
     flcellogrl@flcellogrl:~$ sudo apt-get install libcurl4-openssl-dev
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     The following packages were automatically installed and are no longer required:
     linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic
     linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
     Use 'apt-get autoremove' to remove them.
     The following extra packages will be installed:
     libssl-dev libssl-doc
     Suggested packages:
     libcurl3-dbg
     The following packages will be REMOVED:
     libcurl4-gnutls-dev
     The following NEW packages will be installed:
     libcurl4-openssl-dev libssl-dev libssl-doc
     0 upgraded, 3 newly installed, 1 to remove and 10 not upgraded.
     Need to get 3,638 kB of archives.
     After this operation, 6,418 kB of additional disk space will be used.
     Do you want to continue [Y/n]? y
     Get:1 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libssl-dev i386 1.0.1c-4ubuntu8.1 [1,420 kB]
     Get:2 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libcurl4-openssl-dev i386 7.29.0-1ubuntu3.2 [1,182 kB]
     Get:3 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libssl-doc all 1.0.1c-4ubuntu8.1 [1,035 kB]
     Fetched 3,638 kB in 3s (1,000 kB/s)
     (Reading database ... 241509 files and directories currently installed.)
     Removing libcurl4-gnutls-dev ...
     Processing triggers for man-db ...
     Processing triggers for doc-base ...
     Processing 1 removed doc-base file...
     Registering documents with scrollkeeper...
     Selecting previously unselected package libssl-dev.
     (Reading database ... 241214 files and directories currently installed.)
     Unpacking libssl-dev (from .../libssl-dev_1.0.1c-4ubuntu8.1_i386.deb) ...
     Selecting previously unselected package libcurl4-openssl-dev.
     Unpacking libcurl4-openssl-dev (from .../libcurl4-openssl-dev_7.29.0-1ubuntu3.2_i386.deb) ...
     Selecting previously unselected package libssl-doc.
     Unpacking libssl-doc (from .../libssl-doc_1.0.1c-4ubuntu8.1_all.deb) ...
     Processing triggers for doc-base ...
     Processing 1 added doc-base file...
     Registering documents with scrollkeeper...
     Processing triggers for man-db ...
     Setting up libssl-dev (1.0.1c-4ubuntu8.1) ...
     Setting up libcurl4-openssl-dev (7.29.0-1ubuntu3.2) ...
     Setting up libssl-doc (1.0.1c-4ubuntu8.1) ...
     flcellogrl@flcellogrl:~$ sudo apt-get install libcurl4-nss-dev
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     The following packages were automatically installed and are no longer required:
     libssl-dev libssl-doc linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
     Use 'apt-get autoremove' to remove them.
     The following extra packages will be installed:
     libcurl3-nss libnspr4-dev libnss3-dev
     Suggested packages:
     libcurl3-dbg
     The following packages will be REMOVED:
     libcurl4-openssl-dev
     The following NEW packages will be installed:
     libcurl3-nss libcurl4-nss-dev libnspr4-dev libnss3-dev
     0 upgraded, 4 newly installed, 1 to remove and 10 not upgraded.
     Need to get 1,949 kB of archives.
     After this operation, 3,079 kB of additional disk space will be used.
     Do you want to continue [Y/n]? y
     Get:1 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libcurl3-nss i386 7.29.0-1ubuntu3.2 [246 kB]
     Get:2 http://us.archive.ubuntu.com/ubuntu/ raring/main libnspr4-dev i386 2:4.9.5-1ubuntu1 [275 kB]
     Get:3 http://us.archive.ubuntu.com/ubuntu/ raring/main libnss3-dev i386 2:3.14.3-0ubuntu1 [250 kB]
     Get:4 http://us.archive.ubuntu.com/ubuntu/ raring-updates/main libcurl4-nss-dev i386 7.29.0-1ubuntu3.2 [1,179 kB]
     Fetched 1,949 kB in 2s (829 kB/s)
     (Reading database ... 242914 files and directories currently installed.)
     Removing libcurl4-openssl-dev ...
     Processing triggers for man-db ...
     Processing triggers for doc-base ...
     Processing 1 removed doc-base file...
     Registering documents with scrollkeeper...
     Selecting previously unselected package libcurl3-nss:i386.
     (Reading database ... 242622 files and directories currently installed.)
     Unpacking libcurl3-nss:i386 (from .../libcurl3-nss_7.29.0-1ubuntu3.2_i386.deb) ...
     Selecting previously unselected package libnspr4-dev.
     Unpacking libnspr4-dev (from .../libnspr4-dev_2%3a4.9.5-1ubuntu1_i386.deb) ...
     Selecting previously unselected package libnss3-dev.
     Unpacking libnss3-dev (from .../libnss3-dev_2%3a3.14.3-0ubuntu1_i386.deb) ...
     Selecting previously unselected package libcurl4-nss-dev.
     Unpacking libcurl4-nss-dev (from .../libcurl4-nss-dev_7.29.0-1ubuntu3.2_i386.deb) ...
     Processing triggers for doc-base ...
     Processing 1 added doc-base file...
     Registering documents with scrollkeeper...
     Processing triggers for man-db ...
     Setting up libcurl3-nss:i386 (7.29.0-1ubuntu3.2) ...
     Setting up libnspr4-dev (2:4.9.5-1ubuntu1) ...
     Setting up libnss3-dev (2:3.14.3-0ubuntu1) ...
     Setting up libcurl4-nss-dev (7.29.0-1ubuntu3.2) ...
     Processing triggers for libc-bin ...
     ldconfig deferred processing now taking place
     flcellogrl@flcellogrl:~$ sudo apt-get install libcurl4-gnutls-dev
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     The following packages were automatically installed and are no longer required:
     libcurl3-nss libnspr4-dev libnss3-dev libssl-dev libssl-doc linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
     Use 'apt-get autoremove' to remove them.
     Suggested packages:
     libcurl3-dbg
     The following packages will be REMOVED:
     libcurl4-nss-dev
     The following NEW packages will be installed:
     libcurl4-gnutls-dev
     0 upgraded, 1 newly installed, 1 to remove and 10 not upgraded.
     Need to get 0 B/1,172 kB of archives.
     After this operation, 9,216 B disk space will be freed.
     Do you want to continue [Y/n]? y
     (Reading database ... 243136 files and directories currently installed.)
     Removing libcurl4-nss-dev ...
     Processing triggers for man-db ...
     Processing triggers for doc-base ...
     Processing 1 removed doc-base file...
     Registering documents with scrollkeeper...
     Selecting previously unselected package libcurl4-gnutls-dev.
     (Reading database ... 242841 files and directories currently installed.)
     Unpacking libcurl4-gnutls-dev (from .../libcurl4-gnutls-dev_7.29.0-1ubuntu3.2_i386.deb) ...
     Processing triggers for doc-base ...
     Processing 1 added doc-base file...
     Registering documents with scrollkeeper...
     Processing triggers for man-db ...
     Setting up libcurl4-gnutls-dev (7.29.0-1ubuntu3.2) ...
     flcellogrl@flcellogrl:~$ sudo apt-get install xml2
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     The following packages were automatically installed and are no longer required:
     libcurl3-nss libnspr4-dev libnss3-dev libssl-dev libssl-doc linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
     Use 'apt-get autoremove' to remove them.
     The following NEW packages will be installed:
     xml2
     0 upgraded, 1 newly installed, 0 to remove and 10 not upgraded.
     Need to get 14.8 kB of archives.
     After this operation, 75.8 kB of additional disk space will be used.
     Get:1 http://us.archive.ubuntu.com/ubuntu/ raring/universe xml2 i386 0.4-3.1 [14.8 kB]
     Fetched 14.8 kB in 0s (64.5 kB/s)
     Selecting previously unselected package xml2.
     (Reading database ... 243137 files and directories currently installed.)
     Unpacking xml2 (from .../archives/xml2_0.4-3.1_i386.deb) ...
     Processing triggers for man-db ...
     Setting up xml2 (0.4-3.1) ...
     flcellogrl@flcellogrl:~$ sudo apt-get install xml
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     E: Unable to locate package xml
     flcellogrl@flcellogrl:~$ sudo apt-get install cairo
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     E: Unable to locate package cairo
     flcellogrl@flcellogrl:~$ cat /proc/version
     Linux version 3.8.0-31-generic (buildd@aatxe) (gcc version 4.7.3 (Ubuntu/Linaro 4.7.3-1ubuntu1) ) #46-Ubuntu SMP Tue Sep 10 19:56:49 UTC 2013
     flcellogrl@flcellogrl:~$ sudo apt-get install libcairo2-dev^C
     flcellogrl@flcellogrl:~$ sudo apt-get install libcurl4
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     Package libcurl4 is not available, but is referred to by another package.
     This may mean that the package is missing, has been obsoleted, or
     is only available from another source
     However the following packages replace it:
     libcurl3
    E: Package 'libcurl4' has no installation candidate
     flcellogrl@flcellogrl:~$ sudo apt-get install libcurl3
     Reading package lists... Done
     Building dependency tree
     Reading state information... Done
     libcurl3 is already the newest version.
     The following packages were automatically installed and are no longer required:
     libcurl3-nss libnspr4-dev libnss3-dev libssl-dev libssl-doc linux-headers-3.8.0-19 linux-headers-3.8.0-19-generic linux-image-3.8.0-19-generic linux-image-extra-3.8.0-19-generic
     Use 'apt-get autoremove' to remove them.
     0 upgraded, 0 newly installed, 0 to remove and 10 not upgraded.

Restarted RStudio, but still the same:

    > source("http://bioconductor.org/biocLite.R")
     Your Bioconductor is out-of-date, upgrade to version 2.13 by following instructions at http://bioconductor.org/install.
     Bioconductor version 2.12 (BiocInstaller 1.10.4), ?biocLite for help
     A newer version of Bioconductor is available for this version of R, ?BiocUpgrade for help
     > ?BiocUpgrade
     > biocLite()
     BioC_mirror: http://bioconductor.org
     Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
     Warning message:
     installed directory not writable, cannot update packages 'XML', 'spatial'
    Restarting R session...
    > source("http://bioconductor.org/biocLite.R")
     Your Bioconductor is out-of-date, upgrade to version 2.13 by following instructions at http://bioconductor.org/install.
     Bioconductor version 2.12 (BiocInstaller 1.10.4), ?biocLite for help
     A newer version of Bioconductor is available for this version of R, ?BiocUpgrade for help
     > biocLite()
     BioC_mirror: http://bioconductor.org
     Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
     Warning message:
     installed directory not writable, cannot update packages 'XML', 'spatial'
     > biocLite("arrayQualityMetrics")
     BioC_mirror: http://bioconductor.org
     Using Bioconductor version 2.12 (BiocInstaller 1.10.4), R version 3.0.2.
     Installing package(s) 'arrayQualityMetrics'
     also installing the dependency ‘Cairo’
    trying URL 'http://cran.rstudio.com/src/contrib/Cairo_1.5-2.tar.gz'
     Content type 'application/x-gzip' length 83972 bytes (82 Kb)
     opened URL
     ==================================================
     downloaded 82 Kb
    trying URL 'http://bioconductor.org/packages/2.12/bioc/src/contrib/arrayQualityMetrics_3.16.0.tar.gz'
     Content type 'application/x-gzip' length 573179 bytes (559 Kb)
     opened URL
     ==================================================
     downloaded 559 Kb
    * installing *source* package ‘Cairo’ ...
     ** package ‘Cairo’ successfully unpacked and MD5 sums checked
     checking for gcc... gcc -std=gnu99
     checking whether the C compiler works... yes
     checking for C compiler default output file name... a.out
     checking for suffix of executables...
     checking whether we are cross compiling... no
     checking for suffix of object files... o
     checking whether we are using the GNU C compiler... yes
     checking whether gcc -std=gnu99 accepts -g... yes
     checking for gcc -std=gnu99 option to accept ISO C89... none needed
     checking how to run the C preprocessor... gcc -std=gnu99 -E
     checking for grep that handles long lines and -e... /bin/grep
     checking for egrep... /bin/grep -E
     checking for ANSI C header files... yes
     checking for sys/wait.h that is POSIX.1 compatible... yes
     checking for sys/types.h... yes
     checking for sys/stat.h... yes
     checking for stdlib.h... yes
     checking for string.h... yes
     checking for memory.h... yes
     checking for strings.h... yes
     checking for inttypes.h... yes
     checking for stdint.h... yes
     checking for unistd.h... yes
     checking for string.h... (cached) yes
     checking sys/time.h usability... yes
     checking sys/time.h presence... yes
     checking for sys/time.h... yes
     checking for unistd.h... (cached) yes
     checking for an ANSI C-conforming const... yes
     checking for pkg-config... /usr/bin/pkg-config
     checking whether pkg-config knows about cairo... yes
     checking for configurable backends... cairo cairo-ft cairo-pdf cairo-png cairo-ps cairo-xlib cairo-xlib-xrender
     configure: CAIRO_CFLAGS=-I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12
     checking if R was compiled with the RConn patch... no
     checking cairo.h usability... yes
     checking cairo.h presence... yes
     checking for cairo.h... yes
     checking for PNG support in Cairo... yes
     checking for ATS font support in Cairo... no
     configure: CAIRO_LIBS=-lfreetype -lpng12 -lz -lXrender -lcairo -lXext -lX11
     checking for library containing deflate... none required
     checking whether Cairo programs can be compiled... yes
     checking whether cairo_image_surface_get_format is declared... no
     checking for FreeType support in cairo... yes
     checking whether FreeType needs additional flags... no
     checking wheter libjpeg works... yes
     checking wheter libtiff works... no
     configure: creating ./config.status
     config.status: creating src/Makevars
     config.status: creating src/cconfig.h
     ** libs
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairobem.c -o cairobem.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairogd.c -o cairogd.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c cairotalk.c -o cairotalk.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-backend.c -o img-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-jpeg.c -o img-jpeg.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c img-tiff.c -o img-tiff.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c pdf-backend.c -o pdf-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c ps-backend.c -o ps-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c svg-backend.c -o svg-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c w32-backend.c -o w32-backend.o
     gcc -std=gnu99 -I/usr/share/R/include -DNDEBUG -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12 -I. -Iinclude -O2 -pipe -g -fpic -O2 -pipe -g -c xlib-backend.c -o xlib-backend.o
     xlib-backend.c:34:74: fatal error: X11/Intrinsic.h: No such file or directory
     compilation terminated.
     make: *** [xlib-backend.o] Error 1
     ERROR: compilation failed for package ‘Cairo’
     * removing ‘/home/flcellogrl/R/i686-pc-linux-gnu-library/3.0/Cairo’
     ERROR: dependency ‘Cairo’ is not available for package ‘arrayQualityMetrics’
     * removing ‘/home/flcellogrl/R/i686-pc-linux-gnu-library/3.0/arrayQualityMetrics’
    The downloaded source packages are in
     ‘/tmp/Rtmpsc5TVk/downloaded_packages’
     Warning messages:
     1: In install.packages(pkgs = pkgs, lib = lib, repos = repos, ...) :
     installation of package ‘Cairo’ had non-zero exit status
     2: In install.packages(pkgs = pkgs, lib = lib, repos = repos, ...) :
     installation of package ‘arrayQualityMetrics’ had non-zero exit status
     3: installed directory not writable, cannot update packages 'XML', 'spatial'
     > library("arrayQualityMetrics")
     Error in library("arrayQualityMetrics") :
     there is no package called ‘arrayQualityMetrics’
     > library(arrayQualityMetrics)
     Error in library(arrayQualityMetrics) :
     there is no package called ‘arrayQualityMetrics’