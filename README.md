# SingleCellOpenProblems

[![Travis CI Build](https://api.travis-ci.com/singlecellopenproblems/SingleCellOpenProblems.svg?branch=master)](https://travis-ci.com/singlecellopenproblems/SingleCellOpenProblems)
[![Netlify Status](https://api.netlify.com/api/v1/badges/83b92388-53c7-4fef-9003-e14d94c6ac6f/deploy-status)](https://app.netlify.com/sites/openproblems/deploys)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Formalizing and benchmarking open problems in single-cell genomics.

[**Visit the Open Problems Website**](https://openproblems.netlify.app/)

## API

Each task consists of datasets, methods, and metrics.

Datasets should take no arguments and return an AnnData object. If `test is True`, then the method should load the full dataset, but only return a small version of the same data (preferably <200 cells and <500 genes) for faster downstream analysis.

```
function dataset(bool test=False) -> AnnData adata
```

Methods should take an AnnData object and store the output in-place in  `adata.obs` according to the specification of the task.

```
function method(AnnData adata) -> None
```

Metrics should take an AnnData object and return a float.

```
function metric(AnnData adata) -> float
```

Task-specific APIs are described in the README for each task.

* [Label Projection](openproblems/tasks/label_projection)
* [Multimodal Data Integration](openproblems/tasks/multimodal_data_integration)

## Adding a new dataset

Datasets are loaded under `openproblems/data`. Each data loading function should download the appropriate dataset from a stable location (e.g. from Figshare) be decorated with `openproblems.data.utils.loader` in order to cache the result.

## Adding a dataset / method / metric to a task

To add a dataset, method, or metric to a task, simply create a new `.py` file corresponding to your proposed new functionality and import the main function in the corresponding `__init__.py`. E.g., to add a "F2" metric to the label projection task, we would create `openproblems/tasks/label_projection/metrics/f2.py` and add a line
```
from .f2 import f2
```
to [`openproblems/tasks/label_projection/metrics/__init__.py`](openproblems/tasks/label_projection/metrics/__init__.py).

For datasets in particular, these should be loaded using a `loader` function from `openproblems.data`, with only task-specific annotations added in the task-specific data file.

For methods and metrics, they should be decorated with the appropriate function in `openproblems.tools.decorators` to include metadata required for the evaluation and presentation of results.

Note that data is not normalized in the data loader; normalization should be performed as part of each method. For ease of use, we provide a collection of common normalization functions in [`openproblems.tools.normalize`](openproblems/tools/normalize.py).

## Adding a new task

The task directory structure is as follows

```
opensproblems/
  - tasks/
    - task_name/
      - README.md
      - __init__.py
      - checks.py
      - datasets/
        - __init__.py
        - dataset1.py
        - ...
      - methods/
        - __init__.py
        - method1.py
        - ...
      - metrics/
        - __init__.py
        - metric1.py
        - ...
```

`task_name/__init__.py` can be copied from an existing task.

`checks.py` should implement the following functions:

```
check_dataset(AnnData adata) -> bool # checks that a dataset fits the task-specific schema
check_method(AnnData adata) -> bool # checks that the output from a method fits the task-specific schema
```

For adding datasets, methods and metrics, see above.
