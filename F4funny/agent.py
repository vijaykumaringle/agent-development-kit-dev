from google.adk.agents import Agent
#from google.adk.models import Model
#from google.adk.tools import Tool
from F4funny.sub_agents.santa_banta_agent import santa_banta_agent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the humor generation model
#humor_model = Model(
#    name="gemini-2.0-flash",
#    model="gemini-2.0-flash",
#    description="Gemini flash model for generating humorous content",
#    temperature=0.7,
#    max_tokens=200
#)

# Define the root agent
root_agent = Agent(
    name="F4funnyAgent",
    #model=humor_model,
    model="gemini-2.0-flash",
    description="Orchestration agent for F4funny witty humor agent.",
    instruction="""
    You are F4funny, a witty humor agent that generates funny jokes, puns, and humorous content.
    Your goal is to make people laugh while maintaining good taste and avoiding offensive content.
    
    When generating humor:
    1. Keep it light-hearted and dark 
    2. Keep offensive jokes
    3. Consider the cultural context of the joke
    4. Avoid a professional tone
    5. Use simple language
    """,
    sub_agents=[santa_banta_agent]  # Will be populated with sub-agents
)
