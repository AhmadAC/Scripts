# CSV_to_List
Script comes "as is", no warranty.

This converts a CSV list from clipboard into a word list with new lines. 

```text
E.g. cat,dog   , pig       ,    horse

cat
dog
pig
horse
```

Requirements:
Python3, pyperclip

How to run:<br />
After installing requirements, copy a list as shown above, and run the bat file. After, paste into a word processor. Done!

# Google News Scraper<br /> 
Scrapes 99 top news articles based on your key search words.<br />
Original base code written by watching John Watson Rooney's YT video https://www.youtube.com/@JohnWatsonRooney  <br />
I tweaked it to have a GUI and to export to Excel formatted to the way I like it.<br />
This also works on Android phones, with Pydroid3

Script comes "as is", no warranty.

New Python users can import this list to install the dependencies
```
pip install pandas
pip install xlsxwriter
pip install tk
pip install datetime
pip install "setuptools<58"
pip install -U --no-deps "dateparser>=1.0.0"
pip install -U --no-deps "feedparser>=6.0.8"
pip install pygooglenews==0.1.2
pip uninstall feedparser
y
pip install -U --no-deps "feedparser>=6.0.8"
pip install sgmllib3k
```

"if there's a "base64" error, uninstall and reinstall feedparser, should work then

Requirements:<br />
Python3, Google unblocked (if blocked, use a VPN)

# combine_pics2pdf<br /> 
To run this script, please provide a directory path as a command line argument, copy the path to your clipboard, or the script's current directory should have pictures.<br /> 
        

This script converts all image files in a specified directory to a single PDF file. It first checks if a directory path is provided as a command line argument, copied to the clipboard, or the current script directory has pictures. If not, it displays an error message and exits the script. It then loops through all image files in the directory and checks if they are in jpeg, jpg, or png format. It  adds a new page to the PDF for each image, It resizes the image to fit within the page size while maintaining aspect ratio, and centers the image on the page. Finally, it creates the full path of the output file and saves the PDF to that location.
<br /> 
Requirements: fpdf, pyperclip, PIL

