This repository contains the computational data, screening queries, and analysis scripts required to reproduce the virtual screening campaign and cheminformatics analyses described in the manuscript: _"Structure-based Virtual Screening Identifies Novel G protein-Biased Agonists at Mu Opioid Receptor."_

## 📁 Repository Structure
Plaintext
```
├── 1_vs/                        # Virtual Screening Workflow
│   ├── 1_ph4_queries/           # 3D pharmacophore queries
│   ├── 1_rocs_queries/          # ROCS (shape/color) queries
│   ├── 2_ph4_scripts/           # Execution scripts for pharmacophore screening
│   ├── 2_rocs_scripts/          # Execution scripts for ROCS screening
│   └── 3_cluster_merge/         # Reference scripts for clustering hit lists
├── 2_docking_md/                # Binding Mode & Simulation Analysis
└── 3_novelty_check/             # Cheminformatics & Chemical Space Analysis
```

## 📂 Directory Contents
### `1_vs/` (Virtual Screening)
This directory contains the core files used to execute the parallel virtual screening campaign against the 5 million-compound library.

- **`1_ph4_queries` & `1_rocs_queries`**: The final 3D pharmacophore and shape-based queries derived from our unified structural hypothesis.

- **`2_ph4_scripts` & `2_rocs_scripts`**: The computational scripts utilized to run the virtual screening.

- **`3_cluster_merge`**: Scripts used to cluster and merge the results from the different queries. Note: Because the final consensus selection involved manual expert curation, these scripts are provided as reference templates.

### `2_docking_md/` (Binding Mode Analysis)
Contains the predicted docking poses for the three prioritized hit compounds (**3**, **10**, and **12**) within the MOR orthosteric site. This folder also includes the configuration scripts required to run the Molecular Dynamics (MD) simulations and analyze the resulting trajectories.

### `3_novelty_check/` (Chemical Space Analysis)
Includes the scripts used to verify the structural novelty of the three hit compounds. This covers the Principal Component Analysis (PCA) and structural similarity calculations comparing the hits against the broader property space of known opioid receptor ligands.
