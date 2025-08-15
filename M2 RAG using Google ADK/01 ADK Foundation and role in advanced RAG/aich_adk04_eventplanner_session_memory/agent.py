import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session
from google.genai.types import Content, Part

def create_event_planner_agent():
    """Create event planner agent"""
    agent = Agent(
        name="AICH_Event_Planner_Agent",
        model="gemini-2.0-flash",
        description="Agent specialized in generating full-day itineraries based on mood, interests, and budget.",
        instruction="""
        You are an expert event planner. Your goal is to create a comprehensive plan for any event requested by the user using your search tool.

        You should:
        1.  **Clarify the Event:** If the user's request is vague, ask for key details like event type, number of attendees, budget, and location.
        2.  **Brainstorm Themes:** Suggest 2-3 creative themes for the event.
        3.  **Find Venues:** Use your search tool to find 3-5 potential venues that fit the event's requirements.
        4.  **Suggest a Schedule:** Propose a high-level schedule or agenda for the event.
        5.  **Summarize:** Present the information in a clear, organized format.

        """,
        tools=[google_search]
    )
    return agent;

# event_planner_agent = create_event_planner_agent()
root_agent = create_event_planner_agent()
event_planner_agent = root_agent
print(f"🧞 Agent '{event_planner_agent.name}' is created and ready!")