#!/usr/bin/env python3
"""Task 6: Complete Multi-Agent Demo"""

import asyncio
import os
from dotenv import load_dotenv

# Load environment variables FIRST before importing ADK modules
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

from google.adk.agents import LlmAgent
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Fix relative import error by using absolute import
from sub_agents import activity_curator, flight_specialist, hotel_expert

# Complete coordinator with all patterns available
root_agent = LlmAgent(
    name="travel_coordinator",
    model="gemini-3.5-flash",
    instruction="""You are the TravelWise Travel Coordinator.

CRITICAL RULE: You MUST ALWAYS delegate to your sub_agents - NEVER answer directly!

You manage a team of THREE specialists that you MUST use:
- flight_specialist: For ALL flight questions
- hotel_expert: For ALL hotel/accommodation questions
- activity_curator: For ALL activity/attraction questions

FOR EVERY TRAVEL REQUEST:
1. You MUST consult ALL THREE specialists
2. Your response MUST include FLIGHTS, HOTELS, and ACTIVITIES sections
3. NEVER skip any specialist - all three are required!

If user asks for trip planning:
- Sequential: FIRST flights, THEN hotels, FINALLY activities
- Or consult all three simultaneously for an overview

NEVER make up answers - ALWAYS delegate to your specialists!
NEVER respond with just one or two categories - ALL THREE are required!""",
    sub_agents=[flight_specialist, hotel_expert, activity_curator],
)

APP_NAME = "travel_assistant"
USER_ID = "demo_user"


async def main():
    # -- Configure all services -------------------------------------
    session_service = InMemorySessionService()
    memory_service = InMemoryMemoryService()
    artifact_service = InMemoryArtifactService()

    # -- Create the Runner -----------------------------------------
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
        memory_service=memory_service,
        artifact_service=artifact_service,
    )

    # -- Create a session ------------------------------------------
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    print(f"\n🚀 Travel Assistant - Full Runner Demo")
    print(f"Session ID: {session.id}")
    print(f"Services: Session ✅  Memory ✅")
    print(f"Type 'quit' to exit\n")

    # -- Interactive loop (Streaming Mode) -------------------------
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if not user_input or user_input.lower() in ["quit", "exit"]:
            break

        content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)],
        )

        print("\nTravel Assistant: ", end="", flush=True)

        # This block streams the agents' multi-turn thought process and text chunks in real-time
        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=session.id,
            new_message=content,
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(part.text, end="", flush=True)
        print("\n")

    # -- Session summary -------------------------------------------
    final_session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session.id,
    )

    print(f"\n📊 Session Summary")
    print(f"Events: {len(final_session.events)}\n")


if __name__ == "__main__":
    asyncio.run(main())
