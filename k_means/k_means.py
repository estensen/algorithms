def k_means(centroids, data_points, data_poin_names):
    counter = 0
    while True:
        # Compute distances
        distances = compute_distances(centroids, data_points)

        # Assign each point to closest centroid
        assigned_points = [[] for x in centroids]
        assigned_points = assign_points(assigned_points, distances)

        # Recompute centroids
        print("Iteration {0}:".format(counter))
        prev_centroids = centroids[:]
        centroids = compute_centroids(centroids, assigned_points, data_points)
        for i, item in enumerate(centroids):
            print()
            print("Cluster #{0}".format(i))
            print("Old centroid {0}".format(prev_centroids[i]))
            #print("Distances to points: {0}".format(i))
            print("Points closest: {0}".format(assigned_points[i]))
            print("New centroid {0}".format(item))
        print()

        if set(prev_centroids) == set(centroids):
            print("There is convergence!")
            break
        counter += 1

def compute_centroids(centroids, assigned_points, data_points):
    for i, centroid in enumerate(centroids):
        if not assigned_points[i]:
            break
        # Map indices to data point values
        assigned_points[i] = [data_points[i] for i in assigned_points[i]]
        centroids[i] = sum(assigned_points[i]) / len(assigned_points[i])
    return centroids

def assign_points(assigned_points, distances):
    zipped = zip(distances[0], distances[1], distances[2])
    for z, point in enumerate(zipped):
        assigned_points[point.index(min(point))].append(z)
    return assigned_points

def compute_distances(centroids, data_points):
    distances = [data_points[:] for x in range(len(centroids))]
    for i, centroid in enumerate(centroids):
        for j, distance in enumerate(distances[i]):
            # print("abs({0} - {1}) = {2}".format(distance, centroid, abs(distance - centroid)))
            distances[i][j] = abs(distance - centroid)
    return distances

def read_data(filename, i):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.split('\n')
    data_points = []
    for line in lines:
        line = line.split(';')[i]
        data_points.append(line)
    return data_points

def main():
    # Initial centroids
    centroids = [4, 5, 8]
    print("Initial centroids: {0}".format(centroids))
    data_points = read_data("data.txt", 1)
    data_points = [int(i) for i in data_points]
    data_point_names = read_data("data.txt", 0)
    print("Data points:")
    print(*("{0}".format(p) for p in zip(data_points, data_point_names)))
    k_means(centroids, data_points, data_point_names)

main()
