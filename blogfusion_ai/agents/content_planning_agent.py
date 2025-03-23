from __future__ import annotations

from typing import final

from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


@final
class ContentPlanningAgent:
    __slots__ = (
        "model",
        "prompt",
        "chain",
    )

    def __init__(self, model: OllamaLLM) -> None:
        self.model = model
        self.prompt = PromptTemplate(
            input_variables=["research_summary"],
            template=(
                "Based on the following research summary:\n\n{research_summary}\n\n"
                "Generate a detailed outline for a 2000-word SEO-optimized blog post. "
                "Include main headings, subheadings, and a logical content structure."
            ),
        )
        self.chain = LLMChain(llm=self.model, prompt=self.prompt)

    def run(self, research_summary: str) -> None:
        return self.chain.run({"research_summary": research_summary})
