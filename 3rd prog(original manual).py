!pip -q install gensim nltk matplotlib

import nltk,numpy as np,matplotlib.pyplot as plt
from nltk.corpus import reuters
from gensim.models import Word2Vec
from sklearn.decomposition import PCA

nltk.download("reuters")
nltk.download("punkt_tab")

corpus=[[w.lower() for w in s if w.isalpha()]
        for s in reuters.sents()[:5000]]

model=Word2Vec(corpus,vector_size=50,window=5,min_count=2)

words=['health','disease','doctor','patient',
       'medicine','hospital']

X=PCA(2).fit_transform(np.array([model.wv[w] for w in words if w in model.wv]))

plt.scatter(X[:,0],X[:,1])

for i,w in enumerate([w for w in words if w in model.wv]):
    plt.annotate(w,(X[i,0],X[i,1]))

plt.show()

for w,s in model.wv.most_similar('disease',topn=5):
    print(w,round(s,4))
