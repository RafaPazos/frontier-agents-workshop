### Scenario 7 - agent observability and evaluation

Goal: The Agent Framework Python SDK is designed to efficiently generate comprehensive logs, traces, and metrics throughout the flow of agent/model invocation and tool execution. In this scenario you will learn how to turn on observability for your agents, route telemetry to a backend such as Application Insights (if available), and interpret traces and metrics to understand agent behavior. You will also explore how evaluation loops and custom metrics can help validate whether your agents are grounded and behaving as expected. This is relevant because production agentic systems must be measurable, debuggable, and continuously improvable, not just capable of producing good single responses. By the end, you should be comfortable instrumenting an existing agent, inspecting its behavior over multiple runs, and using evaluation outputs to drive improvements.

Task:
- Select one of the agents you built in a previous scenario (or use a sample agent from this repo) and enable tracing and metrics for it.
- Configure the observability environment variables (for example, `ENABLE_OTEL` and `ENABLE_SENSITIVE_DATA`) and confirm that traces are being emitted.
- If you have access to Application Insights or another OTEL-compatible backend, connect your traces and visualize key spans such as model calls and tool executions.
- Define at least one custom metric or evaluation criterion (e.g., groundedness, latency, tool success rate) and log it during agent runs.
- Feed a small set of test prompts through your agent and use the collected traces and metrics to validate and iteratively improve its behavior.

Relevant references
- Agent Framework evaluation sample (self-reflection): https://github.com/microsoft/agent-framework/tree/main/python/samples/getting_started/evaluation/self_reflection

Relevant samples:
- `samples/evaluation/self-evaluation.py` – example of running evaluations and analyzing results.

Input queries:
- "Run these five prompts through my travel agent and show me which ones failed the groundedness check."
- "Explain the sequence of tools and model calls for this conversation."
- "Which prompts are causing the highest token usage or latency?"
- "How did the agent's answers change after applying the self-reflection loop?"

Tooling tips:
Use the environment variables `ENABLE_OTEL=true` and `ENABLE_SENSITIVE_DATA=true` to turn on detailed observability for the Agent Framework. Start by running the `samples/evaluation/self-evaluation.py` script to understand how evaluation loops, metrics, and result files (such as JSONL outputs) are structured. If you are sending traces to Application Insights or another OTEL backend, verify export configuration via your devcontainer or environment settings and then inspect spans, attributes, and metrics in that UI. When iterating, keep your test prompt set small but diverse so you can quickly rerun evaluations and compare before/after changes to your agent.