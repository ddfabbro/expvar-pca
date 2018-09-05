# extended-pca
Extension of PCA class from `scikit-learn` to fit data according to given explained variance

## Installation

There is no installation for this package.

To use it, simply clone this repository by

```
git clone https://github.com/ddfabbro/extended-pca.git
```

and add the root directory to your `PYTHONPATH` environment variable

```
export PYTHONPATH=$PYTHONPATH:$(pwd)/extended-pca
```

Alternatively, you can drop the source code directory in your project and use it directly.

## Usage

Import `numpy` and `ExtendedPCA`
```
import numpy as np
from ExtendedPCA import PCA
```
Initialize random data `X` and specify target explained variance `target_exp_var`
```
X = np.random.rand(64,27)
target_exp_var = .8
```
Calculate PCA as you would normally do using `scikit-learn`
```
pca = PCA(whiten=True,svd_solver='randomized').fit_exp_var(X,target_exp_var)
```
(optional) You can also specify search bounds for faster convergence
```
bounds = [10,20]
pca = PCA(whiten=True,svd_solver='randomized').fit_exp_var(X,target_exp_var,bounds)
```
