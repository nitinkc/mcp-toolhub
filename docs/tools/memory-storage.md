# Memory & Storage Tools

## Notes — `add_note` & `read_notes` { #notes }

Simple file-based note taking. Demonstrates **file I/O** in MCP tools.

```python
@mcp.tool()
def add_note(content: str) -> str: ...

@mcp.tool()
def read_notes() -> str: ...
```

**Example prompts**

```
Add a note: "MCP uses stdio transport by default"
Save this as a note: "Always unset VIRTUAL_ENV before running uv"
Read all my notes
What notes have I saved?
```

---

## Member Database — `add_person_to_member_database` { #members }

Demonstrates **structured Pydantic input** — Claude constructs a typed `Person` object from natural language.

```python
class Person(BaseModel):
    first_name: str
    last_name: str
    years_of_experience: int
    previous_addresses: List[str]

@mcp.tool()
def add_person_to_member_database(person: Person) -> str: ...
```

**Example prompts**

```
Add Jane Smith to the member database — she has 7 years of experience
  and previously lived at 12 Oak Street and 45 Maple Avenue.

Log a new member: John Doe, 3 years experience, no previous addresses.

Add me to the database: first name Alex, last name Johnson,
  12 years experience, previously at 100 Main St, New York.
```

!!! info "Why this matters"
    This shows how MCP + Pydantic lets Claude turn free-form natural language into validated, structured data — no parsing code needed.

---

## Vector Memory — `save_memory` & `search_memory` { #vector-memory }

Persists knowledge to an **OpenAI vector store** and retrieves it semantically. Requires `OPENAI_API_KEY`.

```python
@mcp.tool()
def save_memory(memory: str) -> dict: ...

@mcp.tool()
def search_memory(query: str) -> dict: ...
```

**Example prompts**

```
Save this to memory: "The MCP ToolHub project uses FastMCP and uv for packaging"

Remember that: "Perplexity sonar-pro is the best model for web search in this server"

Search my memories for anything about MCP configuration

What do I know about web search setup?
```

!!! warning "Requires OpenAI API key"
    Set `OPENAI_API_KEY` in your `.env` file before using memory tools.

