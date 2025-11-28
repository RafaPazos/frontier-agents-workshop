### Scenario 5 - declarative agents

Goal: In this scenario you will learn how to describe agents and their orchestration declaratively instead of writing all orchestration logic in Python. You will see how prompts, models, tools, and workflows can be expressed in YAML so that capabilities and flows can be versioned and operated like configuration. This is relevant when you want product or operations teams to adjust agent behavior without changing application code, or when you want to reuse the same orchestration across environments. You will also compare the imperative workflows from earlier scenarios with their declarative equivalents to understand when each approach makes sense. By the end, you should feel comfortable reading, modifying and extending declarative agent and workflow definitions.

Task:
- Study the existing declarative assistant definitions (for example, the weather and location assistants) and understand how prompts, models and output schemas are configured.
- Build or adapt a declarative agent that recommends locations and a declarative agent that reports weather, based on the YAML samples.
- Create or update a declarative workflow that executes a sequence of “location recommendation” followed by “weather check” using these agents.
- Ensure that responses follow a clear JSON output schema so they are easy to consume from code or tools.
- Run the declarative agents and workflow using the provided runner script and adjust configuration (not code) to change behavior.

Relevant references
- Declarative agents and workflows overview: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/vs-code-agents-workflow-low-code?view=foundry

Relevant samples:
- `samples/declarative-agents/weather-assistant.yaml` – declarative assistant that can call a weather tool.
- `samples/declarative-agents/location-assistant.yaml` – declarative assistant returning structured JSON with language, answer and type.
- `samples/declarative-agents/travel-agengy-workflow.yaml` – workflow that chains location and weather assistants.
- `samples/declarative-agents/run-simple-assistant.py` – simple runner for testing declarative assistants.

Input queries:
- "I speak German. Recommend two cities I could visit next month and tell me what the weather will be like."
- "Recommend a weekend trip destination and include the expected weather in JSON."
- "Change my preferred language to Spanish and repeat your recommendation."

Tooling tips:
Open the YAML files for the declarative agents and workflow side by side to see how they reference each other. Use `run-simple-assistant.py` to quickly test changes to a single assistant definition before wiring it into the workflow. When you need to change behavior (for example, output format or temperature settings), prefer editing the YAML configuration instead of modifying Python code. Validate that the assistant responses match the declared `outputSchema` so downstream tools can rely on the structure. As a bonus challenge, try adding a new field to the output schema (such as a confidence or recommendationReason) and update the instructions so the model fills it correctly.
