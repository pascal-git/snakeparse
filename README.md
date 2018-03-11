# Conda Recipe for snakeparse

## Pre-requisites

This requires `conda-build` to be installed:

```
conda install -y -q conda-build
```

### Installing `snakeparse`

To install locally and use your local channel:

```
cd conda
conda-build .
conda install -y snakeparse --use-local
conda config --add channels local
popd
```
