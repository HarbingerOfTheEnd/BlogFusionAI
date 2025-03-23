from __future__ import annotations

from re import DOTALL, sub
from typing import final

from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


@final
class ResearchAgent:
    __slots__ = (
        "model",
        "prompt",
        "chain",
    )

    def __init__(self, model: OllamaLLM) -> None:
        self.model = model
        self.prompt = PromptTemplate(
            input_variables=[],
            template=(
                "Identify a trending HR-related topic. Provide a detailed summary including current statistics, "
                "challenges, emerging trends, and any relevant background information. "
                "Present your response in a clear and comprehensive manner."
            ),
        )
        self.chain = self.prompt | self.model

    def run(self) -> str:
        return sub(
            r"<think>.*?</think>",
            "",
            self.chain.invoke({}),
            flags=DOTALL,
        )
