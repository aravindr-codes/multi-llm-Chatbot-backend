import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_llm_response(message: str, model_name: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "user", "content": message}],
            temperature=0.7,
            max_tokens=256
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error calling LLM: {str(e)}"