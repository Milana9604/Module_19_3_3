import requests

status='available'
data={"id":0,"category":{"id":0,"name":"string"},"name":"doggie","photoUrls":["string"],"tags":[{"id":0,"name":"string"}],"status":"available"}
res = requests.post(f"https://petstore.swagger.io/v2/pet", data = data, headers = {'accept': 'application/json', 'Content-Type': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())