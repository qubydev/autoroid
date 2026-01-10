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

<p></p>

<p align="center">
<a href="https://www.producthunt.com/products/autoroid?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-autoroid" target="_blank" rel="noopener noreferrer">
   <img alt="Autoroid - AI-Powered Android Automation Assistant | Product Hunt" width="200" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1060746&amp;t=1768029907318">
</a>
</p>

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Gug9UumH57Q?si=1Mt961KDJ7-_59mA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


## 👉 Introduction

**Autoroid** leverages Large Language Models (LLMs) to understand your intent and interact with your Android device through **ADB**.
From navigating apps to automating human actions like taps, swipes, and text input — just tell Autoroid what you want to do.


## ✨ Features

* **Natural Language Control** -
  Ask to do something in human language:
  `Open Settings and enable dark mode`

* **UI Awareness** -
  Parses Android UI hierarchies to intelligently locate buttons, text, and inputs.

* **Universal Android Support** -
  Works with physical devices and emulators as long as ADB is enabled.

* **Configurable LLM Backend** -
  Supports OpenAI, Gemini, Anthropic and Ollama.


## 🚀 Quick Start

### 1. Install ADB

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

4. **Connect your device (any one of the below)**

   * Enable **USB Debugging** on your Android device and connect via USB
   * Start an android emulator

5. **Verify installation**

   ```bash
   adb devices
   ```

   You should see your device ID listed.

---

### 2. Clone the repo

Clone the repository and install dependencies.

```bash
git clone https://github.com/qubydev/autoroid.git
cd autoroid
```

### 3. Install packages

```bash
pip install -r requirements.txt
```

---

### 4. Configuration

Create a `.env` file in the project root.

```bash
cp .env.example .env
```

#### All Variables

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

### 5. Running Autoroid

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


## 🤝 Contributing

Contributions are welcome ❤️! Please fork the repository and submit a pull request with your changes.


## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.