import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

SERVER_URL = "http://localhost:8001/sse"

async def main():
    print(f"📡 Connecting to MCP Server at: {SERVER_URL}...")
    
    # 1. Establish the SSE transport channel
    async with sse_client(url=SERVER_URL) as (read_stream, write_stream):
        # 2. Create an MCP Client Session over the streams
        async with ClientSession(read_stream, write_stream) as session:
            
            # 3. Initialize the protocol handshake
            await session.initialize()
            print("🤝 Handshake successful! Querying registered tools...")
            
            # 4. List the available tools broadcasted by the server
            response = await session.list_tools()
            
            print("\n============================================================")
            print("🛠️  DISCOVERED MCP TOOLS:")
            print("============================================================")
            for tool in response.tools:
                print(f"• Name:        {tool.name}")
                print(f"  Description: {tool.description}")
                print(f"  Schema:      {tool.inputSchema}")
            print("-" * 60)

if __name__ == "__main__":
    asyncio.run(main())