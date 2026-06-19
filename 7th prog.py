!pip install transformers==4.52.4 sentencepiece accelerate
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

long_text = """
Artificial Intelligence (AI) is a rapidly advancing field that aims to create machines capable of human-like thinking.
AI is used in various industries, from healthcare to finance, improving efficiency and accuracy. Machine learning,
a subset of AI, enables computers to learn from data and make predictions without being explicitly programmed.
With deep learning, neural networks can process vast amounts of information and recognize patterns, leading
to advancements in self-driving cars, natural language processing, and medical diagnostics.
"""

summary = summarizer(
    long_text,
    max_length=130,
    min_length=50,
    do_sample=False
)

print("Original Text:")
print(long_text)

print("\nSummarized Text:")
print(summary[0]["summary_text"])
