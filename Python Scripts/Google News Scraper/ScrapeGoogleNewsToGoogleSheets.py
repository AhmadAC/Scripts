# Written by Ahmad Cooper
# Automatically scrape news to GoogleSheets

import json
import gspread
from oauth2client.client import OAuth2Credentials
from pygooglenews import GoogleNews

# Load credentials from file
with open("credentials.json") as f:
    creds_json = json.load(f)

# Create OAuth2 credentials object
creds = OAuth2Credentials.from_json(json.dumps(creds_json))

# Create client object and open the sheet
#  change the Sheet name "News" to whatever sheet you want to append the data to
client = gspread.authorize(creds)
sheet = client.open("News").sheet1

search_term = input('Type what you want to scrape to Google Sheets: ')

# Scrape the news articles and links
gn = GoogleNews()
stories = []
search = gn.search(search_term)
news_items = search['entries']
for item in news_items:
    story = {
        'News Article': item.title,
        'Link': item.link
    }
    stories.append(story)

# Construct data to write to the sheet
data = [
    ['News Article', 'Link'],
    *[(s['News Article'], s['Link']) for s in stories]
]

# Get existing data from the sheet
existing_data = sheet.get_all_values()

# Create a set to keep track of unique rows based on columns A and B
unique_rows = set()

# Create a list to keep track of duplicate rows
duplicate_rows = []

# Loop through each row and check if it's a duplicate, if not add it to the unique set
for row in existing_data:
    if (row[0], row[1]) not in unique_rows:
        unique_rows.add((row[0], row[1]))
    else:
        # If it's a duplicate, add it to the duplicate list
        duplicate_rows.append(row)

# Delete all the duplicate rows from the sheet in one batch operation
if duplicate_rows:
    batch_requests = []
    for r in duplicate_rows:
        start_row = sheet.find(r[0], in_column=1).row
        end_row = sheet.find(r[1], in_column=2).row
        batch_requests.append({
            'range': f'A{start_row}:B{end_row}',
            'values': [['', '']]
        })
    sheet.batch_update(batch_requests)

# Insert the new data below the existing data
if data:
    sheet.insert_rows(data, row=len(existing_data)+1)