# 🚀 Apollo People Lookup Telegram Bot

This Telegram bot fetches user input (e.g., "Find details of Sundar Pichai" or "Email of Sam Altman"), returns structured person details (simulated from Apollo.io), and automatically logs the result to a Google Sheet.

---

## ✅ Features

- Accepts **natural text input** via Telegram bot (English/Hindi)
- Parses queries like:
  - `"Find details of Sundar Pichai"`
  - `"Email of Sam Altman"`
- Responds with:
  - 👤 Name  
  - 💼 Title  
  - 🏢 Company  
  - 📧 Email  
  - 🔗 LinkedIn  
- Logs every search to a **Google Sheet** with:
  - Timestamp  
  - User query  
  - Retrieved details (name, title, company, email, LinkedIn)

---

## 🧠 Tech Stack

- Python 3.10+
- [`python-telegram-bot`](https://python-telegram-bot.org/) v20+
- `gspread`, `oauth2client`, `requests`, `beautifulsoup4`
- Google Sheets API
- Telegram Bot via [@BotFather](https://t.me/botfather)

---

## 🔧 Setup Instructions

### 📍 1. Clone the project

git clone https://github.com/YOUR-USERNAME/Internship-Work.git
cd Internship-Wor


### 📦 2. Install dependencies

pip install -r requirements.txt


---

## 🔐 3. Google Sheets API Setup (Service Account Credentials)

### ✨ How to Create a Google Cloud JSON Credential File

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. **Create or Select a Project**
3. Enable these APIs under **APIs & Services > Library**:
   - ✅ Google Sheets API
   - ✅ Google Drive API
4. Go to **IAM & Admin > Service Accounts**
   - Click **Create Service Account**
   - Name it (e.g. `sheets-bot`)
   - Proceed, assign `Editor` role if available (or skip)
5. Open the new service account → Go to **Keys** tab
   - Click **Add Key > Create New Key**
   - Choose **JSON** → Download it ✅
6. Save the `.json` file in your project folder  
   Rename it to match what's used in your Python code (e.g. `apollo-bot-xxx.json`)

### 🔗 Share Your Google Sheet

1. Create a Google Sheet and name it **`apollo`**
2. Open your `.json` file and copy `client_email`
3. Share your sheet with that email (Editor access)

---

## 🤖 4. Telegram Bot Setup

1. Open [@BotFather](https://t.me/botfather) on Telegram
2. Create a bot → copy the API token
3. In `apollo_bot.py`, replace:
4. TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"

---

## ▶️ 5. Run the Bot

python apollo_bot.py


- Open Telegram and talk to your bot!
- Example:
  - `Find details of Elon Musk`
  - `Email of Mark Zuckerberg`
- Check your **Google Sheet** to see logged results.

---

## 🔎 Notes & Limitations

- **Apollo.io** does not offer a free public API.
- This project **simulates** Apollo search results for demo purposes.
- The Python function returns structured dummy data in the expected output format.
- You can replace the search function with real Apollo API code if you get access.

---

## 📸 Screenshots (Optional)

_Add 1–2 screenshots of:_
- ![Uploading WhatsApp Image 2025-07-18 at 19.00.40_4276c133.jpg…]()
- Telegra dummy bot reply

- <img width="1693" height="232" alt="image" src="https://github.com/user-attachments/assets/ca536c30-7eda-4bce-b75a-53016b763e92" />
google sheet saved data


---

## 📁 Files in This Repo

| File              | Purpose                                                  |
|-------------------|----------------------------------------------------------|
| `apollo_bot.py`   | Main bot logic                                           |
| `requirements.txt`| Required Python libraries                                |
| `README.md`       | Project documentation                                    |
| `.gitignore`      | (Recommended) Add your credentials here to exclude them  |

---

## 🛡 Security Warning

> 🚫 Never upload your `Telegram bot token` or `Google credentials JSON` to GitHub

- ⚠ Replace tokens in code with environment variables or local config
- ✅ This repo includes placeholders only

---

## ✅ Final Notes

- You're ready to submit this bot as your **internship assignment Task 1**
- The bot is fully deployable, and can be extended with real Apollo data in future
- Ready for **Task 2: Amazon Scraping**? Let's go!

---

## 🙌 Credits

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Gspread for Google Sheets](https://gspread.readthedocs.io/)
- [Apollo.io](https://www.apollo.io/) for project inspiration


