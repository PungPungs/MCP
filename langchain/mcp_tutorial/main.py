from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain.agents import create_agent
from dotenv import load_dotenv
import asyncio
import pprint


async def main():
    load_dotenv()

    client = MultiServerMCPClient({
        "get_weather" : {
            "transport" : "stdio",
            "command" : "python",
            "args" : ["C:\\dev\\Code\\MCP\\weather\\weather.py"]
        }
    })

    tools = await client.get_tools()
    agent = create_agent(
        model = "claude-sonnet-4-5-20250929",
        tools = tools
    )

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what are the weather alters in California"}]}
    )

if __name__ == "__main__":
    asyncio.run(main())