import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

model = api.load("glove-twitter-25")

words = ['ai', 'computer', 'software', 'database', 'network', 'cloud', 
         'robotics', 'algorithm', 'code', 'data']

vectors = np.array([model[word] for word in words])

pca = PCA(n_components=2)
result = pca.fit_transform(vectors)

plt.figure(figsize=(8, 6))
plt.scatter(result[:, 0], result[:, 1])

for i, word in enumerate(words):
    plt.annotate(word, (result[i, 0], result[i, 1]), fontsize=12)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Visualization of Word Embeddings')
plt.grid(True, alpha=0.3)
plt.show()

input_word = 'computer'
print(f"\n5 words similar to '{input_word}':")
for word, sim in model.most_similar(input_word, topn=5):
    print(f"  {word}: {sim:.4f}")
