### Scenario 2 - Building a user interface for your agent

Goal: In this scenario you will learn how to connect an existing agent to a simple user interface using the AG-UI protocol. Instead of building a full web application, you will focus on a console-based client that can send user input to an agent and display responses in real time. You will understand how AG-UI models conversations, messages, and activities and how these map to your agent’s tools and reasoning steps. This scenario is relevant because most real-world agents are embedded into applications, and you need a clean protocol boundary between the UI and the agent logic. By the end, you should understand why separating UI from agent behavior makes your solution easier to evolve and debug.

Task:
- Reuse or extend an existing weather-capable agent so it can answer weather-related questions for a given user location.
- Implement a console-based AG-UI server or client (based on the samples) that sends user input to the agent and streams back responses.
- Wire a function on the client side that can tell the agent where the user is (for example, by capturing location input once and reusing it).
- Use AG-UI activities and message structures to keep the conversation state consistent between the console app and the agent.
- Run and iterate on your console app to validate that user prompts are correctly forwarded and that agent responses and tool calls are visible.

Relevant references
- AG-UI protocol introduction: https://docs.ag-ui.com/introduction

Relevant samples:
- `samples/ag-ui/simple-ag-ui-client.py` – minimal console-style AG-UI client that connects to an agent endpoint.
- `samples/ag-ui/simple-ag-ui-server.py` – simple AG-UI-compatible server hosting an agent.
- `samples/simple-agents/basic-agent.py` – basic agent implementation you can adapt for weather.

Input queries:
- "Set my location to Seattle and tell me today’s weather."
- "What will the weather be like tomorrow here?"
- "Can you summarize the last three things I asked you?"
- "Change my location to Tokyo and give me a short forecast."

Tooling tips:
Start by running the AG-UI sample server and client to see the basic request/response flow before you change any code. Examine how `simple-ag-ui-client.py` connects to the AG-UI server and how it sends user messages and prints responses, then adapt this to include a function or command that sets the user’s location. Use `simple-ag-ui-server.py` as a guide for how to host your own agent behind AG-UI, wiring your weather tools into that agent. Keep your console app small and focused: delegate all reasoning and tool orchestration to the agent, and let the client focus on input and output only. When troubleshooting, log or print AG-UI messages on both sides so you can see exactly what is being sent and received.
