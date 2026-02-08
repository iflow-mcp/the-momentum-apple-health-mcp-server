import sys

from fastmcp import FastMCP

from app.config import settings
from app.mcp.v1.mcp import mcp_router

print("SETUP -> Setting up the app", file=sys.stderr)
mcp = FastMCP(settings.PROJECT_NAME)

mcp.mount(mcp_router)


def main() -> None:
    """Main entry point for MCP server"""
    mcp.run()


if __name__ == "__main__":
    main()