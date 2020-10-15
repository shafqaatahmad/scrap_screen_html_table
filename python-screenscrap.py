##Screen scrape the columns “Winner”, “Margin”, “Target” and “Opposition” from the
##link http://stats.espncricinfo.com/ci/content/records/283902.html
import requests
from bs4 import BeautifulSoup
import pandas as pd
#Query the website and return the html to the variable 'page'
page = requests.get('http://stats.espncricinfo.com/ci/content/records/283902.html')
html = page.text
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(html,'html.parser')
# We are looking for the particular table to collect the required information    
all_tables=soup.find_all('table')
right_table=soup.find('table', class_='engineTable')
#print (right_table)
# We will be generating lists to load the data into a dataframe
A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==8:     #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[4].find(text=True))
      
# The pandas package is used to convert the data to data frame        
import pandas as pd
df=pd.DataFrame(A,columns=['Winner'])
df['Margin']=B
df['Target']=C
df['Opposition']=D
print (df)


