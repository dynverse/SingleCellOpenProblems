import anndata
import numpy as np

from .utils import loader


@loader
def load_dummy(test=False):
    if test:
        size = (100, 20)
    else:
        size = (1000, 2000)
    adata = anndata.AnnData(np.random.uniform(0, 1, size))
    adata.obs["labels"] = np.random.choice(2, adata.shape[0], replace=True)
    return adata
