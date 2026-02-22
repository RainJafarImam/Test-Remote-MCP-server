import random
import json
from fastmcp import FastMCP

mcp = FastMCP("My Remote MCP server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def random_number() -> int:
    """Generate a random number"""
    return random.randint(1, 100)

@mcp.resource("info://server")
def server_info() -> str:
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Rain Jafar Imam"
    }
    return json.dumps(info, indent=2)

