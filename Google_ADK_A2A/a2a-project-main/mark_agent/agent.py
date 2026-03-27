from crewai import LLM, Agent, Crew, Process, Task
from dotenv import load_dotenv
import os

load_dotenv()
# Step1: Agent & Tool
from tools import AvailabilityTool

class MarkAgent():

    SUPPORTED_CONTENT_TYPES = ["text", "text/plain"]

    def __init__(self):

        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment")
        
        # Use google_genai provider with correct model name
        self.llm = LLM(
                model="gemini/gemini-2.5-flash",
                api_key=self.api_key,
            )

        self.agent = Agent(
                    role="Scheduling Assistant",
                    goal="Answer questions about Mark's availability. Use the AvaiabilityTool to check Mark's calendar. Convert users input date to 'YYYY-MM-DD' format.",
                    backstory="You are a helpful scheduling assistant who checks Mark's calendar.",
                    tools=[AvailabilityTool()],
                    llm=self.llm,
                )

    async def invoke(self, user_question):
        try:
            task = Task(
                description=f"Answer this question: '{user_question}' Use the AvaiabilityTool to check Mark's calendar.",
                expected_output="A clear answer about Mark's availability.",
                agent=self.agent
            )

            crew = Crew(
                    agents=[self.agent],
                    tasks=[task],
                    process=Process.sequential,
                )
            
            result = crew.kickoff()
            return str(result) if result else "No response available"
        except Exception as e:
            print(f"[ERROR] mark_agent.invoke: {e}")
            return f"Sorry, I encountered an error: {str(e)}"
    

# mark_agent = MarkAgent()
# import asyncio
# print(asyncio.run(mark_agent.invoke("Is Mark available on 13th November 2025?")))