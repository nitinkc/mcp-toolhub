# Built-in Prompts

## `analyze_topic`

Returns a prompt instructing Claude to produce a **deep, structured analysis** of any topic.

```python
@mcp.prompt()
def analyze_topic(topic: str) -> str:
    return f"Please do a detailed, structured analysis of the following topic: {topic}"
```

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `topic` | `str` | Any subject to analyse |

**Example invocations**

```
Use the analyze_topic prompt for: "The rise of agentic AI systems"
Analyze the topic of "Model Context Protocol" using the MCP prompt
Run analyze_topic on "Zero-knowledge proofs"
```

---

## `historical_report`

Generates a **structured history report** with introduction, main body, conclusion, and a key-events timeline.

```python
@mcp.prompt()
def historical_report(topic: str, number_of_paragraphs: int = 3) -> str:
```

**Parameters**

| Name | Type | Default | Description |
|:-----|:-----|:--------|:------------|
| `topic` | `str` | — | Historical subject |
| `number_of_paragraphs` | `int` | `3` | Main body paragraph count |

**Example invocations**

```
Use the historical_report prompt for "The Space Race" with 5 paragraphs
Generate a historical report on "The invention of the Internet"
Historical report on "Artificial Intelligence" — 2 paragraphs please
```

---

## `explain_weather_concept`

Explains a meteorological concept in **plain language** — what it is, how it forms, its effects, and a real-world example.

```python
@mcp.prompt()
def explain_weather_concept(concept: str) -> str:
```

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `concept` | `str` | Weather or meteorological concept |

**Example invocations**

```
Explain the weather concept "La Niña" using the MCP prompt
Use explain_weather_concept for "polar vortex"
What is a "derecho"? Use the weather concept prompt.
```

