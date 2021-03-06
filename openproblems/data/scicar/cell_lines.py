from .base import load_scicar
from ..utils import loader

rna_url = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM3271040&format=file&file=GSM3271040%5FRNA%5FsciCAR%5FA549%5Fgene%5Fcount.txt.gz"
rna_cells_url = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM3271040&format=file&file=GSM3271040%5FRNA%5FsciCAR%5FA549%5Fcell.txt.gz"
rna_genes_url = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM3271040&format=file&file=GSM3271040%5FRNA%5FsciCAR%5FA549%5Fgene.txt.gz"
atac_url = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM3271041&format=file&file=GSM3271041%5FATAC%5FsciCAR%5FA549%5Fpeak%5Fcount.txt.gz"
atac_cells_url = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM3271041&format=file&file=GSM3271041%5FATAC%5FsciCAR%5FA549%5Fcell.txt.gz"
atac_genes_url = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM3271041&format=file&file=GSM3271041%5FATAC%5FsciCAR%5FA549%5Fpeak.txt.gz"


@loader
def load_scicar_cell_lines(test=False):
    return load_scicar(
        rna_url,
        rna_cells_url,
        rna_genes_url,
        atac_url,
        atac_cells_url,
        atac_genes_url,
        test=test,
    )
