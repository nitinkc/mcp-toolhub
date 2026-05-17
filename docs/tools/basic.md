# Basic Tools

## `factorial_safe_forLLM` { #factorial }

Returns `n!` with friendly error handling for invalid input.

```python
@mcp.tool()
def factorial_safe_forLLM(n: int) -> str:
    """Return n! with friendly error handling for invalid input."""
```

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `n` | `int` | Non-negative integer |

**Example prompts**

```
What is 10 factorial?
Calculate 0!
What happens if I ask for factorial of -5?
```

---

## `echo` { #echo }

Echoes back any message. The simplest possible MCP tool — perfect for verifying the server is connected.

```python
@mcp.tool()
def echo(message: str) -> str:
    """Echo back the message you send."""
```

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `message` | `str` | Any string |

**Example prompts**

```
Echo "Hello MCP World" back to me
Use the echo tool to confirm the server is running
```

!!! note "Why echo?"
    The `echo` tool is the "Hello World" of MCP — it proves the transport layer, server registration, and tool dispatch are all working before you touch anything more complex.

