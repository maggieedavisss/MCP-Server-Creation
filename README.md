# Leverage this: https://modelcontextprotocol.io/docs/develop/build-server

## Configuration for Claude Desktop
For the config.josn: you must find where claude desktop was downloaded on your computer: users/maggie/AppData/Roaming/Claude/claude_desktop_config.json

## Setting up virtual environment for MCP

### Set up your environment
First, let’s install uv and set up our Python project and environment:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Make sure to restart your terminal afterwards to ensure that the uv command gets picked up.

### Now, let’s create and set up our project:

Create a new directory for our project
uv init weather
cd weather

Create virtual environment and activate it
uv venv
.venv\Scripts\activate

Install dependencies
uv add mcp[cli] httpx

Create our server file
new-item weather.py

## Server must be running locally in terminal 
In the terminal: Run uv run weather.py to start the MCP server, which will listen for messages from MCP hosts OR run this in the terminal python news.py before you launch claude desktop. 
