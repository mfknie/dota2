# %%
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# %%
hero_data = np.genfromtext("/data/ti9/Hero_performances", names = True)

# Preprocessing
hero_names = hero_data[, 1:]
hero_data = hero_data[hero_data['Total Count'] >= 5] 

scaler = StandardScaler()
hero_data_scaled = scaler.fit_transform(hero_data)

pca = PCA(n_components = 0.95, svd_solver="full")
pca_elbow = PCA(svd_solver = "full")

hero_pcs = pca.fit_transform(hero_data_scaled)
hero_pcs_elbow = pca_elbow.fit_transform(hero_data_scaled)


# %%
# Graphing 
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(range(1, pca_elbow.n_components_ + 1), pca_elbow.explained_variance_ratio_, color = "tab:blue")


ax.set_ylim([0, 1])
ax.set_title()

plt.show()



# %%


np.savetext("hero_pcs.csv", hero_pcs)