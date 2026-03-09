from pypdf import PdfReader
from transformers import pipeline

# Load the PDF
reader = PdfReader("US_Employee_Policy.pdf")

# Extract text from all pages
document_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:  # Ensure page has text
        document_text += text + "\n"

# Load the question-answering pipeline
qa_pipeline = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad"
)

# Ask a question
question = "What is the notice period for resignation?"

# Get answer from the QA pipeline
result = qa_pipeline(
    question=question,
    context=document_text
)

# Print results
print("Question:", question)
print("Answer:", result["answer"])
print("Confidence Score:", round(result["score"], 3))