## Strands Agent + AWS Bedrock + BedrockAgentCore

### Setup AWS Credentials
```
# Windows PowersHell:
$env:AWS_ACCESS_KEY_ID="xxxxxxxxxxxxxxxxx"
$env:AWS_SECRET_ACCESS_KEY="yyyyyyyyyyyyyyyyyyyyyyyyyyyy"
$env:AWS_DEFAULT_REGION="zzzzzzzzz"

# Linix
export AWS_ACCESS_KEY_ID="xxxxxxxxxxxxxxxxx"
export AWS_SECRET_ACCESS_KEY="yyyyyyyyyyyyyyyyyyyyyyyyyyyy"
export AWS_DEFAULT_REGION="zzzzzzzzz"
```

### Start AI Agent
```
pip install -r requirements.txt
python agent.py
```

### Send request to AI Agent
```
curl http://127.0.0.1:8080/ping
curl -X POST http://127.0.0.1:8080/invocations -H "Content-Type: application/json" -d '{"prompt": "restart server stg1"}'
```