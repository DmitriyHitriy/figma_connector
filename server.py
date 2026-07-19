import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

FILE_PATH = os.environ.get("REQUIREMENTS_FILE", "requirements.txt")

mcp = FastMCP(
    "figma-local-file-connector",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    ),
    streamable_http_path="/",
)

@mcp.tool()
def read_requirements(file_path: str = "") -> str:
    """Read requirements from a local text file"""
    path = file_path or FILE_PATH

    if not os.path.exists(path):
        return f"File not found: {path}"

    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn

    app = mcp.streamable_http_app()
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
