import sys
from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import FilterCatalog

def remove_PAINS(molekuel):
    params = FilterCatalog.FilterCatalogParams()
    params.AddCatalog(FilterCatalog.FilterCatalogParams.FilterCatalogs.PAINS)
    catalog = FilterCatalog.FilterCatalog(params)

    result = catalog.HasMatch(molekuel)
    return not result

def clean_sdf(input_filepath, output_filepath):
    suppl = Chem.SDMolSupplier(input_filepath)

    cleaned_molecules = []

    # Get the total number of molecules in the SDF file for the progress bar
    total_molecules = len(suppl)

    with tqdm(total=total_molecules, desc="Processing") as pbar:
        for molecule in suppl:
            if molecule is not None:
                if remove_PAINS(molecule):
                    cleaned_molecules.append(molecule)
                pbar.update(1)  # Update progress bar

    writer = Chem.SDWriter(output_filepath)

    for mol in cleaned_molecules:
        writer.write(mol)

    writer.close()
    print("Saved PAINS free SDF to:", output_filepath)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_filepath = sys.argv[1]
        output_filepath = f'{input_filepath}_no_PAINS.sdf'
        clean_sdf(input_filepath, output_filepath)
    else:
        print("Usage: python script.py input.sdf")
     
