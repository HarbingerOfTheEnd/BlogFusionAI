from __future__ import annotations

from typing import final

from langchain.chains.llm import LLMChain
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
        self.chain = LLMChain(llm=model, prompt=self.prompt)

    def generate_response(self) -> str:
        return self.chain.run()
