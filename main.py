import random 
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Remote MCP server", host="0.0.0.0", port=8080)

@mcp.tool()
def add(a:float,b:float) ->float:
    """add two number together """
    return a+b

@mcp.tool()
def random_number()->int:
    """generate a random number"""
    return random.randint(1,100)

@mcp.resource("info://server")
def server_info() -> str:
    info={
        "name":"Simple Calculator Server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools",
        "tools":["add","random_number"],
        "author":"Rain Jafar Imam"
    }
    return json.dumps(info,indent=2)



if __name__ == "__main__":
    mcp.run(transport="streamable-http")