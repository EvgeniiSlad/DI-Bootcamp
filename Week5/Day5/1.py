import requests

# url='http://api.open-notify.org/iss-now.json'

# response = requests.get(url)

# print(response.status_code)

# data=response.json()

# print(data['iss_position'])

url='https://api.chucknorris.io/jokes/random'

response=requests.get(url)

val=response.json()

print(val['value'])

