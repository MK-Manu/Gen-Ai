import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

model = api.load("glove-twitter-25")
words = ['ai','computer','software','database','network','cloud','robotics','algorithm','code','data']

X = PCA(n_components=2).fit_transform(np.array([model[w] for w in words]))

plt.scatter(X[:,0],X[:,1])
for i,w in enumerate(words): plt.annotate(w,(X[i,0],X[i,1]))
plt.show()

for w,s in model.most_similar('computer',topn=5):
    print(w,round(s,4))
