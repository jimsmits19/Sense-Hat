import requests

def post(url, data):
    request = requests.post(url = url, data = data)

def get(url):
    request = requests.get(url)
    return request.text



          
