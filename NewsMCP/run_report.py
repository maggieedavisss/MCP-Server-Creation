import asyncio
from mcp.client import MCPClient

async def main():
    client = MCPClient()

    # Ask user for topic and filename
    topic = input("Enter the news topic: ")
    filename = input("Enter filename (optional, leave blank for default): ") or None

    result = await client.call_tool(
        "generate_tag_news_report",
        topic=topic,
        filename=filename
    )
    print(result)

asyncio.run(main())
