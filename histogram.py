import matplotlib.pyplot as plt
import numpy as np


def hist(A):
    N = A[-1] - A[0] + 1
    a = np.hstack(A)
    _ = plt.hist(a, bins=np.arange(N + 2) + 0.5, range=(0, A[-1] + 2, 1), rwidth=0.8)
    plt.xlabel("Number")
    plt.xticks(np.arange(0,N+2,step=1))
    plt.ylabel("Frequency")
    plt.title("Data Distribution")
    plt.show()
