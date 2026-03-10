from gensim.models import Word2Vec

corpus = [
["doctor","treats","patient"],
["patient","has","disease"],
["doctor","prescribes","medicine"],
["nurse","helps","patient"],
["hospital","treats","disease"]
]

model = Word2Vec(corpus, vector_size=20, window=2, min_count=1)

print("Similar words to 'patient':")
print(model.wv.most_similar("patient", topn=5))
