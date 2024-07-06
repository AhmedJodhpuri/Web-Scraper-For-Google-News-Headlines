

# CHECKING THE HTML PAGE
# from bs4 import BeautifulSoup
# import requests

# link = "https://www.google.com/search?q=google+stock&sca_esv=bedc8d185beb6f7e&biw=1280&bih=567&tbm=nws&ei=cOZ2ZpCxDo3vi-gP5reQkAw&ved=0ahUKEwiQqditvO-GAxWN9wIHHeYbBMIQ4dUDCA0&uact=5&oq=google+stock&gs_lp=Egxnd3Mtd2l6LW5ld3MiDGdvb2dsZSBzdG9jazILEAAYgAQYkQIYigUyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGApI1qMBUJKSAVi7ogFwAXgAkAEBmAH3AqAB1xOqAQUyLTYuM7gBA8gBAPgBAZgCBKAC3wbCAhAQABiABBixAxhDGIMBGIoFwgINEAAYgAQYsQMYQxiKBcICChAAGIAEGEMYigXCAgUQABiABJgDAIgGAZIHBzEuMC4yLjGgB805&sclient=gws-wiz-news"

# def inspect_html(link):
#     try:
#         response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
#         soup = BeautifulSoup(response.text, 'html.parser')  # Using 'html.parser'
        
#         # Print a portion of the HTML to inspect
#         with open("page_content.html", "w", encoding='utf-8') as file:
#             file.write(soup.prettify())
        
#         print("HTML content written to 'page_content.html'. Inspect this file to determine the correct selectors.")
#     except Exception as e:
#         print(f"Error in inspect_html function: {e}")

# inspect_html(link)


import requests
from bs4 import BeautifulSoup
import csv
import re

root = "https://www.google.com/"
link = "https://www.google.com/search?sca_esv=c1df660eec58a1d6&q=random+trending+news&tbm=nws&source=lnms&fbs=AEQNm0CRraR4AFMOJtZDUPiZk_hDEGW7EwGJ8ltzg0fUf3C5Xd1mhrcmUZ_z_Gw36zS3CIPG8xCRAefxrRYeluhQGyKyJmlTO0zgFWYJ90EHfF9J0C9TxZw9GSEMucDwobS1Kn7CvbpdRqSuB9i9sRMNuzwOPGMZJaTGds-9WuvfyoQdaGBXltLW8p7OkrLqC2iIPN4_U-tdIEGb1Z4ergQNfTdQudlkyw&sa=X&ved=2ahUKEwjjn9HG4_mGAxXdYPEDHQmnCScQ0pQJegQIERAB&biw=1280&bih=567&dpr=1.5"

def news(link):
    try:
        response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        with open("random.csv", "a", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            articles = soup.find_all('div', class_='Gx5Zad fP1Qef xpd EtOod pkphOe')
            print(f"Found {len(articles)} articles")

            for item in articles:
                try:
                    a_tag = item.find('a', href=True)
                    if a_tag:
                        raw_link = a_tag['href']
                        if '/url?q=' in raw_link:
                            link = raw_link.split("/url?q=")[1].split('&sa=U&')[0]
                            print(f"Link: {link}")

                    title_tag = item.find('div', class_='BNeawe vvjwJb AP7Wnd')
                    if title_tag:
                        title = title_tag.get_text().replace(",", "")
                        print(f"Title: {title}")

                    desc_tag = item.find('div', class_='BNeawe s3v9rd AP7Wnd')
                    if desc_tag:
                        description = desc_tag.get_text().replace(",", "")
                        # Split the description by " · " and remove Arabic text
                        parts = description.split(" · ")
                        if len(parts) > 1:
                            description = parts[1]
                        else:
                            description = parts[0]
                        # Remove any remaining Arabic characters
                        description = re.sub(r'[\u0600-\u06FF]+', '', description).strip()
                        print(f"Description: {description}")

                    writer.writerow([title, link, description])
                    print(f"Written to CSV: Title - {title}, Link - {link}, Description - {description}")

                except Exception as e:
                    print(f"Error processing item: {e}")

        next_button = soup.find('a', attrs={'aria-label': 'الصفحة التالية'})
        if next_button:
            next_link = root + next_button['href']
            print(f"Next page link: {next_link}")
            news(next_link)
        else:
            print("No more pages to scrape.")
    except Exception as e:
        print(f"Error in main function: {e}")

news(link)
