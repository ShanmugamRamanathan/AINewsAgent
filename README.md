# 📰 AI News Agent

An automated pipeline to fetch, summarize, and send daily AI-related news using an AI model (Gemini), Gmail, and Telegram. Runs daily via GitHub Actions.

---

## ✅ Features

- Fetches the latest news articles
- Summarizes content using Google Gemini
- Sends the summary via:
  - 📧 Gmail
  - 💬 Telegram
- Scheduled to run every day
- Also supports manual execution

---

## 🔧 Setup

### 1. Add GitHub Secrets

Go to:  
**GitHub → Settings → Secrets and variables → Actions → New repository secret**

Add the following:

| Name                | Description                                       |
|---------------------|---------------------------------------------------|
| `GEMINI_API_KEY`     | Your Google Gemini API Key                        |
| `GMAIL_USER`         | Your Gmail address                                |
| `GMAIL_APP_PASSWORD` | 16-digit Gmail App Password (not your real one)   |
| `GMAIL_RECIPIENT`    | The email address to receive the summary          |
| `bot_token`          | Telegram bot token (from @BotFather)              |
| `chat_id`            | Your Telegram chat ID (from getUpdates)           |

---

### 2. Clone & Run Locally

```bash
git clone https://github.com/ShanmugamRamanathan/AINewsAgent.git
cd AINewsAgent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
