import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("iADBL.csv", usecols=lambda column: column != 'date') 
df = df.drop(columns=['Y_close'])

# Convert all columns to numeric, errors='coerce' will set non-convertible values to NaN
df = df.apply(pd.to_numeric, errors='coerce')

print(df.head())

#Scaling the data

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

# print(scaled_data)

#PCA

from sklearn.decomposition import PCA

pca = PCA(n_components=5)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
print(scaled_data.shape)

print(x_pca.shape)
print(x_pca)
print(type(x_pca))
head = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5']
df = pd.DataFrame(x_pca,columns=head)
df.to_csv('pADBL.csv',index=False)



plt.figure(figsize=(8, 6))
plt.scatter(x_pca[:, 0], x_pca[:, 1], color='red', alpha=0.3)  # Using a single color
plt.title('PCA of Stock Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.show()

# print("Explained variance ratio:", pca.explained_variance_ratio_)

# explained_variance_ratio = pca.explained_variance_ratio_
# cumulative_explained_variance = np.cumsum(explained_variance_ratio)

# plt.figure(figsize=(8, 5))
# plt.plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o', linestyle='--')
# plt.title('Cumulative Explained Variance by Principal Components')
# plt.xlabel('Number of Principal Components')
# plt.ylabel('Cumulative Explained Variance')
# plt.grid(True)
# plt.show()




