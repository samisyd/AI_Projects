# run using: uv run jeff_agent.__main__:main.py # --host localhost --port 10004
#  -to run do - uv run .\jeff_agent\__main__.py # --host localhost --port 10005

# then get the agent card from http://localhost:10004/.well-known/agent-card and use it to interact with the agent.
#  You can use the example query "Are you free to play badminton on 2025-11-05?" to test the agent's functionality.
# curl http://localhost:10004/.well-known/agent-card.json

# Step3: Agent Card

#  This is the way that a2a has defined for creating an agent card, which is a standardized way to 
# describe the agent's capabilities, skills, and other relevant information. The agent card is used to 
# register the agent with the a2a system and to provide information about the agent to users who 
# may want to interact with it. In this example, we are creating an agent card for Jeff's
#  scheduling assistant, which has a skill for helping with finding Jeff's availability for
#  badminton games. The agent card includes details such as the agent's name, description, 
# version, supported input and output modes, capabilities, and skills.
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)

from agent import JeffAgent
from a2a.server.request_handlers import DefaultRequestHandler
from agent_executor import JeffAgentExecutor
from a2a.server.tasks import InMemoryTaskStore
from a2a.server.apps import A2AStarletteApplication
import uvicorn

#import httpx

def main(host = "localhost", port = 10004):

    skill = AgentSkill(
        id="schedule_badminton",
        name="Badminton Scheduling Tool",
        description="Helps with finding Jeff's availability for Badminton",
        tags=["scheduling", "badminton"],
        examples=["Are you free to play badminton on 2025-11-05?"]
    )

    agent_card = AgentCard(
        name="Jeff's Agent",
        description="Helps with scheduling badminton games",
        url=f"http://{host}:{port}/",
        version="1.0.0",
        #  can be audio, video, text, or any other content type that the agent can process. This information 
        # is used by the a2a system to route requests to the appropriate agent based on the content type of the request.
        defaultInputModes=JeffAgent.SUPPORTED_CONTENT_TYPES,
        defaultOutputModes=JeffAgent.SUPPORTED_CONTENT_TYPES,
        capabilities=AgentCapabilities(),
        skills=[skill]
    )
    
    # Step4: Host the Agent
    
    # 
    # It is responsible for receiving requests,
    # processing them, and returning responses. The DefaultRequestHandler is a built-in request handler 
    # provided by the a2a framework that can be used to handle requests for agents. It takes an agent executor, 
    # which is responsible for executing the agent's logic, and a task store, which is used to manage tasks and 
    # their associated data. In this example, we are using an in-memory task store for simplicity,
    #  but in a production environment, you would likely want to use a more robust task store that can 
    # handle larger volumes of data and provide persistence across restarts.
    #httpx_client = httpx.AsyncClient()
    
    # request handler - entry point for handling incoming requests to the agent. 
    request_handler = DefaultRequestHandler(
        agent_executor=JeffAgentExecutor(),
        
        # where will our checkpoints and task data be stored. In this example, we are using an in-memory task store for simplicity,
        task_store=InMemoryTaskStore(),

        # push_notifier is used to send real-time updates to clients about the status of their requests. if there is 
        # a long task in progress, the push notifier can be used to update the client on the task's status. In this example, 
        # we are using an in-memory push notifier for simplicity, but in a production environment, you would likely 
        # want to use a more robust push notifier that can handle larger volumes of data and provide persistence across restarts.
        #push_notifier=InMemoryPushNotifier(httpx_client),

    )

    # host the app
    # A2AStarletteApplication is a class provided by the a2a framework that allows you to create a
    #  web application using the Starlette framework.
    server = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )       

    # uvicorn is an ASGI server that can be used to run the Starlette application. It is a lightweight and 
    # fast server that is well-suited for running asynchronous web applications. In this example, we are using 
    # uvicorn to run the A2AStarletteApplication, which will allow us to host our agent and make it accessible 
    # to users who want to interact with it.
    uvicorn.run(server.build(), host=host, port=port)


if __name__ == "__main__":
    main()