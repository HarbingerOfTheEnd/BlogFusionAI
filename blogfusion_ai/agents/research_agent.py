from __future__ import annotations

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

    def __init__(self, model: OllamaLLM, topic: str) -> None:
        self.model = model
        self.prompt = PromptTemplate(
            input_variables=[],
            template=(
                f"IGiven topic: {topic}\nProvide a detailed summary including current statistics, "
                "challenges, emerging trends, and any relevant background information. "
                "Present your response in a clear and comprehensive manner."
            ),
        )
        self.chain = self.prompt | self.model

    def run(self) -> str:
        return self.chain.invoke({})
