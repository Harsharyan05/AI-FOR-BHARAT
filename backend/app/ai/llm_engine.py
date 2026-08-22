"""
LLM Engine

Provides a unified interface for interacting with
multiple Large Language Model providers.

Supported Providers
-------------------
- Ollama
- Gemini
- OpenAI

Author: Harsh Aryan
Project: Cognisys
"""

import os
from abc import ABC, abstractmethod

import ollama
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError
from openai import OpenAI

load_dotenv()


# ==========================================================
# Base LLM
# ==========================================================

class BaseLLM(ABC):
    """
    Base interface for every LLM provider.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        pass


# ==========================================================
# Ollama Provider
# ==========================================================

class OllamaLLM(BaseLLM):
    """
    Local Ollama provider.
    """

    def __init__(
        self,
        model_name: str | None = None,
    ):

        self.model_name = (
            model_name
            or os.getenv(
                "LLM_MODEL",
                "llama3.1:8b",
            )
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        try:

            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            return response["message"]["content"]

        except Exception as error:

            return f"Ollama Error:\n{error}"


# ==========================================================
# Gemini Provider
# ==========================================================

class GeminiLLM(BaseLLM):

    def __init__(
        self,
        model_name: str | None = None,
    ):

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model_name = (
            model_name
            or os.getenv(
                "LLM_MODEL",
                "gemini-3.5-flash",
            )
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        try:

            response = (
                self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                )
            )

            return response.text

        except ClientError as error:

            return f"Gemini Error:\n{error}"

        except Exception as error:

            return str(error)


# ==========================================================
# OpenAI Provider
# ==========================================================

class OpenAILLM(BaseLLM):

    def __init__(
        self,
        model_name: str | None = None,
    ):

        api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not found."
            )

        self.client = OpenAI(
            api_key=api_key
        )

        self.model_name = (
            model_name
            or os.getenv(
                "LLM_MODEL",
                "gpt-5.5",
            )
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        try:

            response = (
                self.client.responses.create(
                    model=self.model_name,
                    input=prompt,
                )
            )

            return response.output_text

        except Exception as error:

            return str(error)


# ==========================================================
# LLM Engine
# ==========================================================

class LLMEngine:
    """
    Provider-independent LLM Engine.
    """

    def __init__(self):

        provider = os.getenv(
            "LLM_PROVIDER",
            "ollama",
        ).lower()

        if provider == "ollama":

            self.client = OllamaLLM()

        elif provider == "gemini":

            self.client = GeminiLLM()

        elif provider == "openai":

            self.client = OpenAILLM()

        else:

            raise ValueError(
                f"Unsupported provider: {provider}"
            )

    def ask(
        self,
        prompt: str,
    ) -> str:

        return self.client.generate(
            prompt
        )