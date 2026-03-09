from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Model name
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example texts
texts = ["Amazing!", "Terrible."]

# Tokenize inputs
inputs = tokenizer(
    texts,
    return_tensors="pt",
    padding=True,
    truncation=True
)

# Run model
with torch.no_grad():
    outputs = model(**inputs)

# Convert logits to probabilities
probs = F.softmax(outputs.logits, dim=-1)

print("Probabilities:")
print(probs)

# Predicted sentiment
predictions = torch.argmax(probs, dim=-1)

for text, pred in zip(texts, predictions):
    print(f"Text: {text} -> Predicted rating: {pred.item() + 1} stars")

# Save model and tokenizer
model.save_pretrained("./my_model")
tokenizer.save_pretrained("./my_model")

# Load model and tokenizer again
model = AutoModelForSequenceClassification.from_pretrained("./my_model")
tokenizer = AutoTokenizer.from_pretrained("./my_model")