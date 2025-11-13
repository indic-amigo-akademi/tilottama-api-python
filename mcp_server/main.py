# Assumes the FastAPI app from above is already defined
import sys
import os
from fastmcp import FastMCP
import logging

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
from api_server.main import PORT, app, APP_NAME


# Convert to MCP server
mcp = FastMCP.from_fastapi(app=app, name=APP_NAME + " MCP")

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=PORT)