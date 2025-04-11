### Commands

mcp run  server.py
uvicorn client_fastapi:app --reload



### POST /tool/call


{
  "tool_name": "add",
  "arguments": {
    "a": 5,
    "b": 7
  }
}

### GET /resource/{scheme}/{identifier}

greeting
Alice

OUR 

farewell
Franz


### POST /openai

{
  "prompt": "What is the capital of France?",
  "model": "gpt-3.5-turbo"
}