from google.adk.agents import Agent
from mcp import MCPTool
from google.oauth2.credentials import Credentials

# Initialize Google Drive credentials (replace with your actual credentials)
credentials = Credentials.from_authorized_user_info(
    info={"token": "YOUR_TOKEN", "refresh_token": "YOUR_REFRESH_TOKEN"},
    scopes=['https://www.googleapis.com/auth/drive.readonly']
)

# Create MCP tool instance with credentials
mcp = MCPTool(credentials)

mcp_agent = Agent(
    name="mcp_agent",
    model="gemini-2.0-flash",
    description="Agent to access and analyze files in Google Drive.",
    instruction="""You are an expert in accessing and analyzing files stored in Google Drive.
    You have tools to search for files, get file details, and read file content.
    
    When asked questions:
    1. First try to search for relevant files using the search_files tool
    2. If found, use get_file_details to get more information about the file
    3. For text files, use get_file_content to read the actual file content
    4. Always explain your findings clearly based on the file information
    
    If you can't find relevant files or encounter errors, explain this to the user.
    """,
    tools=[mcp]
)

