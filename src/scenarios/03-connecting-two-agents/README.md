### Scenario 3 - exposing your agents to other agents

Goal: You have already built an agent that can predict the weather at a specific location and now want to expose your agent via the A2A protocol to another travel planning agent that can make travel plans. In this scenario you will practice separating responsibilities between a weather-focused agent and a travel-planning agent so each can evolve independently. You will learn how to expose an agent capability over A2A, how to consume that capability from another agent, and why this is useful when different teams or systems own different agents. This is relevant because real-world solutions often combine multiple specialized agents rather than putting all logic into a single monolithic assistant. By the end, you should understand how and why to let one agent call another over a well-defined protocol instead of directly sharing code.

Task:
- Build or reuse a weather agent that can answer whether the weather is good at a specific location and date.
- Implement a separate travel planning agent that calls the weather agent via A2A instead of reasoning about weather itself.
- Configure and run an A2A server so the weather agent is exposed as a remote capability the travel agent can invoke.
- Make the travel agent plan a 5-day trip only to locations where the weather is consistently "good" or "sunny" for the requested dates.
- Connect your A2A-enabled weather agent to another participant's travel agent (or vice versa) to validate that the protocol works across different implementations.

Relevant references
- A2A protocol specification: https://a2a-protocol.org/latest/

Relevant samples:
- `samples/a2a_communication/server` – A2A agent server exposing an agent over the protocol.
- `samples/a2a_communication/agent-client.py` – client agent that calls another agent via A2A.
- `samples/simple-agents/basic-agent.py` – starting point for implementing simple tool-based behavior for either agent.

Input queries:
- "Plan a 5-day trip for me somewhere in Europe where the weather will be sunny next month."
- "If the weather is bad in London on my dates, suggest an alternative city with better weather."
- "Explain which locations you checked and why you chose this itinerary."
- "What would the trip look like if I moved the dates by one week?"

Tooling tips:
Start by running the A2A server and client samples to see how two agents communicate before changing any logic. Use the server sample to host your weather agent and expose a function (for example, a tool that returns whether the weather is good on a certain date in a given city). Adapt the client sample so your travel planning agent calls that A2A endpoint instead of doing its own weather reasoning. Keep clear boundaries: treat the weather agent as an external service with a stable interface and let the travel planner focus on itinerary construction and explanation. When debugging, log A2A requests and responses so you can verify which locations and dates were checked and how that influenced the planned trip.
