# --- LOGGING HELPERS ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clean_output(value: str) -> str:
    """Truncates long XML dumps to keep logs readable."""
    if not isinstance(value, str):
        return str(value)
    if "hierarchy" in value or len(value) > 500:
        return value[:200] + f"\n{Colors.WARNING}... [Content Truncated, {len(value)} chars] ...{Colors.ENDC}"
    return value
