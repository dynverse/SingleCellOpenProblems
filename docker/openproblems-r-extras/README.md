# openproblems-r-base Docker image

Base image: [singlecellopenproblems/openproblems-r-base](../openproblems-r-base)

OS: Debian Buster

Python: 3.8

R: 4.0

apt packages:

* [R dependencies](https://github.com/rocker-org/rocker-versioned2/blob/master/scripts/install_R.sh)
* [Rstudio dependencies](https://github.com/rocker-org/rocker-versioned2/blob/master/scripts/install_rstudio.sh)
* [tidyverse dependencies](https://github.com/rocker-org/rocker-versioned2/blob/master/scripts/install_tidyverse.sh)

R packages:

* tidyverse
* BiocManager
* scran
* batchelor
* sparsesvd

Python packages:

* pip
* wheel
* setuptools
* cmake
* openproblems
* rpy2
* scIB
* anndata2ri
* harmonic-alignment
