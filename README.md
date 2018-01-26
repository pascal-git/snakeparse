# Conda Recipe for snakeparse

## Pre-requisites

This requires `conda-build` to be installed:

```
conda install -y -q conda-build
```

## Installation

Both `pyhocon` (version 0.3.38 or higher) and `snakeparse` need to be installed.
Unfortunately the required version for the former is not available via conda-forge and must be installed manually.


### Installing `pyhocon`

To install locally and use your local channel:

```
pushd pyhocon
conda-build .
conda install -y pyhocon --use-local
conda config --add channels local
popd
```

### Installing `snakeparse`

To install locally and use your local channel:

```
pushd snakeparse
conda-build .
conda install -y snakeparse --use-local
conda config --add channels local
popd
```
