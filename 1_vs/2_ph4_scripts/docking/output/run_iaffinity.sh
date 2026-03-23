#! /bin/bash

# This script runs Ligandscout for minimizing the molecules based on MMFF94. @author Yu Chen

workdir=/home/yuchen/or/VS4B/LigandScout/MOR/7t2g_eig_cry/docking/output

#Assuming the below lines have run in the terminal
#source /home/yuchen/.bashrc
#module load ligandscout/ligandscout-4-ilab

# minimize ligand and side chains, before calculating the score.
iaffinity -i ${workdir}/result.sdf -a /home/yuchen/or/VS4B/struct/from_opm/MOR/8efo_nolig.pmz  -o ${workdir}/result_minimized.sdf -m LIGAND

