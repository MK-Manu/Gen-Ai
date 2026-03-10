import gensim.downloader as api

# 1. Load model and get user input
model = api.load("glove-wiki-gigaword-50")
seed = input("Enter a seed word: ").lower()

try:
    # 2. Retrieve top 5 similar words
    sim = [w for w, _ in model.most_similar(seed, topn=5)]
    
    # 3. Construct the paragraph with repetitive structure
    story = f"Once upon a time, there was a {seed} who dreamed of adventure.\n"
    for word in sim:
        story += f"One day, it stumbled upon a {word}, leading it into an unexpected journey.\n"
    story += "The experience changed its life forever."

    # 4. Final Output
    print(f"\nGenerated Paragraph:\n\n{story}")
    print(f"\nsimilar words: {sim}")

except KeyError:
    print("Word not found in vocabulary.")
