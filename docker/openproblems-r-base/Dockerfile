FROM singlecellopenproblems/openproblems:latest

# PART 1: install scripts
RUN cd / && \
  wget https://github.com/rocker-org/rocker-versioned2/archive/master.zip && \
  unzip master.zip && \
  mv /rocker-versioned2-master/scripts /rocker_scripts && \
  rm -r master.zip /rocker-versioned2-master
  
## PART 2: install R
ENV BUILD_DATE=2020-11-12 \
    R_VERSION=4.0.3 \
    CRAN="https://cran.rstudio.com" \ 
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    TERM=xterm \
    R_HOME=/usr/local/lib/R \
    TZ=Etc/UTC
    
RUN UBUNTU_VERSION=bionic /rocker_scripts/install_R.sh

## PART 3: install tidyverse
RUN /rocker_scripts/install_rstudio.sh
RUN /rocker_scripts/install_pandoc.sh
RUN /rocker_scripts/install_tidyverse.sh

## PART 4: install Bioc dependencies
RUN Rscript -e 'remotes::install_cran("BiocManager")'

RUN Rscript -e 'BiocManager::install(version="3.12", update=TRUE, ask=FALSE)'

RUN Rscript -e 'BiocManager::install(c("SingleCellExperiment", "scran"))'
