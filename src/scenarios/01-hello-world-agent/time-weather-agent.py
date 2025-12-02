# Copyright (c) Microsoft. All rights reserved.
"""
Scenario 1 - Your First Time & Weather Agent

This agent can:
- Figure out where the user is based on the conversation
- Tell the user what time it is at their location
- Provide weather information for the user's location
- Remember the user's location across multiple conversation turns

MCP Servers Required:
- User Server (port 8002): Provides user info, location, and time functions
- Weather Server (port 8003): Provides weather information for locations
"""

import os
import asyncio
from datetime import datetime
from typing import Annotated

from agent_framework import AgentThread, ChatAgent, MCPStreamableHTTPTool
from agent_framework.openai import OpenAIChatClient
from pydantic import Field

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# OpenAI Client Configuration
# =============================================================================

if os.environ.get("GITHUB_TOKEN") is not None:
    token = os.environ["GITHUB_TOKEN"]
    endpoint = "https://models.github.ai/inference"
    print("Using GitHub Token for authentication")
elif os.environ.get("AZURE_OPENAI_API_KEY") is not None:
    token = os.environ["AZURE_OPENAI_API_KEY"]
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    print("Using Azure OpenAI Token for authentication")
else:
    raise ValueError("No API key found. Set GITHUB_TOKEN or AZURE_OPENAI_API_KEY environment variable.")

async_openai_client = AsyncOpenAI(
    base_url=endpoint,
    api_key=token
)

# Model configuration - use available models from environment
completion_model_name = os.environ.get("COMPLETION_DEPLOYMENT_NAME", "gpt-4o")
medium_model_name = os.environ.get("MEDIUM_DEPLOYMENT_MODEL_NAME", "gpt-4o-mini")
small_model_name = os.environ.get("SMALL_DEPLOYMENT_MODEL_NAME", "gpt-4o-mini")

chat_client = OpenAIChatClient(
    model_id=medium_model_name,
    api_key=token,
    async_client=async_openai_client
)

# =============================================================================
# MCP Server Configuration
# =============================================================================

# User MCP Server - provides user info, location, and time functions
USER_MCP_URL = os.environ.get("USER_MCP_URL", "http://localhost:8002/mcp")

# Weather MCP Server - provides weather information
WEATHER_MCP_URL = os.environ.get("WEATHER_MCP_URL", "http://localhost:8003/mcp")

# =============================================================================
# Agent Instructions
# =============================================================================

AGENT_INSTRUCTIONS = """You are a helpful time and weather assistant. You help users find out:
1. What time it is at their location
2. What the weather is like at their location

IMPORTANT CAPABILITIES:
- You can look up user information and their timezone location using the user MCP server
- You can get weather information for locations using the weather MCP server
- You remember what the user tells you throughout the conversation

WORKFLOW:
1. If the user tells you where they are (e.g., "I am in London"), remember this location for future queries
2. When asked about time, use the get_current_time tool with their location
3. When asked about weather, use the get_weather_at_location tool with their location
4. If the user moves to a new location, update your memory and use the new location for subsequent queries

LOCATION HANDLING:
- The weather server supports: Seattle, New York, London, Berlin, Tokyo, Sydney
- For time queries, use timezone format like "Europe/London", "Europe/Berlin", "America/New_York"
- If the user mentions a city, map it to the appropriate timezone or weather location

Always be conversational and helpful. If you don't know the user's location yet, politely ask where they are."""

# =============================================================================
# Local Tool - Fallback for timezone conversion
# =============================================================================

def get_current_time_local(
    location: Annotated[str, Field(description="The timezone location in format like Europe/London, America/New_York, etc.")]
) -> str:
    """Get the current time for a given timezone location. Use this as a fallback if MCP server is unavailable."""
    import pytz
    try:
        location = location.strip().replace('"', '').replace('\n', '')
        timezone = pytz.timezone(location)
        now = datetime.now(timezone)
        return f"The current time in {location} is {now.strftime('%I:%M:%S %p')} on {now.strftime('%A, %B %d, %Y')}"
    except Exception as e:
        return f"Sorry, I couldn't find the timezone for '{location}'. Error: {str(e)}"


# =============================================================================
# Main Agent Implementation
# =============================================================================

async def run_time_weather_agent():
    """Run the interactive time and weather agent with conversation memory."""
    
    print("\n" + "=" * 60)
    print("🕐 Time & Weather Agent - Scenario 1")
    print("=" * 60)
    print("\nThis agent can tell you the time and weather at your location.")
    print("It remembers where you are across the conversation.\n")
    print("MCP Servers:")
    print(f"  - User Server: {USER_MCP_URL}")
    print(f"  - Weather Server: {WEATHER_MCP_URL}")
    print("\nType 'quit' or 'exit' to end the conversation.\n")
    print("-" * 60)

    weather_mcp_tool= MCPStreamableHTTPTool(
            name="Weather Server", 
        url=WEATHER_MCP_URL
        )
    
    user_mcp_tool=MCPStreamableHTTPTool(
        name="User Info Server",
        url=USER_MCP_URL
    )

    # Create the agent with MCP tools and local fallback
    agent = ChatAgent(
        chat_client=chat_client,
        name="TimeWeatherAgent",
        instructions=AGENT_INSTRUCTIONS,
        tools=[
            user_mcp_tool,      # MCP server for user info and time
            weather_mcp_tool,   # MCP server for weather
            get_current_time_local  # Local fallback for time
        ]
    )

    # Create a thread to maintain conversation history
    thread = agent.get_new_thread()
    
    # Test queries from the scenario
    test_queries = [
        "I am currently in London",
        "What is the weather now here?",
        "What time is it for me right now?",
        "I moved to Berlin, what is the weather like today?",
        "Can you remind me where I said I am based?"
    ]
    
    print("\n🧪 Running test queries from Scenario 1:\n")
    
    for query in test_queries:
        print(f"👤 User: {query}")
        result = await agent.run(query, thread=thread)
        print(f"🤖 Agent: {result.text}\n")
        print("-" * 40)

    # Interactive mode
    print("\n" + "=" * 60)
    print("💬 Interactive Mode - Ask your own questions!")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input("👤 You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye! Thanks for using the Time & Weather Agent.")
                break
            
            # Run the agent with the user's input, maintaining the thread
            result = await agent.run(user_input, thread=thread)
            print(f"🤖 Agent: {result.text}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using the Time & Weather Agent.")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}\n")


async def run_demo_mode():
    """Run a quick demo without interactive mode - useful for testing."""
    
    print("\n" + "=" * 60)
    print("🕐 Time & Weather Agent - Demo Mode")
    print("=" * 60)

    # Create MCP tools
    user_mcp_tool = HostedMCPTool(
        name="User Info Server",
        url=USER_MCP_URL
    )
    
    weather_mcp_tool = HostedMCPTool(
        name="Weather Server", 
        url=WEATHER_MCP_URL
    )

    # Create the agent
    agent = ChatAgent(
        chat_client=chat_client,
        name="TimeWeatherAgent",
        instructions=AGENT_INSTRUCTIONS,
        tools=[
            user_mcp_tool,
            weather_mcp_tool,
            get_current_time_local
        ]
    )

    # Create thread for conversation memory
    thread = agent.get_new_thread()
    
    # Demo queries
    queries = [
        "I am currently in London",
        "What is the weather now here?", 
        "What time is it for me right now?",
        "I moved to Berlin, what is the weather like today?",
        "Can you remind me where I said I am based?"
    ]
    
    for query in queries:
        print(f"\n👤 User: {query}")
        result = await agent.run(query, thread=thread)
        print(f"🤖 Agent: {result.text}")
        print("-" * 40)

    print("\n✅ Demo complete!")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        asyncio.run(run_demo_mode())
    else:
        asyncio.run(run_time_weather_agent())
