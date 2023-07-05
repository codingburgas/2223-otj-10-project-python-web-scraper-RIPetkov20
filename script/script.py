import requests
from bs4 import BeautifulSoup

url = "https://ardes.bg/laptopi/laptopi?_gl=1*hpljzi*_up*MQ..&gclid=EAIaIQobChMI76mqh7_0_wIVxup3Ch3FqguXEAAYASAAEgKkc_D_BwE"
response = requests.get(url)

model_name = []
processor = []


soup = BeautifulSoup(response.content, "html.parser")

model_name_list = soup.find_all("div",class_= "title")
processor_list = soup.find_all("ul", class_="parameters list-unstyled parameters-ellipsis")

for celement in model_name_list:
    name = celement.text.strip()
    model_name.append(name)
    
for celement in processor_list:
    name = celement.text.strip()
    processor.append(name)



i = 0
while i < 24:
    print(model_name[i])
    print('---------------------------------------------')
    print(processor[i])
    print("\n")
    i +=1

