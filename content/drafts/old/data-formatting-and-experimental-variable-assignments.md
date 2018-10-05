Title: Data Formatting and Experimental Variable Assignments
Date: 2013-10-12 17:01
Author: monsterbashseq
Category: Microarray, R
Slug: data-formatting-and-experimental-variable-assignments
Status: published

    > source('~/Dropbox/HBOI/sponge raw data/microarray_data_formatting.R')
    > names(b)
     [1] "initial_blockdata.RefNumber" "initial_blockdata.ID"        "initial_blockdata.Name"      "initial_blockdata.Row"       "initial_blockdata.Column"    "Block 1 Chip 1"             
     [7] "Block 2 Chip 1"              "Block 3 Chip 1"              "Block 4 Chip 1"              "Block 5 Chip 1"              "Block 6 Chip 1"              "Block 7 Chip 1"             
    [13] "Block 8 Chip 1"              "Block 1 Chip 2"              "Block 2 Chip 2"              "Block 3 Chip 2"              "Block 4 Chip 2"              "Block 5 Chip 2"             
    [19] "Block 6 Chip 2"              "Block 7 Chip 2"              "Block 8 Chip 2"              "Block 1 Chip 3"              "Block 2 Chip 3"              "Block 3 Chip 3"             
    [25] "Block 4 Chip 3"              "Block 5 Chip 3"              "Block 6 Chip 3"              "Block 7 Chip 3"              "Block 8 Chip 3"              "Block 1 Chip 4"             
    [31] "Block 2 Chip 4"              "Block 3 Chip 4"              "Block 4 Chip 4"              "Block 5 Chip 4"              "Block 6 Chip 4"              "Block 7 Chip 4"             
    [37] "Block 8 Chip 4"              "Block 1 Chip 5"              "Block 2 Chip 5"              "Block 3 Chip 5"              "Block 4 Chip 5"              "Block 5 Chip 5"             
    [43] "Block 6 Chip 5"              "Block 7 Chip 5"              "Block 8 Chip 5"              "Block 1 Chip 6"              "Block 2 Chip 6"              "Block 3 Chip 6"             
    [49] "Block 4 Chip 6"              "Block 5 Chip 6"              "Block 6 Chip 6"              "Block 7 Chip 6"              "Block 8 Chip 6"              "Block 1 Chip 7"             
    [55] "Block 2 Chip 7"              "Block 3 Chip 7"              "Block 4 Chip 7"              "Block 5 Chip 7"              "Block 6 Chip 7"              "Block 7 Chip 7"             
    [61] "Block 8 Chip 7"              "Block 1 Chip 8"              "Block 2 Chip 8"              "Block 3 Chip 8"              "Block 4 Chip 8"              "Block 5 Chip 8"             
    [67] "Block 6 Chip 8"              "Block 7 Chip 8"              "Block 8 Chip 8"              "Block 1 Chip 9"              "Block 2 Chip 9"              "Block 3 Chip 9"             
    [73] "Block 4 Chip 9"              "Block 5 Chip 9"              "Block 6 Chip 9"              "Block 7 Chip 9"              "Block 8 Chip 9"             
    > data_length<-length(names(b))
    > data_info<-read.csv("targets_experiment_sample_info.csv")
    > names(data_info)
    [1] "Chip.Number" "File.Name"   "Hyb.Date"    "Tank"        "Treatment"   "Colony"      "Raceway"     "Block"      
    > head(data_info)
      Chip.Number                   File.Name Hyb.Date Tank Treatment Colony Raceway Block
    1           1 253295110067_2012-08-01.txt 8/1/2012   C3        UC      P       B     1
    2           1 253295110067_2012-08-01.txt 8/1/2012   B2        UD      P       A     2
    3           1 253295110067_2012-08-01.txt 8/1/2012   B2        UD      O       A     3
    4           1 253295110067_2012-08-01.txt 8/1/2012   D3        OD     BL       A     4
    5           1 253295110067_2012-08-01.txt 8/1/2012   D1        OD      O       B     5
    6           1 253295110067_2012-08-01.txt 8/1/2012   C3        UC      O       B     6
    > data_info
       Chip.Number                   File.Name  Hyb.Date Tank Treatment Colony Raceway Block
    1            1 253295110067_2012-08-01.txt  8/1/2012   C3        UC      P       B     1
    2            1 253295110067_2012-08-01.txt  8/1/2012   B2        UD      P       A     2
    3            1 253295110067_2012-08-01.txt  8/1/2012   B2        UD      O       A     3
    4            1 253295110067_2012-08-01.txt  8/1/2012   D3        OD     BL       A     4
    5            1 253295110067_2012-08-01.txt  8/1/2012   D1        OD      O       B     5
    6            1 253295110067_2012-08-01.txt  8/1/2012   C3        UC      O       B     6
    7            1 253295110067_2012-08-01.txt  8/1/2012   A3        OC      W       A     7
    8            1 253295110067_2012-08-01.txt  8/1/2012   A1        OC      W       A     8
    9            2 253295110050_2012-07-25.txt 7/25/2012   A1        OC     BL       A     1
    10           2 253295110050_2012-07-25.txt 7/25/2012   C2        UC      P       B     2
