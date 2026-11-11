#----------------------------------------------------------
# Simple AI Agent with three simulation tools
# AWS Bedrock + BedrockAgentCore + Strands
# Copyleft (c) By Denis Astahov
#
# Don't forget to give GitHub *STAR*
#----------------------------------------------------------
from strands import Agent, tool
from strands.models import BedrockModel
from bedrock_agentcore import BedrockAgentCoreApp

# --------------------------------------------------
# AWS Bedrock config
# --------------------------------------------------
AWS_BEDROCK_MODEL_ID     = "global.anthropic.claude-opus-5-5"
AWS_BEDROCK_MODEL_REGION = "us-west-2"

# --------------------------------------------------
# 1. Our Agent tools
# --------------------------------------------------

@tool
def get_server_status(server_name: str):
    """
    Check the current status of a server.
    Args:
        server_name: The name of the server to check.
    """
    return f"Server '{server_name}' is ONLINE!"

@tool
def start_server(server_name: str):
    """
    Start a server.
    Args:
        server_name: The name of the server to start.
    """
    return f"Server '{server_name}' is STARTED!"

@tool
def stop_server(server_name: str):
    """
    Stop a server.
    Args:
        server_name: The name of the server to stop.
    """
    return f"Server '{server_name}' is STOPPED!"


# --------------------------------------------------
# 2. Agent with Model (local Ollama)
# --------------------------------------------------

my_agent = Agent(
    model=BedrockModel(model_id=AWS_BEDROCK_MODEL_ID, region_name=AWS_BEDROCK_MODEL_REGION),
    tools=[get_server_status, start_server, stop_server],
    system_prompt="""
    You are a helpful IT assistant.
    When the user asks about the server, use the appropriate tool.

    Always start your response with:"Yes My Lord!"

    Then provide a short and clear answer.
    """
)

# --------------------------------------------------
# 3. BedrockAgentCore App
# --------------------------------------------------

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):

    prompt = payload.get("prompt", "Hello!")

    result = my_agent(prompt)
    return {
        "response": result.message.get("content", [{}])[0].get("text", str(result))
    }


# --------------------------------------------------
# 4. Start AgentCore
# --------------------------------------------------

if __name__ == "__main__":
    print("AI Agent started, waiting for messages...")
    app.run()
    print("AI Agent Shutdown, Bye!")
