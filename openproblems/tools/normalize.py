import scanpy as sc
import scprep
from . import decorators


@decorators.normalizer
def log_scran_pooling(adata):
    """
    This function scran-normalizes the data
    """
    import scIB.preprocessing

    scprep.run.install_bioconductor("scran")
    # Normalize via scran-pooling with own clustering at res=0.5
    scIB.preprocessing.normalize(adata)

    # Make lightweight
    del adata.raw


def _cpm(adata):
    adata.layers["counts"] = adata.X.copy()
    sc.pp.normalize_total(adata, target_sum=1e6, key_added="size_factors")


@decorators.normalizer
def cpm(adata):
    """Normalize data to counts per million"""
    _cpm(adata)


@decorators.normalizer
def log_cpm(adata):
    """Normalize data to log counts per million"""
    _cpm(adata)
    sc.pp.log1p(adata)


@decorators.normalizer
def sqrt_cpm(adata):
    """Normalize data to log counts per million"""
    _cpm(adata)
    adata.X = scprep.transform.sqrt(adata.X)
