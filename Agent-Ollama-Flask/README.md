## Strands Agent + Ollama + Flask

### Start AI Agent
```
pip install -r requirements.txt
python agent.py
```

### Send request to AI Agent
```
curl http://127.0.0.1:8080/
curl -X POST http://127.0.0.1:8080/ -H "Content-Type: application/json"  -d '{"prompt": "restart servers stg1 to stg3"}'
```