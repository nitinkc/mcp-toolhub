# Screenshot Tool — `capture_screenshot`

Captures the current screen and returns it as a **JPEG image** that Claude can see and describe.

```python
@mcp.tool()
def capture_screenshot() -> Image:
    """Capture the current screen and return it as a JPEG image."""
```

This tool demonstrates returning **binary data** (not text) from an MCP tool using FastMCP's `Image` type. The image is compressed to JPEG at 60% quality to stay under Claude's ~1 MB attachment limit.

---

## How It Works

```python
buffer = io.BytesIO()
screenshot = pyautogui.screenshot()
screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
return Image(data=buffer.getvalue(), format="jpeg")
```

1. `pyautogui.screenshot()` captures the full screen via the OS
2. It's converted to RGB and saved as JPEG into a memory buffer
3. FastMCP's `Image` wrapper sends it back to Claude as a base64-encoded image

---

## Example Prompts

```
Take a screenshot of my screen and describe what you see

Capture my screen — is there anything unusual open?

Screenshot my screen and tell me what the main application is

Take a screenshot and summarize the content visible
```

!!! tip "macOS permissions"
    On macOS you may need to grant **Screen Recording** permission to your terminal app under  
    **System Settings → Privacy & Security → Screen Recording**.

