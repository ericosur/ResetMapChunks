# RASMUS

- https://en.wikipedia.org/wiki/Geometric_median
    - Weiszfeld's algorithm
    - scipy.optimize
- Center of minimum distance (最小距離中心) 找到一個點，其他每個一點到這個點的距離和最小

- https://stackoverflow.com/questions/5241487/android-mapview-setting-zoom-automatically-until-all-itemizedoverlays-are-visi

- stackoverflow https://stackoverflow.com/questions/30299267/geometric-median-of-multidimensional-points

```python
import numpy as np
from scipy.spatial.distance import cdist, euclidean

def geometric_median(X, eps=1e-5):
    y = np.mean(X, 0)

    while True:
        D = cdist(X, [y])
        nonzeros = (D != 0)[:, 0]

        Dinv = 1 / D[nonzeros]
        Dinvs = np.sum(Dinv)
        W = Dinv / Dinvs
        T = np.sum(W * X[nonzeros], 0)

        num_zeros = len(X) - np.sum(nonzeros)
        if num_zeros == 0:
            y1 = T
        elif num_zeros == len(X):
            return y
        else:
            R = (T - y) * Dinvs
            r = np.linalg.norm(R)
            rinv = 0 if r == 0 else num_zeros/r
            y1 = max(0, 1-rinv)*T + min(1, rinv)*y

        if euclidean(y, y1) < eps:
            return y1

        y = y1
```
