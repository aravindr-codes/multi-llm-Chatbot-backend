import os
from dotenv import load_dotenv

load_dotenv()


def _provider_for_model(model_name: str) -> str:
    model_key = model_name.lower()
    if model_key.startswith("claude"):
        return "anthropic"
    return "openai"


def _require_env(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Missing required environment variable: {var_name}")
    return value


def _openai_response(message: str, model_name: str) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=_require_env("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": message}],
        temperature=0.7,
        max_tokens=256,
    )
    return response.choices[0].message.content


def _anthropic_response(message: str, model_name: str) -> str:
    try:
        import anthropic
    except Exception as exc:
        raise ImportError(
            "Anthropic SDK is required for Claude models. Install `anthropic`."
        ) from exc

    client = anthropic.Anthropic(api_key=_require_env("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model=model_name,
        max_tokens=256,
        temperature=0.7,
        messages=[{"role": "user", "content": message}],
    )
    return response.content[0].text


def get_llm_response(message: str, model_name: str) -> str:
    try:
        provider = _provider_for_model(model_name)
        if provider == "anthropic":
            return _anthropic_response(message, model_name)
        return _openai_response(message, model_name)
    except Exception as e:
        return f"Error calling LLM: {str(e)}"
