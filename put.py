import requests

status ='available'
res = requests.put(f"https://petstore.swagger.io/v2/pet", data = {'key1': 'value1', 'key2': 'value2'})

print(res.status_code)
print(res.text)
print(res.json())