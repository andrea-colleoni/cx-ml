import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd
# for animation
# from JSAnimation import IPython_display
# from matplotlib import animation

def initialize_centroids(points, k):
    """returns k centroids from the initial points"""
    centroids = points.copy()
    np.random.shuffle(centroids)
    return centroids[:k]

def closest_centroid(points, centroids):
    """returns an array containing the index to the nearest centroid for each point"""
    distances = np.sqrt(((points - centroids[:, np.newaxis])**2).sum(axis=2))
    return np.argmin(distances, axis=0)    

def move_centroids(points, closest, centroids):
    """returns the new centroids assigned from the points closest to them"""
    return np.array([points[closest==k].mean(axis=0) for k in range(centroids.shape[0])])    

irisdata = pd.read_csv('./iris.csv')

irisdata = irisdata.drop(['sepal_width','petal_width'],axis=1)
irisdata.head()
to_be_clasified = irisdata.drop(['species'],axis=1).values

# plt.scatter(to_be_clasified[:, 0], to_be_clasified[:, 1])
ax = plt.gca()
ax.add_artist(plt.Circle(np.array([1, 0]), 0.75/2, fill=False, lw=3))
ax.add_artist(plt.Circle(np.array([-0.5, 0.5]), 0.25/2, fill=False, lw=3))
ax.add_artist(plt.Circle(np.array([-0.5, -0.5]), 0.5/2, fill=False, lw=3))

# centroids = initialize_centroids(to_be_clasified, 3)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

# closest = closest_centroid(to_be_clasified, centroids)
# print(closest)

# move_centroids(to_be_clasified, closest_centroid(to_be_clasified, centroids), centroids)

plt.subplot(131)
plt.scatter(to_be_clasified[:, 0], to_be_clasified[:, 1])
centroids = initialize_centroids(to_be_clasified, 3)
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

plt.subplot(132)
plt.scatter(to_be_clasified[:, 0], to_be_clasified[:, 1])
closest = closest_centroid(to_be_clasified, centroids)
centroids = move_centroids(to_be_clasified, closest, centroids)
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

plt.subplot(133)
plt.scatter(to_be_clasified[:, 0], to_be_clasified[:, 1])
closest = closest_centroid(to_be_clasified, centroids)
centroids = move_centroids(to_be_clasified, closest, centroids)
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

# create a simple animation
# fig = plt.figure()
# ax = plt.axes(xlim=(-4, 4), ylim=(-4, 4))
# centroids = initialize_centroids(to_be_clasified, 3)

# def init():
#     return

# def animate(i):
#     global centroids
#     closest = closest_centroid(to_be_clasified, centroids)
#     centroids = move_centroids(to_be_clasified, closest, centroids)
#     ax.cla()
#     ax.scatter(to_be_clasified[:, 0], to_be_clasified[:, 1], c=closest)
#     ax.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)
#     return 

# animation.FuncAnimation(fig, animate, init_func=init,
#                         frames=10, interval=200, blit=True)

plt.show()