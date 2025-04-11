# mcp-stock-analysis

curl -X POST http://localhost:8001/get-stock-data \
     -H "Content-Type: application/json" \
     -d '{"ticker": "TSLA"}'

curl -X POST http://localhost:8002/pdf-research \
     -H "Content-Type: application/json" \
     -d '{"ticker": "TSLA"}'

curl -X POST http://localhost:8003/scrape-news \
     -H "Content-Type: application/json" \
     -d '{"query": "Tesla"}'

curl -X POST http://localhost:8000/summarize \
     -H "Content-Type: application/json" \
     -d '{"text": "Some long text to summarize."}'