import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# load the data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# visualize the first two features
plt.figure(figsize=(8, 6))
for i in range(3):
    subset = df[df['target'] == i]
    plt.scatter(subset.iloc[:, 0], subset.iloc[:, 1], label=iris.target_names[i])
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend()
plt.title('Iris Dataset - Two Feature Visualization')
plt.show()
