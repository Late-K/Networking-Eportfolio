import requests 
 
url = 'https://jsonplaceholder.typicode.com/posts' 
data = { 
    "title": "Sample Post", 
    "body": "This is an example post body.", 
    "userId": 1 
} 
 
response = requests.post(url, json=data) 
print(f"Status Code: {response.status_code}")