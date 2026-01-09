<p align="center"><img src="logo.png" width="200" alt="Sloggo Logo"></p>

<h1 align="center">Autoroid</h1>
<p align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square" alt="Version"></a>
<a href="https://developer.android.com/studio/command-line/adb"><img src="https://img.shields.io/badge/Android-ADB-green?style=flat-square&logo=android&logoColor=white" alt="Build"></a>
<a href="https://github.com/phare/sloggo?tab=MIT-1-ov-file#readme"><img src="https://img.shields.io/github/license/phare/sloggo?style=flat-square" alt="License"></a>
</p>

<div align="center">
   AI-Powered Android Automation Assistant
</div>

## 👉 Introduction

**Autoroid** leverages Large Language Models (LLMs) to understand your intent and interact with your Android device through **ADB**.
From navigating apps to automating repetitive actions like taps, swipes, and text input — just tell Autoroid what you want to do.

---

## ✨ Features

* **🗣 Natural Language Control**
  Describe actions like:
  `Open Settings and enable dark mode`

* **👁 UI Awareness**
  Parses Android UI hierarchies to intelligently locate buttons, text, and inputs.

* **🔌 Universal Android Support**
  Works with physical devices and emulators as long as ADB is enabled.

* **⚙ Configurable LLM Backend**
  Supports OpenAI (GPT-4o) and any LangChain-compatible provider.

---

## 🚀 Getting Started

Follow the steps below to set up Autoroid and start automating your Android device.

---

## 🧩 Prerequisites

### Android Debug Bridge (ADB)

ADB must be installed and accessible from your terminal.

1. **Download Android SDK Platform Tools**
   [https://developer.android.com/studio/releases/platform-tools](https://developer.android.com/studio/releases/platform-tools)

2. **Extract** the archive in a new folder `adb`.
   
   Example (Windows):

   ```
   C:\adb\adb.exe
   ```

3. **Add ADB to PATH**

   * Add `C:\adb` to your system environment variables

4. **Connect your device**

   * Enable *USB Debugging* on your Android device
   * Connect via USB or start an emulator

5. **Verify installation**

   ```bash
   adb devices
   ```

   You should see your device ID listed.

---

## 📦 Installation

Clone the repository and install dependencies.

```bash
git clone https://github.com/yourusername/autoroid.git
cd autoroid
```

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
```

**Windows**

```bash
.\venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the project root.

```bash
cp .env.example .env
```

### All Variables

| Variable | Description | Example |
|--------|-------------|---------|
| `LLM_PROVIDER` | LLM backend provider. Must be compatible with LangChain. | `openai \| gemini \| anthropic` |
| `BASE_URL` | Custom API base URL. (Leave empty for default) | `http://localhost:11434/v1` |
| `API_KEY` | API key for the selected LLM provider. | `sk-...` |
| `MODEL` | Model name used by the selected LLM provider. | `gpt-4o` |
| `ADB_PATH` | Path to the `adb` executable if it is not available in your system PATH. | `adb` |
| `SCREEN_DUMP_PATH` | Path on the Android device where the UI hierarchy XML is dumped. | `/sdcard/window_dump.xml` |
| `LOCAL_DUMP_PATH` | Local path where the pulled UI dump XML is stored for processing. | `window_dump.xml` |
| `RECURSION_LIMIT` | Maximum number of reasoning/action steps per goal to prevent infinite loops. | `50` |
| `RATE_LIMIT_DELAY` | Delay in seconds between LLM requests to avoid rate-limit issues. | `0.5` |

---

## ▶ Running Autoroid

Make sure your Android device or emulator is connected.

```bash
python main.py
```

You should see:

```text
🤖 Android Agent Started
Enter Goal:
```

Example commands:

* `Open Chrome and search for cute cats`
* `Launch Instagram and scroll for 10 seconds`
* `Enable airplane mode`

---

## 🤝 Contributing

Contributions are welcome and appreciated ❤️

1. Fork the repository
2. Create a feature branch

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by the Open Source Community
</p>