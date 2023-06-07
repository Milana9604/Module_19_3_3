import requests

status ='available'
res = requests.delete(f"https://petstore.swagger.io/v2/pet/88571088",
                   headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())