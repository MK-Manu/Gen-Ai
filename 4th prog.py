!pip -q install gensim transformers torch

import gensim.downloader as api
from transformers import pipeline

wv=api.load("glove-wiki-gigaword-100")
gen=pipeline("text-generation",model="gpt2")

prompt="Explain machine learning in healthcare"

enriched=" ".join([w for x in prompt.split() for w in(([x]+[i[0] for i in wv.most_similar(x,topn=2)]) if x in wv else [x])])

out1=gen(prompt,max_length=100)[0]["generated_text"]
out2=gen(enriched,max_length=100)[0]["generated_text"]

print("🔹 Original Prompt:\n",prompt)
print("\n🔹 Enriched Prompt:\n",enriched)
print("\n🔹 Output (Original):\n",out1)
print("\n🔹 Output (Enriched):\n",out2)

print("\n🔍 Comparison:")
print("Original length:",len(out1.split()))
print("Enriched length:",len(out2.split()))
print("Insight: Enriched prompt → more detailed but may add noise.")
