# LangGraph Recruiter

An intelligent recruitment application screening system built with **LangGraph** and **LangChain**. This project automates the initial screening process for job applications using AI-powered analysis.

## 📋 Overview

The LangGraph Recruiter system processes job applications and automatically:
- **Categorizes** candidate experience levels (Entry-level, Mid-level, Senior-level)
- **Assesses** technical skillsets against job requirements
- **Routes** applications based on qualifications
- **Schedules** interviews or escalates to recruiters for further review

## 🎯 Key Features

- **Intelligent Application Analysis**: Uses GPT-4 to analyze job applications
- **Multi-step Workflow**: Implements a state machine with LangGraph for complex decision-making
- **Automated Routing**: Intelligently routes candidates based on experience and skill match
- **Python Developer Focus**: Tailored for Python Developer position screening
- **Extensible Architecture**: Easy to adapt for other job positions

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- OpenAI API key

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv add -r requirements.txt
   ```
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 📦 Dependencies

- `langchain` - LLM framework
- `langchain-core` - Core components
- `langchain-community` - Community integrations
- `langgraph` - Graph-based workflow orchestration
- `langchain-openai` - OpenAI integration
- `ipykernel` - Jupyter notebook support

## 🔧 Project Structure

```
LangGraphRecruiter_proj/
├── LangGraph_Recruiter.ipynb   # Main notebook with implementation
├── main.py                      # Entry point (can be extended)
├── requirements.txt             # Project dependencies
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## 📖 Usage

### Running the Notebook

Open and run `LangGraph_Recruiter.ipynb` in Jupyter:
```bash
jupyter notebook LangGraph_Recruiter.ipynb
```

### Workflow Overview

The system uses a state machine graph with the following flow:

1. **START** → Categorize Experience Level
2. **Categorize** → Assess Skillset  
3. **Assess** → Route Application based on:
   - If skills match → Schedule HR Interview
   - If Senior-level but no skill match → Escalate to Recruiter
   - Otherwise → Reject Application
4. **END**

### Creating a Candidate Application

```python
application_text = """
[Your job application details here]
"""

# Run through the workflow
results = app.invoke({"application": application_text})
print(results["response"])
```

## 🤖 How It Works

### State Design
The system uses a `State` TypedDict that tracks:
- `application`: The original job application text
- `experience_level`: Categorized experience level
- `skill_match`: Assessment of Python development skills
- `response`: Final decision/action

### AI Decision Making
Each step uses GPT-4 mini with tailored prompts to:
- Analyze application in context
- Make consistent, criteria-based decisions
- Provide transparent routing logic

## 🔐 Security Notes

- Never commit `.env` or API keys to version control
- Keep `OPENAI_API_KEY` secret
- The `.env` file should be added to `.gitignore`

## 📈 Future Enhancements

- Support for multiple job positions beyond Python Developer
- Resume/CV parsing integration
- Candidate feedback generation
- Interview scheduling integration
- Performance metrics and analytics
- Database storage for application history

## 📝 License

This project is part of an educational course on LangGraph and agentic AI systems.

## 🤝 Contributing

Feel free to extend this project with additional features, job positions, or enhanced routing logic.

---

**Built with LangGraph for intelligent, scalable recruitment workflows**