from __future__ import annotations

from re import DOTALL, sub
from typing import final

from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


@final
class ContentGenerationAgent:
    __slots__ = (
        "model",
        "prompt",
        "chain",
    )

    def __init__(self, model: OllamaLLM) -> None:
        self.model = model
        self.prompt = PromptTemplate(
            input_variables=["outline", "research_summary"],
            template=(
                "Using the following outline:\n\n{outline}\n\n"
                "and the research summary:\n\n{research_summary}\n\n"
                "Generate a high-quality, SEO-optimized blog post of approximately 2000 words as HTML. "
                "Ensure the content is engaging, informative, and well-structured with appropriate headings and subheadings."
            ),
        )
        self.chain = self.prompt | self.model

    def run(self, outline: str, research_summary: str) -> str:
        return sub(
            r"<think>.*?</think>",
            "",
            self.chain.invoke(
                {
                    "outline": outline,
                    "research_summary": research_summary,
                }
            ),
            flags=DOTALL,
        )
