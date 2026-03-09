
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Model name
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create sentiment pipeline
classifier = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer
)

# Example texts in multiple languages
texts = [
    "I love this phone!",              # English
    "Este producto es terrible",      # Spanish
    "C'est incroyable",               # French
    "Das ist sehr schlecht",          # German
    "Questo è fantastico"             # Italian
]

# Run sentiment analysis
results = classifier(texts)

# Print results
for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} | Confidence: {round(result['score'], 2)}")
    print("-" * 40)