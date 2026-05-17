# 🧪 Test All Tools

Run these prompts to verify every tool is working correctly. Great for after a fresh install or when debugging.

---

## The Full Gauntlet

Paste this entire block into Claude for a complete end-to-end test:

```
Let's test every tool in MCP ToolHub one by one. Please:

1. Echo back "All systems go"
2. Calculate 7 factorial
3. Fetch the current price of Bitcoin
4. Add a note: "Full tool test run — all systems checked"
5. Read all notes
6. Search the web: "What is the Model Context Protocol in one sentence?"
7. Add a person to the member database:
   - First name: Test
   - Last name: User
   - Years of experience: 1
   - Previous addresses: ["123 MCP Lane"]
8. Capture a screenshot and briefly describe what's visible
9. Save to memory: "Ran full MCP ToolHub tool test successfully"
10. Search memory for "tool test"

After each step, confirm it worked and show the result.
```

---

## Individual Tool Tests

### Echo

```
Use the echo tool with the message: "Hello from MCP ToolHub 👋"
```

### Factorial

```
What is the factorial of 15?
What happens when you calculate factorial of -3?
What is 0 factorial?
```

### Crypto Price

```
Get me the live USD price of: bitcoin, ethereum, and solana
```

```
What's the price of "notarealcoin" — handle the error gracefully
```

### Notes

```
Add three notes:
1. "MCP Tools = callable functions"
2. "MCP Prompts = message templates"  
3. "MCP Resources = read-only URI data"
Then read all notes back.
```

### Web Search

```
Use the web search tool to answer:
"What are the top 3 use cases for the Model Context Protocol?"
```

### Member Database

```
Add the following people to the member database:
1. Alice Chen, 5 years experience, previously at "10 First St" and "22 Second Ave"
2. Bob Martinez, 10 years experience, no previous addresses
```

### Screenshot

```
Take a screenshot. Without describing it in detail,
just tell me: how many windows are visible?
```

### Memory

```
Save these three facts to memory:
- "FastMCP is the Python framework for building MCP servers"
- "The MCP Inspector runs at localhost:5173"
- "pyautogui is used for screenshot capture in MCP ToolHub"

Then search for "MCP Inspector" and verify it comes back.
```

---

## Checking Resources

```
Show me:
1. The full inventory overview
2. The price of inventory item 123
3. The ID for "Tea"
4. The weather overview
5. A weather statement for "Tokyo"
```

---

## Checking Prompts

```
Use each of the three MCP prompts:
1. analyze_topic → "Artificial Intelligence"
2. historical_report → "The World Wide Web", 2 paragraphs
3. explain_weather_concept → "hurricane"
```

---

!!! success "All green?"
    If every step above returns a valid response without errors, your MCP ToolHub server is fully operational! 🎉

