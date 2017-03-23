from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np


X = np.array([[1, 3], [7, 7], [9, 3], [5, 5], [11, 4], [13, 6]])
point_labels = list("ABCDEF")

#print(X.shape)
#plt.scatter(X[:,0], X[:,1])
#plt.show()

Z = linkage(X, "complete") # single for nearest point, complete for farthest

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("sample index or (cluster size)")
plt.ylabel("distance")
dendrogram(
    Z,
    truncate_mode="lastp",  # show only the last p merged clusters
    p=12,  # show only the last p merged clusters
    leaf_rotation=90.,
    leaf_font_size=12.,
    labels=point_labels,
    distance_sort="descending",
    show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.show()
