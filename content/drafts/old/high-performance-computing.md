Title: High Performance Computing
Date: 2013-12-12 13:46
Author: monsterbashseq
Category: High Performance Computing
Slug: high-performance-computing
Status: published

"When I care how fast I get an answer"

Cluster user setup at work this week.

HPC has a lot of jargon and acronyms.

Intro: According to XSEDE (reference?), 31% of HPC users are in
Molecular Biosciences

Concerned with number of Floating Point Operations Per Second (FLOP/s).
The number the environment can provide is a concern. Delivers large
amounts of processing capacity over long periods of time. Sustained vs.
peak cycles - as close to 100% as possible. For example, "K"
supercomputer &gt;10PetaFLOP/s at 93%

Bioinformatics requires many task computing, completing large number of
relatively short jobs. Need to effectively manage. We are task parallel
vs. other applications more data parallel

Cluster: one or more networks, nodes connected. Software (MPI, open
source) allows nodes to communicate, allows users to reserve resources.
Log on to one node. 1 master, 4 slaves. Interconnect network.

Infiniband "fabric" with multicore parallel workstation

RDMA- Infiniband mediates interconnections

UMA- memory for all

NUMA- pools of memory

1 node has 64 (or 32?) cores

AMD vs. Intel processors, we have AMD

Cannot send data faster than latency and bandwidth of network
(microseconds), want low latency.

Build RAM disk, put files directly on memory of computer, just like
having solid state disk on laptop

Find code for GPU, co-processors (?)

[![Figure\_2.1\_TypicalComputerArchitecture](http://monsterbashseq.files.wordpress.com/2013/12/figure_2-1_typicalcomputerarchitecture.jpg?w=300){.alignnone
.wp-image-710 width="300"
height="163"}](http://e-negotiations.org/wp-content/uploads/2012/09/Figure_2.1_TypicalComputerArchitecture.jpg)

Running faster, cache memory- order in which numbers are stored changes
depending on what language you use. Efficient code will not waste space.
Writing loops impacts the order in which data goes into CPU memory.

Running faster pipelines, n-stage pipeline, eliminate "if" loops with
branch prediction, profile code if possible

Apparently FMA (floating multiplier add) not relevant to bioinformatics
tasks?

Introduce checkpoints in code.
