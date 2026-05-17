# 🧠 Memory Workflows

These prompts demonstrate **persistent AI memory** using OpenAI vector stores — one of the most powerful patterns in MCP.

!!! warning "Requires OpenAI API key"
    Set `OPENAI_API_KEY` in your `.env` before trying these.

---

## Pattern 1: Build a Knowledge Base

Save facts across multiple sessions, then retrieve them semantically.

**Step 1 — Fill the memory store:**
```
Please save the following facts to my memory store:
1. "MCP stands for Model Context Protocol, an open standard by Anthropic"
2. "FastMCP is a Python library that simplifies building MCP servers"
3. "MCP supports three primitives: Tools, Prompts, and Resources"
4. "MCP ToolHub uses pyautogui for screenshot capture"
5. "The MCP Inspector is a browser-based debugger at localhost:5173"
6. "Vector stores in OpenAI enable semantic search over stored text"

Confirm each one was saved.
```

**Step 2 — Retrieve by meaning (not keyword):**
```
Search my memory for anything about "debugging MCP"
```

```
What do I know about "Python libraries for AI servers"?
```

```
Search memory: "how to capture screen"
```

---

## Pattern 2: Session Notes

Use memory as persistent session notes that survive across conversations.

```
I'm starting a new learning session. Save to memory:
"Session 1 complete: installed MCP ToolHub, tested all tools, 
confirmed screenshot and memory tools working. 
Next: explore prompt templates and resource URIs."
```

In a future session:
```
What did I accomplish in my last MCP learning session? Search my memory.
```

---

## Pattern 3: Personal Knowledge Assistant

```
Save these personal preferences to memory:
- "I prefer Perplexity for web search over OpenAI"
- "My vector store is named MCP_ToolHub_Memories"
- "I always run uv with VIRTUAL_ENV unset"

Then search for "my preferences" to verify they're stored.
```

---

## Pattern 4: Research → Save → Recall

Combine web search with memory for a research workflow:

```
1. Search the web for: "latest MCP specification updates 2025"
2. Save a summary of the key points to memory
3. Then immediately search memory for "MCP specification" to verify it saved
```

---

## Pattern 5: Memory + Analysis

```
Search my memory for everything saved about MCP.
Then use the analyze_topic prompt to do a structured analysis of
"Model Context Protocol" based on what you found.
```

---

!!! tip "Why vector memory matters"
    Unlike a notes file (exact text lookup), vector memory enables **semantic search** — you can ask "what do I know about debugging?" and it finds relevant stored facts even if they don't contain the word "debugging".

