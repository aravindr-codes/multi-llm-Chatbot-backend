# main.py
from fastapi import FastAPI, Query, Body
from typing import Optional, Dict, Any


app = FastAPI(
    title="Echo API",
    description="A simple FastAPI application that echoes back the received request.",
    version="1.0.0"
)

@app.get("/")
async def read_root():
    
    return {"message": "Welcome to the Echo API! Try /echo_query or /echo_body."}

@app.get("/echo_query/")
async def echo_query_parameters(
    
    message: str = Query(..., description="A message to echo back."),
    value: Optional[int] = Query(None, description="An optional integer value."),
    is_active: bool = Query(False, description="An optional boolean flag.")
):
 
    # Return a dictionary containing the received query parameters
    return {
        "received_request_type": "GET",
        "received_query_parameters": {
            "message": message,
            "value": value,
            "is_active": is_active
        }
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

