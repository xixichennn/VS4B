from rdkit import Chem
from rdkit.Chem import AllChem, PandasTools
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams

#input sdf containing all molecules to be filtered
sdf = "result_minimized.sdf_no_PAINS.sdf"


#input SMARTS patterns within '' marks with , as delimiter
smarts = [
    # Michael acceptors (corrected version)
    "[$([#6](~[#6])(~[#6])),$([#6](~[#1])(~[#6])),$([#6](~[#1])(~[#1]))]=[#6]~[#6,#7,#15,#16](=[#7,#8,#16])~[#6,#7X3,#8X2]",
    # Tetrafluoroethylene
    "[#6](~[#9])(~[#9])~[#6](~[#9])(~[#9])",
    # Pentahalogenated phenyls
    "[#6]1~[#6](~[#9,#17,#35,#53])~[#6](~[#9,#17,#35,#53])~[#6](~[#9,#17,#35,#53])~[#6](~[#9,#17,#35,#53])~[#6]~1(~[#9,#17,#35,#53])",
    # Thioureas
    "[#7]~[#6](=[#16])~[#7]",
    # Flavones
    "[#8]=[#6]1~c2c(~[#8]~[#6]=,:[#6]~1)cccc2",
    # Thiols
    "[#6]~[#16X2&H1]",
    # Diazo compounds
    "[#7&R0]=[#7&R0]",
    # Aldehydes
    "[#6]~[#6H1&R0]=[#8]",
    # Hydrazones, oximes, imines, hydrazides, hydroxamates, hydrazines
    "[$([#6]=[#7&R0]~[#7,#8]),$([#6]=[#7]~[#7&R0,#8&R0])]",
    "[#6]=[#7&R0]~[#6]",
    "[$([#6](=[#8,#16])~[#7&R0]-[#7,#8]),$([#6](=[#8,#16])~[#7]-[#7&R0,#8&R0])]",
    "[#7&R0]-[#7&R0]",
    # Known cytostatic drugs (temozolomide, anthraquinones, mustards)
    "[#7]1~[#6](=[#8])~[#7]~[#7]~[#7]~[#6]~1",
    "[#6]1(=[#7,#8,#16])~[#6]=,:[#6]~[#6](=[#7,#8,#16])~[*]~[*]~1",
    "[#7,#16]-[#6X4]-[#6]-[#17,#35,#53]",
    # Thioesters
    "[#6]~[#6](=[#16])~[#8,#16]",
    "[#6]~[#6](=[#8])~[#16]",
    # Boronic acids & esters
    "[#5](~[#8])~[#8]"
]

#filterin step dividing a set of molecules into matching (unwanted) and clean set
import os

matches = []
clean = []

# Check if the sdf file exists and is accessible
if not os.path.exists(sdf):
  raise ValueError(f"Cannot access SDF file at {sdf}")

# Open the SDF file using the SDMolSupplier constructor (unchanged)
suppl = Chem.SDMolSupplier(sdf)

for mol in suppl:
  # Flag to track if the molecule matches any SMARTS pattern
  is_match = False
  for i in smarts:
    patt = Chem.MolFromSmarts(i)
    if mol.HasSubstructMatch(patt):
      matches.append(mol)
      is_match = True
      break  # Only break if a match is found

  # Add the molecule to clean only if it didn't match any SMARTS
  if not is_match:
    clean.append(mol)


# Write the matches and clean sets to separate SDF files
w = Chem.SDWriter('unwanted.sdf')
for m in matches: w.write(m)
x = Chem.SDWriter('clean.sdf')
for m in clean: x.write(m)

print("unwanted set", len(matches), 'molecules')
print("clean set", len(clean), 'molecules')

