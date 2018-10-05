Title: Reproducibility with AWS - NGS2015
Date: 2015-08-27 11:38
Author: monsterbashseq
Category: Genomics Workshop, reproducibility, workshops
Slug: reproducibility-with-aws-ngs2015
Status: published

Leigh Sheneman, [PhD student at MSU](http://www.leighsheneman.com/) in
CS. Evolution and learning with digital organisms, applying to real
world organisms in the future!

http://angus.readthedocs.org/en/2015/week3/AWS-tips.html

https://www.flickr.com/photos/lpcohen/20739813479/

Start EC2, medium-sized m3.medium is fine. Log in, update and install
stuff. We need the packages for the software we will run with the
eel-pond protocols: https://khmer-protocols.readthedocs.org/en/v0.8.4/

Discussion about interesting package name,

    apt-get -y install libncurses5-dev

Titus: text window graphics from 70s games, likely needed for samtools
tview? Everyone: Ahhhhh (understanding)

We're going to make public AMI, for times if we wanted to share and
distribute to colleagues for collaboration.

Go to EC2 console.

[![create\_image](https://monsterbashseq.files.wordpress.com/2015/08/create_image.png?w=300){.alignnone
.size-medium .wp-image-1100 width="300"
height="173"}](https://monsterbashseq.files.wordpress.com/2015/08/create_image.png)

[![create](https://monsterbashseq.files.wordpress.com/2015/08/create.png?w=300){.alignnone
.size-medium .wp-image-1101 width="300"
height="156"}](https://monsterbashseq.files.wordpress.com/2015/08/create.png)

[![AMI](https://monsterbashseq.files.wordpress.com/2015/08/ami.png?w=300){.alignnone
.size-medium .wp-image-1102 width="300"
height="134"}](https://monsterbashseq.files.wordpress.com/2015/08/ami.png)

Efficient way to capture OS and software, can terminate instance and
keep AMI and only get charged fraction of cost (about \$0.10 per
month/GB) rather than keeping instance running. Snapshot is for volume
of data rather than image, which is OS filesystem.

Change permissions so you are not the only owner. Since we want to make
public.

[![public\_images](https://monsterbashseq.files.wordpress.com/2015/08/public_images.png?w=300){.alignnone
.size-medium .wp-image-1103 width="300"
height="162"}](https://monsterbashseq.files.wordpress.com/2015/08/public_images.png)

[![lookatpublic](https://monsterbashseq.files.wordpress.com/2015/08/lookatpublic.png?w=300){.alignnone
.size-medium .wp-image-1104 width="300"
height="218"}](https://monsterbashseq.files.wordpress.com/2015/08/lookatpublic.png)

Takes some time to make this public. So, wait a bit before sharing
AMI-ID.

Important, this image was created in the 'N. Virginia' region. This
image is only visible in the 'N. Virginia' region. There are other ways
to share between regions.

Class discussion about costs for hosting images and sharing images
associated with publications. Who pays? If reviewers of papers will need
the images, how does that work? It is easy to share data and software
associated with analyses for studies. We can provide all the
instructions and data and software we want. But no one has figured out a
realistic and sustainable management framework for computing resources
for scientific studies. Reproducibility is of concern, but there are no
incentives for scientists to provide data and transparent analyses via
methods like AWS AMI to demonstrate reproducibility. If this were
required for publication, there would likely be more funding resources
available and everyone would do this instead of a select few. Now,
people can provide stuff like this, but who is really going out and
checking other peoples' data and code and software, besides reviewers
and few colleagues?

**Create Volume**

Make sure the availability zone (e.g. us-east-1e) matches the instance.
If not, pull down menu and select:

![public\_ami](https://monsterbashseq.files.wordpress.com/2015/08/public_ami.png?w=300){.alignnone
.size-medium .wp-image-1105 width="300" height="122"}

[![volume](https://monsterbashseq.files.wordpress.com/2015/08/volume.png?w=300){.alignnone
.size-medium .wp-image-1106 width="300"
height="110"}](https://monsterbashseq.files.wordpress.com/2015/08/volume.png)

[![volume\_avail](https://monsterbashseq.files.wordpress.com/2015/08/volume_avail.png?w=300){.alignnone
.size-medium .wp-image-1107 width="300"
height="146"}](https://monsterbashseq.files.wordpress.com/2015/08/volume_avail.png)

Then attach a new 100GB volume to instance. Log out of ssh, log back in.
Run mount commands to format disk :

[![mount](https://monsterbashseq.files.wordpress.com/2015/08/mount1.png?w=298){.alignnone
.size-medium .wp-image-1109 width="298"
height="300"}](https://monsterbashseq.files.wordpress.com/2015/08/mount1.png)

In the above list /dev/xvda1 is system disk, we attached /dev/xvdf

See elastic cloud computing manual for [Amazon Web Services: AMI,
Volume, Snapshot, and
Instances.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instances-and-amis.html)

https://www.flickr.com/photos/lpcohen/20738536090/

If creating an image for someone else, you would do the above where we
took an image of an OS and a snapshot of a volume.

https://www.flickr.com/photos/lpcohen/20738795578/in/dateposted-public/

Now, (power pose) we will load someone else's snapshot (it's really our
snapshot, but same idea). First, we have to **Launch** an AMI instance,
m3.medium is fine:

[![createAMI](https://monsterbashseq.files.wordpress.com/2015/08/createami1.png?w=300){.alignnone
.size-medium .wp-image-1111 width="300"
height="183"}](https://monsterbashseq.files.wordpress.com/2015/08/createami1.png)

Then, create a volume from the snapshot to add to the running instance.

[![create\_snapshot\_thenvolume](https://monsterbashseq.files.wordpress.com/2015/08/create_snapshot_thenvolume.png?w=300){.alignnone
.size-medium .wp-image-1112 width="300"
height="222"}](https://monsterbashseq.files.wordpress.com/2015/08/create_snapshot_thenvolume.png)

The volume is available to attach:

[![volumes](https://monsterbashseq.files.wordpress.com/2015/08/volumes.png?w=300){.alignnone
.size-medium .wp-image-1113 width="300"
height="89"}](https://monsterbashseq.files.wordpress.com/2015/08/volumes.png)

Under "Actions", attach volume and select the running instance (should
pop up once you start typing).

Log in, then mount volume (do not format new volume because this
contains the data!), and it is there!!

[![mount\_xvdf](https://monsterbashseq.files.wordpress.com/2015/08/mount_xvdf.png?w=300){.alignnone
.size-medium .wp-image-1114 width="300"
height="39"}](https://monsterbashseq.files.wordpress.com/2015/08/mount_xvdf.png)

**Creating a bucket to share files, S3**

If you wanted to host files for others to download, \$0.10/GB per month.

[![S3](https://monsterbashseq.files.wordpress.com/2015/08/s3.png?w=300){.alignnone
.size-medium .wp-image-1115 width="300"
height="121"}](https://monsterbashseq.files.wordpress.com/2015/08/s3.png)

Then, you can get the link for people to download:

    curl -O https://s3.amazonaws.com/lisangs2015/bigwig.py
