from __future__ import annotations

from re import DOTALL, sub
from typing import final

from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


@final
class ReviewAgent:
    __slots__ = (
        "model",
        "prompt",
        "chain",
    )

    def __init__(self, model: OllamaLLM) -> None:
        self.model = model
        self.prompt = PromptTemplate(
            input_variables=["blog_post"],
            template=(
                "Proofread and improve the following blog post. Correct any grammatical errors, enhance readability, "
                "and polish the content quality overall. Return the improved blog post as HTML.\n\nBlog post:\n{blog_post}"
            ),
        )
        self.chain = self.prompt | self.model

    def run(self, blog_post: str) -> str:
        return sub(
            r"<think>.*?</think>",
            "",
            self.chain.invoke({"blog_post": blog_post}),
            flags=DOTALL,
        )
