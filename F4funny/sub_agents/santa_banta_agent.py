from google.adk.agents import Agent
from google.adk.models import Model

# Define Santa and Banta model with specific configuration
santa_banta_model = Model(
    name="gemini-2.5-flash",
    description="Gemini flash model specialized for Santa and Banta jokes",
    temperature=0.8,  # Higher temperature for more creative jokes
    max_tokens=150,   # Shorter responses for punchy jokes
    top_p=0.9,
    top_k=40
)

# Create the Santa and Banta subagent
santa_banta_agent = Agent(
    name="SantaBantaAgent",
    model=santa_banta_model,
    description="Agent specialized in generating Santa and Banta jokes with witty humor",
    instruction="""
    You are the Santa and Banta joke generator. Your job is to create funny, witty jokes 
    in the style of Santa and Banta, two classic Indian comedy characters.
    
    Guidelines:
    1. Always maintain the Santa-Banta format
    2. Keep jokes short and punchy
    3. Use simple, relatable situations
    4. Add a clever twist or punchline
    5. Maintain cultural relevance
    6. Use proper Santa-Banta dialogue style
    
    Example format:
    Santa: [Question/Statement]
    Banta: [Funny Response]
    
    Always return the joke in this format and make sure it's funny!
    """
)
