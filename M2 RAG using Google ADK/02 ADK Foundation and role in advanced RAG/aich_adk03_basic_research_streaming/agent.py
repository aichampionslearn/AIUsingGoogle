# --------------------  
# AIChampionsHub
# Course :  AICH AI Engineering for Agentic World
# Module :  Basic Research Streaming
# --------------------

# -------- Context of Lesson and Additional Information ---------
# Objective : Build a Basic Research Agent 
# 
# Here is a link to list of all LLM Models Supported by ADK
#  https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models

# Link to Search or Grounding : https://ai.google.dev/gemini-api/docs/google-search?lang=python#configure-search
#
# For Voice examples need to set "Set SSL_CERT_FILE=$(python -m certifi)" in Windows
# adk run filename or adk web
# Ctrl+C to stop the agent
# ---------------------------------------------------------------

import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.runners import Runner
from google.genai.types import Content, Part

from google.adk.sessions import InMemorySessionService, Session

# --- Initialize our Session Service ---
session_service = InMemorySessionService()
my_user_id = "AICH_ADK_Event_Planner_001"

root_agent = Agent(
    name="basic_search_agent",   # A unique name for the agent.
    model="gemini-2.0-flash",    # The Large Language Model (LLM) that agent will use.
    
    # Provide a  short description of the agent's purpose.
    description=(                
        "Agent to answer questions using Google Search."
    ),

    # Instructions to set the agent's behavior.
    instruction=(
        "You are an expert researcher who always sticks to the facts."
    ),
    tools=[google_search]        # google_search tool to perform grounding with Google search.
)

async def run_agent_query(agent: Agent, query: str, session: Session, user_id: str):
    """Initializes a runner and executes a query for a given agent and session."""
    print(f"\n🚀 Running query for agent: '{agent.name}' in session: '{session.id}'...")

    runner = Runner(
        agent=agent,
        session_service=session_service,
        app_name=agent.name
    )

    final_response = ""
    try:
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=Content(parts=[Part(text=query)], role="user")
        ):
            if event.is_final_response():
                final_response = event.content.parts[0].text
    except Exception as e:
        final_response = f"An error occurred: {e}"


    print("\n" + "-"*50)
    print("✅ Final Response:")
    display(Markdown(final_response))
    print("-"*50 + "\n")

    return final_response

async def run_event_planner():
    # Create a new, single-use session for this query
    event_planning_session = await session_service.create_session(
        app_name=event_planner_agent.name,
        user_id=my_user_id
    )

    # Note the new budget constraint in the query!
    query = "Plan a small tech meetup for 30 people in New York on AI/ML. Budget under 5000$"
    print(f"🗣️ User Query: '{query}'")

    await run_agent_query(event_planner_agent, query, event_planning_session, my_user_id)

run_event_planner()