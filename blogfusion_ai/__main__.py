from __future__ import annotations

from langchain_ollama import OllamaLLM

from blogfusion_ai import (
    ContentGenerationAgent,
    ContentPlanningAgent,
    ResearchAgent,
    ReviewAgent,
    SeoOptimizationAgent,
)


def main() -> None:
    model = OllamaLLM(model="deepseek-r1")
    research_agent = ResearchAgent(model)
    planning_agent = ContentPlanningAgent(model)
    generation_agent = ContentGenerationAgent(model)
    seo_agent = SeoOptimizationAgent(model)
    review_agent = ReviewAgent(model)

    print("Running Research Agent...")
    research_summary = research_agent.run()
    print("Research Summary:\n", research_summary)

    print("\nRunning Content Planning Agent...")
    outline = planning_agent.run(research_summary)
    print("Outline:\n", outline)

    print("\nRunning Content Generation Agent...")
    blog_post = generation_agent.run(outline, research_summary)
    print("Generated Blog Post:\n", blog_post)

    print("\nRunning SEO Optimization Agent...")
    seo_blog_post = seo_agent.run(blog_post)
    print("SEO Optimized Blog Post:\n", seo_blog_post)

    print("\nRunning Review Agent...")
    final_blog_post = review_agent.run(seo_blog_post)
    print("Final Blog Post:\n", final_blog_post)

    with open("final_blog_post.md", "w", encoding="utf-8") as f:
        f.write(final_blog_post)

    print("\nFinal blog post saved to 'final_blog_post.md'.")


if __name__ == "__main__":
    main()
