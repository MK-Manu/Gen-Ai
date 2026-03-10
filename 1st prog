!pip install gensim
import gensim.downloader as api

model = api.load("glove-twitter-25") 

print(f"Similarity between 'king' and 'queen': {model.similarity('king', 'queen'):.4f}")

result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)[0]
print(f"'King' - 'Man' + 'Woman' = {result[0]} (Similarity: {result[1]:.4f})\n")

print("Words similar to 'Paris':")
for word, sim in model.most_similar('paris', topn=5):
    print(f"{word.capitalize()}: {sim:.4f}")

odd_word = model.doesnt_match(["apple", "banana", "orange", "grape"])
print(f"\nOdd one out: {odd_word}")
