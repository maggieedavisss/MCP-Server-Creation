from typing import Any
from pathlib import Path
import httpx
from mcp.server.fastmcp import FastMCP

# -------------------- Initialize MCP Server -------------------- #
mcp = FastMCP("news")

# -------------------- Constants -------------------- #
NEWS_API_BASE = "https://newsapi.org/v2"
USER_AGENT = "news-app/1.0"
API_KEY = "ab326ef338ff44b5b5d913aebd49f1eb"  

# -------------------- Paths -------------------- #
PROMPT_PATH = Path("prompts/tag.md")
RESOURCE_PATH = Path("resources/draft_example.md")

# -------------------- MCP Prompt -------------------- #
@mcp.prompt()
def tag_prompt() -> str:
    """TAG instructions for drafting news reports"""
    if PROMPT_PATH.exists():
        return PROMPT_PATH.read_text(encoding="utf-8")
    return "You are TAG, an intelligent virtual assistant that writes professional news reports."

# -------------------- MCP Resource -------------------- #
@mcp.resource("news-examples://draft-example")
def draft_example() -> str:
    """Example draft news report in markdown format"""
    if RESOURCE_PATH.exists():
        return RESOURCE_PATH.read_text(encoding="utf-8")
    return "# Example Draft\n\nNo resource file found."

# -------------------- MCP Tool: Draft News Report -------------------- #
@mcp.tool()
async def generate_news_report(topic: str) -> str:
    """
    Generate a news report draft using the TAG prompt + example resource.
    Returns the text to Claude, no files.
    """
    instructions = tag_prompt()
    example_draft = draft_example()

    generated_text = (
        f"{instructions}\n\n"
        f"Example draft to follow:\n{example_draft}\n\n"
        f"Topic: {topic}\n\n"
        f"TAG, please write a full draft news report based on the topic."
    )

    return generated_text

# -------------------- News API Helpers -------------------- #
async def make_news_request(url: str, params: dict = None) -> dict[str, Any] | None:
    """Make a request to the NewsAPI with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
    }
    if params is None:
        params = {}
    params["apiKey"] = API_KEY  # Add the API key to the parameters
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_news_article(article: dict) -> str:
    """Format a news article into a readable string."""
    return f"""
Title: {article.get('title', 'Unknown')}
Source: {article.get('source', {}).get('name', 'Unknown')}
Published: {article.get('publishedAt', 'Unknown')}
Description: {article.get('description', 'No description available')}
URL: {article.get('url', 'No link available')}
"""

# -------------------- MCP Tools: News API -------------------- #
@mcp.tool()
async def get_top_headlines(country: str = "us", category: str = "") -> str:
    """Get top news headlines for a specific country."""
    url = f"{NEWS_API_BASE}/top-headlines"
    params = {"country": country, "category": category} if category else {"country": country}
    
    data = await make_news_request(url, params=params)

    if not data or "articles" not in data:
        return "Unable to fetch news headlines or no articles found."

    articles = [format_news_article(article) for article in data["articles"]]
    return "\n---\n".join(articles)

@mcp.tool()
async def search_news(query: str, language: str = "en") -> str:
    """Search for news articles based on a query string."""
    url = f"{NEWS_API_BASE}/everything"
    params = {"q": query, "language": language}
    
    data = await make_news_request(url, params=params)

    if not data or "articles" not in data:
        return "No results found or error fetching data."

    articles = [format_news_article(article) for article in data["articles"]]
    return "\n---\n".join(articles)

@mcp.tool()
async def get_news_alerts(country: str = "us") -> str:
    """Get latest news alerts for a specific country."""
    url = f"{NEWS_API_BASE}/top-headlines"
    params = {"country": country, "category": "general"}

    data = await make_news_request(url, params=params)

    if not data or "articles" not in data:
        return "Unable to fetch news alerts."

    alerts = [format_news_article(article) for article in data["articles"]]
    return "\n---\n".join(alerts)

# -------------------- Run MCP Server -------------------- #
if __name__ == "__main__":
    mcp.run(transport='stdio')
