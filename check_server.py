import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

SERVER_URL = "https://figma.benzomesto.ru/sse"

async def main():
    print(f"Connecting to MCP server: {SERVER_URL}")
    print()

    async with sse_client(url=SERVER_URL) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()

            result = await session.list_tools()
            tools = result.tools

            print(f"Server: figma-local-file-connector")
            print(f"Status: ONLINE")
            print(f"Tools available: {len(tools)}")
            print()

            for tool in tools:
                print(f"  Tool: {tool.name}")
                print(f"  Description: {tool.description}")
                print(f"  Input schema: {tool.inputSchema}")
                print()

            print("Testing read_requirements tool...")
            result = await session.call_tool("read_requirements", {})
            print(f"  Status: OK")
            print(f"  Content length: {len(result.content[0].text)} chars")
            print(f"  Preview: {result.content[0].text[:200]}...")

if __name__ == "__main__":
    asyncio.run(main())
