import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.environ["GROQ_API_KEY"]
)

researcher = Agent(role = "Researcher Analyst", 
                   goal = "Conduct structured research on a topic",
                   backstory = "Expert in gathering accurate AI insights. ",
                #    constraints = "Use credible sources for research Organize findings in a structured format",
                   llm=groq_llm, verbose=True)

writer = Agent(role = "Technical Writer", 
               goal = "Write a detailed and clear blog post",
               backstory = "Skilled at explaining AI systems clearly",
               llm=groq_llm, verbose=True)

editor = Agent(role = "Content Editor", 
               goal = "Refine and polish the content professionally",   
               backstory = "Improves clarity , grammer and structure.",
               llm=groq_llm, verbose=True)


t1 = Task(
    description="Research how Multi-Agent AI systems work.",
    agent=researcher,
    expected_output="Structured research notes."
)

t2 = Task(
    description="Write a blog post based on research.",
    agent=writer,
    expected_output="Well-structured blog post."
)

t3 = Task(
    description="Edit and polish the blog post.",
    agent=editor,
    expected_output="Final polished blog post."
)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[t1, t2, t3],
    process=Process.sequential
)

print(crew.kickoff())
