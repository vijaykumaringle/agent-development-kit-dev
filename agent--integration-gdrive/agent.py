from google.adk.agents import Agent
from mcp import mcp
from sub_agents.mcp_agent import mcp_agent

# Root Agent
root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="Root agent to orchestrate the conversation.",
    instruction="I can answer your questions about the Media and Communications Program.",
    sub_agents=[mcp_agent]
)
