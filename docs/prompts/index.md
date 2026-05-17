# Prompts Overview

MCP **Prompts** are reusable message templates that guide the LLM's behaviour. Unlike tools (which *do* things), prompts *shape how Claude thinks and responds*.

---

## How Prompts Differ from Tools

| | Tools | Prompts |
|:--|:------|:--------|
| **Purpose** | Take action, return data | Shape LLM response style |
| **Returns** | Any Python type | A string message template |
| **Invoked by** | LLM autonomously | User or client explicitly |
| **Side effects** | Yes (files, APIs, etc.) | No |

---

## Available Prompts

| Prompt | Parameters | What it does |
|:-------|:-----------|:-------------|
| `analyze_topic` | `topic: str` | Deep structured analysis of any subject |
| `historical_report` | `topic: str`, `number_of_paragraphs: int` | Structured history report with timeline |
| `explain_weather_concept` | `concept: str` | Plain-language meteorology explanation |

---

## How to Use Prompts in Claude

In the MCP Inspector, select the **Prompts** tab and choose a prompt.  
In Claude Desktop, you can invoke them via the **slash command** or by asking Claude directly:

```
Use the historical_report prompt for "The Internet" with 4 paragraphs

Apply the analyze_topic prompt to "Large Language Models"

Use explain_weather_concept for "El Niño"
```

[:octicons-arrow-right-24: See all built-in prompts](builtin.md)

