import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans

i = 1
x = []
y = []

#read from file
with open('/home/22204911/Documents/extract4.txt') as f:

    counter = 0

    for line in f:

        n = line.strip('').strip(',').split()
        if len(n) >2:
            x.append(n[2])
            y_2 = []
            for j in n[3:]:
                y_2.append(j)
                # print(y_list[j])
            y.append(y_2)

        counter += 1
        if counter == 100:
            break

# print(f'x: {x}')
# print(f'y: {y}')
data = list(zip(x, y))
# print(f'data: {data}')
linkage_matrix = linkage(y, method = 'complete', metric = 'euclidean')
# print(linkage_matrix)

plt.figure(figsize = (15,15))

dendrogram(linkage_matrix, labels=x)



# data = np.random.rand(80, 2)
# linkage_matrix = linkage(data, method = "ward")

# plt.figure(figsize = (10,5))

# dendrogram(linkage_matrix)

plt.title("hierarchical clustering of evolutionary events")

plt.xlabel("solutions")

plt.ylabel("distance between clusters")

plt.show()


# data = np.random.rand(50, 2)
# number_clusters = 20
# kmeans =KMeans(n_clusters=20)
# kmeans.fit(data)
# cluster_labels =kmeans.labels_
# cluster_centers=kmeans.cluster_centers_

# plt.scatter(data[:, 0], data[:, 1], c=cluster_labels)
# plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker= 'x', color = 'red')
# plt.title("Divisive clustering(K-means)")
# plt.xlabel("solutions")
# plt.ylabel("number of events per solution")

# w = linkage(data, method = "ward")
# dendrogram(w)
# plt.show()

