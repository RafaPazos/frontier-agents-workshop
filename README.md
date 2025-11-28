# Microsoft Agent Framework - learn how to adress agentic enterprise scenarios

Join us for an immersive hands-on lab focused on Microsoft Agent Framework, where you will learn how to build intelligent multi-agent systems that leverage Azure AI capabilities. This session is designed for architects, developers, and AI enthusiasts who want to explore practical implementations of orchestration patterns.

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Environment Setup](#environment-setup)
4. [Workshop Scenarios](#workshop-scenarios)
5. [Troubleshooting](#troubleshooting)
6. [Additional Resources](#additional-resources)

## What is an Agent?

> ***agent***: 	perceives its environment, makes decisions, takes actions autonomously in order to achieve goals, and may improve its performance with learning or acquiring knowledge 

![What is an agent](./what_is_an_agent.png)

A simple LLM-based chatbot primarily focuses on generating responses based on predefined patterns and language models, often requiring user input to continue the conversation. In contrast, autonomous agents are designed to perform tasks independently, making decisions and taking actions without constant user input, often leveraging advanced AI techniques to achieve their goals. 

![Spectrum of agentic behaviour](./spectrum.png)

## Prerequisites

- Python 3.10 or later
- An GitHub account with a developer access token
- Optional: Redis, AI Search and Application Insights

## Environment Setup

1. **Install packages**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**  
    This project does not require azure resources and support GitHub AI models.

    1. Create a personal access token

    To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings or set up an Azure production key. [GitHub Free AI Token](https://github.com/settings/tokens)

    You can now access AI inference with your GitHub PAT. [Learn more about limits based on your plan](https://github.com/marketplace/models/azure-openai/gpt-4o-mini/playground#:~:text=Learn%20more%20about%20limits%20based%20on%20your%20plan.). You do not need to give any permissions to the token. 

    To use the code snippets below, create an environment variable to set your token as the key for the client code.

    If you're using bash:
    ```
    export GITHUB_TOKEN="<your-github-token-goes-here>"
    ```

    or rename the file `.env.template` to `.env` and put the value inside the `.env` file. Each python script will load the value from that value automatically.
 
## Workshop Scenarios

This workshop is organized into seven independent, progressively more advanced scenarios. Each scenario has its own `README.md` in `src/scenarios` describing goals, tasks, references, and example prompts.

1. **Scenario 1 – learning how to build your first agent**  
   Learn how to define a basic agent, connect tools, and use the Agent Framework Dev UI to inspect activities, metrics, and traces while the agent answers time and weather questions and maintains conversational memory.  
   See `src/scenarios/01-hello-world-agent/README.md`.

2. **Scenario 2 – building a user interface for your agent**  
   Build a console-based client that talks to your agent over the AG-UI protocol, so you can send user input and receive agent responses without building a full web UI.  
   See `src/scenarios/02-building-agent-ui/README.md`.

3. **Scenario 3 – exposing your agents to other agents**  
   Expose a weather agent over the A2A protocol and connect it to a separate travel-planning agent that calls it remotely to plan 5-day trips only to locations with good weather.  
   See `src/scenarios/03-connecting-two-agents/README.md`.

4. **Scenario 4 – orchestrating a workflow across multiple agents**  
   Use deterministic workflows to control the order in which several agents (preference collection, location suggestion, weather checking, summarization) collaborate to create a travel plan.  
   See `src/scenarios/04-orchestrating-agents/README.md`.

5. **Scenario 5 – declarative agents and workflows**  
   Recreate the travel planning and weather validation flow using declarative agent and workflow definitions instead of imperative code, to understand low-code orchestration patterns.  
   See `src/scenarios/05-declarative-agents/README.md`.

6. **Scenario 6 – moderating a discussion between agents**  
   Design a multi-agent travel system (places, weather, activities, flights, hotels) coordinated by a moderator/orchestrator such as Magentic One, enforcing global rules like budget, preferred locations, and activity diversity.  
   See `src/scenarios/06-moderating-agents/README.md`.

7. **Scenario 7 – agent observability and evaluation**  
   Enable OpenTelemetry-based tracing and metrics for one of your agents, wire it to an observability backend if available, and use evaluation loops and custom metrics to analyze and improve behavior.  
   See `src/scenarios/07-observability/README.md`.

## Troubleshooting

- **Missing environment variables** — Verify `.env` mirrors the keys called out in notebook setup cells.
- **Package import errors** — Ensure the `agent-framework` packages were installed into the same interpreter that launches Jupyter.
- **Redis connectivity** — Update the connection string in the Redis samples and confirm the service is reachable before running the notebook cells.
- **Application Insights ingestion delay** — Telemetry can take a few minutes to appear in the Azure portal; use the Live Metrics Stream for near-real-time debugging.

## Additional Resources

- Product documentation: <https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview>
- GitHub repository: <https://github.com/microsoft/agent-framework>
- Microsoft AI guidance: <https://learn.microsoft.com/azure/ai-services/>
