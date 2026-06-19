#3rd Extra
!pip -q install gensim nltk matplotlib seaborn

import nltk,numpy as np,matplotlib.pyplot as plt,seaborn as sns
from nltk.corpus import reuters
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

nltk.download("reuters")
nltk.download("punkt")
nltk.download("punkt_tab")

sent=[[w.lower() for w in s if w.isalpha()] for s in reuters.sents()[:5000]]

model=Word2Vec(sent,vector_size=100,window=5,min_count=2)

term="disease"
print(model.wv.most_similar(term,topn=5) if term in model.wv else f"{term} not found")

words=["health","disease","doctor","patient","treatment","medicine","virus","surgery","nurse","hospital"]
words=[w for w in words if w in model.wv]

vec=TSNE(n_components=2,random_state=42,perplexity=3).fit_transform(np.array([model.wv[w] for w in words]))

plt.figure(figsize=(10,6))
sns.scatterplot(x=vec[:,0],y=vec[:,1])

for i,w in enumerate(words):
    plt.annotate(w,(vec[i,0],vec[i,1]))

plt.show()
