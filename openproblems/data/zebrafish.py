import os
import tempfile

import numpy as np
import anndata
import scprep
import scanpy as sc

from .utils import loader, filter_genes_cells


@loader
def load_zebrafish(test=False):
    """Downloads zebrafish data from figshare"""
    URL = "https://ndownloader.figshare.com/files/24566651?private_link=e3921450ec1bd0587870"

    with tempfile.TemporaryDirectory() as tempdir:
        filepath = os.path.join(tempdir, "zebrafish.h5ad")
        scprep.io.download.download_url(URL, filepath)
        adata = anndata.read_h5ad(filepath)
        filter_genes_cells(adata)

    if test:
        sc.pp.subsample(adata, n_obs=500)
        filter_genes_cells(adata)
        adata = adata[:, :100]
        filter_genes_cells(adata)
    return adata
