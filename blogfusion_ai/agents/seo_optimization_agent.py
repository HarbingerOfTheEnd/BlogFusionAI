from __future__ import annotations

from re import DOTALL, sub
from typing import final

from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


@final
class SeoOptimizationAgent:
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
                "Optimize the following blog post for SEO. Improve keyword usage, meta descriptions, "
                "and overall content structure. Ensure headings and subheadings are well defined.\n\nBlog post:\n{blog_post}"
            ),
        )
        self.chain = self.prompt | self.model

    def run(self, blog_post: str) -> str:
        return sub(
            r"<think.*?</think>",
            "",
            self.chain.invoke({"blog_post": blog_post}),
            flags=DOTALL,
        )
