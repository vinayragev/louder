import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pu",
  password="password",
  database="test"
)

mycursor = mydb.cursor()

# Function to fetch image URLs
def scrape_image_urls(url,x,y):
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # If the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Find all img tags on the page
        li_card = soup.find_all('li',class_="event-card")
        
        # Extract the 'src' attribute from each img tag
        img_urls = []
        insert = []
        sql = "INSERT INTO event (city,category,url, image, title, subtitle,date, price) VALUES (%s, %s,%s, %s, %s, %s, %s, %s)"
        for li in li_card:
            image = li.find('div',class_='banner-cont')
            if image:
                link = li.get('data-link')
                name = li.get('data-name')
                if image.get('style'):
                    image = image.get('style')
                else:
                    image = image.get('data-src')
                if li.find('div',class_="date"):
                    date = li.find('div',class_="date").decode_contents()
                else:
                    date = ""
                if li.find('span',class_="price"):
                    price = li.find('span',class_="price").decode_contents()
                else:
                    price = ""
                if li.find('div',class_="subtitle"):
                    subtitle = li.find('div',class_="subtitle").decode_contents()
                else:
                    subtitle = ""
                mycursor.execute('SELECT * FROM event where url = "'+link+'"')
                rows = mycursor.fetchall()
                if len(rows)==0:
                    insert.append((x,y,link, image,name.strip(),subtitle.strip(),date.strip(),price.strip()))
        if len(insert):
            mycursor.executemany(sql, insert)
            mydb.commit()
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

# Example usage

city = ['new delhi']
category=['music','entertainment']
for x in city:
    for y in category:
        url = 'https://allevents.in/'+x+'/'+y+'?ref=cityhome-category-section#search'
        image_urls = scrape_image_urls(url,x,y)


