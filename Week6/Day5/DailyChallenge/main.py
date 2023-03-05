import requests

url=('https://restcountries.com/v3.1/all')

response=requests.get(url)
data=response.json()

country=data[0]
name=country['name']['common']
capital=country['capital']
flag=country['flag']
subregion=country['subregion']
population=country['population']
print(country['name'])