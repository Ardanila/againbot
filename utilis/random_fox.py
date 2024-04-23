import requests

def fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('image')

if __name__ == '__main__':
    image_url = fox()
    if image_url:
        print(image_url)
    else:
        print("Failed to retrieve fox image.")