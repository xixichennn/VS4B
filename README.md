This repository aims to provide necessary data and scripts to reproduce the virtual screening campaign describe in the manuscript 'Structure-based Virtual Screening Identifies
Novel G protein-Biased Agonists at Mu Opioid Receptor'

Here is the list of files and folders in this repository:
- `1_vs`: 
    - `1_ph4_queries` and `1_rocs_queries`, including ph4(pharmacophore) and rocs(shape/color) queries.
    - `2_ph4_scripts` and `2_rocs_scripts`, including the scripts to run the ph4-based and rocs-based virtual screening.
    - `3_cluster_merge`, including the scripts to cluster the screening results from different queries. Since this step includes a lot of manual work, the scipts here are just for reference.
- `2_docking_md`: including the docking poses for the three hit compounds 3, 10, 12, as well as the scripts to run the MD simulations and analyze the results.
- `3_novelty_check`: including the scripts to check the novelty of the three hit compounds 3, 10, 12. 