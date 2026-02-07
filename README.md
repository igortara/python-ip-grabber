# 🛠️ Python IP & Metadata Logger

A lightweight and efficient **Flask-based** tool designed for network metadata collection (IP, User-Agent, Language) with instant notifications via **Discord Webhooks**.



## 🚀 Features
* **Real IP Detection:** Accurately identifies the target's IP even behind proxies or tunnels (using the `X-Forwarded-For` header).
* **Discord Integration:** Sends real-time alerts to your Discord channel with formatted Markdown.
* **Metadata Harvesting:** Collects detailed information about the target's browser, operating system, and system language.
* **Stealth Redirect:** Automatically forwards the user to a target URL (e.g., a YouTube video or a legitimate site) after logging.

## 📋 Requirements
* **Python 3.10+**
* **Linux Mint** / Ubuntu (or any Unix-based OS)
* Libraries: `flask`, `requests`

## ⚙️ Installation & Setup

1. **Clone or create the script:**
   ```bash
   nano logger.py
