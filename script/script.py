import requests
from bs4 import BeautifulSoup

url = "https://ardes.bg/laptopi/laptopi?_gl=1*hpljzi*_up*MQ..&gclid=EAIaIQobChMI76mqh7_0_wIVxup3Ch3FqguXEAAYASAAEgKkc_D_BwE"
response = requests.get(url)

#lists for storing the data before purchase
model_name = []
parameters = []
price = []

#lists for storing the data after purchase
selected_purchase = []
price_purchase = []

soup = BeautifulSoup(response.content, "html.parser")

model_name_elements = soup.find_all("div",class_= "title")
parameters_elements = soup.find_all("ul", class_="parameters list-unstyled parameters-ellipsis")
price_elements = soup.find_all("span", class_="price-num")

# Indexes used for checking if the laptop is below the max value
j = 0
i = 1

select = 0

# Extract model's names
for celement in model_name_elements:
    name = celement.text.strip()
    name = name[7:]
    model_name.append(name)

# Extract the parameters for each laptop 
for celement in parameters_elements:
    name = celement.text.strip()
    parameters.append(name)

# Extract the price of each laptop
for celement in price_elements:
    name = celement.text.strip()
    name = name[:-4]
    name = int(name)
    price.append(name)

max = input("Enter the maximum price you to pay for your laptop: ")

# Check which models' prices are not over the limit
while j < 24:
    if price[j] < int(max):
        selected_purchase.append(model_name[j])
        price_purchase.append(price[j])
        print(i, "|",model_name[j])
        print('---------------------------------------------')
        print(parameters[j])
        print("\n")
        i += 1
    
    j += 1


purchase = input("Enter the number of the laptop you want to buy to see how much does it cost: ")

print("Your laptop:")

# Finds the price of the selected laptop
while select <= i:
    if select == int(purchase):
        print(selected_purchase[select-1], "-", price_purchase[select-1], "lv.")

    select += 1