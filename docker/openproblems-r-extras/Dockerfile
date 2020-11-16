FROM singlecellopenproblems/openproblems-r-base:latest

# Install R packages
RUN Rscript -e 'BiocManager::install("batchelor")'

# Install Python packages
RUN pip install --no-cache-dir 'git+https://github.com/KrishnaswamyLab/harmonic-alignment#subdirectory=python'
