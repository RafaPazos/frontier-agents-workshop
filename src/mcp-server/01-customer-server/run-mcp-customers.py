import uvicorn
import asyncio

from server_mcp_sse_customers import mcp, check_mcp, sse_app

if __name__ == "__main__":
    try:
        asyncio.run(check_mcp(mcp))
        uvicorn.run(sse_app, host="0.0.0.0", port=8001)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Cleaning up...")
    except Exception as e:
        print(f"An error occurred: {e}")