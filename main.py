# main.py
from fastapi import FastAPI, Body
from typing import Dict, Any
from llm_client import get_llm_response

app = FastAPI(
    title="Echo API",
    description="A FastAPI app that echoes request data and queries an LLM.",
    version="1.0.1"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Echo API! Try /chat_completion or /echo_body."}


@app.post("/chat_completion")
async def chat_completion(
    request_data: Dict[str, Any] = Body(
        ...,
        example={"message": "Tell me a joke", "model_name": "gpt-4"},
        description="Provide a message and LLM model name."
    )
):
    message = request_data.get("message")
    model_name = request_data.get("model_name")

    if not message or not model_name:
        return {"error": "Both 'message' and 'model_name' must be provided."}

    llm_response = get_llm_response(message, model_name)

    return {
        "received_request_type": "POST",
        "message": message,
        "model_name": model_name,
        "llm_response": llm_response
    }


@app.post("/echo_body/")
async def echo_request_body(
    request_data: Dict[str, Any] = Body(
        ...,
        example={"name": "Alice", "age": 30, "city": "New York"},
        description="Any JSON object to echo back."
    )
):
    return {
        "received_request_type": "POST",
        "received_request_body": request_data
    }
