python package to install

pip install requests beautifulsoup4 lxml mysql-connector-python

event.sql : First import the mysql database 

Scrap.py file is used to collect data from URL. This will only work with "allevents.in". It collects event date, price, title, image and saves all the information in the database. You can add more city and category, it will collect all the details.

Index.php: File used to show event listing. It shows the event image, ticket price, event title, and event date. In this file you can select city and category. Then all the records come as per selected city and category

email.php file used for storing email of visitar who will rediret to mail website 


I was facing some problem in collecting information from php. So I used Python, it got the job done without any problems.
