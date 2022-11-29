import requests

res = requests.get('https://coinmarketcap.com/currencies/digibyte/')

txt = res.text

status = res.status_code

print(txt, status)