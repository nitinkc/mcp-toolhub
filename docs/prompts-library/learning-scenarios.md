# 🎓 Learning Scenarios

These creative scenarios are designed to **teach MCP concepts** by doing — perfect for workshops, demos, or self-study.

---

## Scenario 1: "The Three Pillars" Tour

*Objective: Experience Tools, Prompts, and Resources as distinct concepts.*

```
I want to understand the three MCP primitives by experiencing each one.

TOOLS — things that DO:
→ Use the echo tool to confirm the server is alive
→ Get the Bitcoin price (external API call)
→ Add a note: "Tools execute actions and return results"

PROMPTS — things that SHAPE:
→ Use analyze_topic: "What makes a good software API?"
→ Use historical_report: "REST APIs" with 2 paragraphs

RESOURCES — things that EXPOSE DATA:
→ Read the inventory overview resource
→ Get the price of item 789
→ Get the weather statement for "San Francisco"

After each section, explain in one sentence how that primitive differs from the others.
```

---

## Scenario 2: The Personal Assistant Setup

*Objective: Build a useful personal assistant in one session using all MCP features.*

```
Let's set up a personal assistant together using MCP ToolHub.

1. Save to memory: my name is [YOUR NAME] and I'm learning about MCP
2. Add a note: "Personal assistant setup — [today's date]"
3. Search the web for: "top 5 productivity tips for developers"
4. Save the best tip to memory
5. Add the tip as a note too
6. Read all notes to confirm everything was saved
7. Search memory for "productivity" to verify the tip was indexed

Now I have a persistent, searchable knowledge base!
```

---

## Scenario 3: Structured Data Mastery

*Objective: Understand Pydantic-validated tool inputs.*

```
I want to build a small member directory. Please add these 5 people:

1. Sarah Connor, 15 years experience, previously: ["Los Angeles", "Denver"]
2. John Doe, 3 years experience, no previous addresses  
3. Ada Lovelace, 20 years experience, previously: ["London", "Birmingham", "Manchester"]
4. Alan Turing, 12 years experience, previously: ["London"]
5. Grace Hopper, 18 years experience, previously: ["New York", "Washington DC"]

After adding all five, explain what a Pydantic BaseModel is and why it's useful for tool inputs.
```

---

## Scenario 4: The Chain Reaction

*Objective: Chain 5+ tools together in a single logical workflow.*

```
Execute this chain without stopping:

1. echo "Chain reaction starting..."
2. Get Ethereum price
3. Search web: "Ethereum use cases beyond currency"  
4. Save to memory: "Ethereum insight: [summarize web search result in 10 words]"
5. Add a note with the Ethereum price and the date
6. Use analyze_topic: "Ethereum and smart contracts"
7. Search memory for "Ethereum"
8. echo "Chain reaction complete!"

Show all results inline and note which tools were called.
```

---

## Scenario 5: MCP Concepts Quiz

*Objective: Use Claude as a quizmaster that validates answers by calling MCP tools.*

```
Quiz me on MCP ToolHub! For each question, use the relevant MCP tool to verify the answer.

Q1: Ask me: "What does the echo tool return?"
  → Use echo to verify my answer

Q2: Ask me: "What's 5 factorial?" 
  → Use factorial tool to check

Q3: Ask me: "What's in the inventory?"
  → Use the inventory resource to reveal the answer

Q4: Ask me: "Name one cryptocurrency you can look up"
  → Fetch that coin's price to confirm it exists

Q5: Ask me: "What are the three MCP prompt names?"
  → Try to call each one I name

Score me at the end — 1 point per correct answer.
```

---

## Scenario 6: The Knowledge Snowball

*Objective: Demonstrate how memory compounds over time.*

```
We're going to build a knowledge snowball about "Python packaging".

Round 1:
- Search web: "what is pyproject.toml?"
- Save key insight to memory
- Add a note: "Learned about pyproject.toml"

Round 2:
- Search web: "what is uv package manager?"
- Save key insight to memory  
- Search memory for "python" to see what we've accumulated

Round 3:
- Search web: "uv vs pip vs poetry comparison"
- Save to memory
- Search memory: "package manager" — how many relevant results now?

Final: Read all notes. Search memory for "packaging". Summarize everything we've learned.
```

---

## Scenario 7: The Socratic MCP Teacher

*Objective: Use MCP prompts to teach MCP itself — meta!*

```
Be my MCP teacher. Use the MCP prompts to teach me about MCP.

Step 1: Use analyze_topic: "Model Context Protocol"
Step 2: Use historical_report: "AI assistant tool-use" with 2 paragraphs  
Step 3: Use explain_weather_concept: "El Niño" — then explain how MCP Prompts
        are like "weather patterns" that shape how AI responds

Then save to memory: "MCP tutorial complete — understood Tools, Prompts, Resources"
And add a note: "MCP ToolHub learning journey — Day 1 complete ✓"
```

---

!!! quote "The real lesson"
    The most powerful MCP pattern isn't any single tool — it's **chaining** tools, prompts, and resources together to create workflows that none of them could accomplish alone.

