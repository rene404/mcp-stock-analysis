# mcp_web_scraper_server.py
"""
An MCP node that scrapes or fakes news headlines for a given company/query.
Replace with real scraping logic if needed.
"""

from mcp import Node, Payload, Param

node = Node()

@node.handle("scrape-news", param=Param("query", str))
def scrape_news(payload: Payload):
    query = payload.payload_data["query"]
    # In production: use requests + BeautifulSoup to scrape real news
    # For demo: Return static headlines
    headlines = [
        f"{query} announces new product launch",
        f"Analysts forecast bullish outlook for {query}",
        f"{query} sees 10% surge in user adoption"
    ]
    return {"headlines": headlines}

if __name__ == "__main__":
    node.run(host="0.0.0.0", port=8003)
