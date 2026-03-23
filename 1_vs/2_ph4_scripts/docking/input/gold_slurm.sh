#!/bin/bash

#SBATCH --job-name=VS4B
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=all-cpu 
#SBATCH --array=1-51

workdir=/home/yuchen/or/VS4B/LigandScout/MOR/8efo_8qy_mini/docking
GOLDHOME=/software/ccdc/goldsuite-5.2/GOLD

# if the output directory exists, delete it
if [ -d ${workdir}/output/${SLURM_ARRAY_TASK_ID} ]; then
    rm -rf ${workdir}/output/${SLURM_ARRAY_TASK_ID}
fi

# create the output directory
mkdir ${workdir}/output/${SLURM_ARRAY_TASK_ID}

# copy the input files to the output directory
cp ${workdir}/input/gold.conf ${workdir}/output/${SLURM_ARRAY_TASK_ID}/gold${SLURM_ARRAY_TASK_ID}.conf
# 10 ligands per job
sed -i 's/xstartxendx/start_at_ligand '$(((SLURM_ARRAY_TASK_ID-1)*300+1))' finish_at_ligand '$((SLURM_ARRAY_TASK_ID*300))'/' ${workdir}/output/${SLURM_ARRAY_TASK_ID}/gold${SLURM_ARRAY_TASK_ID}.conf
sed -i 's/xnumberx/'${SLURM_ARRAY_TASK_ID}'/g'  ${workdir}/output/${SLURM_ARRAY_TASK_ID}/gold${SLURM_ARRAY_TASK_ID}.conf

${GOLDHOME}/bin/gold_auto ${workdir}/output/${SLURM_ARRAY_TASK_ID}/gold${SLURM_ARRAY_TASK_ID}.conf
