from transformers import pipeline

# Example input text
original_text = """
Artificial Intelligence is transforming many industries. 
It helps automate repetitive tasks, analyze huge amounts of data,
and assist humans in decision making. AI is used in healthcare,
finance, transportation, and education. However, there are also
concerns about job displacement, ethical AI use, and data privacy.
"""

# Generate a short summary (1–10 tokens)
short_summarizer = pipeline(
    task="summarization",
    model="cnicu/t5-small-booksum",
)

short_summary_text = short_summarizer(
    original_text,
    min_length=1,
    max_length=10
)

print("Short summary:")
print(short_summary_text[0]["summary_text"])


# Generate a longer summary (50–100 tokens)
long_summarizer = pipeline(
    task="summarization",
    model="cnicu/t5-small-booksum",
)

long_summary_text = long_summarizer(
    original_text,
    min_length=50,
    max_length=100
)

print("\nLong summary:")
print(long_summary_text[0]["summary_text"])