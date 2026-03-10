from transformers import pipeline

model = pipeline("sentiment-analysis")
print("Sentiment Analyzer (type 'exit' to quit)\n")

while True:
    text = input("Enter sentence: ")
    if text.lower() == "exit":
        print("Goodbye!")
        break
    r = model(text)[0]
    print(f"Sentiment: {r['label']}")
    print(f"Confidence: {r['score']:.2f}\n")
