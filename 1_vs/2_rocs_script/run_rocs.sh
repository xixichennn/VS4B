#! /bin/bash

# This script runs ROCS. @author Yu Chen

query=7t2g_PZM21.sdf # PZM21
database=/data/db/chemicals/molport_2023_05/molport_final_2023_05.oeb.gz

OPENEYE=/software/openeye.before2024/bin
#source /home/yuchen/.bashrc
#module load openeye/openeye-2015-02-27

$OPENEYE/rocs -query ${query} -dbase ${database} -besthits 500 -oformat sdf -prefix eig -outputdir . -mpi_np 6

#rocs \
#    # InputOptions
#    # query file
#    -query ${query} \
#    # database file
#    -dbase ${database} \
#
#    # OutputOptions
#    # Maximum number of hits to return. The difference is that maxhits won't search entire database, but -besthits will.
#    -maxhits 5000 \
#    # Output format
#    -oformat sdf \
#    # Prefix for output files
#    -prefix 8qy \
#    # Output directory
#    -outputdir . 
