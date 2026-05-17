# Data & API Tools

## `get_cryptocurrency_price` { #crypto }

Fetches the current USD price of any cryptocurrency via the **CoinGecko** free API — no API key required.

```python
@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """Fetch the current USD price of a cryptocurrency via CoinGecko."""
```

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `crypto` | `str` | CoinGecko coin ID, e.g. `bitcoin`, `ethereum`, `solana` |

**Example prompts**

```
What's the current price of Bitcoin?
Get me Ethereum and Solana prices
Compare the prices of bitcoin, ethereum, and dogecoin
```

!!! tip "Find coin IDs"
    Use [coingecko.com/en/coins](https://www.coingecko.com/en/coins) to find the exact ID for any coin.

---

## `perform_web_search` { #web-search }

Searches the web using a configurable LLM provider (Perplexity, OpenAI, or any OpenAI-compatible API).

```python
@mcp.tool()
def perform_web_search(query: str) -> str:
    """Search the web using a configurable LLM provider."""
```

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `query` | `str` | Any question or search query |

**Provider configuration**

| `WEB_SEARCH_PROVIDER` | Default model | Notes |
|:----------------------|:-------------|:------|
| `perplexity` | `sonar-pro` | Requires `PERPLEXITY_API_KEY` |
| `openai` | `gpt-4o-mini` | Requires `OPENAI_API_KEY` |
| custom | Set via `WEB_SEARCH_MODEL` | Set `WEB_SEARCH_BASE_URL` too |

**Example prompts**

```
Search the web: what are the latest developments in MCP (Model Context Protocol)?
Use web search to find the current top 3 programming languages in 2025
Search for recent news about OpenAI
```

