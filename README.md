# BlogFusion AI - A Multi-Agent Blog Post Generator

## Overview

This project implements a Python-based multi-agent system that generates a high-quality, SEO-optimized blog post (approximately 2000 words) on a trending HR-related topic. The system uses LangChain for building LLM chains and the Ollama "deepseek-r1" model as the language model.

## System Architecture

The system is composed of the following agents:

- **Research Agent:** Identifies trending HR topics and gathers detailed research data.
- **Content Planning Agent:** Creates a structured outline for the blog post based on the research.
- **Content Generation Agent:** Produces the full blog post using the outline and research summary.
- **SEO Optimization Agent:** Enhances the blog post for SEO by refining keywords and content structure.
- **Review Agent:** Proofreads and polishes the final blog content.

## Agent Workflow

1. **Research Agent:** Executes first to determine a trending HR topic and compile relevant details.
2. **Content Planning Agent:** Uses the research output to create a detailed blog outline.
3. **Content Generation Agent:** Generates the draft blog post.
4. **SEO Optimization Agent:** Refines the draft for optimal SEO performance.
5. **Review Agent:** Finalizes the content through proofreading and editing.

## Tools and Frameworks Used

- **LangChain:** For creating LLM chains and managing prompt templates.
- **Ollama llama3.2:** As the language model backend.
- **Python:** For scripting and orchestration.

## Setup and Installation

1. Clone the repository:

    ```bash
    git clone <repository_link>
    cd <repository_folder>
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    uv sync  # Pip: pip install -r requirements.txt
    ```

4. Run the main script:

    ```bash
    python -m blogfusion_ai
    ```

## Final Blog Post

The final SEO-optimized blog post is saved as `final_blog_post.md`.

## Implementation Discussion

The design focuses on modularity and separation of concerns. Each agent is responsible for a distinct step in the blog post creation workflow. By using LangChain and a powerful LLM backend, the system ensures high-quality content and adheres to SEO best practices.
