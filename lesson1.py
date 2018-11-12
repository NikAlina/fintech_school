import requests
headers = {'Accept':'application/vnd.github.v3+json'}
response = requests.get('https://api.github.com/users/NikAlina', headers=headers)
print(response.text)