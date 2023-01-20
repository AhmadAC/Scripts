"""
Original base code written by watching John Watson Rooney's YT video https://www.youtube.com/@JohnWatsonRooney 
I tweaked it to have a GUI and to export to Excel formatted to the way I like it.

Script comes "as is", no warranty.

"New Python users can import this list to install the dependencies

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

"if there's a "base64" error, uninstall and reinstall feedparser, should work then

"""
    #Exports data as a data table
import pandas as pd
    #Formats xlsx file
import xlsxwriter
from pygooglenews import GoogleNews
from tkinter import *
import datetime
import tkinter as TK

#code from https://stackoverflow.com/a/9350788 and https://www.geeksforgeeks.org/change-current-working-directory-with-python/#:~:text=To%20change%20the%20current%20working,as%20a%20new%20directory%20path.
#Save file in the scripts folder
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))



tk = TK.Tk()
tk.title('Google News Scraper')
# tk.iconbitmap(default='transparent.ico')
lab = Label(tk, text='Type what you want to scrape to Excel.')
lab.pack()
def submit():
    username = entry.get()
    gn = GoogleNews()
    tk.destroy()
    #gn = GoogleNews(country = 'Australia')

    def get_titles(search):
        stories = []
        search = gn.search(search)
        newsitem = search['entries']
        for item in newsitem:
            story = {
                'News Article': item.title,
                'Link': item.link
                }
            stories.append(story)
        return stories
    
    dtime = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
    puttoex = get_titles(username)

    df = pd.DataFrame(puttoex)
        #df = pd.to_excel('GoogleNews.xlsx', index=False)
    writer = pd.ExcelWriter(username + '_' + dtime + '.xlsx', engine='xlsxwriter')
        # Write the dataframe data to XlsxWriter. Turn off the default header and
        # index and skip one row to allow us to insert a user defined header.
    df.to_excel(writer, sheet_name='News', startrow=1, header=False, index=False)
        # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['News']
        # Get the dimensions of the dataframe.
    (max_row, max_col) = df.shape
        # Create a list of column headers, to use in add_table().
    column_settings = [{'header': column} for column in df.columns]
        # Add the Excel table structure. Pandas will add the data.
    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
        # Make the columns wider for clarity.
    worksheet.set_column(0, max_col - 1, 100)
        # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    #    #Count data fram rows commented out
    #    #df.count()
    #input()


submit = TK.Button(tk, text="Scrape", command=submit)
submit.pack(side = RIGHT)


entry = Entry()
entry.focus_set()
entry.config(font=('Arial', 18), width=20)
entry.config(bg='#111111', fg='#00FF00', borderwidth='3')
entry.pack()

tk.bind('<Return>', lambda event=None: submit.invoke())
tk.mainloop()
