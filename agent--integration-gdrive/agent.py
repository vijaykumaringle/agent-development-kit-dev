from google.adk.agents import Agent
from google.adk.tools import mcp

# MCP Agent
mcp_agent = Agent(
    name="mcp_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions about the MCP.",
    instruction="You are an expert in the Media and Communications Program. Answer questions about the program.",
    tools=[mcp]
)

# Root Agent
root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="Root agent to orchestrate the conversation.",
    instruction="I can answer your questions about the Media and Communications Program.",
    sub_agents=[mcp_agent]
)
