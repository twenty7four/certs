import requests

url = 'http://numbersapi.com/43/'
resp = requests.get(url)
if resp.status_code == 200:
    print(resp.text)
else:
    print(resp.status_code)