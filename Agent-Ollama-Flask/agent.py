#----------------------------------------------------------
# Simple AI Agent with three simulation tools
# Ollama + Flask + Strands
# Copyleft (c) By Denis Astahov
#
# Don't forget to give GitHub *STAR*
#----------------------------------------------------------
from strands import Agent, tool
from strands.models.ollama import OllamaModel
from flask import Flask, request

# --------------------------------------------------
# Ollama config
# --------------------------------------------------
OLLAMA_HOST_URL = "http://127.0.0.1:11434"  # Ollama API server
OLLAMA_MODEL_ID = "gemma4:12b"              # LLM Model To use

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
    model=OllamaModel(host=OLLAMA_HOST_URL,model_id=OLLAMA_MODEL_ID),
    tools=[get_server_status, start_server, stop_server],
    system_prompt="""
    You are a helpful IT assistant.
    When the user asks about the server, use the appropriate tool.

    Always start your response with:"Yes My Lord!"

    Then provide a short and clear answer.
    """
)

# --------------------------------------------------
# 3. Flask app (local HTTP runtime)
# --------------------------------------------------

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "AI Agent Running!"

@app.route("/", methods=["POST"])
def invoke():
    payload = request.get_json()
    prompt = payload.get("prompt", "Hello!")

    result = my_agent(prompt)
    return {
        "response": result.message.get("content", [{}])[0].get("text", str(result))
    }


# --------------------------------------------------
# 4. Run server
# --------------------------------------------------

if __name__ == "__main__":
    print("AI Agent started, waiting for messages...")
    app.run(host="0.0.0.0", port=8080)
    print("AI Agent Shutdown, Bye!")
