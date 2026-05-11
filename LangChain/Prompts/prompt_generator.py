from langchain_core.prompts import PromptTemplate
# Prompt templates are a powerful tool for generating dynamic prompts based on user input or other variables.
# You can reuse this prompt template across different parts of your application, ensuring consistency and 
# reducing the chances of errors in prompt construction.

# why not use f strings instead of prompt templates? as both of them are used to format strings.
# f strings are a built-in feature of Python that allows you to embed expressions inside string literals, using curly braces {}. 
# They are simple and efficient for basic string formatting tasks.
#  However, they lack the flexibility and functionality that prompt templates provide.

# Prompt templates are a powerful tool for generating dynamic prompts based on user input or other variables.
# they do validation of the input variables, ensuring that the generated prompt is well-formed and meets certain criteria.
#  using pydantic models to validate the input variables, which can help catch errors and ensure that the 
# generated prompt is accurate and relevant.
# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)

template.save('template.json')