#!/bin/bash

######################################################################
#
# Combine trajectory files in sequence––that is, append them end-to-end
#
######################################################################
# @author: Yu Chen

SCHRODINGER=/software/desmond/2022-1

$SCHRODINGER/run trj_merge.py desmond_md_job_1.cms \
0/desmond_md_job_1_0_trj \
1/desmond_md_job_1_1_trj \
2/desmond_md_job_1_2_trj \
3/desmond_md_job_1_3_trj \
4/desmond_md_job_1_4_trj \
-o merged_out \
-concat 0 100
