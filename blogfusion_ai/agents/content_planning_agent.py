from __future__ import annotations

from re import DOTALL, sub
from typing import final

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
                "Generate a detailed outline for a 2000-word SEO-optimized blog post as HTML. "
                "Include main headings, subheadings, and a logical content structure."
            ),
        )
        self.chain = self.prompt | self.model

    def run(self, research_summary: str) -> str:
        return sub(
            r"<think>.*?</think>",
            "",
            self.chain.invoke({"research_summary": research_summary}),
            flags=DOTALL,
        )
