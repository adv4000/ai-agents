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

## Agent on AWS Bedrock AgentCore Runtime
### Create Package to deploy 
1. Install all packages from requirements.txt 
```
# Windows PowersHell:
 uv pip install `
  --python-platform aarch64-manylinux2014 `
  --python-version 3.14 `
  --target=package `
  --only-binary=:all: `
  -r requirements.txt
  
 # Linix
 uv pip install \
  --python-platform aarch64-manylinux2014 \
  --python-version 3.14 \
  --target=package \
  --only-binary=:all: \
  -r requirements.txt
 ```
2. Copy `agent.py` into `package` folder
3. ZIP content of `package` folder, NOT folder itself!


### Send request to AI Agent on AWS Bedrock AgentCore
```
# Windows PowersHell:
aws bedrock-agentcore invoke-agent-runtime `
  --agent-runtime-arn "arn:aws:bedrock-agentcore:us-west-2:855647970705:runtime/agent_server_manager-9sWZc786Y0" `
  --runtime-session-id "test-session-123456789012345678901234567890" `
  --payload '{"prompt":"restart servers stg1 to stg4 !"}' `
  --qualifier DEFAULT `
  response.json
  
Get-Content response.json 


# Linix
aws bedrock-agentcore invoke-agent-runtime \
  --agent-runtime-arn "arn:aws:bedrock-agentcore:us-west-2:855647970705:runtime/agent_server_manager-9sWZc786Y0" \
  --runtime-session-id "test-session-123456789012345678901234567890" \
  --payload '{"prompt":"restart servers stg1 to stg4 !"}' \
  --qualifier DEFAULT \
  response.json

cat response.json
```