import os
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o")
ADB_PATH = os.getenv("ADB_PATH", "adb")
SCREEN_DUMP_PATH = os.getenv("SCREEN_DUMP_PATH", "/sdcard/window_dump.xml")
LOCAL_DUMP_PATH = os.getenv("LOCAL_DUMP_PATH", "window_dump.xml")
RECURSION_LIMIT = int(os.getenv("RECURSION_LIMIT", "25"))
RATE_LIMIT_DELAY = float(os.getenv("RATE_LIMIT_DELAY", "1.0"))
