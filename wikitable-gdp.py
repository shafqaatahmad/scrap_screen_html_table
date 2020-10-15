##Scrap Wikipedia table
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
#Query the website and return the html to the variable 'page'
page = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_exports')
html = page.text
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(html,'html.parser')
# prettify is used to look at nested structure of HTML page
#print(soup.prettify())
 
all_tables=soup.find_all('table')

# Once the table name is located, we have to use the “class” of the table to identify
right_table=soup.find('table', class_='wikitable sortable')

# We will be generating lists to load the data into a dataframe
A=[]
B=[]
C=[]
i=0
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if not cells:
        continue

    link=cells[1].find(href=True)
    A.append(link.get("title"))
    B.append(cells[2].find(text=True))
    C.append(cells[3].find(text=True))
       
# The pandas package is used to convert the data to data frame        
import pandas as pd
df=pd.DataFrame(A,columns=['Country'])
df['Export']=B
df['GDP']=C
df

df.to_csv(r'countrygdp.csv')



