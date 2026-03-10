import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

model = api.load("glove-twitter-25")
words = ['ai','computer','software','database','network','cloud','robotics','algorithm','code','data']

X = PCA(n_components=2).fit_transform(np.array([model[w] for w in words]))

plt.scatter(X[:,0],X[:,1])
for i,w in enumerate(words): plt.annotate(w,(X[i,0],X[i,1]),fontsize=12,xytext=(5,5),textcoords="offset points",bbox=dict(facecolor='white',alpha=0.7))

plt.title("PCA visualization of word Embeddings",fontsize=12)
plt.xlabel("principal component 1", fontsize=12)
plt.ylabel("principal component 2", fontsize=12)
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()

for w,s in model.most_similar('computer',topn=5):
    print(w,round(s,4))
