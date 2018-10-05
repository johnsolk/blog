Title: GRE Powerprep crashes on Ubuntu 13.04
Date: 2013-11-05 21:39
Author: monsterbashseq
Category: software, Ubuntu, Windows
Slug: gre-powerprep-crash-on-ubuntu-13-04
Status: published

Old, famous problem with GRE Powerprep software crashing on Ubuntu OS:

-   http://whynotwiki.com/Getting\_GRE\_Powerprep\_to\_work\_under\_Wine
-   http://ubuntuforums.org/showthread.php?t=861707
-   http://bugs.winehq.org/show\_bug.cgi?id=3766
-   http://www.winehq.org/pipermail/wine-bugs/2009-May/175350.html

I agree with this assessment:

http://www.jonathanmoeller.com/screed/?p=3424

I solved this problem by installing a Virtual Machine with Windows XP on
Ubuntu, then running Powerprep through the VM . See steps below.

Apparently this is a bug with wine. Note that the Powerprep software
requires/auto-launches MS Internet Explorer. I am running wine-1.4.1 on
Ubuntu 13.04:

[![Screenshot from 2013-11-05
21:22:44](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-212244.png){.alignnone
.size-full .wp-image-446 width="640"
height="724"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-212244.png)

    Unhandled exception: page fault on write access to 0x37090df1 in 32-bit code (0x01281c10).
    Register dump:
     CS:0073 SS:007b DS:007b ES:007b FS:0033 GS:003b
     EIP:01281c10 ESP:0033f3a4 EBP:0033f3e0 EFLAGS:00210202(  R- --  I   - - - )
     EAX:01d11720 EBX:7e761000 ECX:01d0a310 EDX:01281c10
     ESI:02849faa EDI:00000144
    Stack dump:
    0x0033f3a4:  7e69ca03 01d11720 00000000 0033f410
    0x0033f3b4:  7d1052db 027fa670 b74f77ad 0033f400
    0x0033f3c4:  7d103fb6 00000000 01d2d2f0 0033f3e8
    0x0033f3d4:  0033f3f8 7d1036d3 7d14b000 0033f440
    0x0033f3e4:  7d104caf 01d0a5a0 00000014 027fa670
    0x0033f3f4:  00000000 856269b4 02849faa 0033f440
    Backtrace:
    =>0 0x01281c10 (0x0033f3e0)
      1 0x7d104caf in jscript (+0x14cae) (0x0033f440)
      2 0x7d106c67 in jscript (+0x16c66) (0x0033f480)
      3 0x7d10e9c1 in jscript (+0x1e9c0) (0x0033f500)
      4 0x7d11666e in jscript (+0x2666d) (0x0033f570)
      5 0x7d118747 in jscript (+0x28746) (0x0033f600)
      6 0x7d8a9059 in mshtml (+0xb9058) (0x0033f6a0)
      7 0x7d8a9276 in mshtml (+0xb9275) (0x0033f6f0)
      8 0x7d8a9423 in mshtml (+0xb9422) (0x0033f740)
      9 0x7d8a9a78 in mshtml (+0xb9a77) (0x0033f7a0)
      10 0x7d873430 in mshtml (+0x8342f) (0x0033f800)
      11 0x7d873848 in mshtml (+0x83847) (0x0033f830)
      12 0x69f691a9 in xul (+0x3291a8) (0x0033f860)
      13 0x69f691d1 in xul (+0x3291d0) (0x0033f880)
      14 0x7d873911 in mshtml (+0x83910) (0x0033f8b0)
      15 0x7d87410b in mshtml (+0x8410a) (0x0033f900)
      16 0x69f7e1d5 in xul (+0x33e1d4) (0x0033f940)
      17 0x69f66404 in xul (+0x326403) (0x0033f960)
      18 0x6a1fbb55 in xul (+0x5bbb54) (0x0033f9a0)
      19 0x6a1fd723 in xul (+0x5bd722) (0x0033fa10)
      20 0x6aa6f8e0 in xul (+0xe2f8df) (0x0033fa30)
      21 0x6a7a7e9e in xul (+0xb67e9d) (0x0033fa90)
      22 0x6a771bce in xul (+0xb31bcd) (0x0033fae0)
      23 0x6a652e86 in xul (+0xa12e85) (0x0033fb20)
      24 0x6a6279a9 in xul (+0x9e79a8) (0x0033fb40)
      25 0x7e9bdac2 WINPROC_wrapper+0x19() in user32 (0x0033fb70)
      26 0x7e9bdc17 WINPROC_wrapper+0x16e() in user32 (0x0033fbc0)
      27 0x7e9c025b in user32 (+0xc025a) (0x0033fc10)
      28 0x7e97feae DispatchMessageW+0x19a() in user32 (0x0033fd20)
      29 0x7ed07b66 IEWinMain+0xfc() in ieframe (0x0033fd80)
      30 0x7ed68a1c wWinMain+0x8f() in iexplore (0x0033fda0)
      31 0x7ed68ced wmain+0x10c() in iexplore (0x0033fe10)
      32 0x7ed68bc6 in iexplore (+0x8bc5) (0x0033fe40)
      33 0x7b8621c8 call_process_entry+0xb() in kernel32 (0x0033fe58)
      34 0x7b86230e call_process_entry+0x151() in kernel32 (0x0033fea8)
      35 0x7bc7f84c call_thread_func_wrapper+0xb() in ntdll (0x0033feb8)
      36 0x7bc7f89b call_thread_func+0x44() in ntdll (0x0033ff98)
      37 0x7bc7f82a in ntdll (+0x6f829) (0x0033ffb8)
      38 0x7bc54b97 in ntdll (+0x44b96) (0x0033ffe8)
      39 0xb75b0c19 wine_call_on_stack+0x1c() in libwine.so.1 (0x00000000)
      40 0xb75b0bf7 wine_switch_to_stack+0x2a() in libwine.so.1 (0xbfd03c58)
      41 0x7bc54ed9 LdrInitializeThunk+0x341() in ntdll (0xbfd03cd8)
      42 0x7b862be7 __wine_kernel_init+0x71b() in kernel32 (0xbfd04b68)
      43 0x7bc5566e __wine_process_init+0x156() in ntdll (0xbfd04bb8)
      44 0xb75af446 wine_init+0x13d() in libwine.so.1 (0xbfd04bf8)
      45 0x7bf011ca main+0x13d() in <wine-loader> (0xbfd05038)
      46 0xb73d9935 __libc_start_main+0xf4() in libc.so.6 (0x00000000)
    0x01281c10: orb    %bh,0x35386ae1(%ecx)
    Modules:
    Module    Address            Debug info    Name (136 modules)
    PE    61700000-61777000    Deferred        mozsqlite3
    PE    61e40000-61e4c000    Deferred        mozalloc
    PE    622c0000-622cd000    Deferred        plds4
    PE    62e40000-62e67000    Deferred        smime3
    PE    64f40000-64f75000    Deferred        nspr4
    PE    68400000-684ea000    Deferred        nss3
    PE    68780000-6879a000    Deferred        nssutil3
    PE    69c40000-6b009000    Export          xul
    PE    6c800000-6c832000    Deferred        ssl3
    PE    6ce40000-6ce4d000    Deferred        plc4
    PE    70180000-704b9000    Deferred        mozjs
    ELF    7b800000-7ba44000    Dwarf           kernel32<elf>
      \-PE    7b810000-7ba44000    \               kernel32
    ELF    7bc00000-7bce4000    Dwarf           ntdll<elf>
      \-PE    7bc10000-7bce4000    \               ntdll
    ELF    7bf00000-7bf04000    Dwarf           <wine-loader>
    ELF    7cdce000-7cdeb000    Deferred        libgcc_s.so.1
    ELF    7d0ca000-7d0df000    Deferred        t2embed<elf>
      \-PE    7d0d0000-7d0df000    \               t2embed
    ELF    7d0df000-7d163000    Dwarf           jscript<elf>
      \-PE    7d0f0000-7d163000    \               jscript
    ELF    7d163000-7d17f000    Deferred        spoolss<elf>
      \-PE    7d170000-7d17f000    \               spoolss
    ELF    7d17f000-7d1a2000    Deferred        localspl<elf>
      \-PE    7d180000-7d1a2000    \               localspl
    ELF    7d1a2000-7d1ab000    Deferred        librt.so.1
    ELF    7d1ab000-7d1b0000    Deferred        libgpg-error.so.0
    ELF    7d1b0000-7d1c7000    Deferred        libresolv.so.2
    ELF    7d1c7000-7d1cb000    Deferred        libkeyutils.so.1
    ELF    7d1cb000-7d215000    Deferred        libdbus-1.so.3
    ELF    7d215000-7d229000    Deferred        libp11-kit.so.0
    ELF    7d229000-7d23b000    Deferred        libtasn1.so.3
    ELF    7d23b000-7d2bf000    Deferred        libgcrypt.so.11
    ELF    7d2bf000-7d2e7000    Deferred        libk5crypto.so.3
    ELF    7d2e7000-7d3b5000    Deferred        libkrb5.so.3
    ELF    7d3b5000-7d3c7000    Deferred        libavahi-client.so.3
    ELF    7d3c7000-7d48c000    Deferred        libgnutls.so.26
    ELF    7d48c000-7d4c9000    Deferred        libgssapi_krb5.so.2
    ELF    7d4c9000-7d528000    Deferred        libcups.so.2
    ELF    7d528000-7d598000    Deferred        dbghelp<elf>
      \-PE    7d530000-7d598000    \               dbghelp
    ELF    7d598000-7d686000    Deferred        comdlg32<elf>
      \-PE    7d5a0000-7d686000    \               comdlg32
    ELF    7d686000-7d73c000    Deferred        winmm<elf>
      \-PE    7d690000-7d73c000    \               winmm
    ELF    7d73c000-7d7de000    Deferred        msvcrt<elf>
      \-PE    7d750000-7d7de000    \               msvcrt
    ELF    7d7de000-7d926000    Dwarf           mshtml<elf>
      \-PE    7d7f0000-7d926000    \               mshtml
    ELF    7d9d7000-7d9e0000    Deferred        libkrb5support.so.0
    ELF    7d9e0000-7d9ee000    Deferred        libavahi-common.so.3
    ELF    7d9f3000-7da06000    Deferred        gnome-keyring-pkcs11.so
    ELF    7da06000-7da1a000    Deferred        msimg32<elf>
      \-PE    7da10000-7da1a000    \               msimg32
    ELF    7da1a000-7da2e000    Deferred        psapi<elf>
      \-PE    7da20000-7da2e000    \               psapi
    ELF    7da2e000-7da6f000    Deferred        winspool<elf>
      \-PE    7da40000-7da6f000    \               winspool
    ELF    7dac7000-7dacc000    Deferred        libcom_err.so.2
    ELF    7dacc000-7db00000    Deferred        ws2_32<elf>
      \-PE    7dad0000-7db00000    \               ws2_32
    ELF    7dc01000-7dc26000    Deferred        iphlpapi<elf>
      \-PE    7dc10000-7dc26000    \               iphlpapi
    ELF    7dc26000-7dc42000    Deferred        wsock32<elf>
      \-PE    7dc30000-7dc42000    \               wsock32
    ELF    7dc42000-7dc6e000    Deferred        msacm32<elf>
      \-PE    7dc50000-7dc6e000    \               msacm32
    ELF    7dc6e000-7dcae000    Deferred        usp10<elf>
      \-PE    7dc70000-7dcae000    \               usp10
    ELF    7dcc6000-7dcfd000    Deferred        uxtheme<elf>
      \-PE    7dcd0000-7dcfd000    \               uxtheme
    ELF    7dcfd000-7dd04000    Deferred        libxfixes.so.3
    ELF    7dd04000-7dd0f000    Deferred        libxcursor.so.1
    ELF    7ddfb000-7de23000    Deferred        libexpat.so.1
    ELF    7de23000-7de5c000    Deferred        libfontconfig.so.1
    ELF    7de5c000-7de6c000    Deferred        libxi.so.6
    ELF    7de6c000-7de70000    Deferred        libxcomposite.so.1
    ELF    7de70000-7de7b000    Deferred        libxrandr.so.2
    ELF    7de7b000-7de85000    Deferred        libxrender.so.1
    ELF    7de85000-7de8b000    Deferred        libxxf86vm.so.1
    ELF    7de8b000-7de8f000    Deferred        libxinerama.so.1
    ELF    7de8f000-7deb3000    Deferred        imm32<elf>
      \-PE    7dea0000-7deb3000    \               imm32
    ELF    7deb3000-7deba000    Deferred        libxdmcp.so.6
    ELF    7deba000-7debe000    Deferred        libxau.so.6
    ELF    7debe000-7dee0000    Deferred        libxcb.so.1
    ELF    7dee0000-7defa000    Deferred        libice.so.6
    ELF    7defa000-7e031000    Deferred        libx11.so.6
    ELF    7e031000-7e043000    Deferred        libxext.so.6
    ELF    7e043000-7e04c000    Deferred        libsm.so.6
    ELF    7e04c000-7e0fd000    Deferred        winex11<elf>
      \-PE    7e060000-7e0fd000    \               winex11
    ELF    7e0fd000-7e198000    Deferred        libfreetype.so.6
    ELF    7e198000-7e1c1000    Deferred        mpr<elf>
      \-PE    7e1a0000-7e1c1000    \               mpr
    ELF    7e1c1000-7e1da000    Deferred        libz.so.1
    ELF    7e1da000-7e254000    Deferred        wininet<elf>
      \-PE    7e1e0000-7e254000    \               wininet
    ELF    7e254000-7e373000    Deferred        comctl32<elf>
      \-PE    7e260000-7e373000    \               comctl32
    ELF    7e373000-7e3e9000    Deferred        shlwapi<elf>
      \-PE    7e380000-7e3e9000    \               shlwapi
    ELF    7e3e9000-7e627000    Deferred        shell32<elf>
      \-PE    7e400000-7e627000    \               shell32
    ELF    7e627000-7e76c000    Deferred        oleaut32<elf>
      \-PE    7e640000-7e76c000    \               oleaut32
    ELF    7e76c000-7e7f6000    Deferred        rpcrt4<elf>
      \-PE    7e780000-7e7f6000    \               rpcrt4
    ELF    7e7f6000-7e811000    Deferred        version<elf>
      \-PE    7e800000-7e811000    \               version
    ELF    7e811000-7e8f2000    Deferred        gdi32<elf>
      \-PE    7e820000-7e8f2000    \               gdi32
    ELF    7e8f2000-7ea62000    Dwarf           user32<elf>
      \-PE    7e900000-7ea62000    \               user32
    ELF    7ea62000-7ead4000    Deferred        advapi32<elf>
      \-PE    7ea70000-7ead4000    \               advapi32
    ELF    7ead4000-7ec36000    Deferred        ole32<elf>
      \-PE    7eaf0000-7ec36000    \               ole32
    ELF    7ec36000-7ece3000    Deferred        urlmon<elf>
      \-PE    7ec40000-7ece3000    \               urlmon
    ELF    7ece3000-7ed57000    Dwarf           ieframe<elf>
      \-PE    7ecf0000-7ed57000    \               ieframe
    ELF    7ed57000-7ed73000    Dwarf           iexplore<elf>
      \-PE    7ed60000-7ed73000    \               iexplore
    ELF    7ed73000-7ed80000    Deferred        libnss_files.so.2
    ELF    7ed80000-7ed8c000    Deferred        libnss_nis.so.2
    ELF    7ed8c000-7eda5000    Deferred        libnsl.so.1
    ELF    7efa5000-7efe8000    Deferred        libm.so.6
    ELF    b73b1000-b73ba000    Deferred        libnss_compat.so.2
    ELF    b73bb000-b73c0000    Deferred        libdl.so.2
    ELF    b73c0000-b7574000    Dwarf           libc.so.6
    ELF    b7575000-b7590000    Deferred        libpthread.so.0
    ELF    b75a1000-b75a7000    Deferred        libuuid.so.1
    ELF    b75a8000-b76ec000    Dwarf           libwine.so.1
    ELF    b76ee000-b7710000    Deferred        ld-linux.so.2
    ELF    b7710000-b7711000    Deferred        [vdso].so
    Threads:
    process  tid      prio (all id:s are in hex)
    0000000e services.exe
        00000034    0
        00000033    0
        0000001d    0
        00000015    0
        00000010    0
        0000000f    0
    00000012 winedevice.exe
        00000020    0
        00000019    0
        00000014    0
        00000013    0
    0000001a plugplay.exe
        0000001f    0
        0000001c    0
        0000001b    0
    00000021 explorer.exe
        00000022    0
    00000025 (D) C:\windows\system32\iexplore.exe
        00000039    0
        00000032    0
        00000031    0
        00000030    0
        0000002f    0
        0000002e    0
        0000002d    0
        0000002c    0
        0000002b    0
        0000002a    0
        00000029    0
        00000028    0
        00000027    0
        00000026    0 <==
    System information:
        Wine build: wine-1.4.1
        Platform: i386
        Host system: Linux
        Host version: 3.8.0-32-generic

So, I installed a virtual machine.  
(use this for server installation:
http://askubuntu.com/questions/73234/is-there-a-way-to-create-a-windows-virtual-machine-on-ubuntu-server)

These instructions ROCK!! http://www.howtogeek.com/117635/

    flcellogrl@flcellogrl:~$ egrep -c ‘(svm|vmx)’ /proc/cpuinfo

Mine returned "2"

Ran the rest of the commands from the instructions, logged out, logged
back in:

[![Screenshot from 2013-11-05
21:38:02](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-213802.png){.alignnone
.size-full .wp-image-448 width="518"
height="179"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-213802.png)

Run "Virtual Machine Manager" from menu:

[![Screenshot from 2013-11-05
21:43:26](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-214326.png){.alignnone
.size-full .wp-image-452 width="493"
height="536"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-214326.png)

This happened, but it prompted to install additional items, so I just
said "Yes":

[![Screenshot from 2013-11-05
21:40:35](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-214035.png){.alignnone
.size-full .wp-image-451 width="557"
height="582"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-214035.png)

Create New Virtual Machine, select ISO Windows XP 32-bit installation
file:

[![Screenshot from 2013-11-05
22:18:01](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-221801.png){.alignnone
.size-full .wp-image-456 width="640"
height="587"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-221801.png)

Of course, this was probably WAY too much memory? I just left all of the
settings to their default, but should have read some instructions, like
these:
http://www.wikihow.com/Install-Windows-XP-on-Ubuntu-with-VirtualBox

[![Screenshot from 2013-11-05
22:20:31](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222031.png){.alignnone
.size-full .wp-image-458 width="469"
height="250"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222031.png)
[![Screenshot from 2013-11-05
22:20:48](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222048.png){.alignnone
.size-full .wp-image-459 width="474"
height="324"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222048.png)
[![Screenshot from 2013-11-05
22:21:11](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222111.png){.alignnone
.size-full .wp-image-460 width="469"
height="590"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222111.png)
[![Screenshot from 2013-11-05
22:22:00](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222200.png){.alignnone
.size-full .wp-image-461 width="640"
height="502"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222200.png)

Parition, now what?

https://help.ubuntu.com/community/HowtoResizeWindowsPartitions  
https://help.ubuntu.com/community/Partitioning%20issues  
http://www.wikihow.com/Install-Windows-XP-on-Ubuntu-with-VirtualBox  
https://help.ubuntu.com/community/Partitioning%20issues  
I chose this option:

[![Screenshot from 2013-11-05
22:25:57](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222557.png){.alignnone
.size-full .wp-image-462 width="640"
height="501"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-05-222557.png)

Windows XP installed and is up and running. Now, of of course, both
Ubuntu and XP through the Virtual Machine are very slow. It took about 5
min for the java-based Powerprep software to load. But, ETS PowerPrep
software practice GRE works. Thanks for wasting a day, ETS. I hope that
I get a better score because of this.

[![Screenshot from 2013-11-06
18:39:43](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-06-183943.png){.alignnone
.size-full .wp-image-466 width="640"
height="406"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-06-183943.png)
[![Screenshot from 2013-11-06
18:43:09](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-06-184309.png){.alignnone
.size-full .wp-image-467 width="640"
height="406"}](http://monsterbashseq.files.wordpress.com/2013/11/screenshot-from-2013-11-06-184309.png)
