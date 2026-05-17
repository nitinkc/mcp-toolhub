"""
MCP ToolHub – myMcpServer.py
============================
A single FastMCP server that demonstrates every core MCP concept:

  ┌─────────────┬────────────────────────────────────────────────────────────┐
  │  Concept     │  Examples in this file                                     │
  ├─────────────┼────────────────────────────────────────────────────────────┤
  │  Tools       │  echo, notes (read/write), crypto price, web search,      │
  │             │  screenshot, member database, memory (save/search)           │
  │  Prompts     │  analyze_topic, historical_report, explain_weather_concept  │
  │  Resources   │  inventory overview/price/id, weather overview/by-city      │
  └─────────────┴────────────────────────────────────────────────────────────┘

Environment variables (see .env.example):
  OPENAI_API_KEY     – required for memory tools
  PERPLEXITY_API_KEY – required for web-search tool
  VECTOR_STORE_NAME  – name of the OpenAI vector store (default: MCP_ToolHub_Memories)
  NOTES_FILE         – path for the notes text file    (default: notes.txt)
  MEMBER_LOG_FILE    – path for the member log file    (default: member_log.txt)
"""

# ── Standard library ──────────────────────────────────────────────────────────
import io
import os
import tempfile

# ── Third-party ───────────────────────────────────────────────────────────────
import pyautogui
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp import Image
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List

# ── Load environment variables from .env (if present) ─────────────────────────
load_dotenv()

# ── Configuration (all customisable via .env) ─────────────────────────────────
OPENAI_API_KEY     = os.getenv("OPENAI_API_KEY", "")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "")
VECTOR_STORE_NAME  = os.getenv("VECTOR_STORE_NAME", "MCP_ToolHub_Memories")
NOTES_FILE         = os.getenv("NOTES_FILE", "notes.txt")
MEMBER_LOG_FILE    = os.getenv("MEMBER_LOG_FILE", "member_log.txt")

# Web-search LLM selector (OpenAI, Perplexity, or any OpenAI-compatible API)
WEB_SEARCH_PROVIDER = os.getenv("WEB_SEARCH_PROVIDER", "perplexity").strip().lower()
WEB_SEARCH_API_KEY  = os.getenv("WEB_SEARCH_API_KEY", "").strip()
WEB_SEARCH_BASE_URL = os.getenv("WEB_SEARCH_BASE_URL", "").strip()
WEB_SEARCH_MODEL    = os.getenv("WEB_SEARCH_MODEL", "").strip()

# ── Single FastMCP instance for the whole server ──────────────────────────────
mcp = FastMCP("MCP ToolHub")



# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 – TOOLS
#  Tools are callable functions that the LLM can invoke to take actions.
# ══════════════════════════════════════════════════════════════════════════════

# ── 1a. Factorial tool (simplest possible numeric tool) ───────────────────────
@mcp.tool()
def factorial_safe_forLLM(n: int) -> str:
    """Return n! with friendly error handling for invalid input.

    Args:
        n: Non-negative integer input.
    """
    if n < 0:
        return "Error: n must be a non-negative integer."

    result = 1
    for i in range(2, n + 1):
        result *= i
    return f"{n}! = {result}"


# ── 1b. Echo tool (demonstrates single-argument tools) ────────────────────────
@mcp.tool()
def echo(message: str) -> str:
    """Echo back the message you send.  Great for testing connectivity.

    Args:
        message: Any string you want echoed back.
    """
    return f"Echo: {message}"


# ── 1c. Note-taking tools (demonstrates file I/O) ─────────────────────────────
@mcp.tool()
def add_note(content: str) -> str:
    """Append a note to the local notes file.

    Args:
        content: The text to append as a new note.
    """
    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"Note appended to '{NOTES_FILE}'."
    except Exception as e:
        return f"Error writing note: {e}"


@mcp.tool()
def read_notes() -> str:
    """Read and return all notes from the local notes file."""
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes.strip() else "No notes found."
    except FileNotFoundError:
        return "Notes file does not exist yet.  Use add_note to create one."
    except Exception as e:
        return f"Error reading notes: {e}"


# ── 1d. Cryptocurrency price tool (demonstrates external HTTP API calls) ───────
@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """Fetch the current USD price of a cryptocurrency via CoinGecko (no API key needed).

    Args:
        crypto: CoinGecko coin id, e.g. 'bitcoin', 'ethereum', 'solana'.
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": crypto.lower(), "vs_currencies": "usd"}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data.get(crypto.lower(), {}).get("usd")
        if price is not None:
            return f"The current price of {crypto} is ${price:,} USD."
        return f"Could not find price for '{crypto}'.  Check the CoinGecko coin id."
    except Exception as e:
        return f"Error fetching price for '{crypto}': {e}"


# ── 1e. Web search tool (demonstrates using an OpenAI-compatible third-party API)
def _resolve_web_search_llm_settings() -> dict:
    """Resolve API key, base URL, and model for web search from env variables."""
    defaults = {
        "perplexity": {
            "base_url": "https://api.perplexity.ai",
            "model": "sonar-pro",
        },
        "openai": {
            "base_url": "",
            "model": "gpt-4o-mini",
        },
    }

    provider_defaults = defaults.get(WEB_SEARCH_PROVIDER, {"base_url": "", "model": "gpt-4o-mini"})

    api_key = WEB_SEARCH_API_KEY
    if not api_key:
        if WEB_SEARCH_PROVIDER == "perplexity":
            api_key = PERPLEXITY_API_KEY
        elif WEB_SEARCH_PROVIDER == "openai":
            api_key = OPENAI_API_KEY

    base_url = WEB_SEARCH_BASE_URL or provider_defaults["base_url"]
    model = WEB_SEARCH_MODEL or provider_defaults["model"]

    return {
        "provider": WEB_SEARCH_PROVIDER,
        "api_key": api_key,
        "base_url": base_url,
        "model": model,
    }


@mcp.tool()
def perform_web_search(query: str) -> str:
    """Search the web using a configurable LLM provider.

    Provider support:
      - openai
      - perplexity
      - any OpenAI-compatible API (set WEB_SEARCH_BASE_URL + WEB_SEARCH_API_KEY)

    Args:
        query: The question or search query.
    """
    settings = _resolve_web_search_llm_settings()

    if not settings["api_key"]:
        return (
            "Web search is not configured. Set WEB_SEARCH_API_KEY, or set provider-specific "
            "keys (OPENAI_API_KEY / PERPLEXITY_API_KEY)."
        )

    try:
        client_kwargs = {"api_key": settings["api_key"]}
        if settings["base_url"]:
            client_kwargs["base_url"] = settings["base_url"]

        client = OpenAI(**client_kwargs)
        response = client.chat.completions.create(
            model=settings["model"],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that searches the web and answers questions concisely.",
                },
                {"role": "user", "content": query},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Web search error ({settings['provider']}): {e}"


# ── 1f. Screenshot tool (demonstrates returning binary Image data) ─────────────
@mcp.tool()
def capture_screenshot() -> Image:
    """Capture the current screen and return it as a JPEG image.

    Use this tool whenever the user asks to see what is on their screen.
    """
    buffer = io.BytesIO()
    screenshot = pyautogui.screenshot()
    # Keep file size under ~1 MB so Claude accepts it
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    return Image(data=buffer.getvalue(), format="jpeg")


# ── 1g. Structured-input tool (demonstrates Pydantic BaseModel arguments) ──────
class Person(BaseModel):
    """Represents a person in the member database."""
    first_name:          str       = Field(..., description="The person's first name")
    last_name:           str       = Field(..., description="The person's last name")
    years_of_experience: int       = Field(..., description="Years of professional experience")
    previous_addresses:  List[str] = Field(default_factory=list, description="List of previous addresses")


@mcp.tool()
def add_person_to_member_database(person: Person) -> str:
    """Log a person's details into the local member database file.

    Args:
        person: A Person object with first_name, last_name, years_of_experience,
                and optionally a list of previous_addresses.
    """
    try:
        with open(MEMBER_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"First Name: {person.first_name}\n")
            f.write(f"Last Name:  {person.last_name}\n")
            f.write(f"Experience: {person.years_of_experience} years\n")
            f.write("Previous Addresses:\n")
            for idx, address in enumerate(person.previous_addresses, 1):
                f.write(f"  {idx}. {address}\n")
            f.write("\n")
        return f"Person '{person.first_name} {person.last_name}' added to '{MEMBER_LOG_FILE}'."
    except Exception as e:
        return f"Error writing to member database: {e}"


# ── 1h. Memory tools (demonstrates OpenAI vector stores) ──────────────────────
def _get_openai_client() -> OpenAI:
    """Return an OpenAI client, raising a clear error if the key is missing."""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set.  Add it to your .env file.")
    return OpenAI(api_key=OPENAI_API_KEY)


def _get_or_create_vector_store(client: OpenAI):
    """Find the named vector store or create it if it doesn't exist yet."""
    for store in client.vector_stores.list():
        if store.name == VECTOR_STORE_NAME:
            return store
    return client.vector_stores.create(name=VECTOR_STORE_NAME)


@mcp.tool()
def save_memory(memory: str) -> dict:
    """Save a piece of text as a memory in an OpenAI vector store.

    Requires OPENAI_API_KEY in the environment.

    Args:
        memory: The text you want to remember.
    """
    try:
        client = _get_openai_client()
        vector_store = _get_or_create_vector_store(client)
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as f:
            f.write(memory)
            f.flush()
            client.vector_stores.files.upload_and_poll(
                vector_store_id=vector_store.id,
                file=open(f.name, "rb"),
            )
        return {"status": "saved", "vector_store_id": vector_store.id}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def search_memory(query: str) -> dict:
    """Search saved memories in the OpenAI vector store.

    Requires OPENAI_API_KEY in the environment.

    Args:
        query: The question or topic to search memories for.
    """
    try:
        client = _get_openai_client()
        vector_store = _get_or_create_vector_store(client)
        results = client.vector_stores.search(
            vector_store_id=vector_store.id,
            query=query,
        )
        content_texts = [
            content.text
            for item in results.data
            for content in item.content
            if content.type == "text"
        ]
        return {"results": content_texts}
    except Exception as e:
        return {"results": [], "error": str(e)}


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 – PROMPTS
#  Prompts are reusable message templates that guide the LLM's behaviour.
# ══════════════════════════════════════════════════════════════════════════════

@mcp.prompt()
def analyze_topic(topic: str) -> str:
    """Return a prompt that asks the LLM to do a detailed analysis of a topic.

    Args:
        topic: The subject to analyse.
    """
    return f"Please do a detailed, structured analysis of the following topic: {topic}"


@mcp.prompt()
def historical_report(topic: str, number_of_paragraphs: int = 3) -> str:
    """Return a prompt that asks the LLM to write a structured historical report.

    Args:
        topic: The historical subject to report on.
        number_of_paragraphs: How many paragraphs the MAIN body section should contain.
    """
    return (
        f"Create a concise research report on the history of '{topic}'.\n\n"
        "Structure the report into exactly three sections:\n"
        "  1. INTRODUCTION – brief context and significance\n"
        f"  2. MAIN – {number_of_paragraphs} paragraph(s) covering key developments\n"
        "  3. CONCLUSION – bullet-point summary of key takeaways\n\n"
        "Include a clearly formatted timeline of key events at the end."
    )


@mcp.prompt()
def explain_weather_concept(concept: str) -> str:
    """Return a prompt that asks the LLM to explain a meteorological concept.

    Args:
        concept: The weather or meteorological concept to explain (e.g. 'El Niño').
    """
    return (
        f"Explain the weather concept of '{concept}' in plain language.\n"
        "Cover: what it is, how it forms, its effects, and a real-world example."
    )


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 – RESOURCES
#  Resources expose read-only data that the LLM can access by URI.
# ══════════════════════════════════════════════════════════════════════════════

# ── Static inventory data (would come from a database in a real app) ──────────
_INVENTORY: dict = {
    "123": {"name": "Coffee",  "price": "6.99"},
    "456": {"name": "Tea",     "price": "17.99"},
    "789": {"name": "Cookies", "price": "84.99"},
}
_NAME_TO_ID = {v["name"]: k for k, v in _INVENTORY.items()}


@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """Return a human-readable overview of all items in the inventory."""
    lines = ["Inventory Overview:", ""]
    for item_id, info in _INVENTORY.items():
        lines.append(f"  • {info['name']} (ID: {item_id}) – ${info['price']}")
    return "\n".join(lines)


@mcp.resource("inventory://{inventory_id}/price")
def get_inventory_price(inventory_id: str) -> str:
    """Return the price for a given inventory item ID.

    Args:
        inventory_id: The numeric item ID (e.g. '123').
    """
    item = _INVENTORY.get(inventory_id)
    if item:
        return f"${item['price']}"
    return f"No item found with ID '{inventory_id}'."


@mcp.resource("inventory://{inventory_name}/id")
def get_inventory_id(inventory_name: str) -> str:
    """Return the inventory ID for a given item name.

    Args:
        inventory_name: The display name of the item (e.g. 'Coffee').
    """
    item_id = _NAME_TO_ID.get(inventory_name)
    if item_id:
        return item_id
    return f"No item found with name '{inventory_name}'."


@mcp.resource("weather://overview")
def get_weather_overview() -> str:
    """Return a general weather service overview / status statement."""
    return (
        "Weather Service: Online\n"
        "Data source: example (replace with a real weather API in production)\n"
        "Tip: Use the weather://{city}/statement resource for city-specific data."
    )


@mcp.resource("weather://{city}/statement")
def get_weather_statement_for_city(city: str) -> str:
    """Return a weather statement for a specific city.

    Args:
        city: The name of the city (e.g. 'London').
    """
    # In a real implementation you would call a weather API here.
    return (
        f"Weather statement for {city}: data not available in this demo.\n"
        "To add real weather data, set a WEATHER_API_KEY in .env and call "
        "an API such as OpenWeatherMap."
    )


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()
