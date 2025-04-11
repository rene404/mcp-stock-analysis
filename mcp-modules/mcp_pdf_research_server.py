# mcp_pdf_research_server.py
"""
An MCP node that returns mock insights from PDFs for a given ticker.
Replace with real PDF parsing logic if needed.
"""

from mcp import Node, Payload, Param

node = Node()

@node.handle("pdf-research", param=Param("ticker", str))
def pdf_research(payload: Payload):
    ticker = payload.payload_data["ticker"]
    # In production: fetch/parse real PDF data, e.g. from SEC EDGAR
    # For demo: Return static text
    return {
        "pdf_summary": f"PDF insights for {ticker}: Earnings up, strong forward guidance."
    }

if __name__ == "__main__":
    node.run(host="0.0.0.0", port=8002)
