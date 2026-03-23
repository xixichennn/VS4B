import os
import sys

import pandas as pd

# inner modules
sys.path.append("/home/yuchen/or/VS4B")
from Scripts.utils import sdf2df, df2sdf

#=============== for table downloaded from Molport ===============#
work_dir = '/home/yuchen/or/VS4B/LigandScout/MOR/7t2g_eig_cry'
# read the file that contains the molport id and purity of the best 500 compounds
molport_file = os.path.join(work_dir , 'molport_ids_purity.txt')
molport_df = pd.read_csv(molport_file, sep='\t')
# for column 'Purity', extract the number after the sign '≥'
molport_df['Purity_value'] = molport_df['Purity'].str.extract(r'(\d+)')
# filter out the rows where 'Purity_value' is smaller than 90 or not a number
molport_90_df = molport_df[molport_df['Purity_value'].astype(float) < 90]
# replace 'Molport' with 'MolPort' in the 'Molport ID' column
molport_90_df['Molport ID'] = molport_90_df['Molport ID'].str.replace('Molport', 'MolPort')

molport_ids_unwanted = molport_90_df['Molport ID'].tolist()
print(f'Number of unwanted compounds: {len(molport_ids_unwanted)}')

#================   for sdf file   =================#
# read the file 'clean.sdf'
clean_sdf_file = os.path.join(work_dir, 'docking', 'output', 'clean.sdf')
clean_sdf_df, clean_sdf_hCoords = sdf2df(clean_sdf_file)
# filter out the rows where 'molport_id' is in 'molport_ids_unwanted'
clean_purity_df = clean_sdf_df[~clean_sdf_df['molport_id'].isin(molport_ids_unwanted)]
output_dir = os.path.join(work_dir, 'docking', 'output')
df2sdf(clean_purity_df, clean_sdf_hCoords, output_dir, 'clean_purity90.sdf')
