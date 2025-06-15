# Agent Development Kit Development

A collection of AI agents built using the Google ADK (Agent Development Kit) for various purposes including humor generation, file management, and social media posting.

## Project Structure

```
agent-development-kit-dev/
├── F4funny/                  # Humor generation agent
│   ├── agent.py            # Root agent configuration
│   ├── sub_agents/         # Sub-agents for F4funny
│   │   └── santa_banta_agent.py  # Santa and Banta joke generator
│   └── __init__.py         # Package initialization
├── agent--integration-gdrive/  # Google Drive integration agent
│   ├── agent.py            # Root agent configuration
│   ├── sub_agents/         # Sub-agents for Google Drive integration
│   │   └── mcp_agent.py    # MCP (Media & Communications Program) agent
│   └── mcp.py              # Google Drive API integration
└── x_posting_agent/        # Social media posting agent
    └── __init__.py         # Package initialization
```

## Agents Overview

### F4funny Agent

A humor generation agent specialized in generating witty and funny content. The main components are:

- **Root Agent (F4funnyAgent)**
  - Uses Gemini 2.0 Flash model
  - Generates light-hearted, dark humor
  - Uses simple language
  - Avoids professional tone

- **Sub-agents**
  - **SantaBantaAgent**: Generates classic Santa and Banta jokes with:
    - Proper dialogue format between Santa and Banta
    - Short, punchy jokes
    - Cultural relevance
    - Clever twists and punchlines

### Google Drive Integration Agent

An agent that integrates with Google Drive to manage files and documents.

- **Root Agent**
  - Manages Google Drive operations
  - Uses Gemini 2.0 Flash model

- **Sub-agents**
  - **MCP Agent**: Handles Media & Communications Program files
    - Searches files in predefined folders
    - Gets file details
    - Reads file content
    - Manages file operations

### X Posting Agent

A social media posting agent (currently under development).

## Setup Instructions

1. Install required dependencies:
```bash
pip install google-adk
pip install python-dotenv
```

2. Set up environment variables:
- Create a `.env` file in each agent directory with required credentials
- For Google Drive integration: Add Google OAuth2 credentials
- For F4funny: No additional credentials required

3. Run the agents:
```bash
python -m F4funny.agent  # For F4funny humor generation
python -m agent--integration-gdrive.agent  # For Google Drive integration
```

## Contributing

Feel free to contribute by:
1. Adding new agents
2. Improving existing agents
3. Adding new features to sub-agents
4. Enhancing documentation

## License

[Add license information here]

## Contact

For questions or support, please contact the project maintainer.