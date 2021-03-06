import numpy as np
from sklearn import decomposition

class PCA(decomposition.PCA):
    def __init__(self,*args,**kwargs):
        decomposition.PCA.__init__(self,*args,**kwargs)

    def fit_exp_var(self,X,explained_variance,bounds=False):
        if not bounds:
            bounds = [1,X.shape[1]]

        n_components = (bounds[0]+bounds[1])//2

        while True:
            self.n_components = n_components
            self.fit(X)

            if np.sum(self.explained_variance_ratio_) > explained_variance:
                bounds[1] = n_components
            else:
                bounds[0] = n_components
                
            n_components = (bounds[0]+bounds[1])//2

            if bounds[0] == bounds[1] or bounds[0] == bounds[1]-1:
                self.n_components = n_components + 1
                return self.fit(X)