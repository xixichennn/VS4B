import os
import sys

import pandas as pd

from rdkit import Chem

# inner modules
sys.path.append("/home/yuchen/or/VS4B")
from Scripts.utils import sdf2df, df2sdf
from Scripts.run_clustering import run_cluster

work_dir = '/home/yuchen/or/VS4B/LigandScout/MOR/7t2g_eig_cry/docking/output'
filename = 'filtered_ph4score_over_0_calcIFC_SP.sdf'

sdf_df, sdf_hCoords = sdf2df(os.path.join(work_dir, filename))
sdf_clu_df = run_cluster(sdf_df, sdf_hCoords, cutoff=0.5, output_dir=work_dir)
