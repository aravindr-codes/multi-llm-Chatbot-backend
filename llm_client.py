import openai

def get_llm_response(message: str, model_name: str) -> str:
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message["content"]
