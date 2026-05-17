# MCP ToolHub

> A learning-focused [Model Context Protocol](https://modelcontextprotocol.io) server that demonstrates every core MCP concept in one place: **Tools**, **Prompts**, and **Resources**.

---

## What's inside

| Category      | Examples                                                                                                                                                                                           |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Tools**     | `factorial_safe_forLLM`, `echo`, `add_note`, `read_notes`, `get_cryptocurrency_price`, `perform_web_search`, `capture_screenshot`, `add_person_to_member_database`, `save_memory`, `search_memory` |
| **Prompts**   | `analyze_topic`, `historical_report`, `explain_weather_concept`                                                                                                                                    |
| **Resources** | `inventory://overview`, `inventory://{id}/price`, `inventory://{name}/id`, `weather://overview`, `weather://{city}/statement`                                                                      |

---

## Quick start

### 1 – Clone & set up environment

```shell
cd mcp-toolhub
uv venv
source .venv/bin/activate
uv pip install -e .
```

### 2 – Configure API keys

```shell
cp .env.example .env
# Edit .env and fill in your keys
```

| Variable              | Purpose                                                                                               | Required?                            |
|:----------------------|:------------------------------------------------------------------------------------------------------|:-------------------------------------|
| `OPENAI_API_KEY`      | Memory tools (`save_memory`, `search_memory`), optional web-search fallback when provider is `openai` | Required for memory tools            |
| `PERPLEXITY_API_KEY`  | Optional web-search fallback when provider is `perplexity`                                            | Optional                             |
| `WEB_SEARCH_PROVIDER` | Web-search provider selector (`openai`, `perplexity`, or custom)                                      | No (default: `perplexity`)           |
| `WEB_SEARCH_API_KEY`  | Preferred API key for `perform_web_search`                                                            | Recommended                          |
| `WEB_SEARCH_BASE_URL` | Base URL for custom/OpenAI-compatible provider                                                        | Optional                             |
| `WEB_SEARCH_MODEL`    | Model name for web search                                                                             | Optional                             |
| `VECTOR_STORE_NAME`   | Name of the OpenAI vector store                                                                       | No (default: `MCP_ToolHub_Memories`) |
| `NOTES_FILE`          | Path for the local notes file                                                                         | No (default: `notes.txt`)            |
| `MEMBER_LOG_FILE`     | Path for the member log file                                                                          | No (default: `member_log.txt`)       |

### 3 – Test interactively (MCP Inspector)

```shell
mcp dev mcpserver/myMcpServer.py

unset VIRTUAL_ENV
uv run mcp dev mcpserver/myMcpServer.py 
```

---

## Install into Claude Desktop

```shell
mcp install mcpserver/myMcpServer.py 
```

OR

Add the following block to your Claude Desktop config file
(`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "mcp-toolhub": {
      "command": "uvx",
      "args": [
        "--from",
        "/absolute/path/to/mcp-toolhub",
        "mcp-toolhub"
      ],
      "env": {
        "OPENAI_API_KEY": "your_openai_api_key",
        "WEB_SEARCH_PROVIDER": "perplexity",
        "WEB_SEARCH_API_KEY": "your_perplexity_api_key"
      }
    }
  }
}
```

Or install directly from a Git repository:

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
        "OPENAI_API_KEY": "your_openai_api_key",
        "WEB_SEARCH_PROVIDER": "perplexity",
        "WEB_SEARCH_API_KEY": "your_perplexity_api_key"
      }
    }
  }
}
```

### Local and GitHub side-by-side (recommended for comparison)

```shell
 uvx --from git+https://github.com/nitinkc/mcp-toolhub.git mcp-toolhub
```

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
        "OPENAI_API_KEY": "your_openai_api_key",
        "WEB_SEARCH_PROVIDER": "perplexity",
        "WEB_SEARCH_API_KEY": "your_perplexity_api_key"
      }
    }
  }
}
```

Use `mcp-toolhub-local` while developing locally, and `mcp-toolhub-github` when sharing a portable config.

---

## Install into VS Code (GitHub Copilot)

Add to your VS Code `settings.json`:

```json
{
  "github.copilot.chat.mcpServers": {
    "mcp-toolhub": {
      "command": "uvx",
      "args": [
        "--from",
        "/absolute/path/to/mcp-toolhub",
        "mcp-toolhub"
      ],
      "env": {
        "OPENAI_API_KEY": "your_openai_api_key",
        "WEB_SEARCH_PROVIDER": "perplexity",
        "WEB_SEARCH_API_KEY": "your_perplexity_api_key"
      }
    }
  }
}
```

---

## Learning guide

`mcpserver/deployment.py` is structured into three clearly labelled sections:

1. **SECTION 1 – TOOLS** — from a simple `factorial_safe_forLLM` function up to structured Pydantic inputs, binary image returns, external API calls, and OpenAI vector store integration.
2. **SECTION 2 – PROMPTS** — reusable message templates with typed parameters.
3. **SECTION 3 – RESOURCES** — read-only URI-addressable data (static and parameterised).

Every function has a Google-style docstring so the LLM can understand and invoke it correctly.

---

## Documentation (MkDocs)

### 1) Install docs dependencies

```shell
# from project root
source .venv/bin/activate
uv pip install -r requirements-docs.txt
```

### 2) Run docs locally (hot reload)

```shell
mkdocs serve
```

Local testing URLs:

- http://127.0.0.1:8000/
- http://localhost:8000/

### 3) Build docs locally

```shell
mkdocs build --clean
```

Built static site output:

- `site/`

### 4) Optional: deploy docs to GitHub Pages

```shell
mkdocs gh-deploy --force
```

Typical Pages URL after deploy:

- `https://nitinkc.github.io/mcp-toolhub/`
