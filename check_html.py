# CHECKING THE HTML PAGE
from bs4 import BeautifulSoup
import requests

link = "https://www.google.com/search?q=google+stock&sca_esv=bedc8d185beb6f7e&biw=1280&bih=567&tbm=nws&ei=cOZ2ZpCxDo3vi-gP5reQkAw&ved=0ahUKEwiQqditvO-GAxWN9wIHHeYbBMIQ4dUDCA0&uact=5&oq=google+stock&gs_lp=Egxnd3Mtd2l6LW5ld3MiDGdvb2dsZSBzdG9jazILEAAYgAQYkQIYigUyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGApI1qMBUJKSAVi7ogFwAXgAkAEBmAH3AqAB1xOqAQUyLTYuM7gBA8gBAPgBAZgCBKAC3wbCAhAQABiABBixAxhDGIMBGIoFwgINEAAYgAQYsQMYQxiKBcICChAAGIAEGEMYigXCAgUQABiABJgDAIgGAZIHBzEuMC4yLjGgB805&sclient=gws-wiz-news"

def inspect_html(link):
    try:
        response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')  # Using 'html.parser'
        
        # Print a portion of the HTML to inspect
        with open("page_content.html", "w", encoding='utf-8') as file:
            file.write(soup.prettify())
        
        print("HTML content written to 'page_content.html'. Inspect this file to determine the correct selectors.")
    except Exception as e:
        print(f"Error in inspect_html function: {e}")

inspect_html(link)
