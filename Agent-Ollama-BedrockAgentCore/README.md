## Strands Agent + Ollama + BedrockAgentCore

### Start AI Agent
```
pip install -r requirements.txt
python agent.py
```

### Send request to AI Agent
```
curl http://127.0.0.1:8080/ping
curl -X POST http://127.0.0.1:8080/invocations -H "Content-Type: application/json" -d '{"prompt": "restart servers stg1 to stg3"}'
```