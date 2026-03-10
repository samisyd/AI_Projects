# Hugging Face Examples

A collection of Python examples demonstrating various NLP tasks using Hugging Face Transformers library and related tools.

## Features

This project includes examples for:
- Sentiment Analysis (binary, star ratings, multilingual)
- Automatic Speech Recognition
- Text Summarization
- Text Generation
- Tokenization
- PDF Processing and Question Answering
- Inference API Usage
- Comprehensive NLP Applications (Jupyter Notebook)

## Installation

1. Clone or download this repository.

2. (Optional) Set up Python environment:
   ```bash
   uv venv  # Creates virtual environment
   uv pip install -r requirements.txt
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. For inference examples, create a `.env` file with your Hugging Face API token:
   ```
   HF_TOKEN=your_huggingface_token_here
   ```

## Requirements

- Python >= 3.13
- torch >= 2.10.0
- transformers >= 4.0.0
- datasets
- soundfile
- pypdf
- huggingface-hub (for inference API)
- pandas, numpy, matplotlib, seaborn (for data analysis and visualization)
- sentence-transformers (for text embeddings)
- jupyter (for running notebooks)

## Scripts

### Sentiment Analysis

- **`sentiment.py`**: Basic sentiment analysis using DistilBERT model. Classifies text as positive or negative.
  ```bash
  python sentiment.py
  ```

- **`sentiment_ex3.py`**: Sentiment analysis with star ratings using BERT multilingual model. Provides probability distributions and saves the model locally.
  ```bash
  python sentiment_ex3.py
  ```

- **`sentiment_multi.py`**: Multilingual sentiment analysis supporting English, Spanish, French, German, and Italian.
  ```bash
  python sentiment_multi.py
  ```

### Speech Recognition

- **`speech_rec.py`**: Automatic speech recognition using Wav2Vec2 model on the PolyAI MINDS-14 dataset.
  ```bash
  python speech_rec.py
  ```

### Text Processing

- **`summarizer_ex.py`**: Text summarization using T5 model. Demonstrates both short and long summary generation.
  ```bash
  python summarizer_ex.py
  ```

- **`text_generationex.py`**: Text generation using GPT-2 model. Generates multiple text completions.
  ```bash
  python text_generationex.py
  ```

- **`tokenize_ex.py`**: Text tokenization example using AutoTokenizer from DistilBERT.
  ```bash
  python tokenize_ex.py
  ```

### PDF Processing

- **`pdf_reader.py`**: Extracts text from PDF files and performs question-answering using DistilBERT. Requires a PDF file named "US_Employee_Policy.pdf" in the same directory.
  ```bash
  python pdf_reader.py
  ```

### Inference API

- **`inference_ex.py`**: Uses Hugging Face Inference API with Together provider for chat completions. Requires HF_TOKEN environment variable.
  ```bash
  python inference_ex.py
  ```

### Jupyter Notebooks

- **`NLP_Applications.ipynb`**: Comprehensive Jupyter notebook demonstrating end-to-end NLP applications including:
  - Data loading and preprocessing of customer reviews
  - Sentiment analysis with visualization
  - Text cleaning impact analysis
  - Time-series sentiment trends
  - Text embeddings using Sentence Transformers
  - Semantic search capabilities
  
  Requires `runway.csv` dataset file. Open in Jupyter Lab/Notebook to run interactively.
  ```bash
  jupyter lab NLP_Applications.ipynb
  ```

### Main

- **`main.py`**: Simple hello world script.

## Usage

Run any of the scripts directly with Python. Make sure you have the required dependencies installed and environment variables set where needed.

For example:
```bash
python sentiment.py
```

## Project Structure

- `.env`: Environment variables (API keys)
- `.gitignore`: Git ignore rules
- `.python-version`: Python version specification
- `.venv/`: Virtual environment (created by uv)
- `pyproject.toml`: Project configuration
- `requirements.txt`: Python dependencies


## License

This project is for educational purposes. Please check Hugging Face model licenses for commercial use.
