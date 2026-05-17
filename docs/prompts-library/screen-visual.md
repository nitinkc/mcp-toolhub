# 🖥️ Screen & Visual

The `capture_screenshot` tool lets Claude **see your screen** — enabling a whole new class of interactions.

!!! tip "macOS permissions"
    Grant **Screen Recording** permission to your terminal in  
    **System Settings → Privacy & Security → Screen Recording**

---

## Basic Screen Awareness

```
Take a screenshot of my screen and tell me:
1. What application is in focus?
2. How many windows are visible?
3. What is the main content on screen?
```

---

## Screen + Notes Combo

```
Take a screenshot, describe what's on screen in one sentence,
then add that description as a note.
```

---

## Screen + Memory

```
Take a screenshot and save to memory what you observe about my current workspace setup.
Later I can ask: "What was on my screen earlier?"
```

---

## Screen + Web Search

```
Take a screenshot. If there's any application, code, or topic visible that you can identify,
search the web for the latest documentation or news about it.
```

---

## Screen + Analysis

```
Take a screenshot and use the analyze_topic prompt
to analyze whatever main subject is visible on screen.
```

---

## Accessibility Helper

```
Take a screenshot and describe everything visible in detail,
as if explaining it to someone who cannot see the screen.
```

---

## Code Review Mode

```
Take a screenshot of my screen.
If you can see any code, review it and suggest improvements.
If no code is visible, tell me what is there instead.
```

---

## Workflow Documenter

```
Take a screenshot.
Then add a note describing what I appear to be working on,
formatted as: "Working on: [topic] — [brief description]"
```

---

!!! info "How the image gets to Claude"
    The screenshot is captured as a PIL image, compressed to JPEG at 60% quality (keeping it under ~1 MB), and returned as a FastMCP `Image` object. Claude receives it as a base64-encoded inline image — no file upload needed.

