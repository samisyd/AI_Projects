from transformers import AutoModelForSequenceClassification, pipeline

my_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
# Load a sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Multiple inputs
texts = ["Love this!", "Hate that."]

# Run the classifier
results = classifier(texts)

# Print results
for result in results:
    print(f"{result['label']} ({round(result['score'], 2)})")