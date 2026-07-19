import os
import re
import subprocess
import threading
from pathlib import Path
from mcp.server.fastmcp import FastMCP

FILE_PATH = os.environ.get("REQUIREMENTS_FILE", "requirements.txt")

mcp = FastMCP("figma-local-file-connector")

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

    app = mcp.sse_app()
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)

    def start_tunnel():
        import subprocess, re
        cmd = "ssh -o StrictHostKeyChecking=no -R 80:localhost:8000 nokey@localhost.run"
        proc = subprocess.Popen(
            cmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        for line in proc.stdout:
            print(line, end="")
            m = re.search(r"https://[\w.-]+\.(?:lhr\.life|localhost\.run)", line)
            if m:
                url = m.group(0)
                print(f"\n=== FIGMA CONNECTOR URL: {url}/sse ===")

    threading.Thread(target=start_tunnel, daemon=True).start()
    server.run()
