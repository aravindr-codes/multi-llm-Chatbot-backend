import unittest
from unittest.mock import patch

import llm_client


class TestLlmClientRouting(unittest.TestCase):
    @patch("llm_client._openai_response", return_value="ok-openai")
    def test_routes_openai_by_default(self, mock_openai):
        response = llm_client.get_llm_response("hi", "gpt-4")

        self.assertEqual(response, "ok-openai")
        mock_openai.assert_called_once_with("hi", "gpt-4")

    @patch("llm_client._anthropic_response", return_value="ok-claude")
    def test_routes_anthropic_for_claude(self, mock_anthropic):
        response = llm_client.get_llm_response("hi", "claude-3-sonnet")

        self.assertEqual(response, "ok-claude")
        mock_anthropic.assert_called_once_with("hi", "claude-3-sonnet")

    @patch("llm_client._google_response", return_value="ok-gemini")
    def test_routes_google_for_gemini(self, mock_google):
        response = llm_client.get_llm_response("hi", "gemini-1.5-pro")

        self.assertEqual(response, "ok-gemini")
        mock_google.assert_called_once_with("hi", "gemini-1.5-pro")


if __name__ == "__main__":
    unittest.main()
