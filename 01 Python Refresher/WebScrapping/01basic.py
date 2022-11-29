import requests
import bs4

res = requests.get('https://learncodeonline.in')

print(type(res))

print(res.text)