import time
import requests

URL = 'https://www.google.ru/?client=safari'
loading_time = requests.get(URL).elapsed.total_seconds()
print(loading_time)