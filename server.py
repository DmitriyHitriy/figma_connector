import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

REQUIREMENTS_DIR = Path(__file__).parent / "requirements"
FILE_PATH = os.environ.get("REQUIREMENTS_FILE", "requirements.txt")

mcp = FastMCP(
    "figma-local-file-connector",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    ),
    streamable_http_path="/",
)

@mcp.tool()
def list_requirements() -> str:
    """List all available requirement files"""
    if not REQUIREMENTS_DIR.exists():
        return "No requirements directory found"

    files = sorted(f.name for f in REQUIREMENTS_DIR.iterdir() if f.suffix == ".txt")
    if not files:
        return "No requirement files found"

    result = "Available requirement files:\n"
    for f in files:
        result += f"  - {f}\n"
    return result

@mcp.tool()
def read_requirements(file_path: str = "") -> str:
    """Read requirements from a local text file.
    If file_path is empty, reads the default file (requirements.txt).
    Files from requirements/ directory can be referenced by name (e.g. 'dashboard.txt')."""
    path = file_path or FILE_PATH

    if not os.path.exists(path):
        alt_path = os.path.join("requirements", path)
        if os.path.exists(alt_path):
            path = alt_path

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
