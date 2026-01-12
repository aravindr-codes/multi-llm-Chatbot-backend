# Backend API

## Run the server
From the `backend` directory:

```
python -m uvicorn main:app --reload
```

If you prefer the `uv` runner:

```
uv run uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Curl commands

### Health/hello
```
curl http://localhost:8000/
```

### Chat completion
```
curl -X POST http://localhost:8000/chat_completion \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"Tell me a joke\",\"model_name\":\"gpt-4\"}"
```

### Echo body
```
curl -X POST http://localhost:8000/echo_body/ \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Alice\",\"age\":30,\"city\":\"New York\"}"
```
