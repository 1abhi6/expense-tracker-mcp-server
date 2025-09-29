# Contains code for MCP server
from fastmcp import FastMCP
from app.main import app

mcp = FastMCP.from_fastapi(
    app=app,
    name="Expense Tracker"
)

if __name__ == "__main__":
    mcp.run()
