Title: IDLE in Windows
Date: 2012-08-25 13:27
Author: monsterbashseq
Category: Python, Windows
Tags: idle, Microsoft Windows, Personal firewall, Programming, Python 2.7, Windows XP
Slug: idle-in-windows
Status: published

When I first installed the Python 3 IDLE on Windows XP and tried to open
the environment, I would get this error message, "IDLE's subprocess
didn't make connection. Either IDLE can't start a subprocess or personal
firewall software is blocking the connection:

[![errormsg\_atwork](http://monsterbashseq.files.wordpress.com/2013/05/errormsg_atwork.jpg?w=640){.alignnone
.size-large .wp-image-35 width="640"
height="528"}](http://monsterbashseq.files.wordpress.com/2013/05/errormsg_atwork.jpg)

I changed my systems firewall exceptions to include IDLE, but it still
did not work. I have Python 2.7 installed also because of an ArGIS
software dependency. So, the next step seemed to be to [run IDLE with
the "-n option", without a
"subprocess"](http://stackoverflow.com/questions/3277946/no-idle-subprocess-connection).

I have no idea what "-n option" or "subprocess" mean.

I found this [forum
post](https://secure.csse.uwa.edu.au/run/help1401?p=np&a=298&all=y5)
(which no longer seems to exist), where someone had posted very clear,
simple step-by-step instructions for setting this up in Windows.
Basically, you want to create a shortcut on your desktop to pythonw.exe
from the installation folder of Python (e.g. C:\\Program
Files\\Python32). When you right-click on the shortcut, modify the
target to:

"C:\\Program Files\\Python32\\pythonw.exe" lib\\idlelib\\idle.py -n

This works! The IDLE should start like this, with "No Subprocess":

[![no
subprocess](http://monsterbashseq.files.wordpress.com/2013/05/no-subprocess.jpg?w=640){.alignnone
.size-large .wp-image-36 width="640"
height="668"}](http://monsterbashseq.files.wordpress.com/2013/05/no-subprocess.jpg)
