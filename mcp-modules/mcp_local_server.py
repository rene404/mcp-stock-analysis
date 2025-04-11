# mcp_local_server.py
"""
An MCP node that summarizes text with OpenAI's GPT-3.5.
Ensure OPENAI_API_KEY is set in your environment.
"""

import os
import openai
from mcp import Node, Payload, Param

openai.api_key = os.getenv("OPENAI_API_KEY")

node = Node()

@node.handle("summarize", param=Param("text", str))
def summarize(payload: Payload):
    text = payload.payload_data["text"]
    # Call OpenAI to summarize
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful summarizer."},
            {"role": "user", "content": text}
        ]
    )
    summary = response["choices"][0]["message"]["content"]
    return {"summary": summary}

if __name__ == "__main__":
    # Run on port 8000, can be changed if needed
    node.run(host="0.0.0.0", port=8000)
