from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from typing import Dict, Any, List, Optional

class MCPTool:
    def __init__(self, credentials: Credentials):
        """Initialize Google Drive service with provided credentials."""
        self.service = build('drive', 'v3', credentials=credentials)
        self.folder_id = "YOUR_PREDEFINED_FOLDER_ID"  # Replace with your Google Drive folder ID

    def search_files(self, query: str) -> List[Dict[str, Any]]:
        """Search files in the predefined folder."""
        try:
            query = f"name contains '{query}' and '{self.folder_id}' in parents"
            results = self.service.files().list(
                q=query,
                fields="files(id, name, mimeType, modifiedTime)"
            ).execute()
            return results.get('files', [])
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_file_details(self, file_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific file."""
        try:
            file = self.service.files().get(
                fileId=file_id,
                fields="id, name, mimeType, size, modifiedTime, description"
            ).execute()
            return file
        except HttpError as error:
            print(f"An error occurred: {error}")
            return {"error": str(error)}

    def get_file_content(self, file_id: str) -> Optional[str]:
        """Get content of a text file."""
        try:
            # Check if file is a text file
            file = self.service.files().get(fileId=file_id).execute()
            if not file['mimeType'].startswith('text/'):
                return None
            
            # Download the file content
            request = self.service.files().get_media(fileId=file_id)
            content = request.execute().decode('utf-8')
            return content
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

# Create an instance of the MCP tool
# Note: In a real application, credentials should be properly loaded
# mcp = MCPTool(credentials)
