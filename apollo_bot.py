import logging
import datetime
import asyncio
import nest_asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
)
import requests
from bs4 import BeautifulSoup

# === SETUP ===

# Your bot token from BotFather
TELEGRAM_TOKEN = "7607811446:AAErKu5I5YjA_3CXHRd-_Vp8ycj-W0NqfcY"

# The name of your Google Sheet and credentials file
GOOGLE_SHEET_NAME = "apollo"
GOOGLE_CREDENTIALS_FILE = "Please Make your Own"

# === ENABLE LOGGING FOR DEBUGGING ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === CONNECT TO GOOGLE SHEETS ===
# Define the permissions (scope) needed to access Sheets & Drive
scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Load your service account credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_FILE, scopes) #type: ignore

# Authorize and connect to Google Sheets
google_client = gspread.authorize(credentials) #type: ignore
sheet = google_client.open(GOOGLE_SHEET_NAME).sheet1  # Access the first tab in the sheet

# === FAKE APOLLO LOOKUP FUNCTION ===
def lookup_person(name):
    """
    Pretends to search Apollo.io and returns dummy info.
    In reality, Apollo.io uses JavaScript to load its data,
    so scraping won't work without a headless browser.
    """
    try:
        # Pretend to make a search (we just format the name)
        formatted_name = name.title()
        username = name.lower().replace(" ", "")
        return {
            "name": formatted_name,
            "title": "Software Engineer",
            "company": "Apollo.io",
            "email": f"{username}@apollo.io",
            "linkedin": f"https://linkedin.com/in/{username}"
        }
    except Exception:
        # If something goes wrong, return fallback values
        return {
            "name": name,
            "title": "Not found",
            "company": "Not found",
            "email": "N/A",
            "linkedin": "N/A"
        }

# === COMMAND: /start ===
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send a welcome message when the user types /start
    await update.message.reply_text("👋 Hey! Send me a name and I’ll try to find their info.") #type: ignore

# === HANDLE ANY MESSAGE ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the text the user sent
    user_input = update.message.text.strip() #type: ignore

    # Look up the person using our fake function
    person = lookup_person(user_input)

    # Format the response to send back
    reply = (
        f"🔍 *Search:* {user_input}\n\n"
        f"👤 *Name:* {person['name']}\n"
        f"💼 *Title:* {person['title']}\n"
        f"🏢 *Company:* {person['company']}\n"
        f"📧 *Email:* {person['email']}\n"
        f"🔗 *LinkedIn:* {person['linkedin']}"
    )

    # Send the message to the user
    await update.message.reply_text(reply, parse_mode="Markdown") #type: ignore

    # Log the query and result to Google Sheets
    sheet.append_row([
        str(datetime.datetime.now()),  # Timestamp
        user_input,                    # What the user searched
        person['name'],
        person['title'],
        person['company'],
        person['email'],
        person['linkedin']
    ])

# === MAIN BOT FUNCTION ===
async def run_bot():
    # Create the Telegram bot app
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Add handlers for /start and normal messages
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is up and running! Send it a name in Telegram.")
    await app.run_polling() #type: ignore

# === RUN THE BOT ===
if __name__ == '__main__':
    # Fixes event loop issues on some systems (like Jupyter or nested loops)
    nest_asyncio.apply()

    # Run the async bot loop
    asyncio.get_event_loop().run_until_complete(run_bot())
