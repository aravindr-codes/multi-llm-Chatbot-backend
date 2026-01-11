from unittest.mock import patch

import llm_client


def test_routes_openai_by_default():
    with patch("llm_client._openai_response", return_value="ok-openai") as mock_openai:
        response = llm_client.get_llm_response("hi", "gpt-4")

    assert response == "ok-openai"
    mock_openai.assert_called_once_with("hi", "gpt-4")


def test_routes_anthropic_for_claude():
    with patch("llm_client._anthropic_response", return_value="ok-claude") as mock_anthropic:
        response = llm_client.get_llm_response("hi", "claude-3-sonnet")

    assert response == "ok-claude"
    mock_anthropic.assert_called_once_with("hi", "claude-3-sonnet")


def test_routes_google_for_gemini():
    with patch("llm_client._google_response", return_value="ok-gemini") as mock_google:
        response = llm_client.get_llm_response("hi", "gemini-1.5-pro")

    assert response == "ok-gemini"
    mock_google.assert_called_once_with("hi", "gemini-1.5-pro")
