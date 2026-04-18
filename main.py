import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for post in data:
        print(post['userId'], post['id'], post['title'])
else:
    print('Error:', response.status_code)

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['userId'], data['id'], data['title'])
else:
    print('Error:', response.status_code)

url = "https://jsonplaceholder.typicode.com/posts"
data = {'userId': 1, 'title': 'New Post', 'body': 'This is a new post'}
response = requests.post(url, data=json.dumps(data), headers={'Content-type': 'application/json'})

if response.status_code == 201:
    print('Post created successfully')
else:
    print('Error:', response.status_code)

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.put(url, data=json.dumps({'userId': 1, 'id': 1, 'title': 'Updated Post', 'body': 'This is an updated post'}), headers={'Content-type': 'application/json'})

if response.status_code == 200:
    print('Post updated successfully')
else:
    print('Error:', response.status_code)

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

if response.status_code == 200:
    print('Post deleted successfully')
else:
    print('Error:', response.status_code)