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