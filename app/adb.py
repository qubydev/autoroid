import subprocess
from app.config import ADB_PATH

def get_adb_devices() -> list[str]:
    result = subprocess.run([ADB_PATH, "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[1:]
    return [line.split("\t")[0] for line in lines if "\tdevice" in line]

def is_device_connected() -> bool:
    return len(get_adb_devices()) > 0
