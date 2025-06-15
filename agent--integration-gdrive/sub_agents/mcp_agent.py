from google.adk.agents import Agent
from mcp import MCPTool
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Google Drive credentials from environment variables
credentials = Credentials.from_authorized_user_info(
    info={
        "token": os.getenv('GOOGLE_DRIVE_TOKEN'),
        "refresh_token": os.getenv('GOOGLE_DRIVE_REFRESH_TOKEN'),
        "client_id": os.getenv('GOOGLE_DRIVE_CLIENT_ID'),
        "client_secret": os.getenv('GOOGLE_DRIVE_CLIENT_SECRET'),
        "token_uri": "https://oauth2.googleapis.com/token"
    },
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

