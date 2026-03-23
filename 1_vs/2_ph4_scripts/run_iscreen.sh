#! /bin/bash

# This script runs Ligandscout for pharmacophore-based screening. @author Yu Chen

cpds=/data/db/chemicals/molport_2023_05/molport_final_2023_05.ldb

# virtual screening with exclusion volume checking abled
iscreen -q 8efo-PZM21_ph4.pmz -d ${cpds} -o screening.sdf -s BEST
