import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Step 1: Define the permissions your app needs to access Google Sheets and Drive
scope = [
    "https://spreadsheets.google.com/feeds",  # Access to Google Sheets
    "https://www.googleapis.com/auth/drive"   # Access to Google Drive
]

# Step 2: Load your service account credentials
# Replace 'your-credentials.json' with the actual file name of your credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("your json clint email", scope)# type: ignore

# Step 3: Authorize your app to use Google Sheets with those credentials
client = gspread.authorize(creds)# type: ignore

# Step 4: Open the Google Sheet by its name
# Make sure the name matches exactly what’s shown in Google Sheets
spreadsheet = client.open("Apollo Search Logs")

# Step 5: Select the first sheet/tab in the spreadsheet
sheet = spreadsheet.sheet1

# Step 6: Read and print the value in cell A1
cell_value = sheet.acell('A1').value
print("The value in cell A1 is:", cell_value)
