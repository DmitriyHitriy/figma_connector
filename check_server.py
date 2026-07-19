import asyncio
import sys
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

SERVER_URL = "https://figma.benzomesto.ru"

async def main():
    sys.stdout.write(f"Checking MCP server: {SERVER_URL}\n\n")
    sys.stdout.flush()

    try:
        async with asyncio.timeout(10):
            async with streamable_http_client(url=SERVER_URL) as streams:
                async with ClientSession(streams[0], streams[1]) as session:
                    await session.initialize()

                    result = await session.list_tools()
                    tools = result.tools

                    sys.stdout.write(f"Server: figma-local-file-connector\n")
                    sys.stdout.write(f"Status: ONLINE\n")
                    sys.stdout.write(f"Tools available: {len(tools)}\n\n")

                    for tool in tools:
                        sys.stdout.write(f"  Tool: {tool.name}\n")
                        sys.stdout.write(f"  Description: {tool.description}\n")
                        sys.stdout.write(f"  Input schema: {tool.inputSchema}\n\n")

                    sys.stdout.write("Testing read_requirements tool...\n")
                    result = await session.call_tool("read_requirements", {})
                    sys.stdout.write(f"  Status: OK\n")
                    sys.stdout.write(f"  Content length: {len(result.content[0].text)} chars\n")
                    sys.stdout.write(f"  Preview: {result.content[0].text[:200]}...\n")

    except BaseExceptionGroup as e:
        for ex in e.exceptions:
            sys.stdout.write(f"Error: {ex}\n")
    except BaseException as e:
        sys.stdout.write(f"Error: {type(e).__name__}: {e}\n")
    sys.stdout.flush()

asyncio.run(main())