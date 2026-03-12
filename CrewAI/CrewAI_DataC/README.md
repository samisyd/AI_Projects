# CrewAI DataCamp Example

A Python project demonstrating the use of CrewAI for building multi-agent AI systems, specifically showcasing web scraping and Retrieval-Augmented Generation (RAG) capabilities.

## Overview

This project provides a practical example of using CrewAI tools to:
- Scrape content from websites
- Save extracted data to files
- Perform text search and analysis using AI agents
- Implement RAG (Retrieval-Augmented Generation) workflows

The example scrapes content from Wikipedia's Artificial Intelligence page and uses an AI agent to answer questions about Natural Language Processing based on the retrieved content.

## Features

- **Web Scraping**: Extract content from websites using CrewAI's ScrapeWebsiteTool
- **File Operations**: Write scraped content to local files with FileWriterTool
- **Text Search**: Perform semantic search on text files using TXTSearchTool
- **AI Agents**: Create and manage AI agents with specific roles and goals
- **Task Management**: Define and execute tasks within a CrewAI crew
- **RAG Implementation**: Demonstrate retrieval-augmented generation workflows

## Prerequisites

- Python 3.13 or higher
- OpenAI API key (for AI agent functionality)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd CrewAI_Datacamp
   ```

2. Install dependencies using uv (recommended):
   ```bash
   uv add -r requirements.txt
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Jupyter Notebook

1. Open the `Crew_ex.ipynb` notebook in Jupyter Lab or VS Code
2. Execute the cells in order to:
   - Install required packages
   - Scrape Wikipedia content
   - Save content to `ai.txt`
   - Set up text search tools
   - Create and run an AI agent to answer questions

### Running the Python Script

A companion script `Crew_ex.py` demonstrates how to define multiple agents (researcher, writer, editor) powered by the Groq LLM, assemble them into a sequential `Crew` process, and execute a simple research-to-blog workflow:

```bash
python Crew_ex.py
```

The script loads credentials from a `.env` file and showcases using `LLM`, `Agent`, `Task`, and `Crew` classes programmatically.

### Key Components

#### 1. Web Scraping
```python
from crewai_tools import ScrapeWebsiteTool

tool = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Artificial_intelligence')
text = tool.run()
```

#### 2. File Writing
```python
from crewai_tools import FileWriterTool

file_writer_tool = FileWriterTool()
result = file_writer_tool._run(filename='ai.txt', content=text, directory='', overwrite=True)
```

#### 3. Text Search Setup
```python
from crewai_tools import TXTSearchTool

tool = TXTSearchTool(txt='ai.txt')
context = tool.run('What is natural language processing?')
```

#### 4. AI Agent Creation
```python
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role='Educator',
    goal='Answer questions based on provided context',
    backstory='You are a data expert',
    tools=[tool]
)

# Define task and create crew
test_task = Task(description="Answer the question", agent=data_analyst)
crew = Crew(agents=[data_analyst], tasks=[test_task])

# Execute
output = crew.kickoff()
```

## Project Structure

```
CrewAI_Datacamp/
├── Crew_ex.ipynb          # Main Jupyter notebook with examples
├── Crew_ex.py             # Python script demonstrating agent workflow with Groq LLM
├── main.py               # Basic Python script (placeholder)
├── ai.txt                # Scraped content from Wikipedia
├── pyproject.toml        # Project configuration
├── requirements.txt      # Python dependencies
├── README.md            # This file
```

## Dependencies

- `crewai>=1.10.1` - Core CrewAI framework
- `crewai-tools>=1.10.1` - CrewAI tools for web scraping, file operations, etc.
- `ipykernel>=7.2.0` - Jupyter notebook kernel

## Environment Setup

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or in Python:
```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
```

## Contributing

Feel free to contribute to this project by:
- Adding more examples
- Improving documentation
- Reporting issues
- Suggesting enhancements

## License

This project is open-source. Please check the license file for details.

## Learn More

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI Tools](https://github.com/crewAIInc/crewAI-tools)
