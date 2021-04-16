import requests

def get_ip():
    req = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
    ip = req.json()['Answer'].split()[4]
    return ip
    
print(get_ip())