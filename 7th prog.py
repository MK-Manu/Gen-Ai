from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text):
    ids = model.generate(
        tokenizer(text, return_tensors="pt", truncation=True)["input_ids"],
        max_length=130, min_length=50
    )
    return tokenizer.decode(ids[0], skip_special_tokens=True)
long_text = """
Artificial Intelligence (AI) is a rapidly advancing field that aims to create machines capable of human-like
thinking.
AI is used in various industries, from healthcare to finance, improving efficiency and accuracy. Machine
learning,
a subset of AI, enables computers to learn from data and make predictions without being explicitly
programmed.
With deep learning, neural networks can process vast amounts of information and recognize patterns,
leading
to advancements in self-driving cars, natural language processing, and medical diagnostics.
"""

summary = summarize_text(long_text)

print("Original Text:")
print(long_text)
print("\nSummarized Text:")
print(summary)
