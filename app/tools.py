from langchain_core.tools import tool
import subprocess
import os
import time
import json
from app.config import ADB_PATH, SCREEN_DUMP_PATH, LOCAL_DUMP_PATH
from app import sanitizer

@tool
def read_screen() -> str:
    """Reads the current screen state and it's interactive elements."""
    subprocess.run([ADB_PATH, "shell", "uiautomator", "dump", SCREEN_DUMP_PATH], capture_output=True)
    subprocess.run([ADB_PATH, "pull", SCREEN_DUMP_PATH, LOCAL_DUMP_PATH], capture_output=True)

    if not os.path.exists(LOCAL_DUMP_PATH):
        return "Error: Could not capture screen."

    with open(LOCAL_DUMP_PATH, "r", encoding="utf-8") as f:
        xml_content = f.read()
        
    elements = sanitizer.get_interactive_elements(xml_content)
    return json.dumps(elements, indent=2)

@tool
def wait(seconds: int) -> None:
    """Waits for a specified number of seconds."""
    time.sleep(seconds)

@tool
def tap(x: int, y: int) -> str:
    """Taps at coordinates (x, y)."""
    subprocess.run([ADB_PATH, "shell", "input", "tap", str(x), str(y)], capture_output=True)
    return f"Tapped at ({x}, {y})"

@tool
def swipe(x1: int, y1: int, x2: int, y2: int, duration: int) -> str:
    """Swipes from (x1, y1) to (x2, y2)."""
    subprocess.run([ADB_PATH, "shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), str(duration)], capture_output=True)
    return f"Swiped {x1},{y1} -> {x2},{y2}"

@tool
def type_text(text: str) -> str:
    """Types text (spaces replaced by %s)."""
    sanitized_text = text.replace(" ", "%s")
    subprocess.run([ADB_PATH, "shell", "input", "text", sanitized_text], capture_output=True)
    return f"Typed: {text}"

@tool
def home() -> str:
    """Presses Home button."""
    subprocess.run([ADB_PATH, "shell", "input", "keyevent", "KEYCODE_HOME"], capture_output=True)
    return "Pressed Home"

@tool
def back() -> str:
    """Presses Back button."""
    subprocess.run([ADB_PATH, "shell", "input", "keyevent", "KEYCODE_BACK"], capture_output=True)
    return "Pressed Back"

# Export the tools list
tools = [read_screen, wait, tap, swipe, type_text, home, back]
tools_by_name = {t.name: t for t in tools}
