# mcp_stock_api_server.py
"""
An MCP node that returns mock or real stock data for a given ticker.
Replace the mock data below with a real API call if desired.
"""

from mcp import Node, Payload, Param

node = Node()

@node.handle("get-stock-data", param=Param("ticker", str))
def get_stock_data(payload: Payload):
    ticker = payload.payload_data["ticker"]
    # Return mock data; replace with real API call (e.g. Alpha Vantage, Yahoo Finance)
    return {
        "ticker": ticker,
        "price": 123.45,
        "volume": 1000000,
        "pe_ratio": 15.2,
        "day_change": "+2.34%"
    }

if __name__ == "__main__":
    node.run(host="0.0.0.0", port=8001)
