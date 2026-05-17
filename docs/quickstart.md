# Quick Start

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager
- API keys for OpenAI and/or Perplexity (optional but recommended)

---

## 1 – Clone & Set Up

```shell
git clone https://github.com/YOUR_USERNAME/mcp-toolhub.git
cd mcp-toolhub
uv venv
source .venv/bin/activate
uv pip install -e .
```

---

## 2 – Configure API Keys

```shell
cp .env.example .env
# Edit .env and fill in your keys
```

| Variable | Purpose | Required? |
|:---------|:--------|:---------|
| `OPENAI_API_KEY` | Memory tools (`save_memory`, `search_memory`) | ✅ For memory tools |
| `PERPLEXITY_API_KEY` | Web search via Perplexity | Optional |
| `WEB_SEARCH_PROVIDER` | `openai`, `perplexity`, or custom | No (default: `perplexity`) |
| `WEB_SEARCH_API_KEY` | Preferred key for web search | Recommended |
| `WEB_SEARCH_BASE_URL` | Base URL for custom provider | Optional |
| `WEB_SEARCH_MODEL` | Model name for web search | Optional |
| `VECTOR_STORE_NAME` | OpenAI vector store name | No (default: `MCP_ToolHub_Memories`) |
| `NOTES_FILE` | Path for notes file | No (default: `notes.txt`) |
| `MEMBER_LOG_FILE` | Path for member log | No (default: `member_log.txt`) |

---

## 3 – Run Interactively (MCP Inspector)

```shell
unset VIRTUAL_ENV
uv run mcp dev mcpserver/myMcpServer.py
```

Open the Inspector UI at **http://localhost:5173** to test all tools, prompts, and resources visually.

---

## 4 – Install into Claude Desktop

=== "Local path"

    ```json
    {
      "mcpServers": {
        "mcp-toolhub": {
          "command": "uvx",
          "args": ["--from", "/absolute/path/to/mcp-toolhub", "mcp-toolhub"],
          "env": {
            "OPENAI_API_KEY": "sk-...",
            "WEB_SEARCH_PROVIDER": "perplexity",
            "WEB_SEARCH_API_KEY": "pplx-..."
          }
        }
      }
    }
    ```

=== "From GitHub"

    ```json
    {
      "mcpServers": {
        "mcp-toolhub": {
          "command": "uvx",
          "args": [
            "--from",
            "git+https://github.com/YOUR_USERNAME/mcp-toolhub.git",
            "mcp-toolhub"
          ],
          "env": {
            "OPENAI_API_KEY": "sk-...",
            "WEB_SEARCH_API_KEY": "pplx-..."
          }
        }
      }
    }
    ```

```shell
 uvx --from git+https://github.com/nitinkc/mcp-toolhub.git mcp-toolhub
```

=== "Side-by-side (local + GitHub)"

    ```json
    {
      "mcpServers": {
        "mcp-toolhub-local": {
          "command": "/absolute/path/to/mcp-toolhub/.venv/bin/mcp",
          "args": [
            "run",
            "/absolute/path/to/mcp-toolhub/mcpserver/myMcpServer.py"
          ],
          "env": {
            "VIRTUAL_ENV": ""
          }
        },
        "mcp-toolhub-github": {
          "command": "uvx",
          "args": [
            "--from",
            "git+https://github.com/nitinkc/mcp-toolhub.git",
            "mcp-toolhub"
          ],
          "env": {
            "OPENAI_API_KEY": "sk-...",
            "WEB_SEARCH_PROVIDER": "perplexity",
            "WEB_SEARCH_API_KEY": "pplx-..."
          }
        }
      }
    }
    ```

!!! tip "Restart Claude Desktop after editing the config"
    Claude Desktop reads the config file on startup — always restart after making changes.

---

## 5 – Try It!

Once installed, head to [💬 Chat Prompt Recipes](prompts-library/index.md) for copy-paste prompts that test every feature.

